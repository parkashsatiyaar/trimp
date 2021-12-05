from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import re_path
from django.views.generic.base import RedirectView
from api.views import Redirector
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic.base import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Trimp API",
        default_version='v1',
        description="Trimp is online tool for url shortening. You can use it for your projects but for comercial use you have to purchase License, For purchase license you can contact us at parkashsatiyaar0008@gmail.com",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="parkashsatiyaar0008@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('<str:short_char>/', Redirector.as_view(), name="redirector"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns.append(path('', TemplateView.as_view(
    template_name="index.html"), name="home"))
urlpatterns.append(re_path('^.*', RedirectView.as_view(url=f"/swagger/")))
