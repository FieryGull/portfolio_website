from django.db import models


# NavContent + allLinks -----------------------------

class NavContent(models.Model):
    logo_text = models.CharField('Текст логотипа', max_length=50)
    link_logo_image = models.CharField('Ссылка на фотографию', max_length=100, blank=True)
    email = models.EmailField('Почта', max_length=50)
    link_yt = models.CharField('Ссылка на YouTube', max_length=100)
    link_inst = models.CharField('Ссылка на Instagram', max_length=100)
    link_vk = models.CharField('Ссылка на VK', max_length=100)
    link_fb = models.CharField('Ссылка на Ссылка на Facebook', max_length=100)
    link_rg = models.CharField('Ссылка на ResearchGate', max_length=100)
    link_orcid = models.CharField('Ссылка на ORCID', max_length=100)
    link_gs = models.CharField('Ссылка на GoogleScholar', max_length=100)
    link_scopus = models.CharField('Ссылка на Scopus', max_length=100)
    link_publons = models.CharField('Ссылка на Publons', max_length=100)

    def __str__(self):
        return self.logo_text

    class Meta:
        verbose_name = 'Контент навигационного меню и ссылок с главной страницы'
        verbose_name_plural = 'Контент навигационного меню и ссылок с главной страницы'


# HomePage -----------------------------
class HomeBlock(models.Model):
    block_title = models.CharField('Подзаголовок блока информации', max_length=100)
    block_text = models.TextField('Контент блока')
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Контент главной страницы'
        verbose_name_plural = 'Контент главной страницы'


# PublicationsPage -----------------------------

class PublicationBlock(models.Model):
    block_title = models.CharField('Подзаголовок блока информации', max_length=100)
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Контент страницы публикаций'
        verbose_name_plural = 'Контент страницы публикаций'


class Publication(models.Model):
    PublicationsBlock = models.ForeignKey(PublicationBlock, on_delete=models.CASCADE)
    name = models.TextField('Наименование публикации')
    authors_publications = models.TextField('Авторы')
    other_text = models.TextField('Другая информация')
    link = models.CharField('Ссылка на публикацию', max_length=300, blank=False)
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


# BiographyPage -----------------------------

class BiographyBlock(models.Model):
    block_title = models.CharField('Подзаголовок блока информации', max_length=100)
    block_text = models.TextField('Контент блока')
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Контент биографической справки'
        verbose_name_plural = 'Контент биографической справки'
# ---------------------------------------------------------------------------------------


# ProjectsPage ---------------------------------------------

class ProjectBlock(models.Model):
    block_title = models.CharField('Подзаголовок блока информации', max_length=100)
    block_text = models.TextField('Контент блока')
    link_image = models.CharField('Ссылка на изображение', max_length=200, default='/')
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Контент страницы проектов'
        verbose_name_plural = 'Контент страницы проектов'
# ----------------------------------------------------------------


# ConferencesPage ---------------------------------------------

class ConferenceBlock(models.Model):
    block_title = models.CharField('Подзаголовок блока информации', max_length=100)
    block_text = models.TextField('Контент блока')
    link_image = models.CharField('Ссылка на изображение', max_length=200, default='/')
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Контент страницы конференций'
        verbose_name_plural = 'Контент страницы конференций'
# ----------------------------------------------------------------


# ScienceProgress Page ---------------------------------------------


class AchievementBlock(models.Model):
    block_title = models.CharField('Подзаголовок блока информации', max_length=100)
    block_text = models.TextField('Контент блока')
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Контент страницы достижений'
        verbose_name_plural = 'Контент страницы достижений'
# ----------------------------------------------------------------


# CoursesPage ---------------------------------------------

class CourseBlock(models.Model):
    block_title = models.CharField('Подзаголовок блока информации', max_length=100)
    block_text = models.TextField('Описание')
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Контент страницы курсов'
        verbose_name_plural = 'Контент страницы курсов'


class CourseVideo(models.Model):
    video_name = models.CharField('Наименование видео', max_length=100)
    link = models.CharField('Ссылка на видео', max_length=100)
    date = models.DateField('Дата', auto_now_add=True)
    CourseBlock = models.ForeignKey(CourseBlock, on_delete=models.CASCADE)

    def __str__(self):
        return self.video_name

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
# ----------------------------------------------------------------

