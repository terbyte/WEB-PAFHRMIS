# Generated by Django 5.0.6 on 2024-06-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonnelItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RANK', models.CharField(max_length=200)),
                ('LAST_NAME', models.CharField(max_length=200)),
                ('FIRST_NAME', models.CharField(max_length=200)),
                ('MIDDLE_NAME', models.CharField(blank=True, max_length=200, null=True)),
                ('EXTENSION_NAME', models.CharField(blank=True, max_length=200, null=True)),
                ('SERIAL_NUMBER', models.CharField(max_length=200)),
                ('BOS', models.CharField(max_length=200)),
                ('SEX', models.CharField(max_length=10)),
                ('BIRTHDAY', models.DateField(blank=True, null=True)),
                ('CONTACT_NUMBER', models.CharField(blank=True, max_length=200, null=True)),
                ('ADDRESS', models.CharField(blank=True, max_length=200, null=True)),
                ('CLASSIFICATION', models.CharField(max_length=200)),
                ('CATEGORY', models.CharField(max_length=200)),
                ('SOURCE_OF_ENLISTMENT_COMMISION', models.CharField(max_length=200)),
                ('PILOT_RATED_NON_RATED', models.CharField(blank=True, max_length=200, null=True)),
                ('AFSC', models.CharField(blank=True, max_length=200, null=True)),
                ('HIGHEST_PME_COURSES', models.CharField(blank=True, max_length=200, null=True)),
                ('EFFECTIVE_DATE_APPOINTMENT', models.DateField()),
                ('EFFECTIVE_DATE_ENTERED', models.DateField()),
                ('DATE_LAST_PROMOTION_APPOINTMENT', models.DateField(blank=True, null=True)),
                ('UNIT', models.CharField(blank=True, max_length=200, null=True)),
                ('SUB_UNIT', models.CharField(blank=True, max_length=200, null=True)),
                ('DATE_FIRST_TRANCHE_REENLISTMENT', models.DateField(blank=True, null=True)),
                ('DATE_SECOND_TRANCHE_REENLISTMENT', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AFPSN', models.CharField(max_length=200)),
                ('LAST_NAME', models.CharField(max_length=200)),
                ('FIRST_NAME', models.CharField(max_length=200)),
                ('MIDDLE_NAME', models.CharField(max_length=200)),
                ('SUFFIX', models.CharField(max_length=200)),
                ('NEW_UNIT', models.CharField(max_length=200)),
                ('REASSIGN_EFFECTIVEDDATE', models.DateField()),
                ('ASSIGN_CATEGORY', models.CharField(max_length=200)),
                ('REASSIGN_EFFECTIVEDDATE_UNTIL', models.DateField(blank=True, null=True)),
                ('ORDER_UPLOADFILE', models.FileField(upload_to='uploads/orders/')),
            ],
            options={
                'db_table': 'placementinfo',
            },
        ),
    ]
