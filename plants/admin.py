from django.contrib import admin
from .models import Plant, Category

# Register your models here.
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_active")
    list_filter = ("category", "light", "difficulty", "humidity", "is_active")
    search_fields = ("name", "scientific_name")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("friendly_name", "slug", "plant_count")
    search_fields = ("name", "friendly_name")
    prepopulated_fields = {"slug": ("name",)}

    @admin.display(description="Plants")
    def plant_count(self, obj):
        return obj.plants.count()