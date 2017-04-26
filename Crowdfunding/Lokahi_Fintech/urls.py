from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login', views.my_login, name='login'),
    url(r'logout', views.my_logout, name='logout'),
    url(r'signup', views.signup, name='signup'),
    url(r'addmember/(?P<pk>\d+)$', views.addMember.as_view(), name='addmember'),
    url(r'inbox', views.inbox, name='inbox'),
    url(r'sendMessage', views.sendMessage, name='sendMessage'),
    url(r'delete_message/(?P<message_id>[0-9]+)', views.delete_message, name='delete_message'),
    url(r'message_detail/(?P<message_id>[0-9]+)', views.message_detail, name='message_detail'),
    url(r'message_detail_decrypted/(?P<message_id>[0-9]+)', views.message_detail_decrypted,
        name='decrypted_message_detail'),
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
]

