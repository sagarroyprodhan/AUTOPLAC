from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm



def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c,context_instance=RequestContext(request))



def auth_view(request):
    username=request.POST.get('username', '')
    password=request.POST.get('password', '')
    user=auth.authenticate(username=username,password=password)
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/loggedin/')
    else:
        return HttpResponseRedirect('/invalid/')

def invalid_login(request):
    return render_to_response('invalid_login.html',context_instance=RequestContext(request))

def loggedin(request):
    return render_to_response('index2.html',{'fullname':request.user.username},context_instance=RequestContext(request))

def register_user(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')
        else:
            print "yeahhhhhhhh"
    else:
        form = UserCreationForm()
        
    args = {}
    args.update(csrf(request))
    args['form']=UserCreationForm(request.POST)
    print args
    return render_to_response('register.html',args,context_instance=RequestContext(request))

def register_success(request):
    return render_to_response('login.html',context_instance=RequestContext(request))

def index2(request):
    t=get_template("index2.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)

def studentprofile(request):
    t=get_template("studentprofile.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)

def photo(request):
    t=get_template("photo.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)

# def contact(request):
#     t=get_template("contact.html")
#     p=t.render(Context({}))
#     return HttpResponse(p)

def postgrad(request):
    t=get_template("postgrad.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)

def srsec(request):
    t=get_template("srsec.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)

def sec(request):
    t=get_template("sec.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)

def undergrad(request):
    t=get_template("undergrad.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)

# def internships(request):
#     t=get_template("internships.html")
#     p=t.render(Context({}))
#     return HttpResponse(p)

def languages(request):
    t=get_template("languages.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)

def projects(request):
    t=get_template("projects.html")
    p=t.render(Context({'fullname':request.user.username}))
    return HttpResponse(p)





