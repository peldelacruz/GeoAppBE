# Generated by Django 4.0.4 on 2022-06-04 21:52

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
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=60, unique=True)),
                ('usernames', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_company_author_usernames', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateField(blank=True, null=True, verbose_name='last_login')),
                ('is_active', models.BooleanField(default=False, null=True, verbose_name='is_active')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email_address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_customuser_company_company', to='User.company')),
                ('usernames', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fk_customuser_author_usernames', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=250, unique=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_usercustom_project_id', to='User.customuser')),
            ],
        ),
    ]
