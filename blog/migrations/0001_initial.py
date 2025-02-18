# Generated by Django 3.0a1 on 2020-02-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('head1', models.CharField(default='', max_length=200)),
                ('content_head1', models.CharField(default='', max_length=5000)),
                ('head2', models.CharField(default='', max_length=200)),
                ('content_head2', models.CharField(default='', max_length=5000)),
                ('head3', models.CharField(default='', max_length=200)),
                ('content_head3', models.CharField(default='', max_length=5000)),
                ('head4', models.CharField(default='', max_length=200)),
                ('content_head4', models.CharField(default='', max_length=5000)),
                ('author_name', models.CharField(default='', max_length=80)),
                ('publishing_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=80)),
                ('phone', models.CharField(default='', max_length=13)),
                ('description', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
