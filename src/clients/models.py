from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Client(models.Model):
    """Client model"""

    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

    STATE_CHOICES = [
        ('AL','AL'), ('AK','AK'), ('AZ','AZ'), ('AR','AR'), ('CA','CA'), ('CO','CO'),
        ('CT','CT'), ('DC','DC'), ('DE','DE'), ('FL','FL'), ('GA','GA'),
        ('HI','HI'), ('ID','ID'), ('IL','IL'), ('IN','IN'), ('IA','IA'),
        ('KS','KS'), ('KY','KY'), ('LA','LA'), ('ME','ME'), ('MD','MD'),
        ('MA','MA'), ('MI','MI'), ('MN','MN'), ('MS','MS'), ('MO','MO'),
        ('MT','MT'), ('NE','NE'), ('NV','NV'), ('NH','NH'), ('NJ','NJ'),
        ('NM','NM'), ('NY','NY'), ('NC','NC'), ('ND','ND'), ('OH','OH'),
        ('OK','OK'), ('OR','OR'), ('PA','PA'), ('RI','RI'), ('SC','SC'),
        ('SD','SD'), ('TN','TN'), ('TX','TX'), ('UT','UT'), ('VT','VT'),
        ('VA','VA'), ('WA','WA'), ('WV','WV'), ('WI','WI'), ('WY','WY')
    ]
    STATUS_CHOICES = [
        (0, 'New'),
        (1, 'Assigned'),
        (2, 'Contacted'),
        (3, 'Demo Scheduled'),
        (4, 'Demo Complete'),
        (5, 'Application Sent'),
        (6, 'Application Signed'),
        (7, 'Probation'),
        (8, 'Client')
    ]
    SOURCE_CHOICES = [
        (0, 'Website'),
        (1, 'Phone'),
        (2, 'Referral'),
        (3, 'Social Media'),
        (4, 'Email')
    ]
    LANGUAGE_CHOICES = [
        (0, "English"),
        (1, "Spanish"),
        (2, "Other")
    ]
    SUFFIX_CHOICES = [
        (0, ""),
        (1, "Jr."),
        (2, "Sr."),
        (3, "II"),
        (4, "III"),
        (5, "IV"),
        (6, "V"),
        (7, "VI"),
        (8, "VII")
    ]
    SALUTATION_CHOICES = [
        (0, ""),
        (1, "Mr."),
        (2, "Ms."),
        (3, "Mrs."),
        (4, "Dr."),
        (5, "Prof."),
        (6, "Rev.")
    ]

    # Contact fields
    business_name = models.CharField(max_length=32, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    contact_email = models.EmailField(max_length=255, blank=True)
    second_email = models.EmailField(max_length=255, blank=True)
    contact_phone = models.CharField(max_length=32, blank=True)
    contact_ext = models.CharField(max_length=32, blank=True)
    second_phone = models.CharField(max_length=32, blank=True)
    contact_fax = models.CharField(max_length=32, blank=True)
    contact_address = models.CharField(max_length=32, blank=True)
    contact_city = models.CharField(max_length=32, blank=True, null=True)
    contact_zip = models.IntegerField(blank=True, null=True)
    contact_state = models.CharField(max_length=2, blank=True, choices=STATE_CHOICES)
    monthly_volume = models.IntegerField(blank=True, null=True)
    # contact_pref = either a bool or choices or int? decide how to refer later
    pref_language = models.IntegerField(default=0, blank=True, choices=LANGUAGE_CHOICES)
    contact_suffix = models.IntegerField(default=0, blank=True, choices=SUFFIX_CHOICES)
    contact_salutation = models.IntegerField(default=0, blank=True, choices=SALUTATION_CHOICES)

    # Sales Methods
    delivery_sales = models.BooleanField(default=False)
    curbside_sales = models.BooleanField(default=False)
    in_store_sales = models.BooleanField(default=False)
    internet_sales = models.BooleanField(default=False)

    # Internal fields
    lead_source = models.IntegerField(default=None, blank=True, null=True, choices=SOURCE_CHOICES)
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='submitted_by')
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_by')
    assigned_rep = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_rep')
    # signed_off_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, help_text='New is default')
    lead_notes = models.TextField(max_length=20000, blank=True)
    schedule_sent = models.BooleanField(default=False, help_text='Has a scheduling email been sent to client?')
    archived = models.BooleanField(default=False)

    # Time fields
    date_requested = models.DateField(auto_now_add=True)
    date_assigned = models.DateField(blank=True, null=True)
    date_contacted = models.DateField(blank=True, null=True)
    date_demo = models.DateTimeField(blank=True, null=True)
    date_demo_done = models.DateField(blank=True, null=True)
    date_app_sent = models.DateField(blank=True, null=True)
    date_app_accept = models.DateField(blank=True, null=True)
    date_probation = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
