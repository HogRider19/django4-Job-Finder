import requests
import json


class Analyzer:

    BASE_API_URL = 'https://api.hh.ru/vacancies'

    def __init__(self, request) -> None:
        self._request = request
        self._salary_list = []
        self._salary_info = {}
        self._params = {
            'text': request.POST['profession'],
            'per_page':'100',
            'only_with_salary':True,
        }


    def analysis(self, countData):
        self._salary_list = []
        self._params['page'] = 0
        self._salary_info = {}

        for index in range(countData):
            try:
                self._params['page'] = str(index)
                self._salary_list += list(map(
                    lambda x: x['salary'],
                    requests.get(Analyzer.BASE_API_URL, params=self._params).json()['items']
                ))
            except KeyError:
                break
        
        del self._params['page']

        self._salary_info = Analyzer.get_salary_info(self._salary_list)


    def get_all_info(self):
        return {
            'salary_list': self._salary_list,
            'salary_info': self._salary_info,
        }

    
    def get_salary_plot(self):
        mean_salary = []
        for i in self._salary_list:
            if i['from'] !=  None and i['to'] !=  None:
                mean_salary += [int((i['from'] + i['to'])/2)]
            elif i['from'] !=  None:
                mean_salary += [int(i['from'])]
            elif i['to'] != None:
                mean_salary += [int(i['to'])]

        mean_salary = sorted(mean_salary)

        return {
            'straight': mean_salary,
        }
                


    @staticmethod
    def get_salary_info(slary_list):
        salary_from = [i['from'] for i in slary_list if i['from'] != None and i['currency'] == 'RUR']
        salary_to = [i['to'] for i in slary_list if i['to'] != None and i['currency'] == 'RUR']
        salary = salary_from + salary_to

        count = len(salary)
        salary_max = max(salary)
        salary_min = min(salary)
        salary_avg = sum(salary)/count
        
        return {
            'count': count,
            'salary_from': salary_from,
            'salary_to': salary_to,
            'salary_max': salary_max,
            'salary_min': salary_min,
            'salary_avg': salary_avg,
        }