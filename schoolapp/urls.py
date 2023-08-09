from django.urls import path
from . import views
from django.conf import settings  # new
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('login', views.signin, name='login'),
    path('add_student', views.add_student, name='add_student'),
    path('edit_student/<str:id>/', views.edit_student, name='edit_student'),
    path('delete_student/<str:id>/', views.delete_student, name='delete_student'),
    path('student_details/<str:id>/', views.student_details, name='student_details'),
    path('teachers', views.teachers, name='teachers'),
    path('add_teachers', views.add_teachers, name='add_teachers'),
    path('edit_staff/<str:id>/', views.edit_staff, name='edit_staff'),
    path('delete_staff/<str:id>/', views.delete_staff, name='delete_staff'),
    path('student_details/<str:id>/', views.student_details, name='student_details'),
    path('logout', views.logout_view, name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new
