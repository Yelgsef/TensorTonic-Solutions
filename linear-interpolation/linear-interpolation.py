def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    size = len(values)
    v_left = [0] * size 
    pos_left = [0] * size
    v_right = [0] * size 
    pos_right = [0] * size
    
    v_left[0] = values[0]
    v_right[-1] = values[-1]

    last = v_left[0]
    last_pos = 0 
    for i in range(0, size):
        if values[i] is None: 
            v_left[i] = last 
            pos_left[i] = last_pos
        else: 
            v_left[i] = values[i]
            pos_left[i] = i 
            last = v_left[i]
            last_pos = i 

    last = v_right[-1]
    last_pos = size - 1
    print(v_left)
    print(pos_left)
    for i in range(size - 1, -1, -1):
        if values[i] is None: 
            v_right[i] = last 
            pos_right[i] = last_pos
        else: 
            v_right[i] = values[i]
            pos_right[i] = i 
            last = v_right[i]
            last_pos = i 

    # print(v_right)
    # print(pos_right)
    for i in range(1, size - 1):
        if values[i] is None: 
            values[i] = v_left[i - 1] + (i - pos_left[i - 1]) / (pos_right[i + 1] - pos_left[i - 1]) * (v_right[i + 1] - v_left[i - 1])
        # print("I got here")
    return values