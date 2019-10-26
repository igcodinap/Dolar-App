from rest_framework import viewsets

from .models import Dolar
from .serializers import DolarSerializer

class DolarViewSet(viewsets.ModelViewSet):
    queryset = Dolar.objects.all()
    serializer_class = DolarSerializer
