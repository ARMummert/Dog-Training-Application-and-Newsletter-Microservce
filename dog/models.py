from django.db import models
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150, default=None)
    contents = models.FileField(upload_to='uploaded_newsletters/', default=None)

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for sub in subscribers:
            message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject=self.subject,
                    html_content=contents + (
                        '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/delete/'),
                            sub.email,
                            sub.conf_num))
            sg.send(message)

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15, blank=True, null=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


class Profile(models.Model):

    fullname = models.CharField(max_length=100, null=True, blank=True, default=None)
    nickname = models.CharField(max_length=100, null=True, blank=True, default=None)
    gender = models.CharField(max_length=100, null=True, blank=True, default=None)
    breed = models.CharField(max_length=100, null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=None)
    toy = models.CharField(max_length=100, null=True, blank=True, default=None)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    class Meta:
        ordering = ['fullname', 'nickname', 'gender', 'breed', 'age', 'toy', 'image']

    def __str__(self):
        return f"{self.fullname},{self.nickname}, {self.gender},{self.breed}, {self.age},{self.toy}, {self.image}"
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

