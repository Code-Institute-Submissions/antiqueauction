{"filter":false,"title":"urls.py","tooltip":"/accounts/urls.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from . import urls_reset","from .views import register, profile, logout, login","","urlpatterns = [","    url(r'^register/$', register, name='register'),","    url(r'^profile/$', profile, name='profile'),","    url(r'^logout/$', logout, name='logout'),","    url(r'^login/$', login, name='login'),","    url(r'^password-reset/', include(urls_reset)),","]"],"id":1}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":["_"],"id":2}],[{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"remove","lines":["_"],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":41},"end":{"row":9,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1570620265389,"hash":"b48b3f2300fdc8abf32815ad4b94efdeba2c222b"}