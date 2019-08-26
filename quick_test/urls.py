from django.urls import path
from . import view1
from . import view2


urlpatterns = [
    path('view1/', view1.view_1, name='view_1'),
    path('view2/', view2.view_2, name='view_2'),
]