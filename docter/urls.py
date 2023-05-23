"""hosp_mng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
app_name='docter'

from django.contrib import admin
from django.urls import path,include
from docter import views

urlpatterns = [

 path('doc_dashboard',views.doc_dashboard,name='doc_dashboard'),
 path('doc_appointment',views.doc_appointment,name='doc_appointment'),
 path('today_appointment',views.today_appointment,name='today_appointment'),
 path('update_is_available',views.update_is_available,name='update_is_available'),
 path('docno',views.doc_Product,name='docno'),
 path('doc_Profile',views.doc_profile,name='doc_Profile'),
 path('doc_edit_profile',views.doc_edit_profile,name='doc_edit_profile'),
 path('accept/<int:id>',views.accept,name='accept'),
 path('reject/<int:id>',views.reject,name='reject'),
 path('finish/<int:id>',views.finish,name='finish'),
 path('priscribe/<int:id>',views.prescribe,name='prescribe'),
 path('myPatient',views.myPatient,name='myPatient'),
 path('today_Patient',views.today_Patient,name='today_Patient'),
 path('doc_chat',views.doc_chat,name='doc_chat'),
 path('msgg/<int:id>',views.msgg,name='msgg'),
 path('decr/<int:id>',views.decr,name='decr'),
 path('incr/<int:id>',views.incr,name='incr'),
 path('pre2/<int:id>',views.pre2,name='pre2'),
 path('changeTime',views.changeTime,name='changeTime'),
 







 
]
