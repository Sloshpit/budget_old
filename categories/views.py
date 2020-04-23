from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum
from transactions.models import Transaction
from .models import Category

#def index(request):
#    show_categories = Category.objects.all()
#   output = ', '.join[c.category for c in show_categories]
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    show_categories = Category.objects.all()
    show_transactions = Transaction.objects.all()
    template = loader.get_template('categories/index.html')
    total = Transaction.objects.all().aggregate(sum=Sum('amount'))['sum'] or 0.00
    total = "{:.2f}".format(total)

    context = {
        'show_categories': show_categories,
        'show_transactions':show_transactions,
        'total': total,
    }
    return HttpResponse(template.render(context, request))
    