(() => {
  const demo = document.querySelector('[data-shade-demo]');
  if (!demo) return;
  const videos = {
    up: demo.querySelector('[data-video="up"]'),
    down: demo.querySelector('[data-video="down"]')
  };
  const status = demo.querySelector('[data-demo-status]');
  const buttons = [...demo.querySelectorAll('[data-shade-action]')];
  let active = videos.up;
  let direction = 'up';
  let request = 0;
  let ready;

  // Each file contains the same 108 frames in opposite order, at 24 fps.
  // Use the final frame time (not the file duration) for exact reversal mapping.
  const span = video => Math.max(0, Math.min(video.duration, 107 / 24));
  const position = () => {
    const progress = Math.min(1, Math.max(0, active.currentTime / span(active) || 0));
    return direction === 'up' ? progress : 1 - progress;
  };
  const setState = (state, label) => {
    demo.dataset.state = state;
    status.textContent = label;
    buttons.forEach(button => {
      button.setAttribute('aria-pressed', String(
        button.dataset.shadeAction === (state === 'raising' ? 'up' : state === 'lowering' ? 'down' : '')
      ));
    });
  };
  const restingState = () => {
    const value = position();
    if (value <= 0.005) setState('closed', 'Fully closed');
    else if (value >= 0.995) setState('open', 'Fully open');
    else setState('stopped', 'Stopped');
  };
  const stop = () => {
    request += 1;
    Object.values(videos).forEach(video => video.pause());
    restingState();
  };
  const prepare = () => {
    if (ready) return ready;
    ready = Promise.all(Object.values(videos).map(video => new Promise((resolve, reject) => {
      if (video.readyState >= 1) { resolve(); return; }
      const loaded = () => { cleanup(); resolve(); };
      const failed = () => { cleanup(); reject(new Error('Video unavailable')); };
      const cleanup = () => {
        video.removeEventListener('loadedmetadata', loaded);
        video.removeEventListener('error', failed);
      };
      video.addEventListener('loadedmetadata', loaded);
      video.addEventListener('error', failed);
      video.preload = 'auto';
      video.load();
    })));
    return ready;
  };
  const seek = (video, time) => new Promise(resolve => {
    if (Math.abs(video.currentTime - time) < 0.001 && !video.seeking) { resolve(); return; }
    video.addEventListener('seeked', resolve, {once: true});
    video.currentTime = time;
  });
  const move = async nextDirection => {
    const ticket = ++request;
    Object.values(videos).forEach(video => video.pause());
    setState('loading', 'Getting ready…');
    try {
      await prepare();
      if (ticket !== request) return;
      const value = position();
      if ((nextDirection === 'up' && value >= 0.995) || (nextDirection === 'down' && value <= 0.005)) {
        restingState();
        return;
      }
      const next = videos[nextDirection];
      const targetTime = (nextDirection === 'up' ? value : 1 - value) * span(next);
      await seek(next, targetTime);
      if (ticket !== request) return;
      active = next;
      direction = nextDirection;
      Object.values(videos).forEach(video => video.classList.toggle('is-active', video === active));
      setState(nextDirection === 'up' ? 'raising' : 'lowering', nextDirection === 'up' ? 'Raising' : 'Lowering');
      await active.play();
      // New commands already pause both players; never pause a newer request here.
    } catch (_) {
      if (ticket === request) setState('error', 'The demo couldn’t load. Please refresh and try again.');
    }
  };

  Object.values(videos).forEach(video => {
    video.muted = true;
    video.addEventListener('ended', () => {
      if (video !== active) return;
      video.pause();
      restingState();
    });
  });
  buttons.forEach(button => {
    button.disabled = false;
    button.addEventListener('click', () => {
      const action = button.dataset.shadeAction;
      if (action === 'stop') stop();
      else move(action);
    });
  });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) stop();
  });
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      if (entries.some(entry => entry.isIntersecting)) {
        prepare().catch(() => setState('error', 'The demo couldn’t load. Please refresh and try again.'));
        observer.disconnect();
      }
    }, {rootMargin: '300px'});
    observer.observe(demo);
  }
})();
