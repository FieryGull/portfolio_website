from django.contrib import admin
from .models import HomeBlock, BiographyBlock, ConferenceBlock, AchievementBlock, PublicationBlock, \
    ProjectBlock, Publication, CourseBlock, CourseVideo, NavContent
from modeltranslation.admin import TranslationAdmin


@admin.register(NavContent)
class NavContent(TranslationAdmin):
    pass

@admin.register(HomeBlock)
class HomeContent(TranslationAdmin):
    pass


# BiographyAdmin ------------------------
@admin.register(BiographyBlock)
class BiographyBlock(TranslationAdmin):
    pass


# PublicationsAdmin ------------------------
class PublicationInline(admin.TabularInline):
    model = Publication


@admin.register(PublicationBlock)
class PublicationsBlock(TranslationAdmin):
    inlines = [PublicationInline]


# ConferencesAdmin ------------------------

@admin.register(ConferenceBlock)
class ConferenceBlock(TranslationAdmin):
    pass


# ScienceProgressAdmin ------------------------

@admin.register(AchievementBlock)
class ScienceProgressBlock(TranslationAdmin):
    pass


# ConferencesAdmin ------------------------

@admin.register(ProjectBlock)
class ProjectBlock(TranslationAdmin):
    pass


# CoursesAdmin ------------------------
class CoursesVideoInline(admin.TabularInline):
    model = CourseVideo


@admin.register(CourseBlock)
class CoursesBlock(TranslationAdmin):
    inlines = [CoursesVideoInline]