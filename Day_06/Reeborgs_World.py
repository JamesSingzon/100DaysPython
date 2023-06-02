def right_turn():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if front_is_clear():
        while front_is_clear() and not at_goal():
            move()
            if not wall_on_right() and not at_goal():
                right_turn()
    elif wall_on_right() or not front_is_clear():
        turn_left()
    

"""   
while not at_goal():
    if front_is_clear():
        move()
    elif wall_on_right():
        turn_left()
    elif wall_in_front():
        right_turn()
"""