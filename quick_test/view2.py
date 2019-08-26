from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


def in_group_2(user):
    return user.groups.filter(name="Group 2").exists()


@user_passes_test(in_group_2)
def view_2(request):
    return HttpResponse("This is View 2")
