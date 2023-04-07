# Generated by Django 4.1.7 on 2023-04-07 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0028_alter_inventory_isbn_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='isAvailable',
            new_name='is_available',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='price',
        ),
        migrations.AddField(
            model_name='inventory',
            name='cost_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='inventory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='inventory',
            name='manufacturer',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='inventory',
            name='medicine_type',
            field=models.CharField(choices=[('tab', 'Tablet'), ('cap', 'Capsule'), ('syp', 'Syrup'), ('inj', 'Injection'), ('oth', 'Other')], default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='minimum_quantity',
            field=models.PositiveIntegerField(default=0, help_text='Minimum quantity before restocking is required'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='inventory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='manufacturing_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='use YYYY-MM-DD format'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='medicine_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='medicine_use',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
