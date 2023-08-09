from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.


class Class(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Classes'


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.PositiveIntegerField()
    email = models.EmailField(max_length=256)
    class_of_student = models.ForeignKey(Class, on_delete=models.CASCADE)
    BLOOD_CHOICES = (
        ('', ''),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('b+', 'B-'),
        ('ab-', 'AB+'),
        ('ab', 'AB'),
    )
    blood_group = models.CharField(
        max_length=6, choices=BLOOD_CHOICES, default='o+')

    RELIGION_CHOICES = (
        ('christian', 'CHRISTIAN'),
        ('muslim', 'MUSLIM'),
        ('others', 'OTHERS')
    )
    religion = models.CharField( max_length=20, choices=RELIGION_CHOICES, default='')
    GENDER_CHOICES = (
        ('male', 'MALE'),
        ('female', 'FEMALE')
    )
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='male')
    image = models.ImageField(upload_to='images/')
    dob = models.DateField(blank=True, null=True)
    parent_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=50 ,null=True, blank=True)
    LANGUAGE_CHOICE = (
        ('English', 'ENGLISH'),
        ('French', 'FRENCH'),
    )
   
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'


class Staff(models. Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.PositiveIntegerField()
    email = models.EmailField(max_length=256)
    teacher_class = models.ForeignKey(Class, on_delete=models.CASCADE, default='Cleaner')
    GENDER_CHOICES = (
        ('male', 'MALE'),
        ('female', 'FEMALE')
    )
    dob = models.DateField(blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='male')
    qualifications = models.CharField(max_length=255, null=True, blank=True)
    is_primary_school_teacher = models.BooleanField(default=True)
    SUBJECT_TEACHING = (
        ('MATHEMATICS', 'mathematics'),
        ('ENGLISH', 'english'),
        ('BIOLOGY', 'biology')
    )
    subject_teaching= models.CharField(max_length=233, choices=SUBJECT_TEACHING, default='mathematics')
    address = models.TextField(max_length=50 ,null=True, blank=True)
    city = models.CharField(max_length=50 ,null=True, blank=True)
    state = models.CharField(max_length=50 ,null=True, blank=True)
    zip_code = models.CharField(max_length=50 ,null=True, blank=True)
    experience = models.CharField(max_length=50 ,null=True, blank=True)
    country = models.CharField(max_length=50 ,null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Teachers: {self.first_name} {self.last_name}'


class Subject(models.Model):
    name = models.CharField(max_length=120)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_class = models.ForeignKey(
        Class, null=True, blank=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject, null=True, blank=True, on_delete=models.CASCADE)
    test = models.FloatField(default=0)
    exam = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
