# Generated by Django 4.1.5 on 2023-01-26 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_remove_application_application_form_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.level'),
        ),
        migrations.AddField(
            model_name='application',
            name='site_LGA',
            field=models.CharField(default='MN', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.customer'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=255, null=True, unique=True),
        ),
    ]
