from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from directors.models import Directors
from directors.serializers import DirectorSerializer


class DirectorCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Directors.objects.all()
    serializer_class = DirectorSerializer


class DirectorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Directors.objects.all()
    serializer_class = DirectorSerializer
