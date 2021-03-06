# Generated by Django 4.0.4 on 2022-05-11 13:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('joining_date', models.DateField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(upload_to='member/')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'male'), ('Female', 'female'), ('Others', 'others')], max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('month', models.CharField(max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.member')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plan')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plan'),
        ),
        migrations.AddField(
            model_name='member',
            name='trainer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.trainer'),
        ),
    ]
