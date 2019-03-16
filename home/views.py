from django.conf import settings
from django.shortcuts import render


def home(request):
    return render(request, settings.BASE_DIR + '/vue-cli/dist/index.html')
