from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import View
from rest_framework.permissions import AllowAny
from api.models import Urls
from api.serializer import UrlSerializer
# Create your views here.


class ShortenerListAPIView(ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [AllowAny]


class Redirector(View):
    def get(self, request, short_char, *args, **kwargs):
        if not Urls.objects.filter(
                short_char=short_char).exists():
            return redirect('home')
        redirect_link = Urls.objects.filter(
            short_char=short_char).first().original_url
        return redirect(redirect_link)
