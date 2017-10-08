import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import json
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .module.date import Date as Date
from .module.qpx import Qpx as Qpx
from .module.crawler import City as City
from .module.luis import Luis as Luis
from .module.pixnet import Pixnet as Pixnet 
#from .module.link import Link as Link
#from sympy.abc import u, t, x, y, z
class Main:
    def get_flight(text):
        luis_get_city = Luis.get_city(text)
        city_from = luis_get_city[0]
        city_to = luis_get_city[1]
        try:
            date = luis_get_city[2]
        except:
            date = time.strftime("%Y-%m-%d", time.localtime())
        date_format = Date.date_format(date)
        get_city_index = City.get_city_index(city_from, city_to)
        city_from_index = get_city_index[0]
        city_to_index = get_city_index[1]
        flight = Qpx.get_flight(city_from_index, city_to_index, date_format)
        city_url = City.get_city_url(city_to_index )
        #pixnet_url = Pixnet.get_url('city_to_index')
        
        data = '' 
        for row in flight[0][1:]:
            data = data + row
        return data, city_url  


#main = Main 
# Create your views here.

class bot(generic.View):
    def get(self, request, *args, **kwargs):
        verify_code = 'webhook'
        verify_token = request.GET.get('hub.verify_token')
        if verify_code == verify_token:
            return HttpResponse(request.GET.get('hub.challenge'))
        else:
            return HttpResponse('False')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        message = json.loads(self.request.body.decode('utf-8'))
        for row in message['entry']:
            messagings = row['messaging']
            for message in messagings:
                sender_id = message['sender']['id']
                recipient_id = message['recipient']['id']

                try:
                    if message.get('message'):
                        text = message['message']['text']
                        try:
                            data = Main.get_flight(text)
                            ticket = data[0]
                            city_url = data[1]
                            #post_facebook_message(sender_id, ticket, 'https://www.skyscanner.com.tw/', '訂票') 
                            post_facebook_message(sender_id, ticket, city_url, '痞客邦') 
                        except:
                            post_facebook_message(sender_id, '查無結果', 'https://www.facebook.com/smart.flight.tw/', 'Smart Flight')
                except:
                    post_facebook_message(sender_id, '謝謝！', 'https://www.facebook.com/smart.flight.tw/', 'Smart Flight')
        return HttpResponse()

def post_facebook_message(sender_id, text, url, title):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAABo9jWFW8MBAGflGwmX9xI0kaLGsW8edHfaZCgLbgZBIibL8pqB3UOKtoRZCg7r5jZCSXtMxSHZBW0rlzHOEk6UZAhPUG4ZBoZA5YmVm5fYKNPbOZC9tL1V8QyL48eaElPakp1Y1KqrCeovITXpE3ZCbwmefxjtGWAWhR1UwG3pwlrzZBZAeb8yDZCY7'
    response_msg = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            'attachment':{
                'type':'template',
                'payload':{
                    "template_type":"button",
                    "text": text, 
                    "buttons":[
                        {
                            "type":"web_url",
                            "url": url, 
                            "title": title,
                        },
                    ]
                }
            }
        }
    })
    status = requests.post(
        post_message_url,
        headers={"Content-Type": "application/json"},
        data=response_msg)
    print(status.json())

