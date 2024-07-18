"""Practice for Head First Python ch1 - nested list"""
def print_item (the_list, indent = False, level = 0):
    """A function to print each item in nested list, the input parameter
    the_list is a list"""
    for each_item in the_list: 
        if isinstance(each_item, list):
            print_item(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end = '')
            print(each_item)