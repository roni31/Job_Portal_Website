# Generated by Django 2.2 on 2020-06-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtalentpro', '0003_auto_20200630_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='full_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='pincode',
            field=models.PositiveIntegerField(default=560016, null=True),
        ),
    ]