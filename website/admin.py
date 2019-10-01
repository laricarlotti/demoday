from django.contrib import admin
from website.models import User

class Useer(admin.ModelAdmin):
    pass
admin.site.register(User)


