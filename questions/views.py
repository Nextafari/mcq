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
                'answer-1', 'answer-2', 'answer-3', 'answer-4', 'answer-1', 'answer-2', 'answer-3',
                'answer-4', 'answer-1', 'answer-2'
            ]
            print(values, "first")
            for value in values:
                for answer in answers:
                    score = 0
                    if value[0] == answer[0]:    
                        score +=5
                    if value[1] == answer[1]:    
                        score +=5
                    if value[2] == answer[2]:   
                        score +=5
                    if value[3] == answer[3]:   
                        score +=5
                    if value[4] == answer[4]:
                        score +=5
                    if value[5] == answer[5]: 
                        score +=5
                    if value[6] == answer[6]:    
                        score +=5
                    if value[7] == answer[7]:    
                        score +=5
                    # if value[8] == answer[8]:    
                    #     score +=5
                    # if value[9] == answer[9]:    
                    #     score +=5
                    #     # Using the HTTPResponse to return strings
                    #     print(answer)
                
                print(value, "second")
            return HttpResponse(
                '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score)
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