from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


def in_group_1(user):
    return user.groups.filter(name="Group 1").exists()


@user_passes_test(in_group_1)
def view_1(request):
    return HttpResponse("This is View 1")
