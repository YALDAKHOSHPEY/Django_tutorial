from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>سلام! اولین صفحه جنگوی من کار می‌کند 🚀</h1>")