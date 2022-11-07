import os
import time
import threading
import requests

from backed.models import Features, Movie
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

setting = getattr(settings, "API_DOWNLOADER", {"url": None, "time": 0})

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
        print("The response is not in JSON format")
        return {}

    return response


def start_downloader():
    """
    Funkce pro zapnutí automatického stahování z API.
    URL adresa a čas periody se nastavuje v django.settings.
    """
    data = get_json_data(setting.get("url"))

    if data == {}:
        threading.Timer(setting.get("time"), start_downloader).start()
        return

    # print(f"Nastavení pro stáhování je {setting}")
    for movie in data:
        try:
            movieDB = Movie.objects.get(name=movie.get("name"))
        except ObjectDoesNotExist:
            print("Přidání nového filmu do databáze")
        else:
            # print("V databázi už existuje tento objekt")
            continue

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
                print("Feature neexistuje, přidává se do databáze")
                featureDB = Features(name=feature)
                featureDB.save()

            featureDB.movies.add(movieDB)
            featureDB.save()

    threading.Timer(setting.get("time"), start_downloader).start()






