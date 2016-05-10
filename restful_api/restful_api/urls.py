from django.conf.urls import url
from django.contrib import admin
from rest_api_beta import views



urlpatterns = [
    url(r'^api/v1/admin/', admin.site.urls),
	url(r'^api/v1/users/$', views.users_list),
	url(r'^api/v1/urgences/$', views.urgences_list),
	url(r'^api/v1/urgence/(?P<id_emergency>[0-9]+)$', views.urgence_infos),
	url(r'^api/v1/user/(?P<id_user>[0-9]+)$', views.user_infos),
	url(r'^api/v1/user/(?P<user_phone>\w+)$', views.user_post_datas),
	url(r'^api/v1/userauth/$', views.user_auth),
	url(r'^api/v1/photos/(?P<comment_urgence>\w+)$', views.send_photos_urgence),

	# url(r'^api/v1/photos/id_urgence$', views.send_photos_urgence)

	url(r'^api/v1/user/(?P<id_user>[0-9]+)/urgence/(?P<lattitude>[0-9.]+)/(?P<longitude>[0-9.]+)/(?P<altitude>[0-9.]+)/(?P<reason>\w+)/(?P<priority>[0-9]+)$', views.post_create_urgence),
]
