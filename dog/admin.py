from django.contrib import admin
from .models import Subscriber
from .models import Newsletter
from .models import Profile
from .models import Image

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'nickname', 'breed', 'age', 'toy')
    fields = ['fullname', 'nickname', 'breed', 'age', 'toy']

admin.site.register(Profile)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    fields = ['title', 'image']
    
admin.site.register(Image)

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)
