from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import ChoiceInfo, AreaInfo

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
    print(f_id, '--------')
    seconds = ChoiceInfo.objects.filter(belong_to=f_id)
    s_lists = [{"s_id":type_second_choice.id, "s_name":type_second_choice.name}
               for type_second_choice in seconds]
    print(s_lists[0:5])
    s_info = {"s_lists":s_lists}

    return JsonResponse(s_info, safe=False)

###############################################################################
def choose_province(request):
    """查询省"""

    provinces = AreaInfo.objects.filter(pid=None)


    p_lists = [{"p_id": province.id, "p_name": province.name} for province in provinces]
    p_info = {"p_lists":p_lists}
    
    return JsonResponse(p_info, safe=False)


def choose_city(request):
    """查询市"""

    p_id = request.GET.get('p_id')
    print(p_id,'--------')
    citys = AreaInfo.objects.filter(pid=p_id)
    c_lists = [{"c_id": city.id, "c_name": city.name} for city in citys]
    print(c_lists[0:5])
    c_info = {"c_lists": c_lists}
    return JsonResponse(c_info, safe=False)