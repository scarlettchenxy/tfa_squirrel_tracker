
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrelinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField(blank=True, null=True)),
                ('y', models.FloatField(blank=True, null=True)),
                ('uniquesquirrelid', models.CharField(blank=True, max_length=200, null=True)),
                ('hectare', models.CharField(blank=True, max_length=200, null=True)),
                ('shift', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=200, null=True)),
                ('hectaresquirrelnumber', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.CharField(blank=True, max_length=200, null=True)),
                ('primaryfurcolor', models.CharField(blank=True, max_length=200, null=True)),
                ('highlightfurcolor', models.CharField(blank=True, max_length=200, null=True)),
                ('combinationofprimaryandhighlightcolor', models.CharField(blank=True, max_length=200, null=True)),
                ('colornotes', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('abovegroundsightermeasurement', models.CharField(blank=True, max_length=200, null=True)),
                ('specificlocation', models.CharField(blank=True, max_length=200, null=True)),
                ('running', models.CharField(blank=True, max_length=200, null=True)),
                ('chasing', models.CharField(blank=True, max_length=200, null=True)),
                ('climbing', models.CharField(blank=True, max_length=200, null=True)),
                ('eating', models.CharField(blank=True, max_length=200, null=True)),
                ('foraging', models.CharField(blank=True, max_length=200, null=True)),
                ('otheractivities', models.CharField(blank=True, max_length=200, null=True)),
                ('kuks', models.CharField(blank=True, max_length=200, null=True)),
                ('quaas', models.CharField(blank=True, max_length=200, null=True)),
                ('moans', models.CharField(blank=True, max_length=200, null=True)),
                ('tailflags', models.CharField(blank=True, max_length=200, null=True)),
                ('tailtwitches', models.CharField(blank=True, max_length=200, null=True)),
                ('approaches', models.CharField(blank=True, max_length=200, null=True)),
                ('indifferent', models.CharField(blank=True, max_length=200, null=True)),
                ('runsfrom', models.CharField(blank=True, max_length=200, null=True)),
                ('otherinteractions', models.CharField(blank=True, max_length=200, null=True)),
                ('latlong', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
