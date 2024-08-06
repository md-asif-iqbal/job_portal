from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PackageViewSet, PaymentViewSet, UserViewSet, EmployerViewSet, CompanyViewSet, JobViewSet, ResumeViewSet, ApplicationViewSet, MessageViewSet, AssessmentViewSet, JobMatchViewSet, TalentPoolViewSet, EventViewSet, AdminViewSet, AnalyticsViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employers', EmployerViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'assessments', AssessmentViewSet)
router.register(r'job_matches', JobMatchViewSet)
router.register(r'talent_pools', TalentPoolViewSet)
router.register(r'events', EventViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'analytics', AnalyticsViewSet)

router.register(r'packages', PackageViewSet)
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
