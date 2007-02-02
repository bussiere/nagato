from django.conf.urls.defaults import *
from Nagato.view import *
urlpatterns = patterns('',
    # Example:
    # (r'^Nagato/', include('Nagato.foo.urls')),

    # Uncomment this for admin:
 #(r'^admin/', include('django.contrib.admin.urls'))
 (r'^carnet/$', carnet),
 (r'^carnet/rajouter/$', rajouter),
 (r'^carnet/chercher/$', chercher),
 (r'^carnet/mas/$', mas),
 (r'^carnet/mas/chermaj/$', chermaj),
 (r'^carnet/rajouter/rajoutercontact/$', rajoutercontact),
 (r'^carnet/chercher/rechercher/$', rechercher),
)
