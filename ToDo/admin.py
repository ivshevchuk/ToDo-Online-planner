from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_due_date', 'get_status')

    def get_due_date(self, obj):
        return obj.due_date.strftime('%b %d %Y %I:%M %p')

    def get_status(self, obj):
        return obj.status.strftime('%b %d %Y %I:%M %p')

    get_due_date.admin_order_field = 'due_date'

    get_status.admin_order_field = 'status'


admin.site.register(Task, TaskAdmin)
