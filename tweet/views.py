from django.shortcuts import render
from .models import Tweet
from .forms import tweetform , UserRegistrationForm
from django.shortcuts import get_object_or_404  , redirect   #django shortcuts imported
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request ,'index.html' )

#(9) 1st function is to list all the tweets made on page
def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request , 'tweet_list.html' , {'tweets':tweets})

#(10)function is to create a tweet
@login_required
def tweet_create(request):
  
      #when user gives us a filled form
    if request.method =="POST":
       form = tweetform(request.post , request.FILES)
       if  form.is_valid():        #inbuilt django function
          tweet=form.save(commit=False)   #just save the form rn but dont save in database
          tweet.user=request.user
          tweet.save()
          return redirect('tweet_list')
          
    else:   #this is when user is given an empty form
     form=tweetform()
     return render(request ,"tweet_form.html" , {'form':form})
    

    
    #(11)function to edit tweet
@login_required
def tweet_edit(request , tweet_id):
       tweet=get_object_or_404(Tweet , pk=tweet_id , user=request.user)   #user=request,user means a person can only edit his tweet
       if request.method=='POST':
          form = tweetform(request.POST , request.FILES , instance=tweet)
          if  form.is_valid():        
           tweet=form.save(commit=False) 
          tweet.user=request.user
          tweet.save()
          return redirect('tweet_list')
         
       else:
        form=tweetform(instance=tweet)
        return render(request ,"tweet_form.html" , {'form':form})
    
     #(12)function to delete tweet 
@login_required
def tweet_delete(request , tweet_id):
       tweet=get_object_or_404(Tweet , pk=tweet_id , user=request.user)
       if request.method=="POST":
          tweet.delete()
          return redirect ('tweet_list')
       return render(request ,"tweet_confirm_delete.html" , {'tweet':tweet})
    
def register(request):
    if  request.method=="POST":
      form= UserRegistrationForm(request.POST)
      if  form.is_valid():        
           user=form.save(commit=False) 
           user.set_password(form.cleaned_data['password1'])     #set_pasword and cleaned_data are inbuilt in python
           user.save()
           login(request , user)   #all login functionality passed using inbuilt login method
           return redirect('tweet_list')
           
    else:
       form=UserRegistrationForm
    return render(request ,"registration/register.html" , {'form':form})

       