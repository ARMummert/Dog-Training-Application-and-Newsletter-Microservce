from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('new/confirm/confirm/', views.confirm),
    path('delete//delete/', views.delete),
    path("", views.home, name="home"),
    path("dogtraining/", views.dogtraining, name="dog training"),
    path("dogprofile/", views.newProfile, name="create dog profile"),
    path("dogprofile/madeProfile/", views.madeProfile, name="madeProfile"),
    path('dogprofile/upload/', views.image_upload_view)
]
