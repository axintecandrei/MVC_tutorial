import _1_model as M
import _2_view as V
import _3_controller as C

if __name__ == '__main__':
    week_program = []
    c = C.Controller(M.Model(week_program), V.View())
    c.insert_item("Monday","P","Pui", 500)
    c.insert_item("Thursday", "A", "Naut", 200)

    #c.show_items(bullet_points=True)
    c.show_item('Monday')
