from django.shortcuts import render
from django.http import HttpResponse
from models import *

# Create your views here.
def post_list(request):
	results=Post.objects.all()
	return render(request,'blog/posts.html',{'results':results})