# Generated by Django 5.1.2 on 2024-10-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='contact_number',
            field=models.CharField(default='N/A', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='last_donation',
            field=models.DateField(blank=True, null=True),
        ),
    ]