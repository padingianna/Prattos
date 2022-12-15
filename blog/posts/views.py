from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def blog(request):
    return render(request, 'posts/blog.html')


from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import  ListView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from posts.models import Posteos
from commets.models import Comment
from commets.forms import CreateCommentForm 



"""def posteoslist(request):

    posts = Posteos.objects.all()

    return render(request, 'posts/blog.html', {'posts': posts})"""


class PostsFeedView(ListView):

    template_name = 'posts/blog.html'
    model = Posteos
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ('-creado',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):

    template_name = 'posts/details.html'
    model = Posteos



class CreatePostView(CreateView):
    model = Posteos
    template_name= 'posts/posteo.html'
    success_url= 'posts/blog'
    fields = ['titulo','image_header','posteo',
    ]

    