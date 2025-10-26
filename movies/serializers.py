from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from actors.serializers import ActorSerializer
from directors.serializers import DirectorSerializer
from genres.serializers import GenreSerializer


class MovieModelSerializers(serializers.ModelSerializer):

    
    class Meta:
        model = Movie
        fields = '__all__'

    # Validação de dados tem que iniciar com validate_nomedocampodoModel(self, value)
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value

    def validate_resume(self, value):
        if len(value) > 400:
            raise serializers.ValidationError('Resumo não pode ser maior que 400 caracteres.')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)  # n para n 
    director = DirectorSerializer()
    genre = GenreSerializer()
    # Adicione um campo
    # SerializerMethodField -> E um campo calculado  | Um campo que vai ter uma lógica
    # read_only=True -> Apenas um campo de leitura GET
    rate = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Movie
        fields =  ['id', 'title', 'genre', 'director', 'actors', 'release_date', 'rate', 'resume']

    # Campo calculdo tem que iniciar com get_nomedocampo(self, obj)
    def get_rate(self, obj):
        # aggregate -> Agregando um campo
        # Avg -> Calcula a média
        # obj.reviews -> veio de model reviews - movie - related_name
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
