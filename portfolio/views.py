from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from portfolio.forms import FeedbackForm
from portfolio.models import Profile, Experience


# Create your views here.
def portfolio(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def profile(request):
    pic = Profile.objects.all()
    img_pic = Experience.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(profile)
    else:
        form = FeedbackForm()
    context = {
        'pic': pic,
        'img_pic': img_pic,
        'form': form


    }
    return render(request, 'index.html', context)



