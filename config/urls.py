"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views import contact
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, study_groups, resources, login, register, join_group, logout_view, notes, python_notes, tasks, sessions, note_detail, complete_task, upload_file, about, profile, contact, exam_questions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('study-groups/', study_groups, name='study_groups'),
    path('resources/', resources, name='resources'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('join-group/<int:group_id>/', join_group, name='join_group'),
    path('logout/', logout_view, name='logout'),
    path('notes/', notes, name='notes'),
    path('python-notes/', python_notes, name='python_notes'),
    path('tasks/',tasks, name='tasks' ),
    path('sessions/',sessions, name='sessions'),
    path('note/<int:note_id>/', note_detail, name='note_detail'),
    path('complete-task/<int:task_id>/', complete_task, name='complete_task'),
    path('upload_file/', upload_file, name='upload_file'),
    path('about/', about, name='about'),
    path('profile/', profile, name='profile'),
    path('contact/', contact, name='contact'),
    path('exam-questions/', exam_questions, name='exam_questions'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
