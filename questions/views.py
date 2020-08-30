from django.shortcuts import render
from django.http import HttpResponse
import time


def home_view(request):
    global your_score
    score = 0
    your_score = HttpResponse("you scored " + str(score) + '%')
    if request.method == "POST":
        if request.POST.get("submit"):
            q1 = request.POST.get("question-1")
            q2 = request.POST.get("question-2")
            q3 = request.POST.get("question-3")
            q4 = request.POST.get("question-4")
            q5 = request.POST.get("question-5")
            q6 = request.POST.get("question-6")
            q7 = request.POST.get("question-7")
            q8 = request.POST.get("question-8")
            q9 = request.POST.get("question-9")
            q10 = request.POST.get("question-10")
            values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
            answers = [
                'answer-1', 'answer-2', 'answer-3', 'answer-4', 'answer-1,' 'answer-2', 'answer-3',
                'answer-4', 'answer-1', 'answer-2'
            ]
            print(values, "first")
            if values[0] == answers[0]:
                # Using the HTTPResponse to return strings
                score = 0
                score +=50
                print(values, "second")
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[1] == answers[1]:
                score +=10
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[2] == answers[2]:
                score +=15
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[3] == answers[3]:
                score +=20
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[4] == answers[4]:
                score +=25
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[5] == answers[5]:
                score +=30
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[6] == answers[6]:
                score +=35
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[7] == answers[7]:
                score +=40
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[8] == answers[8]:
                score +=45
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            elif values[9] == answers[9]:
                score +=50
                return HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
                )
            else:
                return HttpResponse(
                    'You did not reach the cut off mark'
                )
    else:
        
        return render(request, 'index.html', {'your_score': your_score})


def timer(request):
    while True:
        t = 20
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        return timer
        time.sleep(1)
        t -=1
    return render(request, 'index.html', {'timer': timer})