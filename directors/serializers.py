from rest_framework import serializers
from directors.models import Directors


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Directors
        fields = '__all__'
