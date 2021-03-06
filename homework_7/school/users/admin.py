from django.contrib import admin

from .models import (
    Teacher,
    Customer,
    Student,
    FeedbackMessage,
)

from django.contrib.auth.admin import UserAdmin


class BaseUserAdminConfig(UserAdmin):
    # define method thet will be visiblein the admin panel
    # lesson 18 0:55
    actions = ["say_hello"]
    # This method can do modifications on selected objects
    def say_hello(self, request, queryset):
        # print(queryset)
        for item in queryset:
            print(item)

    search_fields = (
        "email",
        "last_name",
        "first_name",
    )
    list_filter = (
        "is_active",
        "is_staff",
    )
    ordering = ("-last_name",)
    list_display = (
        "last_name",
        "first_name",
        "email",
        "email",
        "phone",
        "is_active",
        "is_staff",
    )

    fieldsets = (
        (
            "Main info",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "ssn",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "ssn",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


class CustomerAdminConfig(BaseUserAdminConfig):
    fieldsets = (
        (
            "Main info",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "ssn",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                )
            },
        ),
        (
            "Additional",
            {"fields": ("want_invoice",)},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "ssn",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "want_invoice",
                ),
            },
        ),
    )


class StudentAdminConfig(BaseUserAdminConfig):
    fieldsets = (
        (
            "Main info",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "ssn",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                )
            },
        ),
        (
            "Additional",
            {"fields": ("bound_customer",)},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "ssn",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "bound_customer",
                ),
            },
        ),
    )


admin.site.register(
    Customer,
    CustomerAdminConfig,
)
admin.site.register(
    Student,
    StudentAdminConfig,
)
admin.site.register(
    Teacher,
    BaseUserAdminConfig,
)
admin.site.register(FeedbackMessage)