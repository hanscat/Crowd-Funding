from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'cardetail/(?P<car_id>[0-9]+)', views.report_detail, name='car_detail_page'),
    # url(r'userdetail', views.user_detail, name='user_detail_page'),
    # url(r'login_page', views.login_page, name='loginPage'),
    url(r'login', views.my_login, name='login'),
    url(r'logout', views.my_logout, name='logout'),
    url(r'signup', views.signup, name='signup'),
    url(r'addmember/(?P<pk>\d+)$', views.addMember.as_view(), name='addmember'),
    url(r'showusers', views.showUsers, name='showusers'),
    url(r'addgroup/$', views.MakeGroup.as_view(), name='addgroup'),
    url(r'addreport/$', views.MakeReport.as_view(), name='addreport'),
    url(r'addfile/$', views.addFile.as_view(), name='addfile'),
    url(r'FileList/$', views.FileList.as_view(), name='filelist'),
    url(r'ReportList/$', views.ReportList.as_view(), name='reportlist'),
    url(r'linkfile/(?P<pk>\d+)$', views.linkfile.as_view(), name='linkfile'),
    url(r'deleteReport/(?P<pk>\d+)$', views.deleteReport.as_view(), name='deleteReport'),
    url(r'GroupList/$', views.GroupList.as_view(), name='grouplist'),
    url(r'deleteGroup/(?P<pk>\d+)$', views.deleteGroup.as_view(), name='deleteGroup'),
    url(r'^validate/$', views.Validate, name='validate'),
    url(r'suspenduser', views.suspendUser, name='suspenduser'),
    url(r'activateuser', views.activateUser, name='activateuser'),
    url(r'deletefromgroup', views.deleteFromGroup, name='deletefromgroup'),
    url(r'makemanager', views.makeManager, name='makemanager')
    # url(r'createListing', views.createListing, name='createListing'),
]