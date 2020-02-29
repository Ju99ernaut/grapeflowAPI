import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PLAN_CHOICES = [
    ('HO', 'Hobbyist'),
    ('DV', 'Developer'),
    ('ET', 'Enterprise'),
]


class Order(models.Model):
    user = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    plan = models.CharField(max_length=2, choices=PLAN_CHOICES, default='HO',)
    amt = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()
    #prevOrder = models.ForeignKey(Order, default='1',on_delete=models.CASCADE)
    invoiceUrl = models.URLField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.plan


class UserData(models.Model):
    user = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    #order = models.ForeignKey(Order, default='1',on_delete=models.CASCADE)
    notifyFeature = models.BooleanField(default=True)
    notifyInvoice = models.BooleanField(default=True)
    notifyNews = models.BooleanField(default=True)
    notifyFeature = models.BooleanField(default=True)
    avatar = models.URLField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'UserData'

    # def __str__(self):
    #    return self.user.username


class Project(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    preview = models.URLField(max_length=100, blank=True, default='')
    classes = models.CharField(
        max_length=100, blank=True, default='fa fa-picture-o gjs-block gjs-one-bg gjs-four-color-h')
    domain = models.URLField(max_length=100, blank=True, default='')
    published = models.BooleanField(default=False)
    lastPublished = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, default='')
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    thumbnail = models.URLField(max_length=100, blank=True, default='')
    favicon = models.URLField(max_length=100, blank=True, default='')
    webclip = models.URLField(max_length=100, blank=True, default='')
    html = models.TextField()
    css = models.TextField()
    js = models.TextField()
    components = models.TextField()
    style = models.TextField()
    metaTitle = models.CharField(max_length=100, blank=True, default='')
    metaDesc = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    lastSaved = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


ASSET_TYPE_CHOICES = [
    ('IMG', 'Image'),
    ('SVG', 'SVG'),
    ('VID', 'Video'),
]


class Asset(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    filename = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(
        max_length=3, choices=ASSET_TYPE_CHOICES, default='IMG',)
    url = models.URLField(max_length=100, blank=True, default='')
    size = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['added']

    def __str__(self):
        return self.filename


class Block(models.Model):
    name = models.CharField(max_length=100, blank=True,
                            default='')  # css class= gjs-block-label
    category = models.CharField(max_length=100, blank=True, default='Extra')
    description = models.TextField()
    html = models.TextField()
    css = models.TextField()
    preview = models.URLField(max_length=100, blank=True, default='')
    classes = models.CharField(
        max_length=100, blank=True, default='gjs-fonts gjs-f-b1 gjs-block gjs-one-bg gjs-four-color-h')
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Logic(models.Model):
    name = models.CharField(max_length=100, blank=True,
                            default='')  # css class= gjs-block-label
    category = models.CharField(max_length=100, blank=True, default='Extra')
    description = models.TextField()
    js = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Logic'

    def __str__(self):
        return self.name
