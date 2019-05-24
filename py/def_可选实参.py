def name_add(first_name,last_name,mid_name='',):
    if mid_name:
        print(first_name+' '+mid_name+' '+last_name)
    else:
        print(first_name+' '+last_name)
        
name_add('李','明')