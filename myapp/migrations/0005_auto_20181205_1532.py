# Generated by Django 2.1.3 on 2018-12-05 15:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='effective_end_date',
            field=models.DateField(blank=True, default=None, help_text='date when this model instance becomes invalid', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='effective_start_date',
            field=models.DateField(blank=True, default=None, help_text='date when this model instance becomes valid', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='globally unique id (UUID4)', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='last_mod_date',
            field=models.DateField(auto_now=True, help_text='when they modified it.'),
        ),
        migrations.AlterField(
            model_name='course',
            name='last_mod_user_name',
            field=models.CharField(default=None, help_text='who last modified this instance', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='courseterm',
            name='effective_end_date',
            field=models.DateField(blank=True, default=None, help_text='date when this model instance becomes invalid', null=True),
        ),
        migrations.AlterField(
            model_name='courseterm',
            name='effective_start_date',
            field=models.DateField(blank=True, default=None, help_text='date when this model instance becomes valid', null=True),
        ),
        migrations.AlterField(
            model_name='courseterm',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='globally unique id (UUID4)', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='courseterm',
            name='last_mod_date',
            field=models.DateField(auto_now=True, help_text='when they modified it.'),
        ),
        migrations.AlterField(
            model_name='courseterm',
            name='last_mod_user_name',
            field=models.CharField(default=None, help_text='who last modified this instance', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='effective_end_date',
            field=models.DateField(blank=True, default=None, help_text='date when this model instance becomes invalid', null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='effective_start_date',
            field=models.DateField(blank=True, default=None, help_text='date when this model instance becomes valid', null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='globally unique id (UUID4)', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='last_mod_date',
            field=models.DateField(auto_now=True, help_text='when they modified it.'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='last_mod_user_name',
            field=models.CharField(default=None, help_text='who last modified this instance', max_length=80, null=True),
        ),
    ]