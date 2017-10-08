from .luis_sdk import LUISClient


class Luis:
    def process_res(res):
        '''
        A function that processes the luis_response object and prints info from it.
        :param res: A LUISResponse object containing the response data.
        :return: None
        '''
        print('---------------------------------------------')
        print('LUIS Response: ')
        print('Query: ' + res.get_query())
        print('Top Scoring Intent: ' + res.get_top_intent().get_name())

        if res.get_dialog() is not None:
            if res.get_dialog().get_prompt() is None:
                print('Dialog Prompt: None')
            else:
                print('Dialog Prompt: ' + res.get_dialog().get_prompt())
            if res.get_dialog().get_parameter_name() is None:
                print('Dialog Parameter: None')
            else:
                print('Dialog Parameter Name: ' + res.get_dialog().get_parameter_name())
                print('Dialog Status: ' + res.get_dialog().get_status())
            print('Entities:')
        city = []    
        for entity in res.get_entities():
            print('"%s":' % entity.get_name())
            print('Type: %s, Score: %s' % (entity.get_type(), entity.get_score()))
            city.append(entity.get_name())
        print(city)
        return city    
    
    def get_city(text):
        try:
            APPID = 'c7b9e5ea-36f3-41e0-b0fe-50d241acffb6'
            APPKEY = '5af969e342f54abeaad0cfdb5145b3a5'
            #TEXT = input('Please input the text to predict:\n')
            CLIENT = LUISClient(APPID, APPKEY, True)
            res = CLIENT.predict(text)
            while res.get_dialog() is not None and not res.get_dialog().is_finished():
                TEXT = input('%s\n'%res.get_dialog().get_prompt())
                res = CLIENT.reply(TEXT, res)
            data = Luis.process_res(res)
            return data

        except Exception as exc:
            print(exc)
     
     
     
