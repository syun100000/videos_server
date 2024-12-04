from django.contrib import admin
from .models import Video, Tag, Actor

# Register your models here.
# ビデオ、タグ、出演者モデルを管理サイトに登録
admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(Actor)
