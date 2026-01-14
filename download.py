import requests
from datetime import datetime

def download_file():
    lien_carte = 'https://www.data.gouv.fr/api/1/datasets/r/bfba7898-aed3-40ec-aa74-abb73b92a363'
    today = datetime.now().strftime("%Y%m%d_%H%M%S")
    reponse = requests.get(lien_carte)
    with open(f'carte_{today}.geojson', 'wb') as f:
        f.write(reponse.content)
    print(f"Téléchargement effectué : carte_{today}.geojson")

if __name__ == "__main__":
    download_file()