# Generated by Django 4.0.4 on 2022-06-21 21:22

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=25, unique=True, verbose_name='Company')),
                ('tradeName', models.CharField(max_length=100, unique=True, verbose_name='Trade name')),
                ('fiscalName', models.CharField(max_length=50, unique=True, verbose_name='Fiscal name')),
                ('nif', models.CharField(max_length=25, verbose_name='NIF')),
                ('country', models.CharField(max_length=25, verbose_name='Country')),
                ('legalDomicile', models.CharField(max_length=100, verbose_name='Legal domicile')),
                ('state', models.CharField(max_length=25, verbose_name='State')),
                ('zipCode', models.CharField(max_length=25, verbose_name='Zip code')),
                ('phoneNumber1', models.CharField(max_length=25, verbose_name='Phone number 1')),
                ('phoneNumber2', models.CharField(max_length=25, verbose_name='Phone number 2')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('web', models.URLField(max_length=250, verbose_name='Web')),
                ('contact1', models.CharField(max_length=50, verbose_name='Contact 1')),
                ('positionContact1', models.CharField(max_length=50, verbose_name='Position contact 1')),
                ('phoneNumberContact1', models.CharField(max_length=25, verbose_name='Phone number contact 1')),
                ('contact2', models.CharField(max_length=50, verbose_name='Contact 2')),
                ('positionContact2', models.CharField(max_length=50, verbose_name='Position contact 2')),
                ('phoneNumberContact2', models.CharField(max_length=25, verbose_name='Phone number contact 2')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=50, unique=True, verbose_name='Project')),
                ('description', models.CharField(max_length=250, unique=True, verbose_name='Description')),
                ('isActive', models.BooleanField(verbose_name='Is Active')),
                ('sortOrder', models.CharField(max_length=6, unique=True, verbose_name='Sort order')),
                ('createdDateTime', models.DateField(default=django.utils.timezone.now, verbose_name='Created Date Time')),
                ('modifiedDateTime', models.DateField(default=django.utils.timezone.now, verbose_name='Modified Date Time')),
                ('projectCode', models.CharField(default='?????', max_length=5, unique=True, verbose_name='Project code')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectCompanys', to='User.company')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortUserRol', models.CharField(max_length=3, unique=True, verbose_name='Short use rol')),
                ('isActive', models.BooleanField(verbose_name='Active')),
                ('role', models.CharField(max_length=25, unique=True, verbose_name='Role')),
            ],
        ),
        migrations.CreateModel(
            name='StatusProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortStatusProject', models.CharField(max_length=2, unique=True)),
                ('isActive', models.BooleanField()),
                ('statusProject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_login', models.DateField(default=django.utils.timezone.now, verbose_name='Last login')),
                ('username', models.CharField(default='SOME STRING', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='User name')),
                ('first_name', models.CharField(blank=True, default='SOME STRING', max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, default='SOME STRING', max_length=150, verbose_name='Last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff status')),
                ('date_joined', models.DateField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('DOB', models.DateField(default=django.utils.timezone.now, verbose_name='DOB')),
                ('phoneNumber1', models.CharField(max_length=25, verbose_name='Phone Number 1')),
                ('phoneNumber2', models.CharField(max_length=25, verbose_name='Phone Number 2')),
                ('LoginValidFrom', models.DateField(default=django.utils.timezone.now, verbose_name='Login Valid From')),
                ('IsPasswordToBeUpdated', models.SmallIntegerField(blank=True, null=True, verbose_name='Password to be updated')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('userCode', models.CharField(default='????????', max_length=8, unique=True, verbose_name='User code')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userCompanys', to='User.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamCompanys', to='User.company')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamProjects', to='User.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roleCustomUser', to='User.role')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamCustomUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='createdByUserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectCustomUserCreate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='modifiedByUserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectCustomUserModify', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='statusProject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectStatuss', to='User.statusproject'),
        ),
    ]
