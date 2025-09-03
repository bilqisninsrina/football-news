from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406432141',
        'name': 'Bilqis Nisrina Dzahabiyah Mulyadi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
