
from ensurepip import version
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, LoginForm, ProfileForm, ChangePasswordForm, ResetPasswordForm, ResetPasswordConfirmForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.core.cache import cache

# Create your views here.

class SignupFormView(FormView):
    template_name = "dashboard/signup.html"
    form_class = SignupForm


    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            usr = form.save()
            group = Group.objects.get(name="Author")
            usr.groups.add(group)
            messages.success(self.request,"Your are successfully registered !!")
            return HttpResponseRedirect("/signup/")
        return render(request,self.template_name,{"form":form})




class LoginFormView(LoginView):
    template_name = "dashboard/login.html"
    form_class = LoginForm

    def get(self, request):
        if not self.request.user.is_authenticated == True:
            form  = LoginForm()
            return render(request, self.template_name, {"form":form})
        else:
            return HttpResponseRedirect("/profile/")

    def post(self, request):
        if not self.request.user.is_authenticated == True:
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data["username"]
                upass = form.cleaned_data["password"]
                user = authenticate(username=uname,password=upass)
                if user !=None:
                    login(request,user)
                    return HttpResponseRedirect("/profile/")
            return render(request,self.template_name,{"form":form})
        else:
            return HttpResponseRedirect("/profile/")   


@method_decorator(login_required, name="dispatch")
class ProfileFormView(TemplateView):
    template_name = "dashboard/profile.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        form = ProfileForm(instance=self.request.user)
        ip = self.request.session["ip"]
        count = cache.get("count",0,version=int(self.request.user.id))
        context["form"] = form
        context["ip"] = ip
        context["count"] = count
        return context

    def post(self, request):
        form = ProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your profile has been updated successfully !!")
            return HttpResponseRedirect("/profile/")

@method_decorator(login_required, name="dispatch")
class LogoutFormView(LogoutView):
    template_name = "newsfeed/home.html"


@method_decorator(login_required, name="dispatch")
class ChangePasswordFormView(PasswordChangeView):
    template_name = "dashboard/changepassword.html"
    form_class = ChangePasswordForm
    success_url = "/changepassworddone/"

    def form_valid(self, form):
        form = super().form_valid(form)
        messages.success(self.request,"Your password has been changed now !!")
        return form

@method_decorator(login_required, name="dispatch")
class ChangePasswordDoneFormView(PasswordChangeDoneView):
    template_name = "dashboard/changepassworddone.html"

class ResetPasswordFormView(PasswordResetView):
    template_name = "dashboard/resetpassword.html"
    form_class = ResetPasswordForm
    success_url = "/resetpassworddone/"


class ResetPasswordDoneFormView(PasswordResetDoneView):
    template_name = "dashboard/resetpassworddone.html"


class ResetPasswordConfirmFormView(PasswordResetConfirmView):
    template_name = "dashboard/resetpasswordconfirm.html"
    form_class = ResetPasswordConfirmForm
    success_url = "/resetcomplete/"

    def form_valid(self, form):
        form = super().form_valid(form)
        messages.success(self.request,"Your password has been changed now !!")
        return form

class ResetPasswordCompleteFormView(PasswordResetCompleteView):
    template_name = "dashboard/resetpasswordcomplete.html"


