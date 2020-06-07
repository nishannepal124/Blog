from django.shortcuts import render
#from django.views.generic import TemplateView
#from django.views import generic
# Create your views here.
from django.http import HttpResponse
from .models import Post , Author

#def index(request):
    #return HttpResponse("Hello, world. You're at the blog index.")

def postView(request):
    post = Post.objects.all()
    fp = Post.objects.filter(feature=True)
    featurePost = fp[0:2]
    recentPost=post[0:6]
    rp=post[6:7]
    recentPost3=post[7:13]
    featurePost2 = fp[0:3]
    context={
        'post':featurePost,
        'latestPost':recentPost,
        'latestPost2':rp,
        'latestPost3':recentPost3,
        'featurePost2':featurePost2,


    }
    template_name = 'index.html'
    return render(request,template_name,context)


def blog_post(request):
    template_name='blog-post.html'
    return render(request,template_name,{})
#class IndexPageView(generic.ListView):
def about(request):
    template_name='about.html'
    return render(request,template_name,{})




#class AboutPageView(TemplateView):
    #template_name='about.html'
