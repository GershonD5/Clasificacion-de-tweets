from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.
import random

from .models import Tweet#, Choice

#Get tweets and display

def index(request):
    tweets_list= Tweet.objects.order_by('-id')[:5]
    context= {'tweets_list': tweets_list}

    return render(request, 'polls/index.html',context)

#show specifici tweet and choices

def detail(request, tweet_id):
    try:
        tweet=Tweet.objects.get(pk=tweet_id)
    except Tweet.DoesNotExist:
        raise Http404("El tweet no existe")
    return render(request,'polls/detail.html',{'tweet':tweet})

#Get tweet y mostrar resultado

def results(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'polls/results.html',{ 'tweet':tweet })


# Vote for a tweet choice


def ofensivo(request, tweet_id):
    # print(request.POST['choice'])
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    tweet.ofensivo +=1
    tweet.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:detail', args=(random.randrange(rangoMenor(),rangoMayor(),1),)))

def NoOfensivo(request, tweet_id):
    # print(request.POST['choice'])
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    tweet.No_Ofensivo +=1
    tweet.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(random.randrange(rangoMenor(),rangoMayor(),1),)))




def rangoMayor():
    return Tweet.objects.last().id

def rangoMenor(): 
    return Tweet.objects.first().id

