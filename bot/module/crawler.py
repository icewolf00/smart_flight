import csv

class City:
    def get_city_index(city_from, city_to):
        city_from = city_from.lower()
        city_to = city_to.lower()
        print(city_from, city_to)
        with open('city2.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            city_from_index = ''
            city_to_index = ''
            for row in reader:
                if row['cht'] == city_from:  
                    city_from_index = row['code']
                if row['cht'] == city_to:
                    city_to_index = row['code']
        return city_from_index, city_to_index            

    def get_city_url(city_to_index):
        with open('city_url.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = ''
            for row in reader:
                if row['city'] == city_to_index:
                    data = row['url']
        if len(data) != 0:
            return data
        else:
            return 'https://www.facebook.com/smart.flight.tw/'



