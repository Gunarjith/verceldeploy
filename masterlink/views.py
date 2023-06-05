from django.http import HttpResponse
from django.http import HttpResponse
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import uuid
reference_id = uuid.uuid4()


def login(request):

    url = "https://test.cashfree.com/api/v1/order/create"

    payload = {
        "appid": "TEST3931154d6e90b54bfbc3b4946d511393",
        "secretKey": "TEST701a10a8d7389d719903c77dda9fa993fbc0db63",
        "orderId": reference_id,
        "orderAmount": "1",
        "orderCurrency": "INR",
        "oderNote": "pay",
        "customerName": "mohan",
        "customerEmail": "abcd@gmail.com",
        "customerPhone": "8494863493",
        # "returnUrl": "https://cashfree.com",

         "notifyUrl": "https://verceldeploy-h3tim9s0e-gunarjith.vercel.app/payment_info/",
    }
    headers={
        'content_type':'application/json'
    }

    response = requests.request("POST", url, data=payload,headers=headers)
    print(response.text)

    return render(request,'home.html',{"response":response.text})


def payment_info(request):
    print(request.data)
    if request.method == 'POST':
        # Fetch the payment response details from the request
        order_id = request.POST.get('order_id')
        payment_status = request.POST.get('payment_status')
        print(order_id)
        print(payment_status)
    return None



