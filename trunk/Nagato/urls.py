from django.conf.urls.defaults import *
from Nagato.view import current_datetime
urlpatterns = patterns('',
    # Example:
    # (r'^Nagato/', include('Nagato.foo.urls')),

    # Uncomment this for admin:
 #(r'^admin/', include('django.contrib.admin.urls'))
 (r'^now/$', current_datetime),
)
