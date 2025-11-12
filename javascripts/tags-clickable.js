// Script pour rendre les tags cliquables
document.addEventListener('DOMContentLoaded', function() {
  // Sélectionner tous les tags
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
    tag.addEventListener('click', () => {
      const tagText = tag.textContent.trim();
      // Activer la recherche avec le tag
      const searchInput = document.querySelector('.md-search__input');
      if (searchInput) {
        searchInput.value = tagText;
        searchInput.form.submit();
      }
    });
  });
});
