# Generated by Django 4.0.4 on 2022-05-10 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_member_uid_member_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='For',
        ),
        migrations.AddField(
            model_name='payment',
            name='month',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(upload_to='member/'),
        ),
        migrations.AddField(
            model_name='member',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.plan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='type',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.CASCADE, to='main.plan'),
            preserve_default=False,
        ),
    ]
