# --coding:utf-8--

bDrawed = False

def PaintAroundCell():
    move_down()
    paint()
    move_up()
    move_up()
    paint()
    move_down()
    move_left()
    paint()
    move_right()
    move_right()
    paint()

for i in range(5):
    for j in range(5):
        if i % 2 == 0 and is_free_right():
            move_right()
        elif is_free_left():
            move_left()
        if is_cell_painted() and not bDrawed:
            PaintAroundCell()
            bDrawed = True
    if is_free_up():
        move_up()

if is_free_right():
    move_right()        
