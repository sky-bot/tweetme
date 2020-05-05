from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
# Create your views here.
from tweets.models import Tweets
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        'id': tweet_id,
        # 'content': obj.content,
        # 'image': obj.image
    }
    status = 200
    try :
        obj = Tweets.objects.get(tweet_id=tweet_id)
        data['content'] = obj.content
    except Exception as e:
        data['message'] = "Not Found"
        status = 404
    
    return JsonResponse(data, status=status)    

def tweet_list_view(request, *args, **kwargs):
    all_tweets = Tweets.objects.all()
    tweet_list = [{'id': row.tweet_id, "content": row.content} for row in all_tweets]
    data= {
        "isUser": False,
        "response" : tweet_list
    }
    return JsonResponse(data)