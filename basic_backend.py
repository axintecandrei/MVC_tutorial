import mvc_exceptions as mvc_exc

week_prog = list()  # global variable where we keep the data


def create_item(day, food_cat,food_type, quantity):
    global week_prog
    results = list(filter(lambda x: x['Day'] == day, week_prog))
    if results:
        raise mvc_exc.DayAlreadyStored('"{}" already stored!'.format(day))
    else:
        week_prog.append({'Day': day, 'Food Category': food_cat, "Food Type": food_type, 'Quantity': quantity})


def create_items(app_week_prog):
    global week_prog
    week_prog = app_week_prog


def read_item(day):
    global week_prog
    return_certain_day = list(filter(lambda x: x['Day'] == day, week_prog))
    if return_certain_day:
        return return_certain_day[0]
    else:
        raise mvc_exc.DayNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(day))


def read_items():
    global week_prog
    return [day for day in week_prog]

def update_item(day, food_cat,food_type, quantity):
    global week_prog
    idxs_day = list(filter(lambda i_x: i_x[1]['Day'] == day, enumerate(week_prog)))
    if idxs_day:
        day_idx_to_update, day_to_update = idxs_day[0][0], idxs_day[0][1]
        week_prog[day_idx_to_update] = {'Day': day, 'Food Category': food_cat, "Food Type": food_type, 'Quantity': quantity}
    else:
        raise mvc_exc.DayNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(day))
def delete_item(day):
    global week_prog
    idxs_day = list(filter(lambda i_x: i_x[1]['Day'] == day, enumerate(week_prog)))
    if idxs_day:
        day_idx_to_delete, day_to_delete = idxs_day[0][0], idxs_day[0][1]
        del week_prog[day_idx_to_delete]
    else:
        raise mvc_exc.DayNotStored(
            'Can\'t delete "{}" because it\'s not stored'.format(day))
def main():
    '''
    global week_prog
    create_item("Monday","P","Pui", 500)
    create_item("Thursday", "A", "Naut", 200)
    print(read_items())
    update_item("Monday", "C","Pizza", 250)
    print(read_items())
    delete_item("Thursday")
    print(read_items())
    '''
    pass


