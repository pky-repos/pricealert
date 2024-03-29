# Generated by Django 4.1.7 on 2024-02-26 12:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceAlert',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('symbol', models.CharField(max_length=10)),
                ('price_limit', models.FloatField()),
                ('lower_higher', models.CharField(choices=[('l', 'lower'), ('h', 'higher')], max_length=2)),
                ('status', models.CharField(choices=[('CR', 'Created'), ('DE', 'Deleted'), ('TR', 'Trigerred'), ('IA', 'Inactive')], default='CR', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
