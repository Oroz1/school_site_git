# Generated by Django 3.2.10 on 2022-01-02 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
