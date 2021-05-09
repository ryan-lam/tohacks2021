# Generated by Django 3.2 on 2021-05-09 01:20

from django.db import migrations, models
import django.db.models.deletion
import names
from random import randint, choice


def initialize(apps, schema_editor):
    Client = apps.get_model('main', 'Client')
    Rep = apps.get_model('main', 'Rep')

    c = Client(username=f"client1", name="John Doe", age=randint(20, 35), address="123 Toronto Avenue", gender="M", income=50000)
    c.save()
    c = Client(username=f"client2", name="Jane Doe", age=randint(20, 35), address="321 Spadina Avenue", gender="F", income=100000)
    c.save()

    r = Rep(username=f"rep1", name="James Donne", age=randint(20, 35), address="999 MLH Road", gender="M", expertise="AUTO", description="None", hours="9am-5pm")
    r.save()
    r = Rep(username=f"rep2", name="Jill Dunkin", age=randint(20, 35), address="29 Hacker Street", gender="F", expertise="HOME", description="None", hours="10am-8pm")
    r.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('Other', 'Other')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.profile')),
                ('income', models.IntegerField()),
            ],
            bases=('main.profile',),
        ),
        migrations.CreateModel(
            name='Rep',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.profile')),
                ('expertise', models.CharField(choices=[('AUTO', 'AUTO'), ('HOME', 'HOME')], max_length=256)),
                ('description', models.CharField(max_length=500)),
                ('hours', models.CharField(max_length=256)),
            ],
            bases=('main.profile',),
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=64)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='main.client')),
                ('rep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rep', to='main.rep')),
            ],
        ),
        migrations.RunPython(initialize),
    ]