from django.urls import path
from .views import PostView, MessageView,Postdetail

urlpatterns = [
    
    #path('room', MachineView.as_view()),
    path('api/blog/', PostView.as_view(), name='posts'),
    path('api/blog/<int:pk>', Postdetail.as_view(), name='post-detail'),
    path('api/message/', MessageView.as_view()),
    path('', TemplateView.as_view(template_name='index.html')),
    #path('create-room', CreateMachineView.as_view()),
    
]  