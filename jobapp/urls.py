from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PackageView, PaymentView, UserView, EmployerView, CompanyView, JobView, ResumeView, ApplicationView, MessageView, AssessmentView, JobMatchView, TalentPoolView, EventView, AdminView, AnalyticsView
router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'employers', EmployerView)
router.register(r'companies', CompanyView)
router.register(r'jobs', JobView)
router.register(r'resumes', ResumeView)
router.register(r'applications', ApplicationView)
router.register(r'messages', MessageView)
router.register(r'assessments', AssessmentView)
router.register(r'job_matches', JobMatchView)
router.register(r'talent_pools', TalentPoolView)
router.register(r'events', EventView)
router.register(r'admins', AdminView)
router.register(r'analytics', AnalyticsView)
router.register(r'packages', PackageView)
router.register(r'payments', PaymentView, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
