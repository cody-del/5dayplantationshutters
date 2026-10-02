const navigationDetails = [...document.querySelectorAll('.site-header details')];

document.addEventListener('pointerdown', (event) => {
  navigationDetails.forEach((menu) => {
    if (!menu.contains(event.target)) menu.open = false;
  });
});

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  const menu = document.activeElement.closest('details[open]');
  if (!menu || !navigationDetails.includes(menu)) return;
  menu.open = false;
  menu.querySelector('summary').focus();
  event.preventDefault();
});

navigationDetails.forEach((menu) => {
  menu.addEventListener('focusout', (event) => {
    if (event.relatedTarget && !menu.contains(event.relatedTarget)) menu.open = false;
  });
  menu.addEventListener('click', (event) => {
    if (event.target.closest('a')) menu.open = false;
  });
});
