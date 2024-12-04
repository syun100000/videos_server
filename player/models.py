from django.db import models

# Create your models here.

# ビデオ
class Video(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=1000)
    description = models.TextField()
    number = models.IntegerField(null=True)
    path = models.CharField(max_length=1000)

# タグ
class Tag(models.Model):
    name = models.CharField(max_length=1000, primary_key=True, unique=True)
    description = models.TextField(null=True)

# 出演者
class Actor(models.Model):
    name = models.CharField(max_length=1000, primary_key=True, unique=True)
    description = models.TextField(null=True)
    birth = models.DateField(null=True)
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()   # 名前を小文字に変換
        # 空白を削除
        self.name = self.name.replace(" ", "")
        # 全角スペースを削除
        self.name = self.name.replace("　", "")
        super(Actor, self).save(*args, **kwargs)