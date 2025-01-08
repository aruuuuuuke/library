from django.db import models

class Books(models.Model):
    GENRE_CHOICES = (
        ('Классика','Классика'),
        ('Трилер', 'Трилер'),
        ('Романтика', 'Романтика')
    )
    image = models.ImageField(upload_to='books/', verbose_name ="Загрузите фото" )
    title = models.CharField(max_length=100, verbose_name ="Напишите название книги")
    decription = models.TextField(verbose_name ="Введите анотацию к книге")
    price = models.IntegerField(verbose_name ="Укажите цену книги", default=350)
    date = models.DateField(verbose_name ="Ведите дату выхода книги")
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name ="Укажите жанр книги")
    author_name = models.CharField(max_length=100, verbose_name ="Введите имя автора")
    author_email = models.EmailField(verbose_name ="Введите имэйл автора", blank=True)

    class Meta:
        verbose_name = 'книга',
        verbose_name_plural = 'список книг'
#
    def __str__(self):
        return self.title