# Generated by Django 3.2.7 on 2021-09-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.IntegerField(blank=True, choices=[('1', 'English'), ('2', 'Tamil'), ('3', 'Hindi'), ('4', 'Telugu'), ('5', 'Malayalam')], default='1', help_text='Enter the language', max_length=1)),
            ],
        ),
    ]
