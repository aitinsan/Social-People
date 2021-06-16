from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse


@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminPanelView(request):
    context = {

    }

    return render(request, 'admin_panel/admin-panel.html', context=context)