from django.shortcuts import render, redirect

from instrumentation.utils import upload_image_to_supabase

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                # Upload image to Supabase and get the image URL
                image_url = upload_image_to_supabase(image_file)
                if image_url:
                    # Save the product with the image URL
                    product = form.save(commit=False)
                    product.image_url = image_url
                    product.save()
                    return redirect('product_list')
            else:
                # Handle case where no image is provided
                form.add_error('image', 'Image upload failed.')
    else:
        form = ProductForm()

    return render(request, 'your_template.html', {'form': form})
