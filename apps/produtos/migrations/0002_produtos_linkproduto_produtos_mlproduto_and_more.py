# Generated by Django 4.0.2 on 2022-02-28 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='linkproduto',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='produtos',
            name='mlproduto',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='produtos',
            name='saborproduto',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]