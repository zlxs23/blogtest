# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField(null=True, verbose_name='内容', blank=True)),
                ('views', models.IntegerField(default=0, verbose_name='点击次数')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ['-created'],
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField(verbose_name='评论内容')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('article', models.ForeignKey(null=True, verbose_name='文章', to='blog.Article', blank=True)),
                ('pid', models.ForeignKey(null=True, verbose_name='父级评论', to='blog.Comment', blank=True)),
            ],
            options={
                'verbose_name_plural': '评论',
                'ordering': ['-date_publish'],
                'verbose_name': '评论',
            },
        ),
    ]
