# Generated by Django 4.2.2 on 2023-08-27 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KuProApp', '0002_remove_user_birth_date_remove_user_mobile_number_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='seller_owner',
            field=models.ForeignKey(default=1, limit_choices_to={'user_type': 'SELLER'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
