# Generated by Django 2.0.3 on 2018-08-17 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MatchChecked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubgHackGoso.Item')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubgHackGoso.Player')),
            ],
        ),
        migrations.AddField(
            model_name='matchchecked',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubgHackGoso.Player'),
        ),
    ]
