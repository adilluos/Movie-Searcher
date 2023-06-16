from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
import requests

def index(request):
    #Making try-except block for excluding KeyError
    #This is made because in post request may be field which API cannot work with
    try:
        #accepting POST request
        film_title = request.POST.get('message', '')

        #when POST has been made, the webpage changes
        if request.method == 'POST':
            film_title1 = str(film_title)
            url = "https://imdb8.p.rapidapi.com/auto-complete"

            querystring = {"q": film_title1}

            headers = {
                "X-RapidAPI-Key": "62008096b2mshfb208128fa454d7p14c074jsne7881457ef9a",
                "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            #accepting all information from API
            title = response.json()["d"][0]["l"]
            image_url = response.json()["d"][0]["i"]["imageUrl"]
            year = response.json()["d"][0]["y"]
            cast = response.json()["d"][0]["s"]
            title1 = response.json()["d"][1]["l"]
            image_url1 = response.json()["d"][1]["i"]["imageUrl"]
            year1 = response.json()["d"][1]["y"]
            cast1 = response.json()["d"][1]["s"]
            title2 = response.json()["d"][2]["l"]
            image_url2 = response.json()["d"][2]["i"]["imageUrl"]
            year2 = response.json()["d"][2]["y"]
            cast2 = response.json()["d"][2]["s"]
            title = title.replace('\'', '')
            cast = cast.replace('\'', '')
            year = str(year)
            title1 = title1.replace('\'', '')
            cast1 = cast1.replace('\'', '')
            year1 = str(year1)
            title2 = title2.replace('\'', '')
            cast2 = cast2.replace('\'', '')
            year2 = str(year2)

            #the variable which gives info to HTML page
            context = {
                'title': title,
                "image_url": image_url,
                "year": year,
                "cast": cast,
                'title1': title1,
                "image_url1": image_url1,
                "year1": year1,
                "cast1": cast1,
                'title2': title2,
                "image_url2": image_url2,
                "year2": year2,
                "cast2": cast2,
                #The 2 variables below create the if statement in html page,
                #Which allow the webpage to show certain information in certain conditions
                'is_post_request': True,
                'errors': False
            }
            return render(request, 'main/index.html', context)
        #when POST has not been made. Basically, the first page
        return render(request, 'main/index.html', {'is_post_request': False, 'no_errors': False})
    except (KeyError, IndexError):
        return render(request, 'main/index.html', {'is_post_request': False, 'no_errors': True})
