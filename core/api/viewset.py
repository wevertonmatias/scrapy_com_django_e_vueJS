from rest_framework.viewsets import ModelViewSet
from core.models import Citacoes
from .serializers import CitacoesSerializers

class CitacoesViewSet(ModelViewSet):
    queryset = Citacoes.objects.all()
    serializer_class = CitacoesSerializers
