# Generated by Django 2.1.3 on 2018-11-13 14:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20181109_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('effective_start_date', models.DateField(blank=True, default=None, null=True)),
                ('effective_end_date', models.DateField(blank=True, default=None, null=True)),
                ('last_mod_user_name', models.CharField(default=None, max_length=80, null=True)),
                ('last_mod_date', models.DateField(auto_now=True)),
                ('name', models.TextField(max_length=100, unique=True)),
                ('course_terms', models.ManyToManyField(to='myapp.CourseTerm')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
