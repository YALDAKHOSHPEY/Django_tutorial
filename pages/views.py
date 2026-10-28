from django.shortcuts import render

def home(request):
    context = {
        'title': 'به جنگو خوش آمدید 🚀',
        'message': 'این صفحه با استفاده از Template رندر شده است.',
        'skills': ['Templates', 'Models', 'ORM', 'Admin', 'Forms'],
    }
    return render(request, 'pages/home.html', context)