# Generated by Django 4.1.3 on 2022-12-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_avaliacao_estrelas_alter_features_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='estrelas',
            field=models.IntegerField(choices=[(4, '★★★★'), (2, '★★'), (1, '★'), (5, '★★★★★'), (3, '★★★')], max_length=5, verbose_name='Estrelas'),
        ),
        migrations.AlterField(
            model_name='features',
            name='icon',
            field=models.CharField(choices=[('lni-laptop-phone', 'Pc/Celular'), ('lni-rocket', 'Foguete'), ('lni-layers', 'Multicamada'), ('lni-leaf', 'Folha'), ('lni-cog', 'Engrenagem'), ('lni-database', 'Banco de dados')], max_length=18, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Design'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-rocket', 'Foguete'), ('lni-cog', 'Engrenagem'), ('lni-mobile', 'Mobile')], max_length=12, verbose_name='Icone'),
        ),
    ]