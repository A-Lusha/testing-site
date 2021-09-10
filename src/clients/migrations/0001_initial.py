# Generated by Django 3.2.7 on 2021-09-10 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=32)),
                ('first_name', models.CharField(blank=True, max_length=32)),
                ('last_name', models.CharField(blank=True, max_length=32)),
                ('contact_email', models.EmailField(blank=True, max_length=255)),
                ('second_email', models.EmailField(blank=True, max_length=255)),
                ('contact_phone', models.CharField(blank=True, max_length=32)),
                ('contact_ext', models.CharField(blank=True, max_length=32)),
                ('second_phone', models.CharField(blank=True, max_length=32)),
                ('contact_fax', models.CharField(blank=True, max_length=32)),
                ('contact_address', models.CharField(blank=True, max_length=32)),
                ('contact_city', models.CharField(blank=True, max_length=32, null=True)),
                ('contact_zip', models.IntegerField(blank=True, null=True)),
                ('contact_state', models.CharField(blank=True, choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')], max_length=2)),
                ('monthly_volume', models.IntegerField(blank=True, null=True)),
                ('pref_language', models.IntegerField(blank=True, choices=[(0, 'English'), (1, 'Spanish'), (2, 'Other')], default=0)),
                ('contact_suffix', models.IntegerField(blank=True, choices=[(0, ''), (1, 'Jr.'), (2, 'Sr.'), (3, 'II'), (4, 'III'), (5, 'IV'), (6, 'V'), (7, 'VI'), (8, 'VII')], default=0)),
                ('contact_salutation', models.IntegerField(blank=True, choices=[(0, ''), (1, 'Mr.'), (2, 'Ms.'), (3, 'Mrs.'), (4, 'Dr.'), (5, 'Prof.'), (6, 'Rev.')], default=0)),
                ('delivery_sales', models.BooleanField(default=False)),
                ('curbside_sales', models.BooleanField(default=False)),
                ('in_store_sales', models.BooleanField(default=False)),
                ('internet_sales', models.BooleanField(default=False)),
                ('lead_source', models.IntegerField(blank=True, choices=[(0, 'Website'), (1, 'Phone'), (2, 'Referral'), (3, 'Social Media'), (4, 'Email')], default=None, null=True)),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Assigned'), (2, 'Contacted'), (3, 'Demo Scheduled'), (4, 'Demo Complete'), (5, 'Application Sent'), (6, 'Application Signed'), (7, 'Probation'), (8, 'Client')], default=0, help_text='New is default')),
                ('lead_notes', models.TextField(blank=True, max_length=20000)),
                ('schedule_sent', models.BooleanField(default=False, help_text='Has a scheduling email been sent to client?')),
                ('archived', models.BooleanField(default=False)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('date_assigned', models.DateField(blank=True, null=True)),
                ('date_contacted', models.DateField(blank=True, null=True)),
                ('date_demo', models.DateTimeField(blank=True, null=True)),
                ('date_demo_done', models.DateField(blank=True, null=True)),
                ('date_app_sent', models.DateField(blank=True, null=True)),
                ('date_app_accept', models.DateField(blank=True, null=True)),
                ('date_probation', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('assigned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_by', to=settings.AUTH_USER_MODEL)),
                ('assigned_rep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_rep', to=settings.AUTH_USER_MODEL)),
                ('submitted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submitted_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
