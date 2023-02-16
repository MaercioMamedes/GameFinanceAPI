from rest_framework import viewsets
from core.models import Paper
from core.serializers import PaperSerializer


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

