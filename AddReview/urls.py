#from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
   path('review/', views.show_review),
   path('', views.welcome),
   path('add-review/<int:ide>/', views.add_review),
   path('add-review/<int:ide>/verification/', views.verification),
   path('add-review/<int:ide>/error/', views.error),
]