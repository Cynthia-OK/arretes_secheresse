import requests
from datetime import datetime
import pytz
import time

def is_time_to_download():
    # Définir le fuseau horaire de Paris
    paris_tz = pytz.timezone('Europe/Paris')
    now = datetime.now(paris_tz)
    # Vérifier si l'heure actuelle est 11h25 (avec une marge de 2 minutes)
    return (now.hour == 11 and now.minute == 25) or (now.hour == 11 and now.minute == 26)

def download_file():
    lien_carte = 'https://www.data.gouv.fr/api/1/datasets/r/bfba7898-aed3-40ec-aa74-abb73b92a363'
    today = datetime.now().strftime("%Y%m%d_%H%M%S")
    reponse = requests.get(lien_carte)
    # Vérifier que la requête a réussi
    reponse.raise_for_status()
    # créer le nom du fichier avec la date actuelle
    filename = f"carte_{today}.geojson"
    with open(filename, 'wb') as f:
        f.write(reponse.content)
    print(f"Téléchargement effectué : carte_{today}.geojson")

def main():
    if is_time_to_download():
        print(f"Heure actuelle à Paris : {datetime.now(pytz.timezone('Europe/Paris')).strftime('%H:%M')}")
        download_file()
    else:
        print(f"Heure actuelle à Paris : {datetime.now(pytz.timezone('Europe/Paris')).strftime('%H:%M')} - Pas 11h25, rien à faire.")

if __name__ == "__main__":
    main()