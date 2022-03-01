from django.urls import path

from .views import GrantApplicationView


app_name = 'grant'

urlpatterns = [
    path('apply/', GrantApplicationView.as_view(), name='apply'),
]