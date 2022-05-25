from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
#from django_extensions.db.fields import AutoSlugField


class CatMenu(models.Model):
    class Meta():
        ordering = ['cat_menu_name']
        verbose_name = 'Основные блюды->Категория'
        verbose_name_plural = 'Основные блюды->Категории'


    cat_menu_name = models.CharField(max_length=40, blank=True, verbose_name='Имя категории')
    slug = models.SlugField(verbose_name='slug', null=True, db_index=True, unique=True, blank=True)
    cat_menu_name_image = models.ImageField(upload_to='image/menu/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото категории меню')


    def __str__(self):
        return self.cat_menu_name


class BaseMenu(models.Model):
    class Meta():
        ordering = ['title_menu']
        verbose_name = 'Основная блюда'
        verbose_name_plural = 'Основные блюды'


    category = models.ForeignKey(CatMenu, on_delete=models.CASCADE, verbose_name='Категория')
    title_menu = models.CharField(max_length=40, blank=True, verbose_name='Заголовок меню')
    slug = models.SlugField(verbose_name='slug', null=True, db_index=True, unique=True, blank=True)
    text_menu = models.TextField(blank=True, verbose_name='Текст меню')
    image_menu = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, verbose_name='фото')


    def __str__(self):
        return self.title_menu


class ContactForm(models.Model):
    class Meta():
        verbose_name = 'Сообщения от пользователя'
        verbose_name_plural = 'Сообщении от пользователей'


    full_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, verbose_name='Email')
    phone_number = models.IntegerField()
    message = models.TextField(blank=True, verbose_name='Сообщения')

    def __str__(self):
        return self.full_name

class Menu_Category(models.Model):
    class Meta():
        ordering = ['product_cat_name']
        verbose_name = 'Меню->Категория'
        verbose_name_plural = 'Меню->Категории'

    product_cat_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Названия категории продукта')
    slug = models.SlugField(unique=True, db_index=True, blank=True, verbose_name='slug')

    def get_absolute_url(self):
        return reverse('Nomad_Coffee_Naryn_app:menu_category',
                       args=[self.slug])
    def __str__(self):
        return self.product_cat_name

class Menu(models.Model):
    class Meta():
        ordering = ['title']
        index_together = (('id', 'slug'),)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


    category = models.ForeignKey(Menu_Category,on_delete=models.CASCADE, related_name='cat_name')
    product_image = models.ImageField(blank=True, upload_to='product_image/%Y/%m/%d/')
    title = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True, verbose_name='slug')
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Menu, self).save(*args, **kwargs)

        def get_absolute_url(self):
            return reverse('Nomad_Coffee_Naryn_app:menu_category',
                           args=[self.id, self.slug])

    def __str__(self):
        return self.title


class Profile(models.Model):
    class Meta():
        ordering = ['user']
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профиль пользователей'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Menu)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

# resizing images
def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)