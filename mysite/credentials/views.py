from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contactform,internshipsform
from .models import contact,internships
from django.http import HttpResponse
#from cs243.view import 
# Create your views here.



def contact(request):
    language='en-gb'
    session_language= 'en-gb'
    
    if 'lang' in request.COOKIES:
        language=request.COOKIES['lang']
        
    if 'lang' in request.session:
        session_language = request.session['lang']
        
    f=contactform(request.POST)
    if f.is_valid():
        
        new=f.save(commit=False)
        new.username=request.user.username
        #new.email=user.email
        #new.lastname='prodhan'
        # firstname=f.cleaned_data['firstname']
        #new_join, created=student.objects.get_or_create(firstname=firstname)
        new.save()
    context={"form":f,"language":language,"session_language":session_language}
    template="contact.html"
    return render(request,template,context)

def language(request,language='en-gb'):
    response = HttpResponse("setting languages to %s" % language)
    
    response.set_cookie('lang',language)
    
    request.session['lang'] = language
    
    return response


def internships(request):
    f2=internshipsform(request.POST)
     #obj=contact.objects.get(pk=id)
     #f2=student2form(instance=obj)
     # if request.POST:
     #     f2=internshipsform(request.POST)
     
    if f2.is_valid():
             
            #obj=contact.objects.get(email="abc")
        
        new=f2.save(commit=False)
        #new.email=user.email
        new.save()
  
    context={"form2":f2}
    template="internships.html"
    return render(request,template,context)
