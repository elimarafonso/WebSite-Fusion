# Generated by Django 4.1.3 on 2022-11-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_features_options_alter_features_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='linkedin',
            field=models.CharField(default='#', max_length=200, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='features',
            name='icon',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Pc/Celular'), ('lni-leaf', 'Folha'), ('lni-layers', 'Multicamada'), ('lni-database', 'Banco de dados')], max_length=18, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='instagram',
            field=models.CharField(default='#', max_length=200, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='twitter',
            field=models.CharField(default='#', max_length=200, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-cog', 'Engrenagem'), ('lni-layers', 'Design'), ('lni-users', 'Usuários'), ('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile')], max_length=12, verbose_name='Icone'),
        ),
    ]
