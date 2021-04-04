from django.urls import path
from . import views,urls
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    path('predict_disease', views.predict_disease , name="predict_disease"),
    path('map_display/<str:disease>',views.map_display, name="map_display"),
    path('doctorAdd',views.doctor_add, name="doctor_add"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)