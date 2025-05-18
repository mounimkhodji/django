// Initialisation après chargement du DOM
document.addEventListener('DOMContentLoaded', function() {
  // GSAP Animations
  gsap.registerPlugin(ScrollTrigger);
  
  // Animation du header
  gsap.from("header", {
    duration: 1,
    y: -100,
    opacity: 0,
    ease: "power3.out"
  });
  
  // Animation des sections
  gsap.utils.toArray(".section").forEach((section, i) => {
    gsap.from(section, {
      scrollTrigger: {
        trigger: section,
        start: "top 80%",
        toggleActions: "play none none none"
      },
      opacity: 0,
      y: 50,
      duration: 0.8,
      delay: i * 0.1
    });
  });
  
  // Dark Mode Toggle
  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const html = document.documentElement;
      const isDark = html.getAttribute('data-theme') === 'dark';
      html.setAttribute('data-theme', isDark ? 'light' : 'dark');
      localStorage.setItem('theme', isDark ? 'light' : 'dark');
    });
  }
  
  // Initialiser le thème
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  
  // Animation des bulles
  createBubbles();
});

// Créer des bulles animées
function createBubbles() {
  const bubbleContainer = document.querySelector('.bubbles');
  if (!bubbleContainer) return;
  
  for (let i = 0; i < 20; i++) {
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    
    // Position aléatoire
    const size = Math.random() * 30 + 10;
    const posX = Math.random() * 100;
    const delay = Math.random() * 10;
    const duration = Math.random() * 20 + 10;
    
    bubble.style.width = `${size}px`;
    bubble.style.height = `${size}px`;
    bubble.style.left = `${posX}%`;
    bubble.style.animationDelay = `${delay}s`;
    bubble.style.animationDuration = `${duration}s`;
    bubble.style.opacity = Math.random() * 0.5 + 0.1;
    
    bubbleContainer.appendChild(bubble);
  }
}

// Gestion des formulaires
document.querySelectorAll('form').forEach(form => {
  form.addEventListener('submit', function(e) {
    const submitBtn = this.querySelector('button[type="submit"]');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Traitement...';
    }
  });
});