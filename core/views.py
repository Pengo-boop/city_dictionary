from django.shortcuts import render

# Create your views here.
def main(request):
    cities = ['Moscow', 'Toronto', 'Saint Petersburg', 'Vancouver']
    return render(request, 'main.html', {'cities': cities})
    
