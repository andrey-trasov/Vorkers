from django.contrib import admin


from vorkers.models import Vorkers


@admin.register(Vorkers)
class VorkersAdmin(admin.ModelAdmin):
    list_display = ("full_name", "team_number", "salary", "specialization")
