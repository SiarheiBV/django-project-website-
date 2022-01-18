# Generated by Django 4.0.1 on 2022-01-18 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0003_alter_post_image_delete_commentbest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Аватар')),
                ('email_two', models.EmailField(max_length=254, verbose_name='Доп. email')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('slug', models.SlugField(default='', verbose_name='URL')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиля',
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.DeleteModel(
            name='CommentBest',
        ),
    ]