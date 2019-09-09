from rest_framework import serializers

from .models import *

class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    reponse = ReponseSerializer(many=True, required=False)
    class Meta:
        model = Question
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many = True, read_only = True, required = False)

    class Meta:
        model = Quiz
        fields = '__all__'
