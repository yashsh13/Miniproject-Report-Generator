// Show overlay on form submit; let the normal navigation/download clear it when response arrives.
document.getElementById("pptForm").addEventListener("submit", function () {
  const overlay = document.getElementById("overlay");
  const btn = document.getElementById("generateBtn");
  overlay.classList.remove("d-none");
  overlay.setAttribute("aria-hidden", "false");
  btn.disabled = true;
  btn.setAttribute("aria-busy", "true");
});

// year in footer
document.getElementById("year").textContent = new Date().getFullYear();

// Optional: Animate elements on first paint (already handled by CSS via .fade-in-up classes)