from django.shortcuts import redirect
from django.urls import reverse

# Views for redirecting URLs go here

def home_redirect(request):
    return reverse('/studentLogin/')
