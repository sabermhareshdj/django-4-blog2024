from django.shortcuts import render , redirect
from .models import Post , Comment
from .forms import PostForm , CommentForm


from django.views.generic import ListView,DetailView ,CreateView,UpdateView,DeleteView

# def post_list(request):       # query : template : context 
#   data = Post.objects.all()
#   return render(request,'post_list.html',{'posts':data}) # context

class PostList(ListView):  #template : post_list
  model = Post             # context = post_list , object_list




def post_detail(request,pk):
  data = Post.objects.get(id=pk)
  post_comments = Comment.objects.filter(post=data)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      myform = form.save(commit=False)
      myform.user = request.user
      myform.post = data
      myform.save()
  else:
    form = CommentForm()
  return render(request,'blog/post_detail.html',{'post':data , 'form':form , 'post_comments':post_comments})





# class PostDetail(DetailView):
#   model = Post


def add_comment(request):
  pass


# def post_new(request):
#   if request.method == 'POST':
#     form =PostForm(request.POST,request.FILES)
#     if form.is_valid():
#       myform = form.save(commit=False)
#       myform.author = request.user
#       form.save()
#       return redirect('/blog')
#   else:
#     form = PostForm()
#   return render(request,'new_post.html',{'form':form})

class PostCreate(CreateView):
  model = Post
  fields = ['title','content','create_date','draft','tags','author','image']
  success_url = '/blog'


# def edit_post(repuest,post_id):
#   data = Post.objects.get(id=post_id)
#   if repuest.method == 'POST':
#     form =PostForm(repuest.POST,repuest.FILES,instance=data)
#     if form.is_valid():
#       myform = form.save(commit=False)
#       myform.author = repuest.user
#       form.save()
#       return redirect('/blog')
#   else:
#     form = PostForm(instance=data)
#   return render(repuest,'edit_post.html',{'form':form})

class PostUpdate(UpdateView):
  model = Post
  fields = ['title','content','create_date','draft','tags','author','image']
  success_url = '/blog'
  template_name = 'blog/edit_post.html'

# def delete_post(request,post_id):
#     data = Post.objects.get(id=post_id)
#     data.delete()
#     return redirect('/blog')

class PostDelete(DeleteView):
  model = Post
  success_url = '/blog'

