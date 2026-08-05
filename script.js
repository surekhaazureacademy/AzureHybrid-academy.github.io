function prevSlide() {
  const carousel = document.getElementById('videoCarousel');
  carousel.scrollLeft -= carousel.offsetWidth;
}
 
function nextSlide() {
  const carousel = document.getElementById('videoCarousel');
  carousel.scrollLeft += carousel.offsetWidth;
}
function autoplaySlides() {
  const carousel = document.getElementById('videoCarousel');
  setInterval(() => {
    carousel.scrollLeft += carousel.offsetWidth;
    if (carousel.scrollLeft >= carousel.scrollWidth - carousel.offsetWidth) {
      carousel.scrollLeft = 0;
    }
  }, 5000);
}
 
window.onload = autoplaySlides;
