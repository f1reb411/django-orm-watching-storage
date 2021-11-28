from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):

    not_leaved = Visit.objects.filter(leaved_at=None)
    people_in_storage = []

    for person in not_leaved:
        duration = get_duration(person)
        readable_duration = format_duration(duration)
        is_strange = is_visit_long(person)
        non_closed_visits = {
                'who_entered': person.passcard.owner_name,
                'entered_at': person.entered_at,
                'duration': readable_duration,
                'is_strange': is_strange
                }
        people_in_storage.append(non_closed_visits)

    context = {
        'non_closed_visits': people_in_storage,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
