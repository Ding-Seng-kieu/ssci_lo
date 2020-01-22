from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from .models import ChoiceInfo, Position


def choose_first(request):
    """第一级选项"""

    firsts = ChoiceInfo.objects.filter(belong_to=None)


    f_lists = [{"f_id": first.id, "f_name": first.name} for first in firsts]
    f_info = {"f_lists":f_lists}
    
    return JsonResponse(f_info, safe=False)


def choose_second(request):
    """第二级选项"""

    f_id = request.GET.get('f_id')
    #print(f_id,'--------')
    seconds = ChoiceInfo.objects.filter(belong_to=f_id)
    s_lists = [{"s_id": second.id, "s_name": second.name} for second in seconds]
    #print(s_lists[0:5])
    s_info = {"s_lists": s_lists}
    return JsonResponse(s_info, safe=False)


def position_list(request):
    """地名列表"""

    context = {}
    context['positions'] = Position.objects.all()

    return render(request, 'position_list.html', context)

def position_detail(request, number):
    """地名详情"""

    context = {}
    context['position'] = get_object_or_404(Position, id = number)

    return render(request, 'position_detail.html', context)