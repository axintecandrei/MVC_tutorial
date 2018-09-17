import basic_backend
import mvc_exceptions as mvc_exc

class Model():
    def __init__(self, application_items):
        self._item_type = 'Week Food Scheduler'
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    '''
    Next methods should be an exact copy as
    the funtions from basic_backend
    
    But for lasiness reasson I just used the 
    function from that module
    
    If for futher want to update this class
    methods with the content of basic_backend
    functions remember to add a list that 
    will hold the week days
    
    self.week_prog = []
    '''

    def create_item(self,day, food_cat,food_type, quantity):
        basic_backend.create_item(day, food_cat,food_type, quantity)

    def create_items(self, week_prog):
        basic_backend.create_items(week_prog)

    def read_item(self, day):
        return basic_backend.read_item(day)

    def read_items(self):
        return basic_backend.read_items()

    def update_item(self, day, food_cat,food_type, quantity):
        basic_backend.update_item(day, food_cat,food_type, quantity)

    def delete_item(self, day):
        basic_backend.delete_item(day)
