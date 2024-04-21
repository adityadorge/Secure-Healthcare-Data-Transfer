from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields':('email', 'password','name','role','last_login')}),
        ('Permissions', {'fields':(
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )})
    )
    add_fieldsets = (
        (
            None,{
                'classes':('wide',),
                'fields':('email','role', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff','last_login', 'role')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)