from rest_framework import viewsets

from .models import *
from .serializers import *


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer