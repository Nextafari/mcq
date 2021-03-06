from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    global your_score
    score = 0
    your_score = HttpResponse("you scored " + str(score*2) + '%')
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
                '1', '2', '3', '4', '1', '2', '3',
                '4', '1', '2'
            ]
            print(values, "first")
            score = 0
            for value in values:
                if value in answers:
                    score +=5    
                elif score < 37.5:
                    return HttpResponse(f"Your score, {score*2}. Your did not reach the cutoff mark")
            return HttpResponse(
                '<div class="container p-5 mb-5 rounded"><h3>Score</h3><br><br><p><style>.container{margin-top: 60px;background-color: rgba(62, 128, 0, 0.363);color: black;margin-left: 20px;box-shadow: 10px 10px gray;}</style></p></div>' + str(score*2)
            )               
    else:        
        return render(request, 'index.html', {'your_score': your_score})

