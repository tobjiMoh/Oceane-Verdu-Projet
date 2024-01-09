# Importation du module PySimpleGUI pour la création d'interfaces graphiques
import PySimpleGUI as sg
# Importation du module threading pour utiliser des threads pour le rafraîchissement des données
import threading
# Importation du module time pour ajouter des délais dans le rafraîchissement
import time
# Importation du module requests pour effectuer des requêtes HTTP
import requests

# Fonction pour récupérer les données depuis une URL
def get_data(url):
    try:
        # Effectue une requête GET à l'URL spécifiée
        response = requests.get(url)
        # Lève une exception en cas de code HTTP d'erreur
        response.raise_for_status()
        # Parse la réponse JSON
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # En cas d'erreur lors de la requête, affiche un message et retourne None
        print(f"Erreur lors de la récupération des données depuis {url}: {e}")
        return None

# Fonction pour rafraîchir et mettre à jour les données dans la fenêtre
def fetch_and_update(window, url):
    while True:
        # Récupère les données depuis l'URL
        data = get_data(url)
        if data:
            # Formate les données pour affichage dans la fenêtre
            formatted_data = f"CO2: {data.get('CO2', '')}\nEclairement: {data.get('Eclairement', '')}\nHumidité: {data.get('Humidite', '')}\nTempérature: {data.get('Temperature', '')}\nDate: {data.get('Timestamp', '')}"
            # Met à jour l'élément d'affichage des données dans la fenêtre
            window['-DATA-'].update(formatted_data)
        # Délai de rafraîchissement de 5 secondes
        time.sleep(5)

# Fonction pour créer et afficher une fenêtre de données
def create_data_window(url):
    # Définition du layout de la fenêtre
    layout = [
        [sg.Text(f"Données provenant de l'URL : {url}")],
        [sg.Multiline(size=(60, 10), key='-DATA-', disabled=True)],
        [sg.Button('Quitter')]
    ]
    # Création de la fenêtre
    window = sg.Window('Données', layout, finalize=True)
    # Création et démarrage d'un thread pour le rafraîchissement des données
    thread = threading.Thread(target=fetch_and_update, args=(window, url))
    thread.daemon = True
    thread.start()
    # Boucle principale de la fenêtre
    while True:
        # Lecture des événements de la fenêtre avec un timeout pour rendre l'interface réactive
        event, values = window.read(timeout=100)
        # Condition de sortie si la fenêtre est fermée ou le bouton 'Quitter' est pressé
        if event == sg.WIN_CLOSED or event == 'Quitter':
            break
    # Fermeture de la fenêtre une fois la boucle terminée
    window.close()

# Fonction principale du script
def main():
    # Définition des URLs pour chaque salle
    urls = {
        'Salle 225': "http://applis.iut.univ-paris-diderot.fr/SALLE225/last/",
        'Salle 017': "http://172.20.28.224/SALLE017/last",
        'Amphi': "http://172.20.28.224/AMPHI/last"
    }

    # Définition du layout de la fenêtre principale
    layout = [
        [sg.Button(room) for room in urls.keys()],
        [sg.Button('Quitter')]
    ]

    # Création de la fenêtre principale
    main_window = sg.Window('Choix des salles', layout)

    # Boucle principale de la fenêtre principale
    while True:
        # Lecture des événements de la fenêtre principale
        event, values = main_window.read()
        # Condition de sortie si la fenêtre est fermée ou le bouton 'Quitter' est pressé
        if event == sg.WIN_CLOSED or event == 'Quitter':
            break
        # Si un bouton correspondant à une salle est pressé, crée la fenêtre de données associée
        if event in urls:
            create_data_window(urls[event])

    # Fermeture de la fenêtre principale une fois la boucle terminée
    main_window.close()

# Exécution de la fonction principale si le script est exécuté directement
if __name__ == "__main__":
    main()
