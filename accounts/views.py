from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum
from .models import Account


def index(request):
    template = loader.get_template('accounts/index.html')
    show_accounts = Account.objects.all()
    card_total_object = Account.objects.filter(account_name__contains="Westjet").values('balance')
    card_total = card_total_object[0]['balance']
    other_account_total = Account.objects.exclude(account_name__contains="Westjet").aggregate(sum=Sum('balance'))['sum'] or 0.00
    total = other_account_total - card_total
    context = {
        'show_accounts': show_accounts,
        'total': total    }
    return HttpResponse(template.render(context, request))