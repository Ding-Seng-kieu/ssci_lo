from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import ChoiceInfo

def choose_first(request):
    """第一级选项"""

    firsts = ChoiceInfo.objects.filter(belong_to=None)

    f_lists = [{"f_id":type_first_choice.id, "f_name":type_first_choice.name}
              for type_first_choice in firsts]
    f_info = {"f_lists":f_lists}

    return JsonResponse(f_info, safe=False)

def choose_second(request):
    """第二级选项"""

    f_id = request.GET.get('f_id')
    print(p_id, '--------')
    seconds = ChoiceInfo.objects.filter(belong_to=f_id)
    s_lists = [{"s_id":type_second_choice.id, "s_name":type_second_choice.name}
               for type_second_choice in seconds]
    print(s_lists[0:5])
    s_info = {"s_lists":s_lists}

    return JsonResponse(s_info, safe=False)