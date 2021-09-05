from django.db.models.base import Model
from django.views.generic import ListView,CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from django.views.generic import DeleteView
from django.shortcuts import redirect

class PostListView(ListView):
    model=Post
    template_name="tweet/index.html"
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5

class PostCreateView(CreateView):
    model=Post
    fields=['content']
    template_name='tweet/post_create.html'
    success_url='/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
