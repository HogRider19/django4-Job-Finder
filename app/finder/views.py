from django.shortcuts import redirect, render
from .utility import Analyzer
import requests
import json


def home(request):
    return render(request, 'finder/home.html')


def analysis(request):
    if request.method == 'GET':
        return render(request, 'finder/analysis.html')
    else:

        analyzer = Analyzer(request)
        analyzer.analysis(countData=int(request.POST['countData']))
        info = analyzer.get_all_info()

        mean_salary = analyzer.get_salary_plot()['straight']

    
        mean_salary_json = json.dumps(mean_salary)

        return render(
            request,
            'finder/analysis.html',
            {'info': info, 'mean_salary':mean_salary_json}
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