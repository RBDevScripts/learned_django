from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home-page"),
    path('about/',views.about,name="about-page"),
    path('contact/',views.contact,name="contact-page"),
    path('product/',views.product,name="product-page"),
    path('crud/',views.showUser,name="crud-page"),
    path('delete/<int:id>',views.delete,name="delete-page"),
    path('add/',views.add,name="add-page"),
    path('update/<int:id>',views.update,name="update-page"),
]
