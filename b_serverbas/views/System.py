from rest_framework.permissions import IsAuthenticated
from ..permissions import *
from ..serializers import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView , ListAPIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage

# Notification
class NotificationListCreateView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class NotificationRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated,AdminPermission]
# Notification_to
class Notification_toListCreateView(ListCreateAPIView):
    queryset = Notification_to.objects.all()
    serializer_class = Notification_toSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class Notification_toRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Notification_to.objects.all()
    serializer_class = Notification_toSerializer
    permission_classes = [IsAuthenticated,AdminPermission]
# Search
class SearchListView(ListAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    permission_classes = [IsAuthenticated,UserPermission]

    def get_queryset(self):
        return Search.objects.filter(user=self.request.user)
    
class SearchListCreateView(ListCreateAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class SearchRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = SearchSerializer
    permission_classes = [IsAuthenticated, UserPermission]


# InterestedJobs
class InterestedJobsListCreateView(ListCreateAPIView):
    queryset = InterestedJobs.objects.all()
    serializer_class = InterestedJobsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class InterestedJobsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = InterestedJobs.objects.all()
    serializer_class = InterestedJobsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# RateWorker
class RateWorkerListCreateView(ListCreateAPIView):
    queryset = RateWorker.objects.all()
    serializer_class = RateWorkerSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class RateWorkerRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = RateWorker.objects.all()
    serializer_class = RateWorkerSerializer
    permission_classes = [IsAuthenticated,UserPermission]
# Apply_For
class Apply_ForListCreateView(ListCreateAPIView):
    queryset = Apply_For.objects.all()
    serializer_class = Apply_ForSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class Apply_ForRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Apply_For.objects.all()
    serializer_class = Apply_ForSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

# Send Code verification Email

class VerifyConfirmationCodeAPIView(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')

        if not email or not code:
            return Response(
                {"error": "Email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Email content with HTML styling
        subject = "Your Verification Code - Neural software factory"
        html_content = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <h2 style="color: #2c3e50;">Welcome to NSF!</h2>
            </div>
            
            <p style="font-size: 16px;">Hello,</p>
            
            <p style="font-size: 16px;">Thank you for registering with us. Here's your verification code:</p>
            
            <div style="background-color: #f8f9fa; padding: 15px; text-align: center; margin: 20px 0; border-radius: 6px;">
                <h1 style="margin: 0; color: #2c3e50; letter-spacing: 3px;">{code}</h1>
            </div>
            
            <p style="font-size: 16px;">This code will expire in 10 minutes.</p>
            
            <p style="font-size: 16px;">If you didn't request this code, please ignore this email.</p>
            
            <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #e0e0e0; font-size: 14px; color: #7f8c8d;">
                <p>Best regards,<br>The NSF Team</p>
            </div>
        </div>
        """
        
        # Plain text fallback
        text_content = f"""
        Welcome to Neural software factory!
        
        Your verification code is: {code}
        
        This code will expire in 10 minutes.
        
        If you didn't request this code, please ignore this email.
        
        Best regards,
        The NSF Team
        """
        
        try:
            email = EmailMessage(
                subject,
                html_content,
                None,  # Uses DEFAULT_FROM_EMAIL from settings
                [email],
            )
            email.content_subtype = "html"  # Set content to HTML
            email.send()
            
            return Response(
                {"message": f"Verification code sent to {email}"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": f"Failed to send email: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )