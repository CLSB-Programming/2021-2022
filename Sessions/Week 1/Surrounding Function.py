def surrounding(cp_x, cp_y, output_array, destination):
    #Checks all 8 surrounding blocks from cp
    #Creates a weight for all 8, to be compared
    for i in range(9):
        if i == 0:
            try:
                optionx = cp_x - 1
                optiony = cp_y - 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        elif i == 1:
            try:
                optionx = cp_x
                optiony = cp_y + 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        elif i == 2:
            try:
                optionx = cp_x + 1
                optiony = cp_y + 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        elif i == 3:
            try:
                optionx = cp_x - 1
                optiony = cp_y
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        elif i == 4:
            try:
                optionx = cp_x + 1
                optiony = cp_y
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        elif i == 5:
            try:
                optionx = cp_x - 1
                optiony = cp_y - 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        elif i == 6:
            try:
                optionx = cp_x
                optiony = cp_y - 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        elif i == 7:
            try:
                optionx = cp_x + 1
                optiony = cp_y - 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        elif i == 8:
            try:
                optionx = cp_x - 1
                optiony = cp_y + 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except:
                pass
        try:
            if bp.index(option) != -1: #Checks whether position is a blocked position
                pass
        except:
            try:
                if destination == "fp":
                    if checked.index(option) != -1: #Checks whether position is already checked
                        pass
                else:
                    if direct_checked.index(option) != -1:
                        pass
            except:
                if ((option[0] > -1) and (option[0] < x_length)) and ((option[1] > -1) and (option[1] < y_length)): # Prevents an odd event, where the pathfinder goes around the edges of the screen, going into index values of -1 somehow
                    #This calculates the weight of a node, dependent on the distance from both the 
                    #Starting Point and Finishing Point, using Pythagorus' Theorem
                    spd = (( (sp["x"]*10 - optionx*10)**2 + (sp["y"]*10 - optiony*10)**2 )** 0.5)
                    fpd = (( (fp["x"]*10 - optionx*10)**2 + (fp["y"]*10 - optiony*10)**2 )** 0.5)
                    if destination == "fp":
                        fpd *= 10
                    else:
                        spd *= 10
                    weight = spd + fpd
                    if destination == "fp":
                        if (optionx == fp["x"]) and (optiony == fp["y"]):
                            weight = 0
                    else:
                        if (optionx == sp["x"]) and (optiony == sp["y"]):
                            weight = 0
                    weights.append([weight, optionx, optiony])
                    output_array.append(option)


    """
    KEY
    ---
    lowest[0] = weight
    lowest[1] = index

    weights[i][0] = weight
    weights[i][1] = x
    weights[i][2] = y
    """

    lowest = [0,0]
    for i in range(len(weights)):
        print(weights[lowest[1]])
        if i == 0:
            lowest[0] = weights[i][0]
            lowest[1] = i
        if weights[i][0] == 0:
            lowest[0] = weights[i][0]
            lowest[1] = i
        try:
            if destination == "fp":
                if weights[i][0] <= lowest[0]:
                    lowest[0] = weights[i][0]
                    lowest[1] = i
            else:
                try:
                    if path.index(weights[i]) == -1:
                        pass
                except:
                    lowest[0] = weights[i][0]
                    lowest[1] = i
        except:
            pass
    try:
        if destination == "fp":
            path.append([weights[lowest[1]][1], weights[lowest[1]][2]])
        cp_x = weights[lowest[1]][1]
        cp_y = weights[lowest[1]][2]
        del weights[lowest[1]]
        print(cp_x, cp_y)
        return cp_x, cp_y
    except:
        print("No possible path found")
        possible = False
        endgame()
        return
