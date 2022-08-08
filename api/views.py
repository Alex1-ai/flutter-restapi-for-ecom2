from django.http  import JsonResponse

# Create your views here.

def home(request):
    return JsonResponse({
        'info':"Djanog & react course",
        'name': "Chidi"
    })
