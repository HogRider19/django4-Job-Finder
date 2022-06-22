from audioop import avg
from django.shortcuts import redirect, render
import requests
import json


def home(request):
    return render(request, 'finder/home.html')


def analysis(request):
    if request.method == 'GET':
        return render(request, 'finder/analysis.html')
    else:

        params = {
            'text': request.POST['profession'],
            'per_page':'100',
            'page':'0',
            'only_with_salary':True,
        }

        vacancies = []
        for index in range(1,int(request.POST['countData'])):
            try:
                params['page'] = str(index)
                vacancies += list(map(
                    lambda x: x['salary'],
                    requests.get('https://api.hh.ru/vacancies', params=params).json()['items']
                ))
            except KeyError:
                break

        count = len(vacancies)
        salary_from = [i['from'] for i in vacancies if i['from'] != None]
        salary_to = [i['to'] for i in vacancies if i['to'] != None]
        max_salary = max(salary_from + salary_to)
        salary_min = min(salary_from + salary_to)
        salary_avg = sum(salary_from + salary_to)/count

        return render(
            request,
            'finder/analysis.html',
            {'info':{'count':count, 'max':max_salary, 'min':salary_min, 'avg':salary_avg}}
        )


def searchvacancies(request):
    if request.method == 'GET':
        return render(request, 'finder/searchvacancies.html')
    else:

        params = {
            'text': request.POST['profession'],
            'per_page':'30',
        }

        vacancies = requests.get('https://api.hh.ru/vacancies', params=params).json()['items']

        return render(request, 'finder/searchvacancies.html', {'vacancies' : vacancies})