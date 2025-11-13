/**
 * Script de diagnostic pour le consentement aux cookies
 * À exécuter dans la console du navigateur pour débugger
 */

(function() {
  console.log('=== DIAGNOSTIC CONSENTEMENT AUX COOKIES ===');
  console.log('');

  // 1. Vérifier localStorage
  console.log('1. Contenu de localStorage :');
  console.log('   Nombre d\'items:', localStorage.length);

  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const value = localStorage.getItem(key);

    if (key.includes('consent') || key.includes('cookie') || key.includes('__md')) {
      console.log(`   ${key}:`, value);

      // Essayer de parser si c'est du JSON
      try {
        const parsed = JSON.parse(value);
        console.log('   └─ Parsed:', parsed);
      } catch (e) {
        console.log('   └─ Non-JSON');
      }
    }
  }

  console.log('');

  // 2. Vérifier la clé spécifique MkDocs Material
  console.log('2. Clé __md_consent :');
  const mdConsent = localStorage.getItem('__md_consent');
  if (mdConsent) {
    console.log('   Valeur brute:', mdConsent);
    try {
      const parsed = JSON.parse(mdConsent);
      console.log('   Parsed:', parsed);
      console.log('   Type:', typeof parsed);
      console.log('   Propriétés:', Object.keys(parsed));
    } catch (e) {
      console.log('   Erreur parsing:', e.message);
    }
  } else {
    console.log('   ❌ Non trouvé');
  }

  console.log('');

  // 3. Vérifier les scripts GA4 dans le DOM
  console.log('3. Scripts Google Analytics dans le DOM :');
  const gaScripts = document.querySelectorAll('script[src*="googletagmanager.com"]');
  console.log('   Nombre de scripts:', gaScripts.length);
  gaScripts.forEach((script, i) => {
    console.log(`   Script ${i + 1}:`, script.src);
  });

  console.log('');

  // 4. Vérifier si gtag est défini
  console.log('4. État de gtag :');
  console.log('   typeof gtag:', typeof gtag);
  console.log('   gtag défini:', typeof gtag !== 'undefined');

  console.log('');

  // 5. Vérifier dataLayer
  console.log('5. État de dataLayer :');
  console.log('   typeof dataLayer:', typeof dataLayer);
  if (typeof dataLayer !== 'undefined') {
    console.log('   dataLayer.length:', dataLayer.length);
    console.log('   dataLayer:', dataLayer);
  }

  console.log('');
  console.log('=== FIN DU DIAGNOSTIC ===');
})();
