# Generated by Django 4.0.2 on 2022-04-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, default='C://Users/Nitin Manali/Python3.10/DjangoApp/NewsApp/blog/static/blog/images/CSK.png', null=True, upload_to='postimages'),
        ),
    ]
