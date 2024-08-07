from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status
from .models import User, Employer, Company, Job, Resume, Application, Message, Assessment, JobMatch, TalentPool, Event, Admin, Analytics
from .serializers import UserSerializer, EmployerSerializer, CompanySerializer, JobSerializer, ResumeSerializer, ApplicationSerializer, MessageSerializer, AssessmentSerializer, JobMatchSerializer, TalentPoolSerializer, EventSerializer, AdminSerializer, AnalyticsSerializer
from rest_framework.response import Response
from .models import Package, PaymentTransaction
from .serializers import PackageSerializer, PaymentTransactionSerializer
import stripe
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class JobMatchViewSet(viewsets.ModelViewSet):
    queryset = JobMatch.objects.all()
    serializer_class = JobMatchSerializer

class TalentPoolViewSet(viewsets.ModelViewSet):
    queryset = TalentPool.objects.all()
    serializer_class = TalentPoolSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer


# payment way use stripe 

stripe.api_key = 'sk_test_51L1XB5H61fNE2hoYTiZMAM7NCaqXElYMe6BQHmL3YiBp4FzyqQBH8d1iOicXG9gFZLLnl2AYkVpo8jnUqof8g1nt00wC5IDpRf'

class PackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class PaymentViewSet(viewsets.ViewSet):

    def create(self, request):
        user = request.user
        package_id = request.data.get('package_id')
        token = request.data.get('stripe_token')

        try:
            package = Package.objects.get(id=package_id)
            charge = stripe.Charge.create(
                amount=int(package.price * 100),
                currency='usd',
                description=f'Payment for {package.name}',
                source=token
            )

            payment = PaymentTransaction.objects.create(
                user=user,
                package=package,
                transaction_id=charge.id,
                amount=package.price,
                status='Completed'
            )

            serializer = PaymentTransactionSerializer(payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Package.DoesNotExist:
            return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)