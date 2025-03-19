from django.shortcuts import render, redirect
from .models import Category, Page, CategoryForm, PageForm

# Display Categories and Pages
def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

# Add a New Category
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

# Add a New Page
def add_page(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.save()
            return redirect('index')
    else:
        form = PageForm()
    return render(request, 'add_page.html', {'form': form, 'category': category})
