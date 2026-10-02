const reviewSection = document.querySelector('.reviews');
const reviewTrack = reviewSection.querySelector('.review-track');
const reviewCards = [...reviewTrack.querySelectorAll('.review-card')];
const previousReview = reviewSection.querySelector('.review-prev');
const nextReview = reviewSection.querySelector('.review-next');
const reviewPosition = reviewSection.querySelector('.review-position');
const reviewDialog = reviewSection.querySelector('.review-dialog');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

reviewSection.classList.add('reviews-enhanced');
reviewSection.querySelectorAll('button[hidden]').forEach((button) => { button.hidden = false; });

function reviewStep() {
  return reviewCards[0].getBoundingClientRect().width + parseFloat(getComputedStyle(reviewTrack).gap);
}

function updateReviewControls() {
  const step = reviewStep();
  const visible = Math.round(reviewTrack.clientWidth / step);
  const first = Math.round(reviewTrack.scrollLeft / step);
  previousReview.disabled = reviewTrack.scrollLeft < 2;
  nextReview.disabled = reviewTrack.scrollLeft >= reviewTrack.scrollWidth - reviewTrack.clientWidth - 2;
  const label = visible === 1 ? `Review ${first + 1} of ${reviewCards.length}` : `Reviews ${first + 1}–${Math.min(first + visible, reviewCards.length)} of ${reviewCards.length}`;
  if (reviewPosition.textContent !== label) reviewPosition.textContent = label;
}

function moveReview(direction) {
  reviewTrack.scrollBy({ left: direction * reviewStep(), behavior: reduceMotion.matches ? 'instant' : 'smooth' });
}

previousReview.addEventListener('click', () => moveReview(-1));
nextReview.addEventListener('click', () => moveReview(1));
reviewTrack.addEventListener('scroll', updateReviewControls, { passive: true });
reviewTrack.addEventListener('keydown', (event) => {
  if (event.target !== reviewTrack || !['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
  event.preventDefault();
  moveReview(event.key === 'ArrowLeft' ? -1 : 1);
});
new ResizeObserver(updateReviewControls).observe(reviewTrack);

reviewCards.forEach((card) => {
  card.querySelector('.review-read').addEventListener('click', () => {
    reviewDialog.querySelector('h2').textContent = card.querySelector('h3').textContent;
    reviewDialog.querySelector('.review-dialog-text').textContent = card.querySelector('.review-quote').textContent;
    reviewDialog.querySelector('.review-dialog-note').textContent = card.dataset.excerpt === 'true' ? 'Excerpt from a Google review.' : 'Google customer review.';
    reviewDialog.showModal();
  });
});
reviewDialog.querySelector('.review-close').addEventListener('click', () => reviewDialog.close());
reviewDialog.addEventListener('click', (event) => {
  const bounds = reviewDialog.getBoundingClientRect();
  if (event.target === reviewDialog && (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom)) reviewDialog.close();
});
updateReviewControls();
