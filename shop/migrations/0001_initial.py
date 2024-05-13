from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.FloatField(default=0)),
                ('image', models.ImageField(upload_to='shop/bestselling/')),
                ('price', models.FloatField()),
                ('price_type', models.CharField(choices=[('USD',), ('RUB',)], default='USD', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='shop/fruits/')),
                ('information', models.TextField()),
                ('price', models.FloatField()),
                ('price_type', models.CharField(choices=[('USD',), ('RUB', )], default='USD', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='shop/vegetables/')),
                ('information', models.TextField()),
                ('price', models.FloatField()),
                ('price_type', models.CharField(choices=[('USD',), ('RUB',)], default='USD', max_length=20)),
            ],
        ),
    ]
