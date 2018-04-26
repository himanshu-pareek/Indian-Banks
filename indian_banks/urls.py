"""indian_banks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, re_path
from BankInfo import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^branches/$', views.BranchList.as_view ()),
    url(r'^data/add_banks/$', views.add_banks_from_file),
    url(r'^data/add_branches/$', views.add_branches_from_file),
    # re_path (r'^branch/(?P<ifsc_code>\w+)/$', views.getBranch.as_view ()),
    # re_path (r'^branches/(?P<bank_name>\w+)/(?P<city_name>\w+)/$', views.BranchList.as_view ()),
    # url (r'', views.index),
]

urlpatterns = format_suffix_patterns (urlpatterns)
