# Generated by Django 2.2 on 2021-05-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210521_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.')], max_length=10, null=True),
        ),
    ]
