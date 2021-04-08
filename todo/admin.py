from django.contrib import admin
from .models import todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status',)

admin.site.register(todo,TodoAdmin)
