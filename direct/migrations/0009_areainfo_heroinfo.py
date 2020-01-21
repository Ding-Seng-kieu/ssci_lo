# Generated by Django 2.2 on 2020-01-21 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0008_auto_20200120_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='areas', to='direct.AreaInfo')),
            ],
            options={
                'verbose_name': '地区信息',
                'verbose_name_plural': '地区信息',
                'db_table': 'areainfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='areainfo', to='direct.AreaInfo')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='areainfos', to='direct.AreaInfo')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='direct.AreaInfo')),
            ],
            options={
                'verbose_name': '人物信息',
                'verbose_name_plural': '人物信息',
                'db_table': 'heroinfo',
            },
        ),
    ]
