from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Goalified',
        'name': 'Nadine Aisyah',
        'class_name': 'PBP F'
    }
    return render(request, 'main/main.html', context)
