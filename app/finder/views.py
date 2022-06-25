from django.shortcuts import redirect, render
from .utility import Analyzer
import requests


def home(request):
    return render(request, 'finder/home.html')


def analysis(request):
    if request.method == 'GET':
        return render(request, 'finder/analysis.html')
    else:

        analyzer = Analyzer(request)
        analyzer.analysis(countData=int(request.POST['countData']))
        info = analyzer.get_all_info()

        straight_dis_point = analyzer.get_salary_plot()['straight']

        print(straight_dis_point)

        return render(
            request,
            'finder/analysis.html',
            {'info': info, 'straight_dis_point':straight_dis_point}
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