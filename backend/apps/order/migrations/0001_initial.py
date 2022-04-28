# Generated by Django 3.2.9 on 2022-04-28 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.CharField(max_length=255, verbose_name='Адрес')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Почтовый индекс')),
                ('mobile', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('notice', models.CharField(max_length=255, verbose_name='Комментарий')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('confirmed', 'Подтверждён'), ('send', 'Отправлен'), ('send', 'Отправлен'), ('delivered', 'Доставлен'), ('rejected', 'Отменён')], default='new', max_length=9, verbose_name='Статус')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
