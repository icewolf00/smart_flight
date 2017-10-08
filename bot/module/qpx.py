import json
import requests

class Qpx:
    def get_flight(city_from_index, city_to_index, date):
        data = Qpx.get_flight_max(city_from_index, city_to_index, date, 1)
        return data

    def get_flight_max(city_from_index, city_to_index, date, solution):
        N = solution
        api_key = 'AIzaSyAyJQ81tqKIsYZOGeordKOBh22VFPgqVHo'
        url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
        headers = {'content-type': 'application/json'}
        params = {
            "request": {
                "slice": [{
                    "origin": city_from_index,
                    "destination": city_to_index,
                    "date": date, #"2017-09-08"
                }],
                "passengers": {
                    "adultCount": 1
                },
                "solutions": N,
                "refundable": False
            }
        }

        response = requests.post(url, data=json.dumps(params), headers=headers)
        data = response.json()
        city_to = city_to_index 
        city_from = city_from_index 
        aircraft = data['trips']['data']['aircraft'][0]['name']
        carrier = data['trips']['data']['carrier'][0]['name']
        ticket = [[] * N for row in range(N)]
        for i in range(N):
            sale_total = data['trips']['tripOption'][i]['saleTotal']
            duration = data['trips']['tripOption'][i]['slice'][0]['duration']
            time_arrival = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['leg'][0]['arrivalTime']
            time_departure = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['leg'][0]['departureTime']
            mileage = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['leg'][0]['mileage']
            sale_total = data['trips']['tripOption'][i]['saleTotal']
            ticket[i].append(carrier)
            ticket[i].append('\nDeparture City : ' + city_from)
            ticket[i].append('\nArrival City : ' + city_to)
            ticket[i].append('\nAircraft : ' + aircraft)
            ticket[i].append('\nAirline : ' + carrier)
            ticket[i].append('\nTime Departure : ' + time_departure)
            ticket[i].append('\nTime Arrival : ' + time_arrival)
            ticket[i].append('\nDuration : %s' % (str(duration)))
            ticket[i].append('\nMileage : %s' % (str(mileage)))
            ticket[i].append('\nPrice : ' + sale_total)
 
        return ticket
            
#city_from = input()
#city_to = input()
#date = '2017-12-12'
#print(Qpx.get_flight_max(city_from, city_to, date, 5))
