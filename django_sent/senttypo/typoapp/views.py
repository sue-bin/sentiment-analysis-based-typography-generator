from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from ko_papago import ko_papago
from sentiment import sentiment
from sent import sentence_to_image


def load(request):
    return render(request, 'index2.html')

def ko_sentiment(request):
    trans = ''
    emotion =''
    txt = ''
    image = ''
    if request.method == "POST":
        txt = request.POST['translate']

        # global trans
        
        trans = ko_papago(txt)
        emotion = sentiment(trans)

        image = sentence_to_image(trans, emotion,'/Users/jupiter/Desktop/BIGTA/감성타이포/local_django_sent/senttypo/static/img/')


        #save directory
        

    return render(request, 'index.html',{'text': txt, 'trans_text': trans, 'emotion': emotion, 'image':image})


def show_mc(request):
    
    return render (request, 'font.html')


