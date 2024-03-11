// Écoute l'événement de chargement d'onglet
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete') {
      // Injecte le contenu script dans la page
      chrome.scripting.executeScript({
        target: {tabId: tabId},
        files: ['contentScript.js']
      });
    }
  });
  