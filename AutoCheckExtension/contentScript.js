// Fonction pour gérer les boutons radio dans les divs avec la classe 'r1'
function handleRadioInputsInDivs() {
    console.log("Recherche des divs avec la classe 'r1'...");
    const divsWithClassR1 = document.querySelectorAll('div.r1');
    console.log(`Nombre de divs avec la classe 'r1' trouvé : ${divsWithClassR1.length}`);
    divsWithClassR1.forEach(div => {
      const radioGroups = new Set(); // Pour suivre les groupes de boutons radio déjà traités
      const radios = div.querySelectorAll('input[type="radio"]');
      console.log(`Nombre de boutons radio trouvés dans la div : ${radios.length}`);
      radios.forEach(radio => {
        if (!radioGroups.has(radio.name) && radio.checked) { // Vérifie si le bouton radio est le premier du groupe et est coché
          radioGroups.add(radio.name);
          console.log(`Bouton radio '${radio.name}' sélectionné.`);
        } else {
          radio.checked = false; // Décoche les autres boutons radio du même groupe
        }
      });
    });
  }
  
  // Exécute la fonction lors du chargement de la page
  handleRadioInputsInDivs();
  