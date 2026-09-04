from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import F
from django.http import FileResponse, Http404
from django.contrib import messages
from .models import Certificate, Contact, GalleryPhoto
from .models import GalleryPhoto
from .models import Video
from .models import TrainingService, Course
from .forms import AdmissionForm, EnrollmentForm
from .models import Admission




# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    certificates = Certificate.objects.all()

    context = {
        'certificates': certificates,
    }


    return render(request, 'about.html',context)

def gallery(request):
    photos = GalleryPhoto.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'gallery.html', context)


def photo_view(request, pk):
    photo = get_object_or_404(GalleryPhoto, pk=pk)

    photo.views += 1
    photo.save(update_fields=['views'])

    return render(
        request,
        'hero/photo_detail.html',
        {
            'photo': photo
        }
    )
    
    
    
def video_gallery(request):

    category = request.GET.get('category', 'all')

    videos = Video.objects.filter(
        is_active=True
    ).order_by('-created_at')

    if category != 'all':
        videos = videos.filter(category=category)

    categories = [
        ('all', 'All Videos'),
        ('personal', 'Personal'),
        ('school', 'School Event'),
        ('rap', 'Rap Videos'),
        
    ]

    context = {
        'videos': videos,
        'categories': categories,
        'active_category': category,
    }

    return render(
        request,
        'videos.html',
        context
    )


def video_detail(request, slug):

    video = get_object_or_404(
        Video,
        slug=slug,
        is_active=True
    )

    # Increase view count
    Video.objects.filter(
        id=video.id
    ).update(
        views=F('views') + 1
    )

    video.refresh_from_db()

    related_videos = Video.objects.filter(
        is_active=True,
        category=video.category
    ).exclude(
        id=video.id
    ).order_by('-created_at')[:6]

    context = {
        'video': video,
        'related_videos': related_videos,
    }

    return render(
        request,
        'hero/video_detail.html',
        context
    )


def download_video(request, slug):

    video = get_object_or_404(
        Video,
        slug=slug,
        is_active=True
    )

    if not video.video_file:
        raise Http404("Video file not available.")

    Video.objects.filter(
        id=video.id
    ).update(
        downloads=F('downloads') + 1
    )

    response = FileResponse(
        video.video_file.open('rb'),
        as_attachment=True,
        filename=video.video_file.name.split('/')[-1]
    )

    return response


def services(request):
    service = TrainingService.objects.first()
    courses = service.courses.filter(active=True) if service else Course.objects.none()

    return render(
        request,
        'services.html',
        {
            'service': service,
            'courses': courses,
        }
    )

def contact(request):
      if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

       
        try:
            # Save to Database
            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email_address=email,
                phone_number=phone,
                interested_service=service,
                message=message
            )
            
            messages.success(request, "Thank you! Your message has been received. I'll contact you soon.")
            return redirect('contact')
            
        except Exception as e:
            messages.error(request, "Something went wrong. Please try again.")
            return render(request, 'contact.html')
      
      return render(request, 'contact.html')

def photos(request):
    photos = GalleryPhoto.objects.all()
    return render(request, 'photos.html', {'photos': photos})






def service_page(request):
    service = TrainingService.objects.first()
    courses = service.courses.filter(active=True) if service else Course.objects.none()

    return render(
        request,
        "training/service.html",
        {
            "service": service,
            "courses": courses,
        }
    )


def enroll(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id,
        active=True
    )

    if request.method == "POST":

        form = EnrollmentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            enrollment = form.save(
                commit=False
            )

            enrollment.course = course

            enrollment.save()

            messages.success(
                request,
                "Your enrollment has been submitted successfully."
            )

            return redirect(
                "training:service"
            )

    else:

        form = EnrollmentForm()

    return render(
        request,
        "training/enroll.html",
        {
            "course": course,
            "service": course.service,
            "form": form,
        }
    )
    
    
    
def admission(request):
    form = AdmissionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Your admission form has been submitted successfully!"
        )
        return redirect("training:admission")

    return render(request, "contact.html", {"form": form})