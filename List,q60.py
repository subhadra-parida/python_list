string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
def n(string_list):
    i=0
    new_list=[]
    while i<len(string_list):
        if string_list[i] not in new_list:
            new_list.append(string_list[i])
        i=i+1
    print(new_list)
n(string_list)