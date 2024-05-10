from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin.views.decorators import staff_member_required
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


# Ensure users go through the allauth workflow when logging into admin.
admin.site.login = staff_member_required(admin.site.login, login_url='/accounts/login')
# Run the standard admin set-up.
admin.autodiscover()

admin.site.register(User, UserAdmin)