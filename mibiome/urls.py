"""mibiome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps.index.views import AboutView, CoEVIDDView, ContactView, HomeView, \
    NotableProjectsView, ResearchView, ServicesView, GrantView, ApplyView, \
    ClinicalgenomicsView, TechnologyView, TermsAndConditionsView,\
    error_404, error_500

handler404 = 'apps.index.views.error_404'
handler500 = 'apps.index.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', AboutView.as_view(), name='about'),
    path('coevidd/', CoEVIDDView.as_view(), name='coevidd'),
    path('contact-us/', ContactView.as_view(), name='contact'),
    path('notable-projects/', NotableProjectsView.as_view(),
         name='notable_projects'),
    path('research/', ResearchView.as_view(), name='research'),
    path('services/', ServicesView.as_view(), name='services'),
    path('technology/', TechnologyView.as_view(), name='technology'),
    path('grant/', GrantView.as_view(), name='grant'),
    path(
        'clinicalgenomics/',
        ClinicalgenomicsView.as_view(), name='clinical_genomics'),
    path('apply/', ApplyView.as_view(), name='apply'),
    path(
        'terms-and-conditions/',
        TermsAndConditionsView.as_view(), name='terms'),
    path('forms/', include('apps.quote.urls')),
    path('user/', include('apps.user.urls')),
    path('grants/', include('apps.grant.urls')),
    # path('flash-sale/', include('apps.sale.urls')),
    path('', HomeView.as_view(), name='home'),
]