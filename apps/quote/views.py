from datetime import date
import pdfkit

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views.generic import TemplateView

from .forms import QuoteForm, SampleSubForm
from .models import Quote


class QuoteFormView(TemplateView):
    template_name = 'quote/quote_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = date.today().strftime('%Y-%m-%d')
        return context
    
    def post(self, request, *args, **kwargs):
        form = QuoteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            try:
                quote = Quote.objects.create(**form.cleaned_data)
            except:
                context = self.get_context_data()
                context['list_errors'] = ['Database Error']
                return render(request, self.template_name, context=context)
            self.send_mail(form, email)
            self.send_mail_to_cust(email, name, quote.unique_id)
            return redirect('quote:quote')
        else:
            print(form.errors)
            context = self.get_context_data()
            context['errors'] = form.errors.as_data()
            return render(request, self.template_name, context=context)
    
    def send_mail(self, form, email):
        subject = 'New Quote Form Submission'
        from_email = settings.EMAIL_HOST_USER
        to = ['javed@mibiome.com',]
        html = get_template('email/quote.html')
        html = html.render({
            'form': form
        })
        pdf = pdfkit.from_string(html, False)
        msg = EmailMultiAlternatives(
            subject=subject,from_email=from_email, to=to,
            body=f'PFA the quote response pdf file.\nUser Email ID: {email}')
        msg.attach(filename='quote.pdf', content=pdf)
        msg.send()
    
    def send_mail_to_cust(self, email, name, unique_code):
        subject = 'miBiome Therapeutics Confirmation'
        from_email = settings.EMAIL_HOST_USER
        to = [email,]
        send_mail(
            subject=subject, from_email=from_email, recipient_list=to,
            message=f'Hello {name}!\n\nWe have received your request for a Quote.\n\n{unique_code} is your Request Number. For future doubts and queries use this Request Number for smooth communication and you can also use this Request Number for Sample Submission Form.\n\nOur team will connect with you soon.\n\nThanks.\n\nmiBiome Therapeutics LLP'
        )


class SampleSubView(TemplateView):
    template_name = 'quote/sample_sub_form.html'

    def post(self, request, *args, **kwargs):
        try:
            post_type = request.POST['post_type']
        except KeyError:
            context = self.get_context_data()
            context['list_errors'] = ['Type of form not received']
            return render(request, self.template_name, context=context)
        
        try:
            request_number = request.POST['request_number']
        except KeyError:
            context = self.get_context_data()
            context['list_errors'] = ['Request number not received']
            return render(request, self.template_name, context=context)
        
        try:
            quote = Quote.objects.get(unique_id=request_number)
        except Quote.DoesNotExist:
            context = self.get_context_data()
            context['list_errors'] = ['This request number does not exist']
            return render(request, self.template_name, context=context)
        
        if post_type == 'request-number':
            return render(request, self.template_name, context={
                'quote': quote
            })
        else:
            if quote.sample_sub_attempts >= 3:
                context = self.get_context_data()
                context['list_errors'] = ['Maximum attempts reached for this form']
                context['quote'] = quote
                return render(request, self.template_name, context=context)
            form = SampleSubForm(request.POST)
            if form.is_valid():
                try:
                    sample_labelled = request.POST.getlist('sample_labelled')
                    species = request.POST.getlist('species')
                    source = request.POST.getlist('source')
                    qubit = request.POST.getlist('qubit')
                    total_volume = request.POST.getlist('total_volume')
                    total_amount = request.POST.getlist('total_amount')
                    od_280 = request.POST.getlist('od_280')
                    od_230 = request.POST.getlist('od_230')
                    library_type = request.POST.getlist('library_type')
                    barcode = request.POST.getlist('barcode')
                    pcr_product_size = request.POST.getlist('pcr_product_size')
                    gb_sample = request.POST.getlist('gb_sample')
                    remark = request.POST.getlist('remark')
                except KeyError:
                    context = self.get_context_data()
                    context['list_errors'] = ['All values of sample information were not provided']
                    context['qutoe'] = quote
                    return render(request, self.template_name, context=context)
                samples = []
                for i in range(sample_labelled.__len__()):
                    data_set = {}
                    data_set['sample_labelled'] = sample_labelled[i]
                    data_set['species'] = species[i]
                    data_set['source'] = source[i]
                    data_set['qubit'] = qubit[i]
                    data_set['total_volume'] = total_volume[i]
                    data_set['total_amount'] = total_amount[i]
                    data_set['od_280'] = od_280[i]
                    data_set['od_230'] = od_230[i]
                    data_set['library_type'] = library_type[i]
                    data_set['barcode'] = barcode[i]
                    data_set['pcr_product_size'] = pcr_product_size[i]
                    data_set['gb_sample'] = gb_sample[i]
                    data_set['remark'] = remark[i]
                    samples.append(data_set)
                self.send_mail(form, samples)
                quote.sample_sub_attempts += 1
                quote.save()
                return redirect('quote:sample')
            else:
                print(form.errors)
                context = self.get_context_data()
                context['errors'] = form.errors.as_data()
                context['quote'] = quote
                return render(request, self.template_name, context=context)
    
    def send_mail(self, form, samples):
        subject = 'New Sample Submission Form'
        from_email = settings.EMAIL_HOST_USER
        to = ['hello@mibiome.com',]
        html = get_template('email/sample.html')
        html = html.render({
            'form': form,
            'samples': samples
        })
        pdf = pdfkit.from_string(html, False)
        msg = EmailMultiAlternatives(
            subject=subject, from_email=from_email, to=to, body='PFA the sample submission form pdf file.')
        msg.attach(filename='sample_submission.pdf', content=pdf)
        msg.send()