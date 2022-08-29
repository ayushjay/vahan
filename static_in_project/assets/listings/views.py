from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .filters import ListingFilter
from django.core.mail import send_mail
# Create your views here.
def index(request):
    all = Listing.objects.all()
    news = Listing.objects.filter(category='New')
    useded = Listing.objects.filter(category='Used')

    myFilter = ListingFilter(request.GET, queryset=all)
    all = myFilter.qs



    context = {
        'all':all,
        'news':news,
        'useded':useded,

        'myFilter': myFilter
    }
    return render(request, 'index.html', context)

def cars(request):
    all = Listing.objects.all()

    myFilter = ListingFilter(request.GET, queryset=all)

    all = myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(all, 1)
    try:
        all = paginator.page(page)
    except PageNotAnInteger:
        all = paginator.page('1')
    except EmptyPage:
        all = paginator.page(paginator.num_pages)

    page_obj = paginator.get_page(page)

    context = {
        'myFilter': myFilter,
        'all':all,
        'page_obj':page_obj

    }
    return render(request, 'cars.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'question from ' + name,
            message,
            email,
            ['ivanap041@gmail.com'],


        )

        return render(request, 'contact.html', {'name':name})
    else:
        return render (request, 'contact.html')
