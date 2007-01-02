from django.conf.urls.defaults import *
import sys
sys.path.append('Site')
from timeview import current_datetime
from erreur import erreur404
urlpatterns = patterns('',(r'^now/$','timeview.current_datetime'),)
#urlpatterns = patterns('',(r'','erreur.erreur404'),)

