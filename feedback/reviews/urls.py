from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.reviews),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/favorite",views.AddFavoriteView.as_view()),
    path("reviews/<int:id>",views.SingleReviewView.as_view())
    # path("thank-you", views.thank_you)
]
