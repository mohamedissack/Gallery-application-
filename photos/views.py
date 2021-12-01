from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Location,Catergory


# Create your views here.
def home(request):
    images = Image.objects.all()
    locations =Location.get_locations() 
    catergory =Catergory.objects.all()
    # images = Image.objects.filter(catergory__name=cay)
    return render(request,'all-photos/home.html',{"images":images,"locations":locations,"catergory":catergory})

def locate_image(request,location):
    images = Image.filter_by_location(location)
    return render(request,'all-photos/location.html',{"located_images":images})

def search_results(request):
    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Image.search_by_catergory(search_term)
        message = f"{search_term}"
        
        return render(request, 'all-photos/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image catergory"
        return render(request, 'all-photos/search.html', {"message": message})

# def catergory(request):

#     return render(request, 'all-photos/catergory.html', )


# def nature(request):
    
#     images = Image.objects.all()
    
#     return render(request, 'all-photos/nature.html',{"images":images})

# def travel(request):
#     images = Image.objects.all()
#     locations =Location.get_locations() 
#     return render(request, 'all-photos/travel.html',{"images":images})

# def animals(request):
#     images = Image.objects.all()
#     locations =Location.get_locations() 
#     return render(request, 'all-photos/animals.html',{"images":images})

# def food(request):
#     images = Image.objects.all()
#     locations =Location.get_locations() 
#     return render(request, 'all-photos/food.html',{"images":images})

# def work(request):
#     images = Image.objects.all()
#     locations =Location.get_locations() 
#     return render(request, 'all-photos/work.html',{"images":images})