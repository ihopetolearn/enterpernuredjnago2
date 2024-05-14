from django.contrib import admin
from .models import Recipe,RecipeIngredient


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    fields = ["name","quantity","direction","unit"]
    extra = 2


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display =["name","user"]
    readonly_fields = ["timestamp","updated_time"]
    raw_id_fields = ["user"]


admin.site.register(Recipe,RecipeAdmin)

