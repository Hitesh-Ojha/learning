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

def list_to_num(index): 
    return list_of_relationships[index]

num_of_relation = [(data["id"], list_to_num(data["id"])) for data in data ] 

print("Number of relationships for each person:", num_of_relation) 

""" 
### What I learned here? 
1. I learned how to create a list of dictionaries to represent data and relationships between entities.
2. I learned how to iterate through a list of relationships and update the corresponding entries in the
    data list.  
3. I learned how to calculate the mean of a list of values and print it. 
4. I learned how to create a function that takes an index and returns the corresponding value from a list.

### well that all about python , think of each person as a node in a graph and the relationships as edges connecting those nodes
each person has a list of relationships that represent the connections to other people in the graph. 
what if a node is a network replecting a social media platform and the relationships are the connections between users or a party
there are many ways to represent and analyze relationships in a graph, such as using adjacency lists or matrices, and applying algorithms to find shortest paths, clusters, or communities within the network.
"""

def friends_of_friends(index):
    friends = data[index]["relationship"]
    friends_of_friends_set = set()
    
    for friend in friends:
        friends_of_friends_set.update(data[friend]["relationship"])
    
    return list(friends_of_friends_set)

for i in range(len(data)):
    fof = friends_of_friends(i)
    print(f"Friends of friends for {data[i]['name']} (ID: {data[i]['id']}): {fof}") 
