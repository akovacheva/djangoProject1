"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from learnApp.views import home,index,course_details, courses, events, login_user, register,logout_user,comments,course_details3,course_details2,results #prebaruvanje_postovi
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home, name='quiz.html'),
    path('index/', index, name='index.html'),
    path('course-details/', course_details, name='course-details.html'),
    path('course-details2/', course_details2, name='course-details2.html'),
    path('course-details3/', course_details3, name='course-details3.html'),
    path('courses/', courses, name='courses.html'),
    path('events/', events, name='events.html'),
    path('login_user/', login_user, name='login.html'),
    path('register/', include('django.contrib.auth.urls')),
    path('register/', register, name='register.html'),
    path('logout_user',logout_user,name='logout'),
    path('comments/',comments,name='comments'),
    path('results/',results, name='results'),
    #path('prebaruvanje_postovi',prebaruvanje_postovi, name='prebaruvanje_postovi')


]
