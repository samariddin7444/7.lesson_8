from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_bestsell_likes_fruit_likes_vegetable_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fruit',
            options={'ordering': ('id',)},
        ),
        migrations.AddIndex(
            model_name='fruit',
            index=models.Index(fields=['id'], name='shop_fruit_id_9f79df_idx'),
        ),
    ]
