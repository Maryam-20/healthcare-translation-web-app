from django.urls import path
from translator.views import home, translate_text

urlpatterns = [
    path('', home, name="home"),
    path('api/translate/', translate_text, name="translate"),
]
