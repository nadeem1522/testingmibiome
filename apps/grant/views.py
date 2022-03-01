from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from .models import GrantApplication


class GrantApplicationView(LoginRequiredMixin, TemplateView):
    template_name = 'grant/apply.html'

    def get_ipaddress(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def send_mail_to_team(self, user, grant):
        subject = 'New Grant Application'
        from_email = settings.EMAIL_HOST_USER
        to = ['hello@mibiome.com',]
        email_template_name = 'grant/apply_team.txt'
        c = {
            'name': user.name(),
            'email': user.email,
            'phone': user.phone,
            'affiliation': user.affiliation,
            'designation': user.designation,
            'industry': user.industry,
            'title': grant.title,
            'description': grant.description,
            'nature_of_experiment': grant.nature_of_experiment,
            'dna_source': grant.dna_source,
            'dna_source_others': grant.dna_source_others,
        }
        email = render_to_string(email_template_name, c)
        send_mail(subject, email, from_email, to, fail_silently=False)

    def post(self, request, *args, **kwargs):
        try:
            title = request.POST['title']
            description = request.POST['description']
            nature_of_experiment = request.POST['nature_of_experiment']
            dna_source = request.POST['dna_source']
            dna_source_others = request.POST['dna_source_others']
        except KeyError:
            return JsonResponse({
                'status': False, 'message': 'All the fields are not submitted'
            })
        
        ip = self.get_ipaddress(request)
        application = GrantApplication.objects.create(
            user=request.user,
            title=title,
            description=description,
            nature_of_experiment=nature_of_experiment,
            dna_source=dna_source,
            dna_source_others=dna_source_others,
            ipaddress=ip
        )

        try:
            self.send_mail_to_team(request.user, application)
        except BadHeaderError:
            return JsonResponse({
                'status': False, 'message': 'Connection error please try again'
            })
        
        return JsonResponse({
            'status': True, 'message': 'Successfully submitted'
        })