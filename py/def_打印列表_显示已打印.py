def print_modles(unprint_modles,complete_print):
    """逐个打印print_modles里面内容"""
    while unprint_modles:
        list=unprint_modles.pop()
        print(list)
        complete_print.append(list)

def show_printed(complete_print):
    #for i in complete_print:
    #    print(i)
    print(complete_print)

unprint_modles = ['1','2','3','4','5']
complete_print = []
print_modles(unprint_modles,complete_print)
show_printed(complete_print)
