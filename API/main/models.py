import uuid
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
PLAN_CHOICES = [
    ('HO', 'Hobbyist'),
    ('DV', 'Developer'),
    ('PR', 'Premium'),
    ('ET', 'Enterprise'),
]


class Order(models.Model):
    '''
    Orders Model, Usage is outside of the editor
    '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, default='0', on_delete=models.CASCADE)
    plan = models.CharField(max_length=2, choices=PLAN_CHOICES, default='HO',)
    amt = models.DecimalField(decimal_places=2, max_digits=20)
    created = models.DateTimeField(auto_now_add=True)
    invoiceUrl = models.URLField(
        max_length=100, blank=True, default='')  # todo invoice generation

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.plan

    @property
    def expires(self):
        return self.created + datetime.timedelta(days=30)

    @property
    def active(self):
        return self.expires >= timezone.now()


class UserData(models.Model):
    '''
    User Data Model, Usage is outside of the editor
    '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, default='0', on_delete=models.CASCADE, related_name='user_data')
    company = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    #order = models.ForeignKey(Order, default='1',on_delete=models.CASCADE)
    notifyFeature = models.BooleanField(default=True)
    notifyInvoice = models.BooleanField(default=True)
    notifyNews = models.BooleanField(default=True)
    avatar = models.URLField(max_length=100, blank=True, default='')
    about = models.TextField(blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'UserData'

    def __str__(self):
        return self.user.username


class Project(models.Model):
    '''
    Projects Model, Usage is inside of the editor on init
    '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, default='0', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    multipage = models.BooleanField(blank=True, default=False)
    customDomain = models.BooleanField(blank=True, default=False)
    customDomainUrl = models.URLField(max_length=100, blank=True, default='')
    public = models.BooleanField(blank=True, default=False)
    market = models.BooleanField(blank=True, default=False)
    branding = models.BooleanField(blank=True, default=True)
    # ?url for project thumbnail
    preview = models.URLField(max_length=100, blank=True, default='')
    classes = models.CharField(
        max_length=100, blank=True, default='fa fa-picture-o gjs-block gjs-one-bg gjs-four-color-h')
    # todo use project name in subdomain if empty or allow user to set
    domain = models.CharField(max_length=100, blank=True, default='')
    # todo set true if project is published
    published = models.BooleanField(blank=True, default=False)
    lastPublished = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    '''
    Pages Model, Usage is inside of the editor
    '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, default='')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    thumbnail = models.URLField(max_length=100, blank=True, default='')
    favicon = models.URLField(max_length=100, blank=True, default='')
    webclip = models.URLField(max_length=100, blank=True, default='')
    html = models.TextField(blank=True, default='')
    css = models.TextField(blank=True, default='')
    # Remove since script data is kept in the components field
    script = models.TextField(blank=True)
    components = models.TextField(blank=True, default='[]')
    assets = models.TextField(blank=True, default='[]')
    styles = models.TextField(blank=True, default='[]')
    metaTitle = models.CharField(max_length=100, blank=True, default='')
    metaDesc = models.CharField(max_length=100, blank=True, default='')
    slug = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    lastSaved = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

    def getUser(self):
        return self.project.user


class Asset(models.Model):
    '''
    Assets Model, Usage is inside of the editor on init
    '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, default='0', on_delete=models.CASCADE)
    height = models.IntegerField(default='0')
    width = models.IntegerField(default='0')
    file = models.ImageField(
        blank=False, null=False, default='0', height_field='height', width_field='width')
    #filename = models.CharField(max_length=100, blank=True, default='')
    # fileType = models.CharField(
    #    max_length=3, choices=ASSET_TYPE_CHOICES, default='IMG',)
    #url = models.URLField(max_length=100, blank=True, default='')
    # size = models.IntegerField()  # find way to calculate or drop
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['added']

    def __str__(self):
        return self.file.name

    @property
    def size(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value) + ext


class Block(models.Model):
    '''
    Blocks Model, Usage is inside of the editor on init.
    For storing user's custom blocks
    '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True,
                            default='')  # css class= gjs-block-label
    category = models.CharField(max_length=100, blank=True, default='Extra')
    description = models.TextField(blank=True, default='')
    html = models.TextField(blank=True, default='')
    css = models.TextField(blank=True, default='')
    script = models.TextField(blank=True, default='')
    # components = models.TextField(blank=True, default='[]')#!
    # assets = models.TextField(blank=True, default='[]')#!
    # styles = models.TextField(blank=True, default='[]')#!
    # todo get this from uploaded screenshot
    preview = models.ImageField(blank=False, null=False, default='0')
    classes = models.CharField(
        max_length=100, blank=True, default='gjs-fonts gjs-f-b1 gjs-block gjs-one-bg gjs-four-color-h')
    user = models.ForeignKey(User, default='0', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Logic(models.Model):
    '''
    Logic Model, Usage is outside of the editor on init
    '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True,
                            default='')  # css class= gjs-block-label
    category = models.CharField(max_length=100, blank=True, default='Extra')
    description = models.TextField(blank=True, default='')
    script = models.TextField(blank=True, default='')
    user = models.ForeignKey(User, default='0', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Logic'

    def __str__(self):
        return self.name
