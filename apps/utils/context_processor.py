from apps.models import Address, Jobs


def regions(request):
    return {
        'regions': Address.objects.all(),
    }


def jobs(request):
    return {
        'jobs': Jobs.objects.all(),
    }
