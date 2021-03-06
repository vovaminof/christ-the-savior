from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from adminsortable2.admin import SortableAdminMixin

from savior.apps.menu.models import About, Ministry, Project, Course, Contact


class AboutAdmin(SortableAdminMixin, TranslationAdmin):
	pass


class MinistryAdmin(SortableAdminMixin, TranslationAdmin):
	pass


class ProjectAdmin(SortableAdminMixin, TranslationAdmin):
	pass


class CourseAdmin(SortableAdminMixin, TranslationAdmin):
	pass


class ContactAdmin(TranslationAdmin):
	pass


admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Course, CourseAdmin)