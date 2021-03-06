from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'fbv_book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'fbv_book_detail.html', context={'book': book})


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


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'fbv_book_post.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book-list')


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'cbv_book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'cbv_book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'cbv_book_post.html'
    fields = ('title', 'category', 'author')
    success_url = reverse_lazy('cbv-book-list')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'cbv_book_post.html'
    context_object_name = 'book'
    fields = ('title', 'category', 'author')

    def get_success_url(self):
        return reverse_lazy('cbv-book-detail', kwargs={'pk': self.object.id})


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'cbv_book_delete.html'
    success_url = reverse_lazy('cbv-book-list')
