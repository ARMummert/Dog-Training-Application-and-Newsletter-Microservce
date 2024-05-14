from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .forms import CreateForm
from .models import Profile
from .forms import ImageForm
  
def home(request):
    return render(request, "home.html")
  
def dogtraining(request):
    return render(request, "dogtraining.html")
  
def dogprofile(request):
    return render(request, "dogprofile.html")

def madeProfile(request):
    latest_profile = Profile.objects.latest('id')
    context = {'latest_profile': latest_profile}
    return render(request, 'madeProfile.html', context)

def newProfile(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            nickname = form.cleaned_data['nickname']
            gender = form.cleaned_data['gender']
            breed = form.cleaned_data['breed']
            age = form.cleaned_data['age']
            toy = form.cleaned_data['toy']
            image = form.cleaned_data['image']
            record = Profile(fullname=fullname, nickname=nickname, gender=gender, breed=breed, age=age, toy=toy, image=image)
            record.save()
            return redirect('madeProfile')
    else:
        form = CreateForm()
    return render(request, 'dogprofile.html', {'form': form})


# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
@csrf_exempt
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('confirm'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'new.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'new.html', {'form': SubscriberForm()})

def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'new.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'new.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'new.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'new.html', {'email': sub.email, 'action': 'denied'})

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'madeProfile.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

