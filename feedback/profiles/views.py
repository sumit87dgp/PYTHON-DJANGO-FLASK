from email.mime import image
import profile
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView




# Create your views here.
class ProfilesView(ListView):
    model = UserProfile
    template_name: str = "profiles/user_profiles.html"
    context_object_name = "profiles"



class CreateProfileView(CreateView):
    template_name: str = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url= "/profiles"


def store_file(file):
    with open("temp/image.jpg","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


# class CreateProfileView(View):
    # def get(self, request):
    #     form = ProfileForm()
    #     return render(request, "profiles/create_profile.html",{
    #         "form": form
    #     })

    # def post(self, request):
    #     #print(request.FILES["image"])
    #     submitted_form = ProfileForm(request.POST, request.FILES)
    #     if submitted_form.is_valid():                
    #         #store_file(request.FILES["image"])
    #         profile = UserProfile(image=request.FILES["user_image"])
    #         profile.save()
    #         return HttpResponseRedirect("/profiles")

    #     return render(request,"profiles/create_profile.html",{
    #         "form": submitted_form
    #     })
