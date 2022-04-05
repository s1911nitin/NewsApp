
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.list import ListView
from .forms import MultiplePostForm
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView

# Create your views here.

@method_decorator(login_required, name="dispatch")
class MultiplePostFormView(FormView):
    template_name = "blog/multipleposts.html"
    form_class = MultiplePostForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser == True:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(user__id=int(self.request.user.id))
        context["posts"] = posts
        return context

    def post(self,request):
        form = MultiplePostForm(request.POST,request.FILES)
        if form.is_valid():
            post_title = form.cleaned_data["title"]
            post_desc = form.cleaned_data["desc"]
            img = form.cleaned_data["post_image"]
            id = int(self.request.user.id)
            user_obj = User.objects.get(pk=id)
            obj = Post(title=post_title,desc=post_desc,post_image=img,user=user_obj)
            obj.save()
            messages.success(self.request,"Your post is made !")
            return HttpResponseRedirect("/multipleposts/")
        if self.request.user.is_superuser == True:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(user__id=int(self.request.user.id))
        return render(request,self.template_name,{"form":form,"posts":posts})


@method_decorator(login_required, name="dispatch")
class UpdatePostFormView(UpdateView):
    model = Post
    form_class = MultiplePostForm
    success_url = "/multipleposts/"


@method_decorator(login_required, name="dispatch")
class DeletePostFormView(DeleteView):
    model = Post
    success_url = "/multipleposts/"


class BlogPostView(ListView):
    model = Post
    template_name = "blog/blogpost.html"
    paginate_by = 2
    paginate_orphans = 1






