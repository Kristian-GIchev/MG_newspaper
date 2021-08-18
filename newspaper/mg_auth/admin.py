from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'last_login',)
    list_filter = ('is_staff', 'last_login',)
    search_fields = ('email',)
