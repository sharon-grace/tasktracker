from django.contrib import admin
from .models import Task
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
    list_per_page = 20


admin.site.register(Task,TaskAdmin)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_staff', 'is_active', 'is_super_admin')
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_super_admin')
    search_fields = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_super_admin', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active', 'is_super_admin'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
