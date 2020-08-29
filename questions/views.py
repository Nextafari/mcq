from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    global your_score
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
            values = [q1, q2, q3, q4, q5, q6, q7, q8, q10]
            answers = [
                'answer-1', 'answer-2', 'answer-3', 'answer-4', 'answer-5,' 'answer-6', 'answer-7',
                'answer-8', 'answer-8', 'answer-9', 'answer-10'
            ] 
            print(values)
            if values == answers:
                print(values)
                score = 0
                score += 100
                print(values)
                # Using the HTTPResponse to return strings/HTMl
                your_score = HttpResponse(
                    '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style>you scored 100%</p></div>'
                    )
                print(your_score)
                return your_score

            elif request.POST.get("submit"):
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
                values = [q1, q2, q3, q4, q5, q6, q7, q8, q10]
                answers = [
                    'answer-1', 'answer-2', 'answer-3', 'answer-4', 'answer-5,' 'answer-6', 'answer-7',
                    'answer-8', 'answer-8', 'answer-9', 'answer-10'
                ] 
                if values != answers:
                # Using the HTTPResponse to return strings
                    your_score = HttpResponse(
                        '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style>you scored 75%</p></div>'
                        )
                    return your_score
    else:
        score = 0
        your_score = HttpResponse("you scored " + str(score) + '%')    
    return render(request, 'index.html', {'your_score': your_score})


def timer(request):
    pass