from django.shortcuts import render
from .forms import SelectCarForm
from requests.exceptions import MissingSchema



def ScrapeView(request):

    
    context = {}
    context['SelectCarForm'] = SelectCarForm()
    #for k,v in context:
    #   if k == 'BMW' and v == "X1":
    #conList =  context.items()
    #request.session['conList'] = conList
    
    
    
    
    try:

        if request.method == 'POST' and 'run_script' in request.POST:
            form = SelectCarForm(request.POST)
            if form.is_valid():
                from .scrape import happyScrape
                from .scrape2 import happyScrape2
                #from .sentiment import getSentiment

                happyScrape(form.cleaned_data['brand'], form.cleaned_data['car_model'])
                happyScrape2(form.cleaned_data['brand'], form.cleaned_data['car_model'])
                
            #getSentiment()

    except MissingSchema:
       return render(request,'badSelect.html')


        
        # call function
        #function_to_run() 
        #happyScrape()       
    # return user to required page
    #return HttpResponseRedirect(reverse(scrape:ScrapeView)
    """ if request.method == 'POST' and 'get_score' in request.POST:
        from .sentiment import getSentiment
    

        context = {}
        context['polarity'] = getSentiment()

        return render(request, "score.html", context) 
    """
    return render(request, "scrape.html", context)


def ScoreView(request):
    from .sentiment import getSentiment
    

    context = {}
    context['ps'] = getSentiment()

    return render(request, "score.html", context)

def MLScoreView(request):
    from .ml_roberta import getSentiment_ml
    

    context = {}
    context['ls'] = getSentiment_ml()

    return render(request, "ml_score.html", context)






"""
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def ScrapePostReqView(request):
    conList = request.session.get('conList')

    context = Convert(conList)

    return render(request,"scrapepostreq.html",context)






    def SubmitView(request):
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



   