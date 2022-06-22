from django.shortcuts import redirect, render
import requests
import json


def home(request):
    return render(request, 'finder/home.html')


def analysis(request):
    if request.method == 'GET':
        return render(request, 'finder/analysis.html')
    else:
        return render(request, 'finder/analysis.html')


def searchvacancies(request):
    if request.method == 'GET':
        return render(request, 'finder/searchvacancies.html')
    else:

        params = {
            'text': request.POST['profession'],
            'per_page':'20',
        }

        vacancies_json = json.loads(
            requests.get('https://api.hh.ru/vacancies', params=params).text
        )

        '''
        vacancies = {
            'id':,
            'name' :,
            'area':{
                'id':,
                'name':
            },
            'salary':{
                'from':,
                'to':,
                'currenscy':,
            },
            'address':{
                'city':,
                ''
            }
        }
        '''

        return render(request, 'finder/searchvacancies.html', {'vacancies' : 1})