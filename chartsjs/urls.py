from django.urls import path
from . import views
from playground import urls


urlpatterns = [
    path('', views.Charts.as_view()),
    # path('test-api', views.get_data),
]
