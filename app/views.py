from django.shortcuts import render, redirect
from .models import Question, QuizTopic, QuizHistory
from django.contrib.auth import authenticate, login, logout
from .forms import createuserform, addQuesform
from random import shuffle
from django.db.models import Sum

def home(request):
    if request.method == 'POST':
        selected_topic_id = request.POST.get('topic')
        questions = list(Question.objects.filter(topic_id=selected_topic_id))
        shuffle(questions)

        for q in questions:
            options = [q.option1, q.option2, q.option3, q.option4]
            shuffle(options)

            q.options = options
        context = {
            'questions': questions,
            'topic_id': selected_topic_id,
        }
        return render(request, 'home.html', context)
    else:
        topics = QuizTopic.objects.all()
        return render(request, 'quiz_selection.html', {'topics': topics})
    
def quiz_history(request):
    if request.user.is_authenticated:
        return render(request, 'quizhistory.html', {'quiz_attempts': QuizHistory.objects.filter(user=request.user)})
    else:
        return redirect('home') 
    
def scoreboard(request):
    scoreboard_data = (
        QuizHistory.objects
            .values('user__username')
            .annotate(total_score=Sum('score'))
            .order_by('-total_score')
    )
    return render(request, 'scoreboard.html', {'scoreboard_data': scoreboard_data})

def quiz_selection(request):
    return render(request, 'quiz_selection.html', {'topics': QuizTopic.objects.all()})

# only admin or whoever has is_staff=true can add question from frontend
def addQue(request):
    if request.user.is_staff:
        form = addQuesform()
        if request.method == 'POST':
            form = addQuesform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request, 'addque.html', {'form': form})
    else:
        return redirect('home')

def result(request):
    if request.method == 'POST':
        selected_topic_id = request.POST.get('topic')
        questions = Question.objects.filter(topic_id=selected_topic_id)

        score = 0
        total = 0
        correct_ans = 0
        incorrect_ans = 0
        time_taken = request.POST.get('timer')

        for q in questions:
            total += 1
            selected_option = request.POST.get(str(q.id))

            if selected_option == q.answer:
                score += 1
                correct_ans += 1
            else:
                incorrect_ans += 1

        context = {
            'score': score,
            'total': total,
            'correct_ans': correct_ans,
            'incorrect_ans': incorrect_ans,
            'time_taken': time_taken,
        }
        if request.user.is_authenticated:
            print("@@@@@@@@@@",score)
            QuizHistory.objects.create(
                user=request.user,
                topic=QuizTopic.objects.get(pk=selected_topic_id),
                score=score,
                time_taken=int(request.POST.get('timer', 0)),
            )
        return render(request, 'result.html', context)
    else:
        return redirect('home')

def register(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        return render(request, 'register.html', {'form': form})

def user_login(request, user=None):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('/')
