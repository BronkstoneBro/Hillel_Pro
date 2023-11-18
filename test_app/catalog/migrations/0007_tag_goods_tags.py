# Generated by Django 4.2.7 on 2023-11-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_goods_options_goods_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Имя товару')),
                ('uniq', models.UUIDField(verbose_name='UUID')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='tags',
            field=models.ManyToManyField(related_name='goods_tag', to='catalog.tag'),
        ),
    ]
