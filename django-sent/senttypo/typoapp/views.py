from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from ko_papago import ko_papago
from sentiment import sentiment


def ko_sentiment(request):
    trans = ''
    result =''
    if request.method == "POST":
        txt = request.POST['translate']

        # global trans
        
        trans = ko_papago(txt)
        result = sentiment(trans)


    return render(request, 'index.html',{'trans_text': trans, 'emotion': result})

