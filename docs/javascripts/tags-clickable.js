// Script pour rendre les tags cliquables
document.addEventListener('DOMContentLoaded', function() {
  // Attendre que Material for MkDocs soit complètement chargé
  setTimeout(() => {
    const tags = document.querySelectorAll('.md-tag');

    tags.forEach(tag => {
      // Rendre le tag cliquable
      tag.style.cursor = 'pointer';
      tag.style.transition = 'opacity 0.2s';

      // Effet hover
      tag.addEventListener('mouseenter', () => {
        tag.style.opacity = '0.8';
      });

      tag.addEventListener('mouseleave', () => {
        tag.style.opacity = '1';
      });

      // Clic sur le tag = recherche
      tag.addEventListener('click', (e) => {
        e.preventDefault();
        const tagText = tag.textContent.trim();

        // Ouvrir le panneau de recherche en cliquant sur le bouton
        const searchButton = document.querySelector('.md-search__button[for="__search"]');
        if (searchButton) {
          searchButton.click();

          // Attendre que la recherche soit ouverte
          setTimeout(() => {
            const searchInput = document.querySelector('.md-search__input');
            if (searchInput) {
              // Définir la valeur et déclencher la recherche
              searchInput.value = tagText;
              searchInput.focus();

              // Déclencher l'événement input pour activer la recherche instantanée
              const inputEvent = new Event('input', { bubbles: true });
              searchInput.dispatchEvent(inputEvent);
            }
          }, 100);
        }
      });
    });
  }, 500);
});
