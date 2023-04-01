from django.views.generic import TemplateView
from django.urls import path

# URL configuration for the playground app
urlpatterns = [
    path('', view=TemplateView.as_view(template_name='core/index.html'), name='index'),
]