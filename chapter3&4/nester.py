"""Practice for Head First Python ch1 - nested list"""
import sys
def print_item (the_list, indent = False, level = 0, fn = sys.stdout):
    """A function to print each item in nested list, the input parameter
    the_list is a list"""
    for each_item in the_list: 
        if isinstance(each_item, list):
            print_item(each_item, indent, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end = '', file = fn)
            print(each_item, file = fn)