from django.db import models

# Create your models here.
class Book(models.Model):
    # 定义属性：默认主键自增id字段可不写
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    # 定义默认输出格式
    def __repr__(self):
        return "BOOK: %s" % self.title
    def __str__(self):
        return self.title

    # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        db_table = "books"
        verbose_name = "labrary management"
        verbose_name_plural = "labrary managements"

class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    Book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __repr__(self):
        return "<Hero %s>" % self.name
    def __str__(self):
        return self.name
    # 自定义对应的表名，默认表名：bookApp_hero
    class Meta:
        db_table = "heros"
        verbose_name = "hero management"
        verbose_name_plural = "hero managements"