from django.shortcuts import render

def shop_index(request):
    template_name = "shop/home_template.html"
    return render(request,template_name)