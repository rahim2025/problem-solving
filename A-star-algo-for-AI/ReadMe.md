PROBLEM SCENARIO                                           CO1
On holiday, a flight  currently wants to travel to Bucharest from Arad. But there is no direct way to Bucharest from Arad. However, the cities are connected with each other like a graph. The distance between the connected cities are given. The flight wants to travel through the most optimal way. To find the optimal path to travel, another information is provided: the straight line distance between any city and the final destination (Bucharest). 
Now apply A* search to determine the most optimal value for the route Arad to Bucharest and help the flight. You have to use the straight line distance as the heuristic value for the cities.

INPUTS
Your txt file should take each node followed by each destination it can reach and their corresponding distance and heuristics. You are to read the file then ask the user to input the starting and the destination point.

OUTPUTS
The output will contain the total distance from the starting point to the destination followed by printing the nodes it followed to calculate the distance.


SAMPLE INPUT
In the text file:

Arad 366 Zerind 75 Sibiu 140 Timisoara 118
Zerind 374 Arad 75 Oradea 71
Oradea 380 Zerind 71 Sibiu 151
... ... ... ... ... ...
Bucharest 0 Pitesti 101 Fagaras 211 Giurgiu 90 Urziceni 85
Giurgiu 77 Bucharest 90
... ... ... ... ... …

The text file is arranged as follows:

Each line starts with a node followed by the heuristic of that node
Then the neighboring nodes and the distance from the parent node is given as a pair
All neighboring city-distance pairs are listed after the heuristic.

For example, the text file starts with Arad which has a heuristic of 366. It is the parent node to Zerind, Sibiu and Timisoara which are 75, 140 and 118 km away from Arad. Notice that since Bucharest is the End node which is why it has a heuristic of 0.



In console:
Start node: Arad
Destination: Bucharest


Sample output
Path: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest
Total distance: 418 km

If there is no path found from the Start node to the End node, simply print “NO PATH FOUND”



