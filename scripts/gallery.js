/* Original links remain usable when dialog enhancement is unavailable. */
const galleryLinks = [...document.querySelectorAll('[data-gallery-item]')];
const galleryDialog = document.querySelector('.gallery-dialog');
if (galleryDialog && typeof galleryDialog.showModal === 'function' && galleryLinks.length) {
  const image = galleryDialog.querySelector('[data-gallery-image]');
  const caption = galleryDialog.querySelector('#gallery-caption');
  const position = galleryDialog.querySelector('[data-gallery-position]');
  let selected = 0;
  let opener;

  function displayPhoto(index) {
    selected = (index + galleryLinks.length) % galleryLinks.length;
    const link = galleryLinks[selected];
    image.src = link.href;
    image.alt = link.querySelector('img').alt;
    caption.textContent = link.closest('figure').querySelector('figcaption').textContent;
    position.textContent = (selected + 1) + ' of ' + galleryLinks.length;
  }
  galleryLinks.forEach((link, index) => {
    link.addEventListener('click', (event) => {
      // Preserve open-in-new-tab gestures and the no-JS image link.
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      opener = link;
      displayPhoto(index);
      galleryDialog.showModal();
    });
  });
  galleryDialog.querySelector('.gallery-close').addEventListener('click', () => galleryDialog.close());
  galleryDialog.querySelector('[data-gallery-prev]').addEventListener('click', () => displayPhoto(selected - 1));
  galleryDialog.querySelector('[data-gallery-next]').addEventListener('click', () => displayPhoto(selected + 1));
  galleryDialog.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
      event.preventDefault();
      displayPhoto(selected + (event.key === 'ArrowRight' ? 1 : -1));
    }
  });
  galleryDialog.addEventListener('click', (event) => {
    if (event.target !== galleryDialog) return;
    const box = galleryDialog.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) galleryDialog.close();
  });
  galleryDialog.addEventListener('close', () => opener?.focus());
}
