from django.shortcuts import render, get_object_or_404, redirect
from.models import Items, Transaction
from django.contrib import messages


def index(request) :
    items=Items.objects.all()
    return render(request, "index.html",{"items" : items})

def buy(request):
    if request.method == 'POST':
        items = Items.objects.all()
        item_id = request.POST.get('item_id')
        money = int(request.POST.get('money'))
        quantity = int(request.POST.get('quantity'))
        items = get_object_or_404(Items, id=item_id)


        if money > 200:
            messages.error(request, "Maximum allowed amount is $200.")
            return redirect('index')

        try:
            item = Items.objects.get(id=item_id)
        except Items.DoesNotExist:
            messages.error(request, "Invalid item ID.")
            return redirect('index')

        total_cost = item.price * quantity

        if quantity > item.quantity:
            messages.error(request, "Not enough quantity available.")
            return redirect('index')

        if money < total_cost:
            messages.error(request, "Insufficient funds.")
            return redirect('index')

        item.quantity -= quantity
        item.save()

        change = round(money - total_cost, 2)

        Transaction.objects.create(
            item_name=item,
            quantity=quantity,
            money_inserted=money,
            total_cost=total_cost,
            change=change
        )

        return redirect('success', item_id=item.id, quantity=quantity, total=total_cost, change=change)

    return redirect('index')


def success(request, item_id, quantity, total, change):
    item = get_object_or_404(Items, id=item_id)
    return render(request, 'success.html', {
        'item': item,
        'quantity': quantity,
        'total': total,
        'change': change
    })
