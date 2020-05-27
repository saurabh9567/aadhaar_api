from rest_framework import serializers
from empapi.models import Candidate, UploadImageTest

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class Uan_responseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class Match_resultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('name', 'image')