import os
import time
import threading
import requests

from backed.models import Features, Movie
from django.core.exceptions import ObjectDoesNotExist

def get_json_data(url: str) -> dict:
    """
    Funkce pro stažení dat ve formátu JSON z url adresy.
    :param url: URL adresa pro stažení dat
    :return: JSON data v typu dict.
    """
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print(f"HTML error code: {r.status_code}")
            return {}
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return {}
    except Exception as err:
        print(f'Other error occurred: {err}')
        return {}

    try:
        response = r.json()
    except requests.exceptions.JSONDecodeError:
        print("Odpověď není ve formátu JSON")
        return {}

    return response


def main():
    data = get_json_data("https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json")

    for movie in data:
        features = movie.get("features")
        movieDB = Movie(name=movie.get("name"),
                        shortName=movie.get("shortName"),
                        iconUri=movie.get("iconUri"),
                        manifestUri=movie.get("manifestUri"),
                        description=movie.get("description"))
        movieDB.save()
 
        for feature in features:
            try:
                featureDB = Features.objects.get(name=feature)
            except ObjectDoesNotExist:
                print("Feature neexistuje, přidává se do dazabáze")
                featureDB = Features(name=feature)
                featureDB.save()

            featureDB.movies.add(movieDB)
            featureDB.save()











