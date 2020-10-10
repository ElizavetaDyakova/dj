from django.contrib import admin
from .models import Profile, Add, Category, Comment


admin.site.register(Profile)
admin.site.register(Add)
admin.site.register(Category)
admin.site.register(Comment)


from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)