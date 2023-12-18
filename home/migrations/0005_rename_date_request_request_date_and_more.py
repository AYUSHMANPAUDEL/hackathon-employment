# Generated by Django 5.0 on 2023-12-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_request_is_accepted_alter_request_accepted_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='date',
            new_name='request_date',
        ),
        migrations.AddField(
            model_name='request',
            name='accepted_date',
            field=models.DateField(null=True),
        ),
    ]
