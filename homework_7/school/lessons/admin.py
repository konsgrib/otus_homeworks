from django.contrib import admin

from .models import (
    SchoolGroup,
    GroupType,
    Lesson,
)


admin.site.register(SchoolGroup)
admin.site.register(GroupType)
admin.site.register(Lesson)
