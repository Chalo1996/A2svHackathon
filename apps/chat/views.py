from rest_framework import generics
from .models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

class ChatMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
