from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from .models import Student
from .models import Course
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_students = Student.objects.all().count()
        total_courses = Course.objects.all().count()
        context['total_students'] = total_students
        context['total_courses'] = total_courses
        return context


class CreateStudentView(View):
    def post(self, request):
        studentname = request.POST['Studentname']
        studentemail = request.POST['studentemail']
        phone = request.POST['phone']

        if Student.objects.filter(Studentname=studentname).exists():
            raise ValidationError('Studentname already exists')

        if Student.objects.filter(studentemail=studentemail).exists():
            raise ValidationError('studentemail already exists')

        data = Student(
            Studentname=studentname,
            studentemail=studentemail,
            phone=phone,
            address=request.POST.get('address')
        )
        data.save()
        return redirect('ReadStudentView')


class ReadStudentView(LoginRequiredMixin, View):
    def get(self, request):
        if 'q' in request.GET:
            q = request.GET.get('q')
            students = Student.objects.filter(Studentname__icontains=q)
        else:
            students = Student.objects.order_by('-created_at')

        paginator = Paginator(students, per_page=3)
        page_number = request.GET.get('page')
        studentsfinal = paginator.get_page(page_number)
        totalpage = studentsfinal.paginator.num_pages
        context = {
            'students': studentsfinal,
            'lastpage': totalpage,
            'totalPagelist': [n + 1 for n in range(totalpage)]
        }
        return render(request, 'student/student.html', context)


class DeleteStudentView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, id):
        obj = get_object_or_404(Student, pk=id)
        obj.delete()
        return JsonResponse({'message': 'Deleted'})


class UpdateStudentView(View):
    def get(self, request, id):
        updatestud = get_object_or_404(Student, id=id)
        context = {'updatestud': updatestud}
        return render(request, 'update_student.html', context)

    def post(self, request, id):
        updatestud = get_object_or_404(Student, id=id)
        updatestud.Studentname = request.POST.get('Studentname')
        updatestud.studentemail = request.POST.get('studentemail')
        updatestud.phone = request.POST.get('phone')
        updatestud.address = request.POST.get('address')
        updatestud.save()
        return redirect('ReadStudentView')

# -----------------course-------------------------


class CreateCourseView(LoginRequiredMixin, View):
    def post(self, request):
        print('rrrrrrrrr')
        coursename = request.POST['coursename']
        code = request.POST['code']
        if Course.objects.filter(coursename=coursename).exists():
            raise ValidationError('Coursename already exists')
        if Course.objects.filter(code=code).exists():
            raise ValidationError('Code already exists')
        data = Course(
            coursename=request.POST['coursename'],
            code=request.POST['code'],
            description=request.POST.get('description'),
        )
        data.save()
        return reverse_lazy('ReadCourseView')


class ReadCourseView(LoginRequiredMixin, View):
    def get(self, request):
        if 'q' in request.GET:
            q = request.GET.get('q')
            courses = Course.objects.filter(coursename__icontains=q)
        else:
            courses = Course.objects.order_by('-created_at')
        paginator = Paginator(courses, per_page=3)
        page_number = request.GET.get('page')
        coursesfinal = paginator.get_page(page_number)
        totalpage = coursesfinal.paginator.num_pages
        context = {
            'courses': coursesfinal,
            'lastpage': totalpage,
            'totalPagelist': [n + 1 for n in range(totalpage)]
        }
        return render(request, 'course/course.html', context)


class DeleteCourseView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, id):
        obj = get_object_or_404(Course, pk=id)
        obj.delete()
        return JsonResponse({'message': 'Deleted'})


class UpdateCourseView(View):
    def get(self, request, id):
        updatecours = Course.objects.get(id=id)
        context = {'updatecours': updatecours}
        return render(request, 'update_course.html', context)

    def post(self, request, id):
        updatecours = Course.objects.get(id=id)
        coursename = request.POST.get('coursename')
        code = request.POST.get('code')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        updatecours.coursename = coursename
        updatecours.code = code
        updatecours.description = description
        updatecours.created_at = created_at
        updatecours.save()
        return redirect('ReadCourseView', values=updatecours)
