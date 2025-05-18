from rest_framework.permissions import IsAuthenticated
from ..permissions import *
from ..serializers import *
from rest_framework.generics import ( RetrieveUpdateDestroyAPIView, ListCreateAPIView )

# Conversation
class ConversationListCreateView(ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class ConversationRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

# Messages
class MessagesListCreateView(ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class MessagesRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
