import os
import uuid

from django.db import models

from DjangoUeditor.models import UEditorField


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='标题')
    describe = models.CharField(max_length=200, verbose_name='描述', blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:  # 元信息  描述模型类的信息
        db_table = 't_tag'  # 类对应，数据库中表的名字
        verbose_name = '标签'  # 在后台中显示模型类的名称
        verbose_name_plural = verbose_name
        ordering = ['-add_time']  # 排序


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='标题')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_category'
        verbose_name = '小说分类'
        verbose_name_plural = verbose_name


def save_files_path(instance, filename):
    new_file_name = str(uuid.uuid4()).replace('-', '') + os.path.splitext(filename)[-1]
    return 'img/{}'.format(new_file_name)


class Novels(models.Model):
    n_title = models.CharField(max_length=50, unique=True, verbose_name='小说名字')
    author = models.CharField(max_length=20, verbose_name='作者')
    intro = models.CharField(max_length=255, verbose_name='小说简介')
    content = models.TextField(verbose_name='详细说明')
    icon = models.ImageField(upload_to=save_files_path, verbose_name='小说封面') # 相对MEDIA_ROOT
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类名')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __str__(self):
        return self.n_title

    class Meta:
        db_table = 't_novel'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['publish_time']


class RollSet(models.Model):
    free_levels = ((0, '免费'), (1, 'VIP'))
    name = models.CharField(max_length=50, unique=True, verbose_name='名称')
    free_level = models.IntegerField(verbose_name='免费等级', choices=free_levels, default=0)
    novel = models.ForeignKey(Novels, on_delete=models.CASCADE, verbose_name='所属文章')

    @property
    def free_level_name(self):
        return self.free_levels[self.free_level][1]

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_roll'
        verbose_name = '卷级'
        ordering = ['id']


class Chapter(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')
    content = UEditorField(verbose_name='内容',
                           imagePath='img/images/',
                           width=600, height=800,
                           toolbars='mini')
    publish_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)
    roll = models.ForeignKey(RollSet, on_delete=models.CASCADE, verbose_name='所属章节')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_chapter'
        verbose_name = '小说章节'
        ordering = ['publish_time']