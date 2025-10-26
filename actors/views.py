from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from actors.models import Actors
from actors.serializers import ActorSerializer


class ActorCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
