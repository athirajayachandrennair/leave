from django.contrib import admin

# Register your models here.
from .models import table,enq,ad,staf,jew

admin.site.register(table)
admin.site.register(enq)
admin.site.register(ad)
admin.site.register(staf)
admin.site.register(jew)