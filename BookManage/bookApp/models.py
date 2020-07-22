from django.db import models

# Create your models here.
class Book(models.Model):
    # 定义属性：默认主键自增id字段可不写
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    # 定义默认输出格式
    def __str__(self):
    return "%d" % self.title
    # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        db_table = "books"

class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    content = models.CharField(max_length=100)
    Book = models.ForeignKey('Book', on_delete=False)

    def __str__(self):
    return "%s" % self.name
    # 自定义对应的表名，默认表名：bookApp_hero
    class Meta:
        db_table = "heros"