# Generated by Django 2.2 on 2020-06-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtalentpro', '0002_auto_20200630_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='dob',
            field=models.DateField(default='1947-08-15', verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=30),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='stream',
            field=models.CharField(default='B.E/BTech', max_length=60),
        ),
    ]
