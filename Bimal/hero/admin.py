from django.contrib import admin
from django.utils.html import format_html
from .models import Contact
from .models import Certificate
from .models import GalleryPhoto
from .models import Video
from .models import Admission
# Register your models here.

admin.site.register(Contact)
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'issuer',
        'issue_date',
        'created_at',
    )

    search_fields = (
        'title',
        'issuer',
    )

    list_filter = (
        'issuer',
        'issue_date',
    )





class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'views',
        'created_at'
    )

    list_filter = (
        'category',
        'created_at'
    )

    search_fields = (
        'title',
        'description'
    )

    readonly_fields = (
        'views',
        'created_at'
    )
    
admin.site.register(GalleryPhoto, GalleryPhotoAdmin)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    # Admin list page
    list_display = (
        'thumbnail_preview',
        'title',
        'category',
        'views',
        'downloads',
        'featured',
        'is_active',
        'created_at',
    )

    # Right side filters
    list_filter = (
        'category',
        'featured',
        'is_active',
        'created_at',
    )

    # Search box
    search_fields = (
        'title',
        'description',
    )

    # Automatically create slug from title
    prepopulated_fields = {
        'slug': ('title',)
    }

    # Edit these directly from list page
    list_editable = (
        'featured',
        'is_active',
    )

    # Don't manually change these
    readonly_fields = (
        'views',
        'downloads',
        'created_at',
        'updated_at',
        'thumbnail_preview',
    )

    # Organize Add/Edit form
    fieldsets = (

        (
            '🎬 Video Information',
            {
                'fields': (
                    'title',
                    'slug',
                    'category',
                    'description',
                )
            }
        ),

        (
            '🖼️ Media',
            {
                'fields': (
                    'thumbnail',
                    'thumbnail_preview',
                    'video_file',
                    'youtube_url',
                )
            }
        ),

        (
            '📊 Statistics',
            {
                'fields': (
                    'views',
                    'downloads',
                )
            }
        ),

        (
            '⚙️ Settings',
            {
                'fields': (
                    'featured',
                    'is_active',
                )
            }
        ),

        (
            '📅 Dates',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )

    # Thumbnail preview
    def thumbnail_preview(self, obj):

        if obj.thumbnail:

            return format_html(
                '<img src="{}" width="120" height="70" '
                'style="object-fit:cover;border-radius:8px;" />',
                obj.thumbnail.url
            )

        return "No Thumbnail"

    thumbnail_preview.short_description = "Preview"




from .models import (
    TrainingService,
    Course,
    Enrollment
)


@admin.register(TrainingService)
class TrainingServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "online_classes",
        "offline_classes",
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "duration",
        "active",
        "order",
    )

    list_filter = (
        "active",
    )

    list_editable = (
        "active",
        "order",
    )


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "course",
        "payment_method",
        "transaction_id",
        "status",
        "created_at",
    )

    list_filter = (
        "payment_method",
        "status",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "transaction_id",
    )

    list_editable = (
        "status",
    )
    
    
    
    




@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'course',
        'mode',
        'admission_date',
        'created_at',
    )

    list_filter = (
        'course',
        'mode',
        'gender',
        'admission_date',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'course',
    )