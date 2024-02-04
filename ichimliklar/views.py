from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views import View
from .models import Ichimliklar, ReviewDrinkModel
from .forms import UpdateDrinkForm, CommentForm, CommentUpdateForm

# Create your views here.

@login_required
def homepage_view(request):
    return render(request, "home.html")

class DrinkView(View):
    def get(self, request):
        drinks = Ichimliklar.objects.order_by('name')
        context = {'drinks': drinks}
        return render(request, 'ichimlik/ichimlik.html', context=context)

class UpdateDrinkView(View):
    def get(self, request, pk):
        drink_instance = get_object_or_404(Ichimliklar, pk=pk)
        form = UpdateDrinkForm(instance=drink_instance)
        context = {'form': form, 'drink': drink_instance}
        return render(request, 'ichimlik/update_ichimlik.html', context=context)

    def post(self, request, pk):
        drink_instance = get_object_or_404(Ichimliklar, pk=pk)
        form = UpdateDrinkForm(request.POST, request.FILES, instance=drink_instance)
        if form.is_valid():
            form.save()
            return redirect('drinks')
        context = {'form': form, 'drink': drink_instance}
        return render(request, 'ichimlik/update_ichimlik.html', context=context)

class DeleteDrinkView(View):
    def get(self, request, pk):
        drink_instance = get_object_or_404(Ichimliklar, pk=pk)
        return render(request, 'ichimlik/delete.html', {'drink': drink_instance})

    def post(self, request, pk):
        drink_instance = get_object_or_404(Ichimliklar, pk=pk)
        drink_instance.delete()
        return redirect('drinks')

class AboutDrinkView(View):
    def get(self, request, pk):
        drink = Ichimliklar.objects.get(pk=pk)
        context = {'drink': drink}
        return render(request, 'ichimlik/aboutdrink.html', context=context)

class AddCommentView(View):
    def get(self, request, pk):
        form = CommentForm()
        return render(
            request, "ichimlik/add_comment.html", {"form": form, "drink_id": pk}
        )

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.drink_id = pk
            comment.user = request.user
            comment.save()
            return redirect("drink", pk=pk)
        return render(
            request, "ichimlik/add_comment.html", {"form": form, "drink_id": pk}
        )

class DeleteCommentView(View):
    def get(self, request, pk):
        comment = get_object_or_404(CommentsModel, id=pk)
        return render(request, "ichimlik/delete_comment.html", {"comment": comment})

    def post(self, request, pk):
        comment = get_object_or_404(ReviewDrinkModel, id=pk)
        pk = comment.drink.pk
        comment.delete()
        return redirect("drink", pk=pk)


class UpdateCommentView(View):
    def get(self, request, pk):
        comment = get_object_or_404(ReviewDrinkModel, id=pk)
        form = CommentUpdateForm(instance=comment)
        context = {"form": form, "comment": comment}
        return render(request, "ichimlik/update_comment.html", context=context)

    def post(self, request, pk):
        comment = get_object_or_404(CommentsModel, id=pk)
        form = CommentUpdateForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            pk = comment.drink.pk
            form.save()
            return redirect("drink", pk=pk)
        context = {"form": form, "comment": comment}
        return render(request, "ichimlik/update_comment.html", context=context)

