/**
 * Google Analytics 4 - Événements personnalisés
 * Formation Systeme.io - L'Essentiel en Soi
 *
 * Événements trackés :
 * - Clics sur boutons de partage social
 * - Téléchargements de fichiers PDF
 * - Temps passé sur chaque guide
 * - Clics sur liens de navigation
 * - Expansion des admonitions (tips, warnings)
 */

// === DÉTECTION DE L'ENVIRONNEMENT ===
const isLocalhost = window.location.hostname === 'localhost' ||
                   window.location.hostname === '127.0.0.1';

// === GESTION DU CONSENTEMENT AUX COOKIES ===
// MkDocs Material stocke le consentement dans localStorage sous la clé "__md_consent"
function hasAnalyticsConsent() {
  try {
    const consent = localStorage.getItem('__md_consent');
    if (!consent) {
      // Pas de consentement stocké = pas encore demandé ou refusé
      return false;
    }

    const consentData = JSON.parse(consent);

    // Vérifier différents formats possibles de MkDocs Material
    // Format 1: { analytics: true }
    if (consentData.analytics === true) return true;

    // Format 2: { google: { analytics: true } }
    if (consentData.google && consentData.google.analytics === true) return true;

    // Format 3: { accepted: true } (acceptation globale)
    if (consentData.accepted === true) return true;

    return false;
  } catch (e) {
    console.warn('[Analytics] Erreur lecture consentement:', e);
    // En cas d'erreur, on considère que le consentement n'est pas donné
    return false;
  }
}

// Écouter les changements de consentement
function listenForConsentChange(callback) {
  let callbackExecuted = false;

  function checkAndExecute() {
    if (!callbackExecuted && hasAnalyticsConsent()) {
      callbackExecuted = true;
      console.log('[Analytics] ✅ Consentement Analytics accordé');
      callback();
    }
  }

  // Méthode 1: Observer les changements dans localStorage (autres onglets)
  window.addEventListener('storage', function(e) {
    if (e.key === '__md_consent') {
      console.log('[Analytics] 🔔 Changement de consentement détecté (storage event)');
      checkAndExecute();
    }
  });

  // Méthode 2: Observer les événements personnalisés de MkDocs Material
  document.addEventListener('consent', function(e) {
    console.log('[Analytics] 🔔 Événement consentement MkDocs Material détecté');
    checkAndExecute();
  });

  // Méthode 3: Observer l'apparition du script GA4 dans le DOM
  // Quand l'utilisateur accepte, MkDocs Material injecte le script
  const observer = new MutationObserver(function(mutations) {
    for (let mutation of mutations) {
      for (let node of mutation.addedNodes) {
        if (node.tagName === 'SCRIPT' &&
            node.src &&
            node.src.includes('googletagmanager.com')) {
          console.log('[Analytics] 🔔 Script GA4 ajouté au DOM (consentement accordé)');
          observer.disconnect(); // Arrêter l'observation
          checkAndExecute();
          return;
        }
      }
    }
  });

  observer.observe(document.documentElement, {
    childList: true,
    subtree: true
  });

  // Méthode 4: Polling périodique (fallback)
  // Vérifier toutes les 2 secondes pendant 30 secondes max
  let pollCount = 0;
  const maxPolls = 15;
  const pollInterval = setInterval(function() {
    pollCount++;
    if (callbackExecuted || pollCount >= maxPolls) {
      clearInterval(pollInterval);
      return;
    }

    if (hasAnalyticsConsent()) {
      console.log('[Analytics] 🔔 Consentement détecté (polling)');
      clearInterval(pollInterval);
      checkAndExecute();
    }
  }, 2000);
}

// === ATTENDRE QUE GTAG SOIT DISPONIBLE ===
function waitForGtag(callback, maxAttempts = 100, interval = 100) {
  let attempts = 0;
  let scriptDetected = false;
  let diagnosticLogged = false;

  const checkGtag = setInterval(() => {
    attempts++;

    // Vérifier si le script GA4 est présent dans le DOM (seulement lors des dernières tentatives)
    if (!scriptDetected && attempts > maxAttempts - 10) {
      const gaScripts = document.querySelectorAll('script[src*="googletagmanager.com"]');
      if (gaScripts.length > 0) {
        scriptDetected = true;
        if (!diagnosticLogged) {
          console.log('[Analytics] 📡 Script Google Analytics détecté dans le DOM');
          console.log('[Analytics] Nombre de scripts GA4 :', gaScripts.length);
          gaScripts.forEach((script, idx) => {
            console.log(`[Analytics]   Script ${idx + 1}:`, script.src);
          });
          diagnosticLogged = true;
        }
      }
    }

    if (typeof gtag !== 'undefined') {
      clearInterval(checkGtag);
      console.log('[Analytics] ✅ Google Analytics (gtag) chargé');
      callback();
    } else if (attempts >= maxAttempts) {
      clearInterval(checkGtag);

      // Diagnostic détaillé du problème
      console.group('[Analytics] 🔍 Diagnostic du problème');
      console.log('Hostname:', window.location.hostname);
      console.log('URL complète:', window.location.href);
      console.log('Scripts GA4 détectés dans le DOM:', scriptDetected ? '✅ OUI' : '❌ NON');
      console.log('Consentement Analytics:', hasAnalyticsConsent() ? '✅ ACCORDÉ' : '❌ NON ACCORDÉ');

      if (scriptDetected) {
        if (!hasAnalyticsConsent()) {
          console.warn('[Analytics] ⚠️ Le script GA4 est présent mais le consentement n\'est pas accordé');
          console.log('[Analytics] 🍪 Cause: Système de consentement aux cookies actif');
          console.log('[Analytics] 💡 Solutions:');
          console.log('[Analytics]    1. Cliquer sur "Accepter" dans la bannière de cookies');
          console.log('[Analytics]    2. Gérer les préférences et activer "Analytics"');
          console.log('[Analytics]    3. Le tracking démarrera automatiquement après acceptation');
        } else {
          console.warn('[Analytics] ❌ Le script GA4 est présent mais gtag n\'est pas défini');
          console.warn('[Analytics] 🛡️ Cause probable: Bloqueur de publicité actif');
          console.log('[Analytics] 💡 Solutions:');
          console.log('[Analytics]    1. Désactiver uBlock Origin, AdBlock ou autre bloqueur');
          console.log('[Analytics]    2. Tester en navigation privée sans extensions');
          console.log('[Analytics]    3. Ajouter une exception pour ce site dans le bloqueur');
        }
      } else {
        console.warn('[Analytics] ❌ Aucun script Google Analytics trouvé dans le DOM');
        console.warn('[Analytics] 🔧 Causes possibles:');
        console.log('[Analytics]    1. Consentement aux cookies non accordé (vérifier la bannière)');
        console.log('[Analytics]    2. ID GA4 non configuré dans mkdocs.yml');
        console.log('[Analytics]       → Section: extra.analytics.property');
        console.log('[Analytics]    3. Version de MkDocs Material < 9.0.0 (vérifier requirements.txt)');
        console.log('[Analytics]    4. Configuration mkdocs.yml incorrecte (ancienne syntaxe google_analytics)');
      }
      console.groupEnd();

      if (isLocalhost) {
        console.log('[Analytics] ℹ️ Mode développement - Simulation du tracking (gtag non chargé)');
        // En dev local, créer un gtag factice pour le debugging
        window.gtag = function(...args) {
          console.log('[Analytics DEV]', ...args);
        };
        callback();
      } else {
        console.warn('[Analytics] ⚠️ Google Analytics (gtag) non disponible après', maxAttempts * interval, 'ms');
        console.log('[Analytics] Les événements ne seront pas trackés');
      }
    }
  }, interval);
}

// === FONCTION D'INITIALISATION ===
function initializeAnalytics() {
  console.log('[Analytics] 🚀 Initialisation des événements personnalisés');

  // Attendre que le DOM soit chargé
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupEventTracking);
  } else {
    setupEventTracking();
  }
}

// === CONFIGURATION DES ÉVÉNEMENTS ===
function setupEventTracking() {

    // === 1. TRACKING DES BOUTONS DE PARTAGE SOCIAL ===
    const shareButtons = document.querySelectorAll('.share-button');

    if (shareButtons.length > 0) {
      shareButtons.forEach(button => {
        button.addEventListener('click', function(e) {
          const network = this.classList.contains('twitter') ? 'Twitter' :
                         this.classList.contains('facebook') ? 'Facebook' :
                         this.classList.contains('linkedin') ? 'LinkedIn' :
                         this.classList.contains('email') ? 'Email' : 'Unknown';

          const pageTitle = document.title;
          const pageUrl = window.location.pathname;

          gtag('event', 'share', {
            'event_category': 'Social',
            'event_label': network,
            'page_title': pageTitle,
            'page_path': pageUrl,
            'value': 1
          });

          console.log(`[Analytics] Partage : ${network} - ${pageTitle}`);
        });
      });

      console.log(`[Analytics] ${shareButtons.length} boutons de partage trackés`);
    }


    // === 2. TRACKING DES TÉLÉCHARGEMENTS PDF ===
    const pdfLinks = document.querySelectorAll('a[href$=".pdf"]');

    if (pdfLinks.length > 0) {
      pdfLinks.forEach(link => {
        link.addEventListener('click', function(e) {
          const fileName = this.href.split('/').pop();
          const pageTitle = document.title;

          gtag('event', 'download', {
            'event_category': 'Downloads',
            'event_label': fileName,
            'page_title': pageTitle,
            'value': 1
          });

          console.log(`[Analytics] Téléchargement PDF : ${fileName}`);
        });
      });

      console.log(`[Analytics] ${pdfLinks.length} liens PDF trackés`);
    }


    // === 3. TRACKING DU TEMPS PASSÉ SUR LA PAGE ===
    let startTime = Date.now();
    let pageTitle = document.title;
    let pagePath = window.location.pathname;

    // Identifier le numéro du guide depuis le titre
    const guideMatch = pageTitle.match(/(\d{2})\s*-/);
    const guideNumber = guideMatch ? guideMatch[1] : 'unknown';

    // Envoyer le temps passé au départ de la page
    window.addEventListener('beforeunload', function() {
      const timeSpent = Math.round((Date.now() - startTime) / 1000); // en secondes

      // Ne tracker que si l'utilisateur a passé au moins 10 secondes
      if (timeSpent >= 10) {
        gtag('event', 'timing_complete', {
          'name': 'Guide Reading Time',
          'value': timeSpent,
          'event_category': 'Engagement',
          'event_label': `Guide ${guideNumber}`,
          'page_title': pageTitle,
          'page_path': pagePath
        });

        console.log(`[Analytics] Temps passé : ${timeSpent}s sur ${pageTitle}`);
      }
    });

    // Tracker également toutes les 60 secondes pour les longues sessions
    setInterval(function() {
      const timeSpent = Math.round((Date.now() - startTime) / 1000);

      if (timeSpent > 0 && timeSpent % 60 === 0) {
        gtag('event', 'scroll_engagement', {
          'event_category': 'Engagement',
          'event_label': `${timeSpent / 60} minutes`,
          'page_title': pageTitle,
          'value': timeSpent / 60
        });

        console.log(`[Analytics] Engagement : ${timeSpent / 60} minutes`);
      }
    }, 60000); // Toutes les 60 secondes


    // === 4. TRACKING DES CLICS SUR NAVIGATION ===
    const navButtons = document.querySelectorAll('.md-button, a[href*="GUIDE"]');

    if (navButtons.length > 0) {
      navButtons.forEach(button => {
        button.addEventListener('click', function(e) {
          const href = this.getAttribute('href');
          const buttonText = this.textContent.trim();

          // Déterminer le type de navigation
          let navType = 'Internal Link';
          if (buttonText.includes('Suivant') || buttonText.includes('→')) {
            navType = 'Next Guide';
          } else if (buttonText.includes('Précédent') || buttonText.includes('←')) {
            navType = 'Previous Guide';
          } else if (buttonText.includes('Accueil') || buttonText.includes('🏠')) {
            navType = 'Home';
          }

          gtag('event', 'navigation', {
            'event_category': 'Navigation',
            'event_label': navType,
            'target_url': href,
            'button_text': buttonText,
            'value': 1
          });

          console.log(`[Analytics] Navigation : ${navType} → ${href}`);
        });
      });

      console.log(`[Analytics] ${navButtons.length} boutons de navigation trackés`);
    }


    // === 5. TRACKING DES ADMONITIONS (TIPS, WARNINGS) ===
    const admonitions = document.querySelectorAll('.admonition');

    if (admonitions.length > 0) {
      admonitions.forEach((admonition, index) => {
        // Certaines admonitions peuvent être collapsibles
        const title = admonition.querySelector('.admonition-title');

        if (title) {
          title.addEventListener('click', function() {
            const admonitionType = admonition.classList[1] || 'unknown'; // success, tip, warning, etc.
            const titleText = this.textContent.trim();

            gtag('event', 'admonition_click', {
              'event_category': 'Engagement',
              'event_label': admonitionType,
              'admonition_title': titleText,
              'value': 1
            });

            console.log(`[Analytics] Admonition cliquée : ${admonitionType} - ${titleText}`);
          });
        }
      });

      console.log(`[Analytics] ${admonitions.length} admonitions trackées`);
    }


    // === 6. TRACKING DU SCROLL (PROFONDEUR DE LECTURE) ===
    let maxScroll = 0;
    let scrollMilestones = [25, 50, 75, 90, 100];
    let trackedMilestones = [];

    window.addEventListener('scroll', function() {
      const windowHeight = window.innerHeight;
      const documentHeight = document.documentElement.scrollHeight;
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

      const scrollPercent = Math.round((scrollTop + windowHeight) / documentHeight * 100);

      if (scrollPercent > maxScroll) {
        maxScroll = scrollPercent;

        // Vérifier les jalons
        scrollMilestones.forEach(milestone => {
          if (scrollPercent >= milestone && !trackedMilestones.includes(milestone)) {
            trackedMilestones.push(milestone);

            gtag('event', 'scroll_depth', {
              'event_category': 'Engagement',
              'event_label': `${milestone}%`,
              'page_title': pageTitle,
              'value': milestone
            });

            console.log(`[Analytics] Scroll : ${milestone}% de la page`);
          }
        });
      }
    });


    // === 7. TRACKING DES LIENS EXTERNES ===
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="mehdisback.github.io"])');

    if (externalLinks.length > 0) {
      externalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
          const url = this.href;
          const domain = new URL(url).hostname;

          gtag('event', 'external_link', {
            'event_category': 'Outbound',
            'event_label': domain,
            'target_url': url,
            'value': 1
          });

          console.log(`[Analytics] Lien externe : ${domain}`);
        });
      });

      console.log(`[Analytics] ${externalLinks.length} liens externes trackés`);
    }


    // === 8. TRACKING DE LA RECHERCHE (SI ACTIVÉE) ===
    const searchInput = document.querySelector('[data-md-component="search-query"]');

    if (searchInput) {
      let searchTimeout;

      searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);

        searchTimeout = setTimeout(() => {
          const query = this.value.trim();

          if (query.length >= 3) {
            gtag('event', 'search', {
              'event_category': 'Search',
              'search_term': query,
              'value': 1
            });

            console.log(`[Analytics] Recherche : "${query}"`);
          }
        }, 1000); // Attendre 1 seconde après la dernière saisie
      });

      console.log('[Analytics] Recherche trackée');
    }


    // === 9. TRACKING DE LA COMPLÉTION DES CHECKLISTS ===
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    if (checkboxes.length > 0) {
      checkboxes.forEach((checkbox, index) => {
        checkbox.addEventListener('change', function() {
          const isChecked = this.checked;
          const label = this.nextSibling ? this.nextSibling.textContent.trim() : 'Unknown';

          gtag('event', 'checklist_item', {
            'event_category': 'Engagement',
            'event_label': isChecked ? 'Checked' : 'Unchecked',
            'item_text': label.substring(0, 50), // Limiter à 50 caractères
            'page_title': pageTitle,
            'value': isChecked ? 1 : 0
          });

          console.log(`[Analytics] Checklist : ${isChecked ? 'Cochée' : 'Décochée'} - ${label.substring(0, 30)}...`);
        });
      });

      console.log(`[Analytics] ${checkboxes.length} items de checklist trackés`);
    }


  console.log('[Analytics] ✅ Tous les événements personnalisés sont configurés');
}

// === POINT D'ENTRÉE ===
// Vérifier d'abord le consentement, puis attendre que gtag soit disponible

function startAnalytics() {
  console.log('[Analytics] 🚀 Démarrage du système d\'analytics');

  // DEBUG: Afficher le consentement brut
  const rawConsent = localStorage.getItem('__md_consent');
  console.log('[Analytics] 🔍 DEBUG - Consentement brut:', rawConsent);

  if (rawConsent) {
    try {
      const parsed = JSON.parse(rawConsent);
      console.log('[Analytics] 🔍 DEBUG - Consentement parsé:', parsed);
      console.log('[Analytics] 🔍 DEBUG - Propriétés:', Object.keys(parsed));
      console.log('[Analytics] 🔍 DEBUG - consent.analytics:', parsed.analytics);
      console.log('[Analytics] 🔍 DEBUG - consent.google:', parsed.google);
      console.log('[Analytics] 🔍 DEBUG - consent.accepted:', parsed.accepted);
    } catch (e) {
      console.warn('[Analytics] ⚠️ Erreur parsing consentement:', e);
    }
  }

  // Vérifier si on a déjà le consentement
  const hasConsent = hasAnalyticsConsent();
  console.log('[Analytics] 🔍 DEBUG - hasAnalyticsConsent():', hasConsent);

  if (hasConsent) {
    console.log('[Analytics] ✅ Consentement déjà accordé, initialisation...');
    waitForGtag(initializeAnalytics);
  } else {
    console.log('[Analytics] ⏳ En attente du consentement utilisateur...');
    console.log('[Analytics] 💡 Pour activer le tracking, acceptez les cookies Analytics');

    // Écouter les futurs changements de consentement
    listenForConsentChange(function() {
      console.log('[Analytics] 🎉 Consentement reçu, initialisation...');
      waitForGtag(initializeAnalytics);
    });
  }
}

// Démarrer quand le DOM est prêt
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', startAnalytics);
} else {
  startAnalytics();
}
