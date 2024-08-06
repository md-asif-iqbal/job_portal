from django.contrib import admin

# Register your models here.
from .models import Package, PaymentTransaction, User, Employer, Company, Job, Resume, Application, Message, Assessment, JobMatch, TalentPool, Event, Admin, Analytics

admin.site.register(User)
admin.site.register(Employer)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Resume)
admin.site.register(Application)
admin.site.register(Message)
admin.site.register(Assessment)
admin.site.register(JobMatch)
admin.site.register(TalentPool)
admin.site.register(Event)
admin.site.register(Admin)
admin.site.register(Analytics)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_days']

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'transaction_id', 'amount', 'status', 'created_at']