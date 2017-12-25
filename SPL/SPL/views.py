from django.shortcuts import redirect

# Views for redirecting URLs go here

def home_redirect(request):
    return redirect('/app_Transaction')
