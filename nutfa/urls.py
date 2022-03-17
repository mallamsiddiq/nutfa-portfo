from django.contrib import admin
from django.urls import include, path
from blog import views

from django.views.generic import TemplateView


handler404 = views.error_404


urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('frmk', TemplateView.as_view(template_name='index.html')),
    path('fr/about', TemplateView.as_view(template_name='index.html')),
    path('fr/blog', TemplateView.as_view(template_name='index.html')),
    path('fr/blog/<int:pk>', TemplateView.as_view(template_name='index.html')),
    path('fr/projects', TemplateView.as_view(template_name='index.html')),
    path('fr/skills', TemplateView.as_view(template_name='index.html')),
    path('fr/contact', TemplateView.as_view(template_name='index.html')),
]


