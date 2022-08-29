from django.shortcuts import render

from scrape.scrape import happyScrape
from .forms import SelectCarForm

from django.http import (
    Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse
  

def ScrapeView(request):

    
    context = {}
    context['SelectCarForm'] = SelectCarForm()
    #for k,v in context:
    #   if k == 'BMW' and v == "X1":
    if request.method == 'POST' and 'run_script' in request.POST:
        from .scrape import happyScrape

        # call function
        #function_to_run() 
        happyScrape()

        
    # return user to required page
    #return HttpResponseRedirect(reverse(scrape:ScrapeView)

    

    return render(request, "scrape.html", context)


""" def SubmitView(request):
    if request.method == 'GET':
        form = SelectCarForm()
    else:
        info = request.POST['info_name']
        output = script_function(info) 
      # Here you are calling script_function, 
      # passing the POST data for 'info' to it;
        return render(request, 'your_app/your_template.html', {
        'info': info,
        'output': output,
      })
    return render(request, 'your_app/your_template.html', {
        'form': form,
     })

def script_function( post_from_form )
  print post_from_form //optional,check what the function received from the submit;
  return subprocess.check_call(['/path/to/your/script.py', post_from_form])  
"""

   