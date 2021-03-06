# Generated by Django 2.2 on 2020-06-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtalentpro', '0006_auto_20200630_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateprofile',
            name='dob',
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=30),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='pincode',
            field=models.PositiveIntegerField(default=560016, null=True),
        ),
    ]
