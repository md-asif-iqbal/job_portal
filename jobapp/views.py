from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status,generics, mixins
from .models import User, Employer, Company, Job, Resume, Application, Message, Assessment, JobMatch, TalentPool, Event, Admin, Analytics
from .serializers import UserSerializer, EmployerSerializer, CompanySerializer, JobSerializer, ResumeSerializer, ApplicationSerializer, MessageSerializer, AssessmentSerializer, JobMatchSerializer, TalentPoolSerializer, EventSerializer, AdminSerializer, AnalyticsSerializer
from rest_framework.response import Response
from .models import Package, PaymentTransaction
from .serializers import PackageSerializer, PaymentTransactionSerializer
import stripe
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.views import APIView
import stripe
from .models import (
    User
    # User, Employer, Company, Job, Resume, Application, 
    # Message, Assessment, JobMatch, TalentPool, Event, Admin, Analytics
)
from .serializers import (
    UserSerializer
    # UserSerializer, EmployerSerializer, CompanySerializer, 
    # JobSerializer, ResumeSerializer, ApplicationSerializer, 
    # MessageSerializer, AssessmentSerializer, JobMatchSerializer, 
    # TalentPoolSerializer, EventSerializer, AdminSerializer, AnalyticsSerializer
)


class UserView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)
class EmployerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)

class CompanyView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)
    

class JobView(
    
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)

class ResumeView(EmployerView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)
# application view
class ApplicationView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)
# massage view
class MessageView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)

# assignment view
class AssessmentView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)

class JobMatchView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = JobMatch.objects.all()
    serializer_class = JobMatchSerializer
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)


class TalentPoolView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = TalentPool.objects.all()
    serializer_class = TalentPoolSerializer


class EventView(EmployerView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)

class AdminView(EmployerView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class AnalyticsView(EmployerView):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
# # Employer Views
# class EmployerListCreateView(APIView):
#     def get(self, request):
#         employers = Employer.objects.all()
#         serializer = EmployerSerializer(employers, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EmployerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EmployerDetailView(APIView):
#     def get(self, request, pk):
#         employer = Employer.objects.get(pk=pk)
#         serializer = EmployerSerializer(employer)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         employer = Employer.objects.get(pk=pk)
#         serializer = EmployerSerializer(employer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         employer = Employer.objects.get(pk=pk)
#         serializer = EmployerSerializer(employer, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employer = Employer.objects.get(pk=pk)
#         employer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Company Views
# class CompanyListCreateView(APIView):
#     def get(self, request):
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CompanyDetailView(APIView):
#     def get(self, request, pk):
#         company = Company.objects.get(pk=pk)
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         company = Company.objects.get(pk=pk)
#         serializer = CompanySerializer(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         company = Company.objects.get(pk=pk)
#         serializer = CompanySerializer(company, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         company = Company.objects.get(pk=pk)
#         company.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Job Views
# class JobListCreateView(APIView):
#     def get(self, request):
#         jobs = Job.objects.all()
#         serializer = JobSerializer(jobs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = JobSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class JobDetailView(APIView):
#     def get(self, request, pk):
#         job = Job.objects.get(pk=pk)
#         serializer = JobSerializer(job)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         job = Job.objects.get(pk=pk)
#         serializer = JobSerializer(job, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         job = Job.objects.get(pk=pk)
#         serializer = JobSerializer(job, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         job = Job.objects.get(pk=pk)
#         job.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Resume Views
# class ResumeListCreateView(APIView):
#     def get(self, request):
#         resumes = Resume.objects.all()
#         serializer = ResumeSerializer(resumes, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ResumeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ResumeDetailView(APIView):
#     def get(self, request, pk):
#         resume = Resume.objects.get(pk=pk)
#         serializer = ResumeSerializer(resume)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         resume = Resume.objects.get(pk=pk)
#         serializer = ResumeSerializer(resume, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         resume = Resume.objects.get(pk=pk)
#         serializer = ResumeSerializer(resume, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         resume = Resume.objects.get(pk=pk)
#         resume.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Application Views
# class ApplicationListCreateView(APIView):
#     def get(self, request):
#         applications = Application.objects.all()
#         serializer = ApplicationSerializer(applications, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ApplicationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ApplicationDetailView(APIView):
#     def get(self, request, pk):
#         application = Application.objects.get(pk=pk)
#         serializer = ApplicationSerializer(application)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         application = Application.objects.get(pk=pk)
#         serializer = ApplicationSerializer(application, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         application = Application.objects.get(pk=pk)
#         serializer = ApplicationSerializer(application, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         application = Application.objects.get(pk=pk)
#         application.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Message Views
# class MessageListCreateView(APIView):
#     def get(self, request):
#         messages = Message.objects.all()
#         serializer = MessageSerializer(messages, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MessageDetailView(APIView):
#     def get(self, request, pk):
#         message = Message.objects.get(pk=pk)
#         serializer = MessageSerializer(message)
#         return Response(serializer.data)

    # def put(self, request, pk):




# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [IsAuthenticated]

# class EmployerViewSet(viewsets.ModelViewSet):
#     queryset = Employer.objects.all()
#     serializer_class = EmployerSerializer

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# class JobViewSet(viewsets.ModelViewSet):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer

# class ResumeViewSet(viewsets.ModelViewSet):
#     queryset = Resume.objects.all()
#     serializer_class = ResumeSerializer

# class ApplicationViewSet(viewsets.ModelViewSet):
#     queryset = Application.objects.all()
#     serializer_class = ApplicationSerializer

# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# class AssessmentViewSet(viewsets.ModelViewSet):
#     queryset = Assessment.objects.all()
#     serializer_class = AssessmentSerializer

# class JobMatchViewSet(viewsets.ModelViewSet):
#     queryset = JobMatch.objects.all()
#     serializer_class = JobMatchSerializer

# class TalentPoolViewSet(viewsets.ModelViewSet):
#     queryset = TalentPool.objects.all()
#     serializer_class = TalentPoolSerializer

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

# class AdminViewSet(viewsets.ModelViewSet):
#     queryset = Admin.objects.all()
#     serializer_class = AdminSerializer

# class AnalyticsViewSet(viewsets.ModelViewSet):
#     queryset = Analytics.objects.all()
#     serializer_class = AnalyticsSerializer


# payment way use stripe 

# stripe.api_key = 'sk_test_51L1XB5H61fNE2hoYTiZMAM7NCaqXElYMe6BQHmL3YiBp4FzyqQBH8d1iOicXG9gFZLLnl2AYkVpo8jnUqof8g1nt00wC5IDpRf'

# class PackageViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Package.objects.all()
#     serializer_class = PackageSerializer

# class PaymentViewSet(viewsets.ViewSet):

#     def create(self, request):
#         user = request.user
#         package_id = request.data.get('package_id')
#         token = request.data.get('stripe_token')

#         try:
#             package = Package.objects.get(id=package_id)
#             charge = stripe.Charge.create(
#                 amount=int(package.price * 100),
#                 currency='usd',
#                 description=f'Payment for {package.name}',
#                 source=token
#             )

#             payment = PaymentTransaction.objects.create(
#                 user=user,
#                 package=package,
#                 transaction_id=charge.id,
#                 amount=package.price,
#                 status='Completed'
#             )

#             serializer = PaymentTransactionSerializer(payment)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         except stripe.error.StripeError as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         except Package.DoesNotExist:
#             return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)