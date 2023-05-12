import requests


class Bored:
    def __init__(self) -> None:
        self.url = 'http://www.boredapi.com/api/'

    def get_activity(self) -> str:
        '''get activity from bored
        
        Returns:
            str: text of activity
        '''
        url = f'{self.url}activity/'
        r = requests.get(url)

        if r.status_code == 200: return r.json()
        else: return False

    def get_activity_by_type(self, type: str) -> dict:
        '''get activity by type

        Note:
            Type of the activity: ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
        
        Args:
            type (str): type
        
        Returns:
            dict: activity data
        '''
        url = f'{self.url}activity/'

        payoad = {
            'type': type
        }
        r = requests.get(url,params=payoad)

        if r.status_code == 200: return r.json()
        else: return False

    def get_activity_by_id(self, key: int) -> dict:
        '''get activity by key

        Note:
            A unique numeric id: [1000000, ..., 9999999]
        
        Args:
            key (int): key
        
        Returns:
            dict: activity data
        '''
        pass

    def get_activity_by_accessibility(self, accessibility: float) -> dict:
        '''get activity by accessibility

        Note:
            A factor describing how possible an event is to do with zero being the most accessible
            [0.0, ..., 1.0]
        
        Args:
            accessibility (float): accessibility
        
        Returns:
            dict: activity data
        '''
        pass

    def get_activity_by_price(self, price: float) -> dict:
        '''get activity by price

        Note:
            A factor describing the cost of the event with zero being free
            [0, 1]
        
        Args:
            price (float): price
        
        Returns:
            dict: activity data
        '''
        pass

    def get_activity_by_price_range(self, minprice: float, maxprice: float) -> dict:
        '''get activity by price

        Note:
            A factor describing the cost of the event with zero being free
            [0, 1]
        
        Args:
            minprice (float): min price
            maxprice (float): max price
        
        Returns:
            dict: activity data
        '''
        pass
    



bpred = Bored()
print(bpred.get_activity_by_type('social'))