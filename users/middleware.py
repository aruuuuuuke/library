# from django.utils.deprecation import MiddlewareMixin
# from django.http import HttpResponseBadRequest
#
# class AgeClubMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         if request.path == '/register/' and request.method == 'POST':
#             age =  int(request.POST.get('age'))
#             if age < 7 :
#                 return HttpResponseBadRequest("Надо подрасти")
#             elif 7 <= age < 12:
#                 request.club = 'Детский клуб'
#             elif 12 <= age < 18:
#                 request.club = 'Подростковый клуб'
#             elif 18 <= age < 60:
#                 request.club = 'Взрослый клуб'
#             else:
#                 return HttpResponseBadRequest("Пора отдохнуть")
#         elif request.path == '/login/' and request.method == 'GET':
#             setattr(request, 'club', 'Клуб не определен')