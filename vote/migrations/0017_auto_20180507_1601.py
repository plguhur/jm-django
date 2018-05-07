# Generated by Django 2.0.3 on 2018-05-07 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0016_auto_20180429_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='supervisor',
        ),
        migrations.AddField(
            model_name='supervisor',
            name='election',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vote.Election'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
