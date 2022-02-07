from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'fbv_book_list.html', context=context)


def book_post(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm()

    return render(request, 'fbv_book_post.html', {'form': form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'fbv_book_detail.html', context={'book': book})


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'cbv_book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'cbv_book_detail.html'
