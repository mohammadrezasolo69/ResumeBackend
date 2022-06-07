from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class Resume(models.Model):
    PHONE_REGEX = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Invalid phone number.")

    class GenderChoice(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'

    class MaritalStatusChoice(models.TextChoices):
        SINGLE = 'S'
        MARRIED = 'M'

    class MilitaryStatusChoice(models.IntegerChoices):
        SUBJECT = 0
        TO_SERVING = 1
        ENDـSERVICE = 2
        EXEMPT = 3

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='resumes', verbose_name='User')
    title = models.CharField(max_length=255, verbose_name='Title')
    first_name = models.CharField(max_length=255, verbose_name='First name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    profile_img = models.ImageField(upload_to='resume/profile', blank=True, verbose_name='Profile')
    age = models.PositiveIntegerField(verbose_name='Age')
    phone_number = models.CharField(max_length=11, validators=[PHONE_REGEX], verbose_name='Phone number')
    email = models.EmailField(blank=True, verbose_name='Email')
    bie = models.TextField(blank=True, verbose_name='Bie')
    gender = models.CharField(max_length=1, choices=GenderChoice.choices, verbose_name='Gender')
    marital_status = models.CharField(max_length=1, choices=MaritalStatusChoice.choices, verbose_name='Marital status')
    militaryـstatus = models.IntegerField(choices=MilitaryStatusChoice.choices,
                                          verbose_name='Military status')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    class LevelChoice(models.IntegerChoices):
        EXCELLENT = 0
        GOOD = 1
        MEDIUM = 2
        WEAK = 3

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills', verbose_name='Resume')
    title = models.CharField(max_length=100, verbose_name='Skill')
    level = models.IntegerField(choices=LevelChoice.choices, verbose_name='Level')

    def __str__(self):
        return self.title


class Language(models.Model):
    class LevelChoice(models.IntegerChoices):
        EXCELLENT = 0
        GOOD = 1
        MEDIUM = 2
        WEAK = 3

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='language', verbose_name='Resume')
    language = models.CharField(max_length=100, blank=True, verbose_name='Language')
    level = models.IntegerField(choices=LevelChoice.choices, blank=True, verbose_name='Level')

    def __str__(self):
        return self.language


class SocialNetwork(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='social', verbose_name='Resume')
    title = models.CharField(max_length=100, blank=True, verbose_name='Title')
    link = models.URLField(blank=True, verbose_name='Link')

    def __str__(self):
        return self.title


class CourseCertificate(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='course',
                               verbose_name='Resume')
    title = models.CharField(max_length=255, blank=True, verbose_name='Title')
    link = models.URLField(blank=True, verbose_name='Link')
    institute = models.CharField(max_length=255, blank=True, verbose_name='Institute')
    start_date = models.DateTimeField(blank=True, verbose_name='Start')
    end_date = models.DateTimeField(blank=True, verbose_name='End')

    def __str__(self):
        return self.title


class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='project',
                               verbose_name='Resume')
    title = models.CharField(max_length=255, blank=True, verbose_name='Title')
    link = models.URLField(blank=True, verbose_name='Link')
    description = models.TextField(blank=True, verbose_name='Description')
    start_date = models.DateTimeField(blank=True, verbose_name='Start')
    end_date = models.DateTimeField(blank=True, verbose_name='End')

    def __str__(self):
        return self.title


class Education(models.Model):
    class GradeChoice(models.IntegerChoices):
        Cycle = 0
        Diploma = 1
        Bachelor = 2
        Master = 3
        Doctorate = 4
        University = 5
        student = 6

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education',
                               verbose_name='Resume')

    grade = models.IntegerField(choices=GradeChoice.choices, blank=True, verbose_name='Grade')
    major = models.CharField(max_length=200, blank=True, verbose_name='Major')
    start_date = models.DateTimeField(blank=True, verbose_name='Start')
    end_date = models.DateTimeField(blank=True, verbose_name='End')

    def __str__(self):
        return self.major
