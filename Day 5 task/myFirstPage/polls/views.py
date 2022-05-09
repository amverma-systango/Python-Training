from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.views import LoginView

from .models import User, Question, Choice, Participant

# Create your views here.

class Index(TemplateView):
    http_method_names = ['get']
    template_name = 'polls/index.html'
    
    




class Login(LoginView):
    http_method_names = ['get', 'post']
    template_name = "polls/login.html"
    # success_url = 'signup'
    
    

    def post(self, request):
        userNameInp = request.POST['nameInp']
        userPasswordInp = request.POST['passwordInp']

        user = User.objects.filter( user_name = userNameInp )

        if( len(user) != 0 ):   
            request.session["userId"] = user.id
            request.session["userLoginStatus"] = "LoggedIn"

            

            return redirect("/login/{}".format(user.id))
            
        else:
            return HttpResponse("wrong credential")






class Signup(TemplateView):
    http_method_names = ['get', 'post']
    template_name = "polls/signup.html"
    
    
    def post(self, request):
        
        # try:
        #     user = User.objects.filter()
    
        # except:
        #     pass

        userNameInp = request.POST['nameInp']
        userPasswordInp = request.POST['passwordInp']

        print(userNameInp, userPasswordInp)

        user = User.objects.filter( user_name = userNameInp )

        print(user)

    
        if( len(user) == 0 ):
            createUser = User( user_name = userNameInp, user_password = userPasswordInp)
            createUser.save()

            return redirect("/login")
        else:
            return HttpResponse("username unavailable please try again")




class Home(TemplateView):
    http_method_names = ['get']
    template_name = "polls/signup.html"
    
    
    def get(self, request):
        
        print(request.session["userId"])
        user = User.objects.filter(id = request.session["userId"] ).first()

    
        if( len(user) == 0 ):
            createUser = User( user_name = userNameInp, user_password = userPasswordInp)
            createUser.save()

            # return redirect("/login")
            return HttpResponse("home")

        else:
            return HttpResponse("username unavailable please try again")






