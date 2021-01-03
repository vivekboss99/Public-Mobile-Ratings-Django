from django.contrib import admin
from .models import Mobiles
# Register your models here.
class MobileAdmin(admin.ModelAdmin):
    list_display=("id","title","description","link","rating")
    exclude=('rcount',)

admin.site.register(Mobiles,MobileAdmin)
