from django.http import HttpResponse


def erreur404(request):
    html = "<html><body>Erreur 404</body></html>" 
    return HttpResponse(html)