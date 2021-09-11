from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import UserProfile


class UserProfileAdmin(UserAdmin):
    # add_form =
    # form =
    model = UserProfile
    list_display = ["username", "email", "is_staff"]


admin.site.register(UserProfile, UserProfileAdmin)
