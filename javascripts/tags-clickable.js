// Script pour rendre les tags cliquables et navigables
document.addEventListener('DOMContentLoaded', function() {
  // Attendre que Material for MkDocs soit complètement chargé
  setTimeout(() => {
    const tags = document.querySelectorAll('.md-tag');

    tags.forEach(tag => {
      // Rendre le tag cliquable visuellement
      tag.style.cursor = 'pointer';

      // Clic sur le tag = redirection vers la section du tag
      tag.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const tagText = tag.textContent.trim();
        const tagSlug = tagText.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

        // Rediriger vers la page tags avec l'ancre du tag
        const baseUrl = window.location.origin + window.location.pathname.split('/').slice(0, -1).join('/');
        window.location.href = baseUrl + '/tags/#tag-' + tagSlug;
      });
    });
  }, 500);
});
