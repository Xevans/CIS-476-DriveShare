from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UpdateBalanceForm
from django.contrib import messages

# Create your views here.

@login_required
def wallet(request):
    return render(request, 'wallet.html')


@login_required

def wallet(request):
    if request.method == 'POST':
        balance_form = UpdateBalanceForm(request.POST, instance=request.user.profile)

        if balance_form.is_valid():
            #balance_form.save()
            messages.success(request, 'Your balance has been updated successfully')
            # do addition for user balance with the return value in request
            request.user.profile.balance += balance_form.cleaned_data['balance']
            request.user.save()
            return redirect(to='users-wallet')
        
    else:
        balance_form = UpdateBalanceForm(instance=request.user.profile)

    return render(request, 'wallet.html', {'balance_form': balance_form})


