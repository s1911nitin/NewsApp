from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def receiver_func(sender,request,user,**kwargs):
    client_ip = request.META.get('REMOTE_ADDR')
    request.session["ip"] = client_ip

    count = cache.get("count",0,version=int(user.id))
    new_count = count + 1
    cache.set("count",new_count,60*60*10,version=int(user.id))


