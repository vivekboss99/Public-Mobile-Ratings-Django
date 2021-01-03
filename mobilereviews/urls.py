from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("submitrating/<int:mobileid>", views.submitrating, name="submitrating"),
    path("mobile/<int:mobileid>", views.mobile, name="mobile"), #we show the average rating of mobile from all the users
    path("profile/<str:username>", views.profile, name="profile"), #under profile we show the mobile that the user has rated
]

#we need to use JS to update the average rating each time a rating is added 
#so we update the JSON each time a mobile is added with its ID and rating to it
#as we rate the mobile represented with a ID the same ID in JSON is fetched and updated with the new average.
# that new average is updated back into the html view so the model doesn't contain the rating field. It is updated from the JSON