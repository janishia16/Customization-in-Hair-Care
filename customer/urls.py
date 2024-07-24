from django.contrib import admin
from django.urls import path,include
from.import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('welcme',views.welcme,name='welcme'),
    path('quiz',views.quiz,name='quiz'),
    path('payment',views.payment,name='payment'),
    path('oorder',views.oorder,name='oorder'),
    path('confirm',views.confirm,name='confirm'),
    
]
