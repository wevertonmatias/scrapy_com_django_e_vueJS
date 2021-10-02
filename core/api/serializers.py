from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from core.models import Citacoes

class CitacoesSerializers(ModelSerializer):
    class Meta:
        model = Citacoes
        fields = ['id', 'citacao', 'autor']
