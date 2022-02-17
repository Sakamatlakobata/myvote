from django.shortcuts import render
from django.urls import is_valid_path
from .forms import GetBillForm


# form to get bill
def bill_get(request):

    if request.method == "POST":
        form = GetBillForm(request.POST)
        if form.is_valid():
            # print("bill_name is", form.cleaned_data['bill_name'])
            return render(request, 'bill_vote/bill_list.html', {'formdata':form.cleaned_data})

    context = { 'form' : GetBillForm() }
    return render(request, 'bill_vote/bill_get.html', context)


# # display bill found in get_bill
# def display_bill(request):
#     context={'bill_selected':'Bill 101'}
#     return render(request, 'bill_vote/display_bill.html', context)

