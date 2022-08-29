from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car
from .filters import CarFilter
from dealers.models import Dealer
from django.core.mail import send_mail

# Create your views here.
def index(request):
    new_cars = Car.objects.filter(category='New')[:6]
    used_cars = Car.objects.filter(category='Used')[:6]
    latest_cars = Car.objects.all().order_by('-date')[:5]
    all = Car.objects.all()
    myFilter = CarFilter(request.GET, queryset=all)
    all = myFilter.qs

    context = {
        'new_cars':new_cars,
        'used_cars':used_cars,
        'latest_cars':latest_cars,
        'all':all,
        'myFilter':myFilter
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def filter_results(request):
    all = Car.objects.all()
    myFilter = CarFilter(request.GET, queryset=all)
    all = myFilter.qs
    page= request.GET.get('page')
    paginator = Paginator(all, 1)
    try:
        all = paginator.page(page)
    except PageNotAnInteger:
        all = paginator.page('1')
    except EmptyPage:
        all = paginator.page(paginator.num_pages)

    page_obj=paginator.get_page(page)

    context = {
        'all':all,
        'myFilter':myFilter,
        'page_obj':page_obj
    }
    return render(request, 'filter_results.html', context)

def car_detail(request, car_id):
    cars = get_object_or_404(Car, id=car_id)

    context = {
        'cars':cars
    }
    return render(request, 'car_detail.html', context)

def inventory(request):
    inventory_cars = Car.objects.all()
    page= request.GET.get('page')
    paginator = Paginator(inventory_cars, 5)
    try:
        inventory_cars = paginator.page(page)
    except PageNotAnInteger:
        inventory_cars = paginator.page('1')
    except EmptyPage:
        inventory_cars = paginator.page(paginator.num_pages)

    page_obj=paginator.get_page(page)

    context = {
        'inventory_cars':inventory_cars,
        'page_obj':page_obj
    }
    return render(request, 'inventory.html', context )



def dealers(request):
    all_dealers = Dealer.objects.all()
    context = {
        'all_dealers':all_dealers
    }
    return render(request, 'dealers.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'Question from ' + name + '  Email: ' + email,
            message,
            email,
            ['']
        )
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')
