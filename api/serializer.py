from rest_framework.serializers import ModelSerializer
from .models import Urls


class UrlSerializer(ModelSerializer):
    class Meta:
        model = Urls
        fields = "__all__"
