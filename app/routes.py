from flask import render_template, request, current_app as app

# Static list of items with extended information
items = [
    {"title": "Book1", "author": "Author1", "year": 2020, "category": "Category1", "sub_category": "Subcategory1", "language": "English", "material": "Paperback"},
    {"title": "Book2", "author": "Author2", "year": 2019, "category": "Category2", "sub_category": "Subcategory2", "language": "Spanish", "material": "Hardcover"},
    {"title": "Book3", "author": "Author3", "year": 2018, "category": "Category1", "sub_category": "Subcategory1", "language": "French", "material": "Ebook"},
    {"title": "Book4", "author": "Author4", "year": 2021, "category": "Category3", "sub_category": "Subcategory3", "language": "German", "material": "Audiobook"},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    filtered_items = items
    if request.method == 'POST':
        title_filter = request.form.get('title')
        author_filter = request.form.get('author')
        category_filter = request.form.get('category')
        sub_category_filter = request.form.get('sub_category')
        language_filter = request.form.get('language')
        material_filter = request.form.get('material')

        if title_filter:
            filtered_items = [item for item in filtered_items if title_filter.lower() in item['title'].lower()]
        if author_filter:
            filtered_items = [item for item in filtered_items if author_filter.lower() in item['author'].lower()]
        if category_filter:
            filtered_items = [item for item in filtered_items if category_filter.lower() in item['category'].lower()]
        if sub_category_filter:
            filtered_items = [item for item in filtered_items if sub_category_filter.lower() in item['sub_category'].lower()]
        if language_filter:
            filtered_items = [item for item in filtered_items if language_filter.lower() in item['language'].lower()]
        if material_filter:
            filtered_items = [item for item in filtered_items if material_filter.lower() in item['material'].lower()]

    return render_template('index.html', items=filtered_items)

