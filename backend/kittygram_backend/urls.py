from cats.views import AchievementViewSet, CatViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.views.generic import TemplateView
from django.urls import re_path

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),  # Работа с пользователями
    path('api/', include('djoser.urls.authtoken')),  # Работа с токенами
]
urlpatterns += [
    re_path(r'^$', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += [static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT),]
