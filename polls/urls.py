from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
media_root = getattr(settings, 'MEDIA_ROOT', '/media')

app_name = 'polls'
urlpatterns = [
	
    
	url(r'^$',views.test),
	url(r'^vocabtest/$', views.vocabindex),
	url(r'vocabtest/result/$',views.vocabresult),
	url(r'compretest/$', views.compreindex),
	url(r'compretest/result/$',views.compreresult),
	url(r'mathtest/$',views.mathindex),
	url(r'mathtest/result/$',views.mathresult),
	url(r'^studentstd/$', views.std),
	url(r'compositiontest/$', views.Compositionindex),
	url(r'compositiontest/result/$', views.Compositionresult),
	url(r'dict/$',views.dict),
	url(r'dict/result/$',views.dictresult),
	url(r'count/$',views.count),
	url(r'ml/$',views.detect),
	url(r'user/$',views.user),
	url(r'^resource/$', views.resource, name='urlname')


	#(r'^user/(?P<username>\w{0,50})/$', views.profile_page,),


	
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)