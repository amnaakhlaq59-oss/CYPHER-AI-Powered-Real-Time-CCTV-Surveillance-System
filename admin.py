from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# 1. Unregister the default User configuration
admin.site.unregister(User)

# 2. Create a Custom configuration
class CustomUserAdmin(UserAdmin):
    # This list controls what columns appear in the table
    list_display = ('username', 'email', 'first_name', 'is_staff', 'date_joined')
    
    # Optional: This makes the most recent users appear at the top
    ordering = ('-date_joined',)

# 3. Register the User model back with the new configuration
admin.site.register(User, CustomUserAdmin)