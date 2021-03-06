# Generated by Django 2.2 on 2020-01-23 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('choice_code', models.CharField(max_length=1, null=True)),
                ('belong_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='areas', to='direct.ChoiceInfo')),
            ],
            options={
                'db_table': 'choiceinfo',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=7, null=True)),
                ('name', models.CharField(max_length=15)),
                ('banguaci', models.CharField(blank=True, max_length=40, null=True)),
                ('zone', models.CharField(choices=[('01', '鼓楼'), ('02', '台江'), ('03', '仓山'), ('04', '马尾'), ('05', '晋安'), ('06', '长乐'), ('07', '闽侯'), ('08', '连江'), ('09', '罗源'), ('10', '闽清'), ('11', '永泰'), ('12', '平潭'), ('13', '福清'), ('14', '古田'), ('15', '屏南')], max_length=2)),
                ('location', models.CharField(max_length=30)),
                ('coordination', models.CharField(max_length=21)),
                ('note', models.CharField(blank=True, max_length=30, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('first_choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_type', to='direct.ChoiceInfo')),
                ('second_choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_type', to='direct.ChoiceInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound_id', models.CharField(blank=True, max_length=9)),
                ('sounder', models.CharField(max_length=10)),
                ('birthplace', models.CharField(max_length=10)),
                ('birth', models.CharField(max_length=4)),
                ('recorded_time', models.DateField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('sound_position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='direct.Position')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('photo_position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='direct.Position')),
            ],
        ),
    ]
