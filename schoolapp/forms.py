from django import forms
from .models import Student, Staff


class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'phone_no', 'email', 'class_of_student',  'religion', 'gender', 'dob', 'image', 'blood_group', 'parent_name')
        GENDER_CHOICES = (
            ('male', 'MALE'),
            ('female', 'FEMALE')
        )
        BLOOD_CHOICES = (
            ('o+', 'O+'),
            ('o-', 'O-'),
            ('b+', 'B-'),
            ('ab-', 'AB+'),
            ('ab', 'AB'),
        )
        RELIGION_CHOICES = (
            ('christian', 'CHRISTIAN'),
            ('muslim', 'MUSLIM'),
            ('others', 'OTHERS')
         )
        widgets = {
      
          'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':"First Name"}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Last Name"}),
            'parent_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Parent Name"}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'blood_group': forms.Select(choices=BLOOD_CHOICES, attrs={'class':'form-control'}),
            'religion': forms.Select(choices=RELIGION_CHOICES, attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'class_of_student': forms.Select(attrs={'class':'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}),
        }



class AddStaff(forms.ModelForm):
    SUBJECT_TEACHING = (
        ('MATHEMATICS', 'mathematics'),
        ('ENGLISH', 'english'),
        ('BIOLOGY', 'biology')
    )
    is_primary_school_teacher = forms.BooleanField(required=False)
    subject_teaching: forms.Select(choices=SUBJECT_TEACHING, attrs={'class':'form-control'})
    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'phone_no', 'email', 'teacher_class', 'gender','image','is_primary_school_teacher', 'subject_teaching', 'dob', 'qualifications', 'address', 'zip_code', 'city', 'state',  'experience', 'country', 'joining_date')
        GENDER_CHOICES = (
            ('male', 'MALE'),
            ('female', 'FEMALE')
        )
        SUBJECT_TEACHING = (
            ('MATHEMATICS', 'mathematics'),
            ('ENGLISH', 'english'),
            ('BIOLOGY', 'biology')
        )
      
        widgets = {
      
          'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':"First Name"}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Last Name"}),
            'qualifications': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Enter Qualifications"}),
            'experience': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Enter Experience"}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Enter Address"}),
            'teacher_class': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Enter teacher Class"}),
            'subject_teaching': forms.Select(choices=SUBJECT_TEACHING, attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Enter City"}),
            'country': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Enter Country"}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Enter Zip Code"}),
            'state': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Enter State"}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control mt-2'}),
            'joining_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'parent_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Parent Name"}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'teacher_class': forms.Select(attrs={'class':'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}),
            'is_primary_school_teacher':forms.CheckboxInput( attrs={'class': 'form-control mt-2'})
        }
