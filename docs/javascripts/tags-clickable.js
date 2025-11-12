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

        // Construire l'URL de base (garder seulement le répertoire racine, pas le nom de la page)
        const pathParts = window.location.pathname.split('/').filter(p => p);
        // Si le premier segment n'est pas un guide (ne commence pas par un chiffre), on le garde (ex: formation-systemio)
        const isFirstPartRepo = pathParts.length > 0 && !/^\d/.test(pathParts[0]);
        const basePath = isFirstPartRepo ? '/' + pathParts[0] : '';

        // Rediriger vers la page tags avec l'ancre du tag
        window.location.href = window.location.origin + basePath + '/tags/#tag-' + tagSlug;
      });
    });
  }, 500);
});
