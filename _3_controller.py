import mvc_exceptions as mvc_exc

class Controller():

    def __init__(self, model, view):
        self.model = model
        self.view  = view

    def show_items(self, bullet_points =False):
        items = self.model.read_items()
        item_type = self.model.item_type
        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            self.view.show_number_point_list(item_type,items)

    def show_item(self, item_name):
        try:
            item = self.model.read_item(item_name)
            self.view.show_item(item_name, item)
        except mvc_exc.DayNotStored as e:
            self.view.display_missing_item_error(item_name, e)

    def insert_item(self, day, food_cat, food_tpe, quantity):
        assert quantity > 0
        item_type = self.model.item_type

        try:
            self.model.create_item(day, food_cat, food_tpe, quantity)
            self.view.display_item_stored(day, item_type)
        except mvc_exc.DayAlreadyStored as e:
            self.view.display_item_already_stored_error(day, item_type,e)

    def update_item(self, day, food_cat, food_tpe, quantity):
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type

        try:
            older = self.model.read_item(day)
            self.model.update_item(day, food_cat, food_tpe, quantity)
            self.view.display_item_updated(
                day, older['Food Category'],older['Food Type'],older['Quantity'], food_cat,food_tpe, quantity)
        except mvc_exc.DayNotStored as e:
            self.view.display_item_not_yet_stored_error(day, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

    def delete_item(self, name):
        item_type = self.model.item_type
        try:
            self.model.delete_item(name)
            self.view.display_item_deletion(name)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)