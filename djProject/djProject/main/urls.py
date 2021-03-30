from django.urls import path
from . import views
from django.contrib.auth import views as av

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('register', views.register, name='register'),
    path('record', views.record, name='record'),
    path('login', av.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout', views.logout_f, name='logout'),
    path('create_record_nails', views.create_record_nails, name='create_record_nails'),
    path('<int:pk>/delete_nails', views.DeleteRecordNails.as_view(), name='delete_record_nails'),
    path('create_record_eyebrows', views.create_record_eyebrows, name='create_record_eyebrows'),
    path('<int:pk>/delete_eyebrows', views.DeleteRecordEyebrows.as_view(), name='delete_record_eyebrows'),
    path('create_record_eyelashes', views.create_record_eyelashes, name='create_record_eyelashes'),
    path('<int:pk>/delete_eyelashes', views.DeleteRecordEyelashes.as_view(), name='delete_record_eyelashes'),
    path('create_feedback', views.CreateFeedback, name='create_feedback'),
    path('feedbacks', views.Feedbacks, name='feedbacks'),
]
