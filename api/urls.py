from django.urls import path
from .views import main, sum


urlpatterns = [
    path('home/', main),
    path('sum/', sum)
]
