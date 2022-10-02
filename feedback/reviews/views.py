from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# class ReviewView(View):

#     def get(self, request):
#         pass

#     def post():
#         pass

# Create your views here.
def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data['user_name'],
                review_text = form.cleaned_data['review_text'],
                rating = form.cleaned_data['rating']
            )
            review.save()
            #print(form.cleaned_data)
            #entered_name = request.POST['username']
            #print(entered_name)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
        
    return render(request, "reviews/review.html",{
        "form":form
    })    


class ThankYouView(TemplateView):
    template_name: str = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


# class ThankYouView(View):
#     def get(self,request):
#         return render(request,"reviews/thank_you.html")

# def thank_you(request):
#     return render(request,"reviews/thank_you.html")

# class ReviewsListView(TemplateView):
#     template_name: str = "reviews/review_list.html"
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name: str = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews "

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)


class SingleReviewView(TemplateView):
    template_name: str = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        
        context["review"] = selected_review
        return context