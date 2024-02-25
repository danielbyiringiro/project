graph = {"1":["5","6"],
         "2":["1","3","1","4","5"],
         "3":["4","8"],
         "4":["6"],
         "5":["6"],
         "6":[],
         "7":["3","4","6"],
         "8":["4"],
         }
def has_no_source(graph):
    values = graph.values()
    keys = graph.keys()

    values_list = [item for sublist in values for item in sublist]
    #print(values_list)
    no_source = [node for node in keys if node not in values_list]
    #print(no_source)
    return no_source
print(has_no_source(graph))