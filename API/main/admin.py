from django.contrib import admin
from .models import Order, UserData, Project, Page, Asset, Block, Logic

# Register your models here.
admin.site.register(Order)
admin.site.register(UserData)
admin.site.register(Project)
admin.site.register(Page)
admin.site.register(Asset)
admin.site.register(Block)
admin.site.register(Logic)
