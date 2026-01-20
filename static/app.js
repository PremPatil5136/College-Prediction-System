// basic UI behaviour
document.addEventListener("DOMContentLoaded", function(){
  // year
  const y = new Date().getFullYear(); document.getElementById("year")?.append(y);

  // theme toggle
  const themeToggleBtns = document.querySelectorAll("#themeToggle, #themeToggle");
  themeToggleBtns.forEach(btn => btn?.addEventListener("click", () => {
    document.body.classList.toggle("theme-dark");
  }));

  // sign-in modal
  const signinBtn = document.getElementById("signinBtn");
  const signinModal = document.getElementById("signinModal");
  const closeSignin = document.getElementById("closeSignin");
  signinBtn?.addEventListener("click", () => signinModal.classList.add("open"));
  closeSignin?.addEventListener("click", () => signinModal.classList.remove("open"));
  signinModal?.addEventListener("click", (e) => { if(e.target===signinModal) signinModal.classList.remove("open"); });

  // mobile hamburger toggle
  const hamb = document.getElementById("hamburger");
  const navLinks = document.getElementById("navLinks");
  hamb?.addEventListener("click", () => {
    if(navLinks.style.display === "flex") navLinks.style.display = "none";
    else navLinks.style.display = "flex";
  });

  // small enhancement: highlight active nav (based on URL)
  const links = document.querySelectorAll(".nav-links a");
  links.forEach(a => { if(a.href === location.href || a.getAttribute("href") === location.pathname) a.classList.add("active") });
});

