from django.conf import settings
from django.core.mail import send_mail
import requests



def send_order_email(order_email):
    try:
        subject = 'A new Product'
        message = f'Hi Admin, a new order from {order_email}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail( subject, message, email_from, recipient_list )
        print(f"{order_email} order email sent")
    except Exception as e:
        print(e.args)

secret_key = "sk_test_a46784ba9bf4fe706549a6d103c42f5cc5437eed"


def InitPaystack(email,amount):
    try:
        headers = {
                'Authorization': f'Bearer {secret_key}',
                'Content-Type': 'application/json'
            }
        payload = {
            "email": email,
            "amount": str(amount * 100)
            }
        
        url="https://api.paystack.co/transaction/initialize"

        response = requests.post(url,headers=headers,json=payload)
        if response.status_code == 200:
            data = response.json()['data']
            pay_url = data['authorization_url']
            print(pay_url)
            reference = data['reference']
            return {
                "url":pay_url,
                "reference":reference
            }
        return {
                "url":None,
                "message":"error occured"
            }
    except Exception as e:
        print(e.args)
        return {
                "url":None,
                "message":"error occured"
            }