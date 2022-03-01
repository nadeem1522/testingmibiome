from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'index/about.html'


class CoEVIDDView(TemplateView):
    template_name = 'index/coevidd.html'


class ContactView(TemplateView):
    template_name = 'index/contact.html'

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
        except KeyError:
            return JsonResponse({
                'status': False, 'message': 'Didn\'t receive all fields'
            })
        subject = 'Enquiry'
        from_email = settings.EMAIL_HOST_USER
        to = ['hello@mibiome.com',]
        send_mail(
            subject,
            f'Hi There\n{name} with email {email} and contact number as {phone} has an enquiry as follows:\n{message}',
            from_email,
            to
        )
        return JsonResponse({
            'status': True, 'message': 'Successfully Sent'})


class HomeView(TemplateView):
    template_name = 'index/home.html'


class NotableProjectsView(TemplateView):
    template_name = 'index/notable_projects.html'


class ResearchView(TemplateView):
    template_name = 'index/research.html'


class ServicesView(TemplateView):
    template_name = 'index/services.html'


class TechnologyView(TemplateView):
    template_name = 'index/technology.html'


class GrantView(TemplateView):
    template_name = 'index/grants.html'


class ClinicalgenomicsView(TemplateView):
    template_name = 'index/clinicalgenomics.html'


class ApplyView(TemplateView):
    template_name = 'index/apply.html'

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            education = request.POST['education']
            stream = request.POST['stream']
            duration = request.POST['duration']
            resume = request.FILES['resume']
        except KeyError:
            return JsonResponse({
                'status': False, 'message': 'Didn\'t receive all fields'
            })
        subject = 'New Career Application'
        from_email = settings.EMAIL_HOST_USER
        to = ['hello@mibiome.com',]

        msg = EmailMultiAlternatives(
            subject=subject, from_email=from_email, to=to,
            body=f'Hi There!\n\nPlease find following details of the candidate\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nEducation: {education}\nStream: {stream}\nDuration: {duration}')
        msg.attach(filename=resume.name, content=resume.read())
        msg.send()
        return JsonResponse({
            'status': True, 'message': 'Successfully Sent'})


class TermsAndConditionsView(TemplateView):
    template_name = 'index/terms_and_conditions.html'


def error_404(request, exception):
        data = {}
        return render(request, 'index/404.html', data)

def error_500(request):
        data = {}
        return render(request,'index/500.html', data)