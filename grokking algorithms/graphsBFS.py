#breadth-first search algorithm
# este algoritmo permite identificar la ruta mas corta a un nodo y si ese nodo existe
from collections import deque
search_queue = deque() #creates a new queue
def personIsFriend(name): #define if person is friend
    return name[-1] == 'l'

graph = {}
graph["Me"] = ["Brittany", "Mario", "Katiana", "Maria Paula"]
graph["Mario"] = ["Daniel", "Garita", "Brandon",  "Henry", "Brayan"]
graph["Brittany"] = ["Julio", "Seydi", "Rogelio", "Lucy"]
graph["Lucy"] = ["Rogelio", "Me", "Brittany"]
graph["Rogelio"] = ["Lucy", "Me", "Brittany"]
graph["Katiana"]=["Henry"]
graph["Maria Paula"]=["Josue"]
graph["Brayan"] = []
graph["Brandon"] = []
graph["Henry"] = []
graph["Daniel"] = []
graph["Julio"] = []
graph["Seydi"] = []
graph["Garita"] = []

def search(name):
    search_queue = deque() #creates a new queue
    search_queue += graph[name]#adds all of your out neighbors to the search queue
    searched = set()
    while search_queue:
            person = search_queue.popleft() #grabs first person and off the queue 
            if not person in searched:
                if personIsFriend(person):
                    print(f"El individuo {person} es mi amigo")
                    return True
                else:
                    search_queue+=graph[person]
                    searched.add(person)
    return False

search("Me")
    
