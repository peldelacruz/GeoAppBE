from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _
from .managers import CustomUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

import random
import datetime
import string

class Company(models.Model):
    company = models.CharField(_('Company'),max_length=25, unique=True)
    tradeName = models.CharField(_('Trade name'),max_length=100, unique=True)
    fiscalName = models.CharField(_('Fiscal name'),max_length=50, unique=True)
    nif = models.CharField(_('NIF'),max_length=25, unique=False)
    country = models.CharField(_('Country'),max_length=25, unique=False)
    legalDomicile = models.CharField(_('Legal domicile'),max_length=100, unique=False)
    state = models.CharField(_('State'),max_length=25, unique=False)
    zipCode = models.CharField(_('Zip code'),max_length=25, unique=False)
    phoneNumber1 = models.CharField(_('Phone number 1'),max_length=25, unique=False)
    phoneNumber2 = models.CharField(_('Phone number 2'),max_length=25, unique=False)
    email = models.EmailField(_('Email'),max_length=254, unique=False)
    web = models.URLField(_('Web'),max_length=250, unique=False)
    contact1 = models.CharField(_('Contact 1'),max_length=50, unique=False)
    positionContact1 = models.CharField(_('Position contact 1'),max_length=50, unique=False)
    phoneNumberContact1 = models.CharField(_('Phone number contact 1'),max_length=25, unique=False)
    contact2 = models.CharField(_('Contact 2'),max_length=50, unique=False)
    positionContact2 = models.CharField(_('Position contact 2'),max_length=50, unique=False)
    phoneNumberContact2 = models.CharField(_('Phone number contact 2'),max_length=25, unique=False)
    def __str__(self):
        return self.company

class StatusProject(models.Model):
    shortStatusProject = models.CharField(max_length=2, unique=True)
    isActive = models.BooleanField()
    statusProject = models.CharField(max_length=50, unique=False) #Ingeniería de perfil, Estudio de prefactibilidad (ingeniería conceptual), Estudio de factibilidad (ingeniería básica), Ingeniería de detalle, Ejecución (inversional), Operación
    REQUIRED_FIELDS = ['shortStatusProject','isActive','statusProject']
    def __str__(self):
        return '%s: %s' % (self.shortStatusProject, self.statusProject)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    groups = None
    user_permissions = None
    last_login= models.DateField(_('Last login'), default=timezone.now)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('User name'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        default='SOME STRING',
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('First name'), max_length=150, blank=True, default='SOME STRING')
    last_name = models.CharField(_('Last name'), max_length=150, blank=True, default='SOME STRING')
    #is_superuser = None
    is_staff = models.SmallIntegerField(_('Staff'))
    is_active = models.BooleanField(
        _('Active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ))
    is_staff = models.BooleanField(
        _('Staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    date_joined = models.DateField(_('date joined'), default=timezone.now)
    DOB = models.DateField(_('DOB'), default=timezone.now)
    phoneNumber1 = models.CharField(_('Phone Number 1'),max_length=25, unique=False)
    phoneNumber2 = models.CharField(_('Phone Number 2'),max_length=25, unique=False)
    LoginValidFrom = models.DateField(_('Login Valid From'), default=timezone.now)
    IsPasswordToBeUpdated = models.SmallIntegerField(_('Password to be updated'),null=True, blank=True)
    email = models.EmailField(_('Email address'), unique=True)
    company  = models.ForeignKey(Company, related_name='userCompanys', on_delete=models.CASCADE, null=True)
    userCode = models.CharField(_('User code'),max_length=8, unique=True, default='????????') 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    objects = CustomUserManager()

    def __str__(self):
        return '%s: %s' % (self.company,  self.username)


class Project(models.Model):
    project = models.CharField(_('Project'),max_length=50, unique=True) 
    description = models.CharField(_('Description'),max_length=250, unique=True) 
    company  = models.ForeignKey(Company, related_name='projectCompanys', on_delete=models.CASCADE)
    statusProject = models.ForeignKey(StatusProject, related_name='projectStatuss', on_delete=models.CASCADE)
    isActive = models.BooleanField(_('Is Active'))
    sortOrder = models.CharField(_('Sort order'),max_length=6, unique=True)
    createdByUserID = models.ForeignKey(CustomUser, related_name='projectCustomUserCreate', on_delete=models.DO_NOTHING)
    createdDateTime = models.DateField(_('Created Date Time'), default=timezone.now)
    modifiedByUserID = models.ForeignKey(CustomUser, related_name='projectCustomUserModify', on_delete=models.DO_NOTHING)
    modifiedDateTime = models.DateField(_('Modified Date Time'), default=timezone.now)
    projectCode = models.CharField(_('Project code'), max_length=5, unique=True, default='?????') 

    def __str__(self):
        return '%s: %s' % (self.projectCode, self.project)       


class Role(models.Model):
    shortUserRol = models.CharField(_('Short use rol'),max_length=3, unique=True)
    isActive = models.BooleanField(_('Active'))
    role = models.CharField(_('Role'),max_length=25, unique=True) #Ingeniería de perfil, Estudio de prefactibilidad (ingeniería conceptual), Estudio de factibilidad (ingeniería básica), Ingeniería de detalle, Ejecución (inversional), Operación
    REQUIRED_FIELDS = ['shorttatusProject','isActive','statusProject']
    def __str__(self):
        return '%s: %s' % (self.shortUserRol, self.role)

class Team(models.Model):
    company  = models.ForeignKey(Company, related_name='teamCompanys', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='teamProjects', on_delete=models.CASCADE)
    username = models.ForeignKey(CustomUser, related_name='teamCustomUser', on_delete=models.CASCADE)
    role  = models.ForeignKey(Role, related_name='roleCustomUser', on_delete=models.CASCADE)
    def __str__(self):
        return '%s: %s' % (self.company, self.project)