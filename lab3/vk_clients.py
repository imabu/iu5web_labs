from base import *
from exceptions import *
from datetime import datetime
import requests


class GettingID(BaseClient):
    v = 5.58
    user_id = None

    def __init__(self, username):
        super().__init__('https://api.vk.com/method/', 'users.get', 'GET')
        self.user_id = username

    def get_params(self):
        return {'user_ids': self.user_id, 'v': self.v}

    def _get_data(self, method, http_method):
        r = requests.get(self.generate_url(method), self.get_params())
        return self.response_handler(r)

    def _diagram(self, friends_dict):
        age_list = [0 for i in range(120)]
        today = datetime.now()
        for f in friends_dict:
            bdate_str = f.get('bdate')
            try:
                bdate = datetime.strptime(bdate_str, '%d.%m.%Y')
                days = (today-bdate).days
                age = days // 365
                age_list[age] += 1
            except:
                pass
        for i in range(120):
            if (age_list[i]>0):
                print(i,': ','#'*age_list[i])        
    
    def response_handler(self, response):
        res_dic = response.json()
        if (res_dic.get('error')!=None):
            err = res_dic.get('error')
            err_msg = err.get('error_msg')
            raise API_Exception(err_msg)            
        else:
            res_list = res_dic.get('response')
            user_dict = res_list[0]
            user_id = user_dict.get('id')
            print(user_dict.get('last_name'), user_dict.get('first_name'), sep=' ')
            get_friends = GettingFriends(user_id)
            friends_dict = get_friends.execute();
            self._diagram(friends_dict)
            return response


class GettingFriends(BaseClient):
    user_id = None
    fields = 'bdate'
    v = 5.68
    
    def __init__(self, user_id):
        super().__init__('https://api.vk.com/method/', 'friends.get', 'GET')
        self.user_id = user_id
        
    def get_params(self):
        return {'user_id': self.user_id, 'v': self.v, 'fields': self.fields}

    def _get_data(self, method, http_method):
        r = requests.get(self.generate_url(method), self.get_params())        
        return self.response_handler(r)
    def response_handler(self, response):
        res_dic = response.json()
        if (res_dic.get('error')!=None):
            err = res_dic.get('error')
            err_msg = err.get('error_msg')
            raise API_Exception(err_msg)            
        else:
            return res_dic.get('response').get('items')


