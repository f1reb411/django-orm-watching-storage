from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):

    this_passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits_by_passcard = Visit.objects.filter(passcard=this_passcard)
    all_visits_this_passcard = []

    for visit in visits_by_passcard:
        duration = get_duration(visit)
        readable_duration = format_duration(duration)
        is_strange = is_visit_long(visit)
        this_passcard_visits = {
                'entered_at': visit.entered_at,
                'duration': readable_duration,
                'is_strange': is_strange
            }

        all_visits_this_passcard.append(this_passcard_visits)
    context = {
        'passcard': this_passcard,
        'this_passcard_visits': all_visits_this_passcard
    }
    return render(request, 'passcard_info.html', context)
