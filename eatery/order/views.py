from django.shortcuts import render

def home_page(request):

    if request.method == 'POST':
        dish = request.POST.get('dish')
        address = request.POST.get("address")

        return render(request, 'order/home_page.html', {'dish': dish, 'address': address})

    return render(request, 'order/home_page.html')