from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from datetime import date, timedelta
from .models import StudyGroup, StudySession, Note, Task, StudyFile, UserProfile, ContactMessage

def home(request):
    return render(request, 'home.html')

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(
                request,
                'register.html',
                {'error': 'Passwords do not match'}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'register.html',
                {'error': 'Username already exists'}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')

def join_group(request, group_id):
    if not request.user.is_authenticated:
        return redirect('login')

    group = get_object_or_404(StudyGroup, id=group_id)
    group.members.add(request.user)

    return redirect('study_groups')

def join_group(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)

    if request.user.is_authenticated:
        group.members.add(request.user)

    return redirect('study_groups')

def study_groups(request):
    groups = StudyGroup.objects.all()
    return render(request, 'study_groups.html', {'groups': groups})


def resources(request):
    files = StudyFile.objects.all().order_by('-uploaded_at')
    return render(request, 'resources.html', {'files': files})

def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            profile, created = UserProfile.objects.get_or_create(
                user=user
            )

            today = date.today()

            if profile.last_study_date == today:
                pass

            elif profile.last_study_date == today - timedelta(days=1):
                profile.study_streak += 1

            else:
                profile.study_streak = 1

            profile.last_study_date = today
            profile.save()

            auth_login(request, user)

            return redirect('/')

        return render(request, 'login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def notes(request):
    notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'note_detail.html', {'note': note})

def python_notes(request):
    return render(request, 'python_notes_page.html)')

@login_required
def tasks(request):

    user_tasks = Task.objects.filter(user=request.user)

    return render(request, 'tasks.html', {
        'tasks': user_tasks
    })


@login_required
def complete_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.completed = True
    task.save()

    return redirect('tasks')

def sessions(request):
    sessions = StudySession.objects.all()
    return render(request, 'sessions.html', {'sessions': sessions})


def upload_file(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']

        StudyFile.objects.create(
            title=title,
            file=file
        )

        return redirect('resources')

    return render(request, 'upload_file.html')

def about(request):
    return render(request, 'about.html')

def profile(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    return render(request, 'profile.html', {
        'profile_user': request.user,
        'profile': profile
    })


def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, 'contact.html', {
            'success': 'Your message has been sent successfully!'
        })

    return render(request, 'contact.html')

def exam_questions(request):
    return render(request, 'exam_questions.html')