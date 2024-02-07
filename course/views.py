from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def teacher(request):
    return render(request, 'course/teacher.html')

@login_required
def student(request):
    return render(request, 'course/student.html')

@login_required
def index(request):
    return HttpResponse("Hello, I am a index page")
# elearning_app/views.py

# elearning_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# elearning_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Check if the user selected the 'teacher' checkbox
            if request.POST.get('is_teacher'):
                teacher_group = Group.objects.get(name='teacher')
                user.groups.add(teacher_group)

            # Check if the user selected the 'student' checkbox
            if request.POST.get('is_student'):
                student_group = Group.objects.get(name='student')
                user.groups.add(student_group)


            return redirect('login')  # Redirect to the index page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'course/register.html', {'form': form})




# elearning_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect based on user's group
            if user.groups.filter(name='teacher').exists():
                return redirect('teacher')
            elif user.groups.filter(name='student').exists():
                return redirect('student')
            else:
                # Redirect to a default page if the user is not in any specific group
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'course/login.html', {'form': form})


# views.py

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


@login_required
def user_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'course/profile.html', context)


# views.py

from django.shortcuts import render, redirect
from .forms import CourseForm, AttachmentForm
from django.contrib.auth.decorators import login_required

@login_required
def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        attachment_form = AttachmentForm(request.POST, request.FILES)

        if course_form.is_valid() and attachment_form.is_valid():
            course = course_form.save(commit=False)
            course.created_by = request.user
            course.save()

            attachment = attachment_form.save(commit=False)
            attachment.course = course
            attachment.save()

            return redirect('view_courses')  # Redirect to the courses page after adding the course

    else:
        course_form = CourseForm()
        attachment_form = AttachmentForm()

    context = {
        'course_form': course_form,
        'attachment_form': attachment_form,
    }

    return render(request, 'course/add_course.html', context)


from django.shortcuts import render
from .models import Course
from django.contrib.auth.decorators import login_required

@login_required
def view_courses(request):
    courses = Course.objects.filter(created_by=request.user)
    return render(request, 'course/view_courses.html', {'courses': courses})


# views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Course

def courses_list(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 6)
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    return render(request, 'course/courses_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course/course_detail.html', {'course': course})
