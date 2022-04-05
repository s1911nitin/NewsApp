
from django.urls import path
from . import views

urlpatterns = [
    path('multipleposts/', views.MultiplePostFormView.as_view(), name='multipleposts'),
    path('update/<int:pk>/', views.UpdatePostFormView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeletePostFormView.as_view(), name='delete'),
    path('blogpost/', views.BlogPostView.as_view(), name='blogpost'),
]
