from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Goalified',
        'name': 'Nadine Aisyah',
        'class_name': 'Kelas PBP'
    }
    return render(request, 'main/main.html', context)
