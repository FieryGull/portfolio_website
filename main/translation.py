from modeltranslation.translator import register, TranslationOptions
from .models import HomeBlock, BiographyBlock, ConferenceBlock, AchievementBlock, PublicationBlock, \
    Publication, ProjectBlock, CourseVideo, CourseBlock, NavContent


@register(NavContent)
class NavContentTranslationOptions(TranslationOptions):
    fields = ('logo_text', )

@register(HomeBlock)
class HomeBlockTranslationOptions(TranslationOptions):
    fields = ('block_title', 'block_text')


@register(BiographyBlock)
class BiographyContentTranslationOptions(TranslationOptions):
    fields = ('block_title', 'block_text')


@register(ConferenceBlock)
class ConferencesBlockTranslationOptions(TranslationOptions):
    fields = ('block_title', 'block_text')


@register(AchievementBlock)
class ScienceProgressBlockTranslationOptions(TranslationOptions):
    fields = ('block_title', 'block_text')


@register(Publication)
class PublicationsBlockTranslationOptions(TranslationOptions):
    fields = ('name', 'authors_publications', 'other_text',)


@register(PublicationBlock)
class PublicationsContentTranslationOptions(TranslationOptions):
    fields = ('block_title',)


@register(ProjectBlock)
class ProjectsBlockTranslationOptions(TranslationOptions):
    fields = ('block_title', 'block_text')

@register(CourseBlock)
class CoursesContentTranslationOptions(TranslationOptions):
    fields = ('block_title', 'block_text')


@register(CourseVideo)
class CoursesBlockTranslationOptions(TranslationOptions):
    fields = ('video_name',)
