from django.db import models

# Create your models here.
from django.conf import settings # type: ignore

class User(models.Model):
    ROLES = [
        ('Job Seeker', 'Job Seeker'),
        ('Employer', 'Employer'),
        ('Admin', 'Admin')
    ]
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLES)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    pass

class Employer(models.Model):
    employer_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pass

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    culture_description = models.TextField()
    logo_url = models.CharField(max_length=255)
    pass

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    # companyName = models.CharField(max_length=255)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    requirements = models.TextField()
    benefits = models.TextField()
    location = models.CharField(max_length=255)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField()
    status = models.CharField(max_length=50)
    

class Resume(models.Model):
    resume_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    certifications = models.TextField()
    contact_info = models.TextField()
    video_resume_url = models.CharField(max_length=255, null=True, blank=True)

class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_test_url = models.CharField(max_length=255)
    score = models.IntegerField()
    assessment_date = models.DateTimeField()

class JobMatch(models.Model):
    match_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match_score = models.IntegerField()

class TalentPool(models.Model):
    pool_id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permissions = models.TextField()

class Analytics(models.Model):
    analytics_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    views = models.IntegerField()
    applications = models.IntegerField()
    matches = models.IntegerField()
    average_time_to_hire = models.IntegerField()

# here is the pakages class 

class Package(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name
    
    
# payment trans.....
class PaymentTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.transaction_id}"