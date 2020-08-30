from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home_view, name="Homepage view")
]

# from django.shortcuts import render
# from django.http import HttpResponse

# def home_view(request):
#     global your_score
#     if request.method == "POST":
#         if request.POST.get("submit"):
#             q1 = request.POST.get("question-1")
#             q2 = request.POST.get("question-2")
#             q3 = request.POST.get("question-3")
#             q4 = request.POST.get("question-4")
#             q5 = request.POST.get("question-5")
#             q6 = request.POST.get("question-6")
#             q7 = request.POST.get("question-7")
#             q8 = request.POST.get("question-8")
#             q9 = request.POST.get("question-9")
#             q10 = request.POST.get("question-10")
#             values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
#             answers = [
#                 'answer-1', 'answer-2', 'answer-3', 'answer-4', 'answer-1,' 'answer-2', 'answer-3',
#                 'answer-4', 'answer-1', 'answer-2'
#             ]
#             print(values, "first")
#             if values == answers:
#                 print(values, 'second')
#                 # Using the HTTPResponse to return strings/HTMl
#                 html = '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style>you scored 95%</p></div>'
#                 your_score = HttpResponse(html)
#                 print(values, 'third')
#                 return your_score

#         # elif request.POST.get("submit"):
#         #     q1 = request.POST.get("question-1")
#         #     q2 = request.POST.get("question-2")
#         #     q3 = request.POST.get("question-3")
#         #     q4 = request.POST.get("question-4")
#         #     q5 = request.POST.get("question-5")
#         #     q6 = request.POST.get("question-6")
#         #     q7 = request.POST.get("question-7")
#         #     q8 = request.POST.get("question-8")
#         #     q9 = request.POST.get("question-9")
#         #     q10 = request.POST.get("question-10")
#         #     values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
#         #     answers = [
#         #         'answer-1', 'answer-2', 'answer-3', 'answer-4', 'answer-1,' 'answer-2', 'answer-3',
#         #         'answer-4', 'answer-1', 'answer-2'
#         #     ] 
#         #     if values == answers:
#         #     # Using the HTTPResponse to return strings
#         #         html = '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style>you scored 95%</p></div>'
#         #         your_score = HttpResponse(html)
#         #         print(values)
#         #         return your_score
#     else:
#         html = '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style>you scored 0%</p></div>'
#         your_score = HttpResponse(html)   
#     return render(request, 'index.html', {'your_score': your_score})


# def timer(request):
#     pass


# from django.shortcuts import render
# from django.http import HttpResponse

# def home_view(request):
#     global your_score
#     if request.method == "POST":
#         if request.POST.get("submit"):
#             q1 = request.POST.get("question-1")
#             q2 = request.POST.get("question-2")
#             q3 = request.POST.get("question-3")
#             q4 = request.POST.get("question-4")
#             values = [q1, q2, q3, q4]
#             answers = ['answer-1', 'answer-2', 'answer-3', 'answer-4']
#             print(values, "first")
#             if values == answers:
#                 print(values, "second")
#                 # Using the HTTPResponse to return strings
#                 return HttpResponse(
#                     '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style>you scored 100%</p></div>'
#                     )
#                 # print(your_score, "third")
#                 # return your_score

#             # elif request.POST.get("submit"):
#             #     q1 = request.POST.get("question-1")
#             #     q2 = request.POST.get("question-3")
#             #     q3 = request.POST.get("question-3")
#             #     q4 = request.POST.get("question-4")
#             #     values = [q1, q2, q3, q4]
#             #     answers = ['question-1', 'question-2', 'question-3', 'question-4']
#             #     if values
#     else:
#         score = 0
#         your_score = HttpResponse("you scored " + str(score) + '%')
#     return render(request, 'index.html')