from django.urls import path

from .views import QuoteFormView, SampleSubView

app_name = 'quote'

urlpatterns = [
    path('quote-form/', QuoteFormView.as_view(), name='quote'),
    path('sample-submission-form/', SampleSubView.as_view(), name='sample'),
]
