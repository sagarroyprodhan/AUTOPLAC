"""cs243 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cs243.view import login,index2,studentprofile,photo,postgrad,undergrad,srsec,sec,languages,projects
from credentials.views import internships,contact,language

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^login/$', login),
      url(r'^index2/$', index2),
       url(r'^studentprofile/$', studentprofile),
        url(r'^photo/$', photo),
          url(r'^postgrad/$', postgrad),
          url(r'^undergrad/$', undergrad),
          url(r'^srsec/$', srsec),
          url(r'^sec/$', sec),
          url(r'^internships/$', internships),
          url(r'^languages/$', languages),
          url(r'^contact/$', contact),
          url(r'^projects/$', projects),
          url(r'^language/(?P<language>[a-z\-]+)/$', language),
          url(r'^auth/$', 'cs243.view.auth_view'),
          url(r'^invalid/$', 'cs243.view.invalid_login'),
          url(r'^loggedin/$', 'cs243.view.loggedin'),
          url(r'^register/$', 'cs243.view.register_user'),
          url(r'^register_success/$', 'cs243.view.register_success'),
          
          
]
