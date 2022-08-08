from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree

# Create your views here.


# configuring the braintree
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="3ph8zqnjrttsk3z9",
        public_key="y9jfsmg2sgmrkbrt",
        private_key="f9badcafa42c9242224a11185b005bd8"
    )
)


# to check if the user is login
def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


# sending the token
@csrf_exempt
def generate_token(request,id, token):
    if not validate_user_session(id, token):
        return JsonResponse({
            "error":"Invalid session please login again"
        })

    return JsonResponse({'client_token': gateway.client_token.generate(),"success":True})




# receiving information about what the client bought 
# and sending it to the briantree server

@csrf_exempt
def process_payment(request,id, token):
    if not validate_user_session(id, token):
        return JsonResponse({
            "error":"Invalid session please login again"
        })

    nonce_from_the_client = request.POST['paymentMethodNonce']
    amount_from_the_client = request.POST['amount']


    result = gateway.transaction.sale({
        "amount":amount_from_the_client,
        "payment_method_nonce":nonce_from_the_client,
         "options": {
      "submit_for_settlement": True
    }
    })


    if result.is_success:
        return JsonResponse({
            "success":result.is_success,
            'transaction':{
                'id':result.transaction.id,
                'amount':result.transaction.amount,
            }
        })
    else:
        return JsonResponse({
            'error': True,
            'success':False

        })