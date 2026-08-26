from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "training"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),
    path("photos/", views.photos, name="photos"),
    path(
        'gallery/photo/<int:pk>/',
        views.photo_view,
        name='photo_view'
    ),
    
    path(
        'videos/',
        views.video_gallery,
        name='video_gallery'
    ),

    path(
        'video/<slug:slug>/',
        views.video_detail,
        name='video_detail'
    ),

    path(
        'video/<slug:slug>/download/',
        views.download_video,
        name='download_video'
    ),
    path("services/", views.services, name="services"),
       path(
        "",
        views.service_page,
        name="service"
    ),

    path(
        "enroll/<int:course_id>/",
        views.enroll,
        name="enroll"
    ),
    path("contact/", views.contact, name="contact"),
    path('admission/', views.admission, name='admission'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )