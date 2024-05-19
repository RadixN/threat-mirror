

from django.shortcuts import render
from django.db.models import Count
from .models import ThreatData 

def index(request):
    data = ThreatData.objects.all()
    count = ThreatData.objects.values('protocol_application').annotate(count=Count('protocol_application')).order_by()
    count1 = ThreatData.objects.values('time_observation').annotate(count=Count('time_observation')).order_by()
    count2 = ThreatData.objects.values('feed_provider').annotate(count=Count('feed_provider')).order_by()
    count3 = ThreatData.objects.values('malware_name').annotate(count=Count('malware_name')).order_by()
    context = {
        'data': data,
        'count': count,
        'count1': count1,
        'count2': count2,
        'count3': count3,
    }
    return render(request, 'dashboard/index.html', context)