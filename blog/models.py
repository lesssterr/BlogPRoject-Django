from django.db import models

class Post(models.Model):

    title = models.CharField('заголовок записи', max_length=100)
    description = models.TextField('текст записи')
    author = models.CharField('имя автора', max_length=100)
    date = models.DateField('дата публикации')
    img = models.ImageField('изображения', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

class Comments(models.Model):
    '''комментарий'''
    email = models.EmailField()
    name = models.CharField('имя', max_length=50)
    text_comments = models.TextField('текст комментарии', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Likes(models.Model):
    '''лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='публикации', on_delete=models.CASCADE)





