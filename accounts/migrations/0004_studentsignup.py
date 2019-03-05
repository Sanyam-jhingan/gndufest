# Generated by Django 2.1.4 on 2019-01-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_student_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentsignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=60)),
                ('department_name', models.CharField(choices=[('Dept_1', 'BTECH-CSE'), ('Dept_2', 'BTECH-CIVIL'), ('Dept_3', 'BTECH-MECHANICAL')], default='Dept_1', max_length=70)),
                ('semester', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII')], default='I', max_length=10)),
                ('mobile_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
