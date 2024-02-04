from django.urls import path
from .views import DrinkView, UpdateDrinkView, AboutDrinkView, DeleteDrinkView, DeleteCommentView, AddCommentView,UpdateCommentView

urlpatterns = [
    path('drinks/', DrinkView.as_view(), name='drinks'),
    path('<int:pk>/about-drink/', AboutDrinkView.as_view(), name='about-drink'),
    path('update/drink/<int:pk>/', UpdateDrinkView.as_view(), name='update_drink'),
    path('delete/<int:pk>/', DeleteDrinkView.as_view(), name='delete'),
    path("ichimliklar/delete/comment/<int:pk>/", DeleteCommentView.as_view(), name="delete_comment"),
    path('ichimliklar/add_comment/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
    path("ichimliklar/update/comment/<int:pk>/", UpdateCommentView.as_view(), name="update_comment"),

]

