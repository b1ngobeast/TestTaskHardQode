from django.contrib import admin
from .models import Product, StudentInGroup, Lesson, Group, AccessList


admin.site.register(Product)
admin.site.register(StudentInGroup)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(AccessList)
