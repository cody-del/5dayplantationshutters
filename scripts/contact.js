/* Local email draft flow. Replace this adapter with verified GHL submission at launch. */
function consultationMailto(values) {
  const field = (name) => String(values[name] || '').trim();
  const subject = 'Free consultation request — ' + field('product');
  const body = [
    'I would like to arrange a free window treatment consultation.', '',
    'Name: ' + field('name'), 'Email: ' + field('email'),
    'Phone: ' + (field('phone') || 'Not provided'), 'City: ' + field('city'),
    'Interested in: ' + field('product'), '',
    'Window details:', field('message') || 'Please contact me to discuss.',
  ].join('\n');
  return 'mailto:5dayshutters@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
}

const consultationForm = document.querySelector('#consultation-form');
if (consultationForm) {
  const submit = consultationForm.querySelector('button[type="submit"]');
  const status = consultationForm.querySelector('.form-status');
  const fallback = consultationForm.querySelector('[data-email-request]');
  const params = new URLSearchParams(window.location.search);
  const requestedCity = params.get('city');
  const cityField = consultationForm.elements.namedItem('city');
  if (['Largo', 'Clearwater', 'St. Petersburg'].includes(requestedCity) && !cityField.value) {
    cityField.value = requestedCity;
  }
  const productField = consultationForm.elements.namedItem('product');
  const requestedProduct = params.get('product');
  if (requestedProduct && [...productField.options].some((option) => option.value === requestedProduct) && !productField.value) {
    productField.value = requestedProduct;
  }
  submit.disabled = false;
  consultationForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!consultationForm.reportValidity()) return;
    const values = Object.fromEntries(new FormData(consultationForm));
    const draft = consultationMailto(values);
    fallback.href = draft;
    fallback.hidden = false;
    window.location.href = draft;
    status.textContent = 'Send the draft in your email app to finish your request. If it didn’t open, email 5dayshutters@gmail.com or call (813) 317-1077.';
  });
}
