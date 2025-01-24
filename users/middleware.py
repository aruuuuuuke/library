from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class AgeClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience =  int(request.POST.get('experience'))
            if experience < 1 :
                return HttpResponseBadRequest("Вам надо еще набраться опыта")
            elif 1 <= experience < 3:
                request.salary = 'Ваша зарплата будет 1000$'
            elif 3 <= experience < 6:
                request.salary = 'Ваша зарплата будет 2000$'
            elif 6 <= experience < 10:
                request.salary = 'Ваша зарплата будет 5000$'
            else:
                return HttpResponseBadRequest("Пора отдохнуть")
        elif request.path == '/login/' and request.method == 'GET':
            setattr(request, 'salary', 'Зарплата не определена')