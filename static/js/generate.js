// Year in footer
document.getElementById("year").textContent = new Date().getFullYear();

// Fade-in on scroll
const faders = document.querySelectorAll('.fade-in');
const appearOnScroll = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, {threshold: 0.2});
faders.forEach(el => appearOnScroll.observe(el));

// Show overlay on form submit
const form = document.getElementById("reportForm");
const overlay = document.getElementById("overlay");

form.addEventListener("submit", () => {
  overlay.classList.remove("d-none");
  setTimeout(() => {
    overlay.classList.add("d-none");
  },120000);
});