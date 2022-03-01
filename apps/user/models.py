from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    user_count = None

    def generate_customer_id(self):
        if self.user_count:
            self.user_count += 1
            return 'MC{:06d}'.format(self.user_count)
        else:
            last_object = self.model.objects.all().last()
            if last_object:
                self.user_count = int(last_object.customer_id.split('MC')[-1])
            else:
                self.user_count = -1
            self.user_count += 1
            return 'MC{:06d}'.format(self.user_count)

    def create_user(self, email, password, *args, **kwargs):
        customer_id = self.generate_customer_id()
        user = self.model(customer_id=customer_id,
                          email=self.normalize_email(email), *args, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        user = self.create_user(email, password, *args, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    TITLE_CHOICES = (
        ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.'),
        ('Prof.', 'Prof.')
    )
    INDUSTRY_CHOICES = (
        ('Academia', 'Academia'), ('Hospitals', 'Hospitals'),
        ('Diagnostic Laboratory', 'Diagnostic Laboratory'),
        ('Clinicians', 'Clinicians'),
        ('Pharmaceutical Company', 'Pharmaceutical Company'),
        ('Biotech Company', 'Biotech Company'),
        ('Genomics Company', 'Genomics Company'),
        ('Consumer Company', 'Consumer Company')
    )

    customer_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, null=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    affiliation = models.CharField(max_length=500, null=True)
    designation = models.CharField(max_length=500, null=True)
    industry = models.CharField(
        max_length=100, choices=INDUSTRY_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def name(self):
        return f'{self.title} {self.first_name} {self.last_name}'