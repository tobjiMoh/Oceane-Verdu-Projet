**# Oceane-Verdu-Projet
Projet IoT**
# Explication du Script PySimpleGUI avec Rafraîchissement de Données

Ce script Python utilise PySimpleGUI pour créer une interface graphique qui permet de visualiser en temps réel les données provenant de différentes salles. Les données sont obtenues à partir d'URLs spécifiques et sont rafraîchies toutes les 5 secondes.

## Structure du Code

### Fonctions de Récupération des Données
- **get_data(url):** Effectue une requête HTTP GET à une URL donnée et renvoie les données JSON obtenues.
- **fetch_and_update(window, url):** Fonction exécutée dans un thread qui récupère les données depuis une URL et met à jour l'affichage dans une fenêtre PySimpleGUI.

### Création de Fenêtres
- **create_data_window(url):** Crée une nouvelle fenêtre pour afficher les données d'une salle spécifique en utilisant PySimpleGUI.

### Fonction Principale
- **main():** Fonction principale du script qui définit les URLs pour chaque salle, crée la fenêtre principale avec les boutons correspondants, et gère les événements.

## Utilisation des Threads
Le script utilise des threads pour permettre le rafraîchissement continu des données en arrière-plan tout en maintenant la réactivité de l'interface utilisateur.

## Utilisation de PySimpleGUI
Le layout de chaque fenêtre est défini de manière à afficher clairement les données et inclut un bouton 'Quitter' pour fermer la fenêtre.

## Exécution
La fonction principale `main()` est exécutée lorsque le script est lancé directement, lançant ainsi l'interface utilisateur et le rafraîchissement des données.

---



