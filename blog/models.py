# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible

# Create your models here.
# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name = '标题')
    author = models.CharField(max_length=30)
    content = models.TextField(blank = True,null = True,verbose_name = '内容')
    views = models.IntegerField(default=0, verbose_name='点击次数')
    created = models.DateTimeField(verbose_name='创建时间')
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created']

    def __str__(self):
        return self.title
# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return str(self.id)