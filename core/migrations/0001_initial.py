# Generated by Django 3.2.7 on 2021-10-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citacao', models.TextField()),
                ('autor', models.CharField(max_length=150)),
            ],
        ),
    ]
