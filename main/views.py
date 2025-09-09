from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Goalified',
        'name': '2406408224 - Nadine Aisyah Putri Maharani',
        'class_name': 'PBP F'
    }
    return render(request, 'main/main.html', context)
