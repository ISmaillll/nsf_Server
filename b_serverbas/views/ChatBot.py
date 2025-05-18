from rest_framework.permissions import IsAuthenticated
from ..permissions import *
from ..serializers import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ChatSession
class ChatSessionListCreateView(ListCreateAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class ChatSessionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class ChatSessionListView(ListAPIView):
    serializer_class = ChatSessionSerializer
    permission_classes = [IsAuthenticated, UserPermission]

    def get_queryset(self):
        return ChatSession.objects.filter(User=self.request.user).order_by('-updated_at')
    
# Message_Bot
class Message_BotListCreateView(ListCreateAPIView):
    queryset = Message_Bot.objects.all()
    serializer_class = Message_BotSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class Message_BotRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Message_Bot.objects.all()
    serializer_class = Message_BotSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class Message_BotListAPIView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = Message_BotSerializerPlus
    permission_classes = [IsAuthenticated, UserPermission]

    def get_queryset(self):
        return Message_Bot.objects.filter(Session__id=self.kwargs.get('pk'), Session__User=self.request.user)
# Software_recommandation
class Software_recommandationListCreateView(ListCreateAPIView):
    queryset = Software_recommandation.objects.all()
    serializer_class = Software_recommandationSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class Software_recommandationRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Software_recommandation.objects.all()
    serializer_class = Software_recommandationSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class SoftwareRecommandationView(APIView):
    def get(self, request):
        message_id = request.query_params.get("Message")
        if not message_id:
            return Response({"error": "Message parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            message = Message_Bot.objects.get(pk=message_id)
        except Message_Bot.DoesNotExist:
            return Response({"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND)

        recommandations = Software_recommandation.objects.filter(Message_Bot=message)
        serializer = Software_recommandationSerializerPlus(recommandations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        message_id = request.data.get("Message")
        software_ids = request.data.get("Softwares")

        if not message_id or not software_ids:
            return Response({"error": "Message and Softwares are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            message = Message_Bot.objects.get(pk=message_id)
        except Message_Bot.DoesNotExist:
            return Response({"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND)

        recommendations = []
        for sid in software_ids:
            try:
                software = Software.objects.get(pk=sid)
                rec = Software_recommandation.objects.create(Message_Bot=message, Software=software)
                recommendations.append(rec)
            except Software.DoesNotExist:
                continue  # skip invalid IDs

        serializer = Software_recommandationSerializer(recommendations, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# User_Softwares
class User_SoftwaresListCreateView(ListCreateAPIView):
    queryset = User_Softwares.objects.all()
    serializer_class = User_SoftwaresSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class User_SoftwaresRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = User_Softwares.objects.all()
    serializer_class = User_SoftwaresSerializer
    permission_classes = [IsAuthenticated, WorkerManagerPermission]

class User_SoftwaresListAPIView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = User_SoftwaresSerializer
    permission_classes = [IsAuthenticated, UserPermission]

    def get_queryset(self):
        session_id = self.kwargs.get('pk')
        return User_Softwares.objects.filter(Session__id=session_id)

# Dev_Offer
class Dev_OfferListCreateView(ListCreateAPIView):
    queryset = Dev_Offer.objects.all()
    serializer_class = Dev_OfferSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class Dev_OfferRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Dev_Offer.objects.all()
    serializer_class = Dev_OfferSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
