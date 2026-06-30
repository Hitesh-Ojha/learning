from itertools import count


data = [
    {"id" : 0 , "name" : "Pro"},
    {"id" : 1,  "name" : "king"},
    {"id" : 2 , "name" : "bong"},
    {"id" : 3 , "name" : "gong"},
    {"id" : 4 , "name" : "don"},
    {"id" : 5 , "name" : "gone"},
    {"id" : 6 , "name" : "found"},
    {"id" : 7 , "name" : "the"},
    {"id" : 8, "name" : "hero"},
    {"id" : 9 , "name" : "last"} ]

relationship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for i in data: 
    i["relationship"] = [] 


for i, j in relationship:
    data[i]["relationship"].append(j)
    data[j]["relationship"].append(i) 

list_of_relationships = [] 
for i in range(len(data)):
    count = len(data[i]["relationship"])
    list_of_relationships.append(count) 

mean = sum(list_of_relationships) / len(list_of_relationships) 
print("Mean of relationships:", mean) 

