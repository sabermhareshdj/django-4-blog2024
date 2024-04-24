from django.shortcuts import render
from .models import Post
from .forms import PostForm

def post_list(request):
  data = Post.objects.all()
  return render(request,'post_list.html',{'posts':data})

def post_detail(request,post_id):
  data = Post.objects.get(id=post_id)
  return render(request,'post_detail.html',{'post':data})


def post_new(request):
  if request.method == 'POST':
    form =PostForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
  else:
    form = PostForm
  return render(request,'new_post.html',{'form':form})



def edit_post(repuest,post_id):
  pass


def delete_post(request,post_id):
  pass