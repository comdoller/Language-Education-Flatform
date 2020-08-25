from django.contrib import admin

from .models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display =['idx','created','updated']


admin.site.register(Board,BoardAdmin) # 연결하는 방법.

