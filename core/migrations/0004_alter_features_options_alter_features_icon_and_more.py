# Generated by Django 4.1.3 on 2022-11-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_features_rename_servico_servico_nome_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='features',
            options={'verbose_name': 'Recurso', 'verbose_name_plural': 'Recursos'},
        ),
        migrations.AlterField(
            model_name='features',
            name='icon',
            field=models.CharField(choices=[('lni-leaf', 'Folha'), ('lni-rocket', 'Foguete'), ('lni-cog', 'Engrenagem'), ('lni-layers', 'Multicamada'), ('lni-database', 'Banco de dados'), ('lni-laptop-phone', 'Pc/Celular')], max_length=18, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-layers', 'Design'), ('lni-users', 'Usuários'), ('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico')], max_length=12, verbose_name='Icone'),
        ),
    ]
