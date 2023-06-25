# Generated by Django 4.2.2 on 2023-06-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_notificationtype_alter_notification_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('delivery_rate', models.FloatField()),
                ('user_engagement', models.FloatField()),
                ('template', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
