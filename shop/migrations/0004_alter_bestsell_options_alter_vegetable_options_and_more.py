from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_fruit_options_fruit_shop_fruit_id_9f79df_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bestsell',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='vegetable',
            options={'ordering': ('id',)},
        ),
        migrations.AddIndex(
            model_name='bestsell',
            index=models.Index(fields=['id'], name='shop_bestse_id_19a752_idx'),
        ),
        migrations.AddIndex(
            model_name='vegetable',
            index=models.Index(fields=['id'], name='shop_vegeta_id_0d26b7_idx'),
        ),
    ]
