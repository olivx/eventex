from django.conf.urls import url, include
from django.contrib import admin


from eventex.core.views import home
from eventex.subscriptions.views import subscribe, detail


urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
]
