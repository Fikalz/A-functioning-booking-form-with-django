from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name= 'index'),
    path('success/',views.booking_success,name='success'),
    path('showdb',views.showdb,name='showdb'),
    path('update/<int:id>',views.update,name='update'),
    path('delete_contact/<int:id>',views.delete_contact,name='delete_contact')
]
