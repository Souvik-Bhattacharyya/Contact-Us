from django.contrib import admin
from django.utils.html import format_html
from . import models


class ProjectImageInline(admin.TabularInline):
    model = models.ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ]
    list_display = ['title']
    search_fields = ['title', 'description']
    list_filter = ['category']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'date_time']
    search_fields = ['name', 'contact', 'meessage']
    list_filter = ['date_time']
    readonly_fields = ['name', 'contact', 'date_time', 'message']

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False


class ReviewAdmin(admin.ModelAdmin):
    def prof_thumb(self, obj):
        return format_html("<img src='{}' style='width: 64px; height: 64px; object-fit: scale-down; border-radius: 32px;' />".format(obj.img.url))

    list_display = ['prof_thumb', 'name', 'review']
    fields = ['prof_thumb', 'img', 'name', 'review']
    readonly_fields = ['prof_thumb']


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ContactUs, ContactUsAdmin)
admin.site.register(models.Review, ReviewAdmin)
