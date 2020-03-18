from django.http import HttpResponse

# Create your views here.
def home_page(request):
  html = '<html><title>To-Do lists</title></html>'
  return HttpResponse(html)