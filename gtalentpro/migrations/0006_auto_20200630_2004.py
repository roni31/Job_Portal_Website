# Generated by Django 2.2 on 2020-06-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtalentpro', '0005_auto_20200630_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='dob',
            field=models.DateField(default='1947-08-15', verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
        ),
    ]
