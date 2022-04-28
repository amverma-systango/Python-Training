from django.shortcuts import render
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
    
    

    # def post(self, request):
    #     pass





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
        else:
            return HttpResponse("username unavailable please try again")

