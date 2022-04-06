from django.shortcuts import render
from django.views.generic.base import TemplateView
import requests, json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import News
import os
# Create your views here.


class HomePageView(TemplateView):
    template_name = "newsfeed/home.html"

@method_decorator(login_required, name="dispatch")
class BBCNewsView(TemplateView):
    template_name = "newsfeed/bbcnews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        r = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=dcec54f89dc3408fbfab631139c830aa")
        json_string = r.text
        python_dict = json.loads(json_string)

        for item in range(5):
            headline = item+1
            title = python_dict["articles"][item]["title"]
            desc = python_dict["articles"][item]["description"]
            img = python_dict["articles"][item]["urlToImage"]
            news_obj,created = News.objects.update_or_create(headline_number=headline,defaults={"title":title,"description":desc,"news_image":img})
            print(news_obj,created)
        all_news = News.objects.all()
        context["all_news"]=all_news
        return context


@method_decorator(login_required, name="dispatch")
class IndiaNewsView(TemplateView):
    template_name = "newsfeed/indianews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=dcec54f89dc3408fbfab631139c830aa")
        json_string = r.text
        python_dict = json.loads(json_string)

        for item in range(5):
            headline = item+1
            title = python_dict["articles"][item]["title"]
            desc = python_dict["articles"][item]["description"]
            img = python_dict["articles"][item]["urlToImage"]
            news_obj,created = News.objects.update_or_create(headline_number=headline,defaults={"title":title,"description":desc,"news_image":img})
            print(news_obj,created)
        all_news = News.objects.all()
        context["all_news"]=all_news
        return context


@method_decorator(login_required, name="dispatch")
class SportsNewsView(TemplateView):
    template_name = "newsfeed/sportsnews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=dcec54f89dc3408fbfab631139c830aa")
        json_string = r.text
        python_dict = json.loads(json_string)

        for item in range(5):
            headline = item+1
            title = python_dict["articles"][item]["title"]
            desc = python_dict["articles"][item]["description"]
            img = python_dict["articles"][item]["urlToImage"]
            news_obj,created = News.objects.update_or_create(headline_number=headline,defaults={"title":title,"description":desc,"news_image":img})
            print(news_obj,created)
        all_news = News.objects.all()
        context["all_news"]=all_news
        return context


