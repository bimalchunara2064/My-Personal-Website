from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    interested_service = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email_address} {self.phone_number} {self.interested_service} {self.message}"
    
    

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    issue_date = models.DateField(blank=True, null=True)

    description = models.TextField(blank=True)

    # Certificate preview image
    image = models.ImageField(
        upload_to='certificates/images/',
        blank=True,
        null=True
    )

    # Certificate PDF
    certificate_file = models.FileField(
        upload_to='certificates/files/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-issue_date', '-created_at']

    def __str__(self):
        return self.title
    
    

class GalleryPhoto(models.Model):
    CATEGORY_CHOICES = [
        ('personal', 'Personal'),
        ('school', 'School Event'),
        ('travel', 'Travel'),
        ('my family', 'MY Family'),
        ('sports', 'Sports Teams'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='personal'
    )
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    
    
    




class Video(models.Model):

    CATEGORY_CHOICES = [
        ('all', 'All Videos'),
        ('personal', 'Personal'),
        ('school', 'School Event'),
        ('rap', 'Rap Videos'),
        ('group', 'Group Dance Video'),
        
       
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=250,
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='personal'
    )

    description = models.TextField(
        blank=True
    )

  
    video_file = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )


    views = models.PositiveIntegerField(
        default=0
    )

    downloads = models.PositiveIntegerField(
        default=0
    )

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    


class TrainingService(models.Model):
    title = models.CharField(
        max_length=200,
        default="Computer & Technology Training Program"
    )

    description = models.TextField(
        default="Practical technology training designed for students, beginners and aspiring developers."
    )

    online_classes = models.BooleanField(default=True)
    offline_classes = models.BooleanField(default=True)

    languages = models.CharField(
        max_length=255,
        default="🇳🇵 नेपाली, 🇬🇧 English, 🇮🇳 हिन्दी"
    )

    # Payment QR
    esewa_qr = models.ImageField(
        upload_to="training/qr/",
        blank=True,
        null=True
    )

    khalti_qr = models.ImageField(
        upload_to="training/qr/",
        blank=True,
        null=True
    )

    bank_qr = models.ImageField(
        upload_to="training/qr/",
        blank=True,
        null=True
    )

    # Bank details
    bank_name = models.CharField(
        max_length=150,
        blank=True
    )

    account_name = models.CharField(
        max_length=150,
        blank=True
    )

    account_number = models.CharField(
        max_length=100,
        blank=True
    )

    branch = models.CharField(
        max_length=150,
        blank=True
    )

    def __str__(self):
        return self.title


class Course(models.Model):

    service = models.ForeignKey(
        TrainingService,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    icon = models.CharField(
        max_length=20,
        default="💻"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    duration = models.CharField(
        max_length=100
    )

    active = models.BooleanField(
        default=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title






class Enrollment(models.Model):

    PAYMENT_CHOICES = [
        ("esewa", "eSewa"),
        ("khalti", "Khalti"),
        ("bank", "Bank"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("verified", "Verified"),
        ("rejected", "Rejected"),
    ]

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES
    )

    transaction_id = models.CharField(
        max_length=150,
        blank=True
    )

    payment_screenshot = models.ImageField(
        upload_to="training/payments/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name




class Admission(models.Model):

    COURSE_CHOICES = [
        ("Basic Computer", "Basic Computer"),
        ("Web Design", "Web Design"),
        ("3D Print Design", "3D Print Design"),
        ("Full Stack Development", "Full Stack Development"),
        ("Graphic Design", "Graphic Design"),
        ("Python Programming", "Python Programming"),
        ("Digital Marketing", "Digital Marketing"),
    ]

    MODE_CHOICES = [
        ("Online", "Online"),
        ("Physical", "Physical"),
        ("Both", "Online + Physical"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    course = models.CharField(
        max_length=100,
        choices=COURSE_CHOICES
    )

    mode = models.CharField(
        max_length=30,
        choices=MODE_CHOICES
    )

    duration = models.CharField(max_length=100)

    preferred_session = models.CharField(max_length=100)

    preferred_time = models.TimeField(
        null=True,
        blank=True
    )

    education = models.CharField(
        max_length=150,
        blank=True
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )

    admission_date = models.DateField()

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.course}"