from django.contrib import admin
from App.models import iUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group


# Admin panel Changes. 
admin.site.site_header = "✨ ✨ ✨ iCoder ✨ ✨ ✨"
admin.site.site_title = "Welcome to Shuib's' Dashboard."
admin.site.index_title = "Welcome to this Portal."


# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id' ,'email', 'name',  'is_admin')
    list_filter = ('is_admin', 'id')
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'id')
    ordering = ('email', 'id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(iUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
