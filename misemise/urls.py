from django.urls import path
from . import views
import misemise.views

urlpatterns = [
    path('blog/<int:blog_id>/', misemise.views.detail, name='detail'),
    path('blog/new/', misemise.views.new, name='new'),
    path('blog/create/', misemise.views.create, name='create'),
]