"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path,include
from django.urls import path, include
from django.contrib.auth import views as auth_views
from jobapp.views import (
    UserView,EmployerView,CompanyView, JobView, ResumeView, 
    ApplicationView, MessageView, AssessmentView, 
    JobMatchView, TalentPoolView, EventView, 
    AdminView, AnalyticsView
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # # path('accounts/', include('allauth.urls')),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('api/auth/', include('dj_rest_auth.urls')),
    # path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/', include('jobapp.urls')), 
     path('admin/', admin.site.urls),
    # path('api/', include('jobapp.urls')),
    # path('login/', views.custom_login, name='login'),
    # path('logout/', views.custom_logout, name='logout'),
     # User URLs
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserView.as_view()),
    path('employers/', EmployerView.as_view()),
    path('employers/<int:pk>/', EmployerView.as_view()),
    path('companies/', CompanyView.as_view()),
    path('companies/<int:pk>/', CompanyView.as_view()),

    path('jobs/', JobView.as_view()),
    path('jobs/<int:pk>/', JobView.as_view()),

    path('resumes/', ResumeView.as_view()),
    path('resumes/<int:pk>/', ResumeView.as_view()),

    path('applications/', ApplicationView.as_view()),
    path('applications/<int:pk>/', ApplicationView.as_view()),

    path('messages/', MessageView.as_view()),
    path('messages/<int:pk>/', MessageView.as_view()),

    path('assessments/', AssessmentView.as_view()),
    path('assessments/<int:pk>/', AssessmentView.as_view()),

    path('jobmatches/', JobMatchView.as_view()),
    path('jobmatches/<int:pk>/', JobMatchView.as_view()),

    path('talentpools/', TalentPoolView.as_view()),
    path('talentpools/<int:pk>/', TalentPoolView.as_view()),

    path('events/', EventView.as_view()),
    path('events/<int:pk>/', EventView.as_view()),

    path('admins/', AdminView.as_view()),
    path('admins/<int:pk>/', AdminView.as_view()),

    path('analytics/', AnalyticsView.as_view()),
    path('analytics/<int:pk>/', AnalyticsView.as_view()),

    # Employer URLs
    # path('employers/', EmployerListCreateView.as_view(), name='employer-list-create'),
    # path('employers/<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),

    # # Company URLs
    # path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    # path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),

    # # Job URLs
    # path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    # path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),

    # # Resume URLs
    # path('resumes/', ResumeListCreateView.as_view(), name='resume-list-create'),
    # path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),

    # # Application URLs
    # path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    # path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),

    # # Message URLs
    # path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    # path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),

    # # Assessment URLs
    # path('assessments/', AssessmentListCreateView.as_view(), name='assessment-list-create'),
    # path('assessments/<int:pk>/', AssessmentDetailView.as_view(), name='assessment-detail'),

    # # JobMatch URLs
    # path('jobmatches/', JobMatchListCreateView.as_view(), name='jobmatch-list-create'),
    # path('jobmatches/<int:pk>/', JobMatchDetailView.as_view(), name='jobmatch-detail'),

    # # TalentPool URLs
    # path('talentpools/', TalentPoolListCreateView.as_view(), name='talentpool-list-create'),
    # path('talentpools/<int:pk>/', TalentPoolDetailView.as_view(), name='talentpool-detail'),

    # # Event URLs
    # path('events/', EventListCreateView.as_view(), name='event-list-create'),
    # path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),

    # # Admin URLs
    # path('admins/', AdminListCreateView.as_view(), name='admin-list-create'),
    # path('admins/<int:pk>/', AdminDetailView.as_view(), name='admin-detail'),

    # # Analytics URLs
    # path('analytics/', AnalyticsListCreateView.as_view(), name='analytics-list-create'),
    # path('analytics/<int:pk>/', AnalyticsDetailView.as_view(), name='analytics-detail'),
]
