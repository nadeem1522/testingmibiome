from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import validate_password, \
    ValidationError
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import TemplateView, UpdateView

from .forms import ProfileForm


class LoginView(TemplateView):
    template_name = 'user/login.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def get(self, request, *args, **kwargs):
        redirect_url = request.GET.get('next', None)
        if request.user.is_authenticated:
            if redirect_url:
                return redirect(redirect_url)
            else:
                return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return render(request, self.template_name, context={
                'status': False, 'message': 'Email or Password not provided'
            })

        user = authenticate(request=request, username=email, password=password)
        if not user:
            return render(request, self.template_name, context={
                'status': False, 'message': 'Email or Password is incorrect'
            })
        else:
            if user.is_active:
                login(request=request, user=user)
                if user.is_superuser:
                    return redirect('/admin/')
                else:
                    try:
                        next = request.GET['next']
                        return redirect(next)
                    except KeyError:
                        return redirect('grant:apply')
            else:
                return render(request, self.template_name, context={
                    'status': False,
                    'message': 'Inactive user'
                })


class SignUpView(TemplateView):
    template_name = 'user/signup.html'

    def post(self, request, *args, **kwargs):
        # check email and password is there in post request
        try:
            title = request.POST['title']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            affiliation = request.POST['affiliation']
            designation = request.POST['designation']
            industry = request.POST['industry']
            phone = request.POST['phone']
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return JsonResponse({
                'status': False, 'message': 'Please fill all the details'})

        # see if password validations is met
        try:
            validate_password(password)
        except ValidationError as e:
            return JsonResponse({
                'status': False, 'message': str(e).strip("[]'")})

        try:
            get_user_model().objects.create_user(
                title=title,
                first_name=first_name,
                last_name=last_name,
                affiliation=affiliation,
                designation=designation,
                industry=industry,
                phone=phone,
                email=email,
                password=password
            )
        except IntegrityError:
            return JsonResponse({
                'status': False,
                'message': 'This email or phone number is already registered'})

        return JsonResponse({'status': True, 'message': 'Success'})


class ProfileView(UpdateView, LoginRequiredMixin):

    model = get_user_model()
    form_class = ProfileForm
    queryset = get_user_model().objects.all()
    template_name = 'user/profile.html'

    def get_success_url(self):
        return reverse_lazy(
            'user:profile', kwargs={'pk': self.request.user.id})


class PasswordResetView(TemplateView):
    template_name = 'user/password_reset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["password_reset_form"] = PasswordResetForm()
        return context
    
    def post(self, request, *args, **kwargs):
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = get_user_model().objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "miBiome Therapeutics Password Reset Token"
                    email_template_name = "user/password_reset_email.txt"
                    c = {
                        'email': user.email,
                        'domain': self.request.get_host(),
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
                    except BadHeaderError:
                        context = self.get_context_data()
                        context['error'] = 'Invalid header found'
                        return render(
                            request, self.template_name, context=context
                        )
                    return redirect('user:password_reset_done')
            else:
                context = self.get_context_data()
                context['error'] = 'User with this email do not exists'
                return render(
                    request, self.template_name, context=context
                )
        return redirect('user:password_reset')