$(document).ready(function() {
    let points = 0; // Initialisation du score

    function createContainer() {
        // Vérifier s'il y a plus de 5 conteneurs, si oui, supprimer le plus ancien
        if ($('.container').length >= 5) {
            $('.container').first().remove();
        }

        // Générer une position horizontale aléatoire pour le conteneur
        let containerX = Math.round(Math.random() * ($('.screen').width() - 100)); // Largeur ajustée du conteneur
        let container = $('<div class="container">').css({
            "margin-left": containerX
        });

        // Générer une question de multiplication aléatoire
        let limit = parseInt($('#limit').val()); // Parser la limite entrée en un entier
        let randomNum1 = Math.round(Math.random() * limit);
        let randomNum2 = Math.round(Math.random() * limit);
        let paragraphText = randomNum1.toString() + " × " +  randomNum2.toString();
        let paragraph = $('<p>').text(paragraphText);
        container.data('result', randomNum1 * randomNum2); // Stocker le résultat de la multiplication dans les données du conteneur
        container.append(paragraph);

        // Ajouter le conteneur à l'écran
        $('.screen').append(container);

        // Déplacer le conteneur vers le bas toutes les 2 secondes
        container.intervalID = setInterval(function() {
            let currentPosition = parseInt(container.css('margin-top')) || 0;
            let screenHeight = $('.screen').height();
            if (currentPosition < screenHeight - container.height()) {
                container.css('margin-top', currentPosition + 50 + 'px'); // Déplacer le conteneur de 10px vers le bas
            } else {
                clearInterval(container.intervalID); // Arrêter l'animation une fois que le conteneur atteint le bas
                container.remove(); // Supprimer le conteneur une fois qu'il a atteint le bas de l'écran
            }
        }, 2000); // Toutes les 2 secondes
    }

    // Gestionnaire d'événements pour le champ de limite
    $("#limit").on('keyup', function(e) {
        if (e.key === 'Enter') {
            // Démarrer la boucle de jeu
            createContainer(); // Créer le premier conteneur
            $("#answer").focus(); // Mettre le focus sur le champ de réponse
            $('#points').html(points); // Mettre à jour l'affichage des points
            // Ajouter un gestionnaire d'événements pour le champ de réponse
            $('#answer').off('keyup').on('keyup', function(e) {
                if (e.key === 'Enter') {
                    let answer = parseInt($('#answer').val());
                    let result = $('.container').last().data('result'); // Récupérer le résultat de la multiplication depuis les données du dernier conteneur ajouté
                    if (answer === result) {
                        points++; // Incrémenter le score si la réponse est correcte
                        $('.container').last().remove(); // Supprimer le conteneur correspondant
                        $('#points').html(points); // Mettre à jour l'affichage des points
                    }
                    $('#answer').val(''); // Effacer le champ de réponse
                }
            });
        }
    });
});
