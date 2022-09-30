from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post, Comment, QuesModel
from .forms import PostForm, NewUserForm, CommentForm


# Create your views here.


def home(request):
    return render(request, 'learnApp/quiz.html')

def index(request):
    return render(request, 'learnApp/index.html')


def course_details(request):
    return render(request, 'learnApp/course-details.html')
def course_details2(request):
    return render(request, 'learnApp/course-details2.html')
def course_details3(request):
    return render(request, 'learnApp/course-details3.html')
def courses(request):
    return render(request, 'learnApp/courses.html')

def comments(request):
    if request.method == 'POST':
        form_data = CommentForm(request.POST)
        if form_data.is_valid():
            comment = form_data.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect("comments")
    queryset = Comment.objects.all().order_by('-date_created')
    context = {'comments':queryset, 'form':CommentForm}
    return render(request,'learnApp/comments.html',context=context)

def events(request):
    if request.method == 'POST':
        form_data = PostForm(request.POST)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("events.html")
    queryset = Post.objects.all().order_by('-date_created')
    context = {'posts': queryset, "form":PostForm}
    return render(request, 'learnApp/events.html', context=context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('courses.html')

        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Погрешно корисничко име или лозинка.")
            return redirect('login.html')

    else:
        return render(request,'learnApp/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,'Uspesno se odlogiravte')
    return redirect('login.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registration successful.")
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="learnApp/register.html", context={"register_form": form})




#kviz

def results(request):
    return render(request, 'learnApp/results.html')

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.ans):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'learnApp/results.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request, 'learnApp/quiz.html', context)


# #searchbar
# def prebaruvanje_postovi(request):
#
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         naslov = Post.objects.filter(title__contains=searched)
#         return render(request,'learnApp/prebaruvanje_postovi.html',{'searched':searched, 'naslov':naslov})
#     else:
#         return render(request, 'learnApp/prebaruvanje_postovi.html', {})