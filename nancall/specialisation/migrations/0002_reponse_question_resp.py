# Generated by Django 2.2.4 on 2019-09-08 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialisation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reponse',
            name='question_resp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_rep', to='specialisation.Question'),
        ),
    ]