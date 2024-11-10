import heapq


def createScenario(fileName): #create a scenario from the input file
    scenario = {}
    with open(fileName) as file:
        for line in file:
            cities = line.split()
            parentCity = cities[0]
            heuristic = int(cities[1])

            if parentCity not in scenario:
                scenario[parentCity ] ={
                    "heuristic" : heuristic,
                    "connectedCities" : {}
                }
            
            cityNumber = 2 
            while (cityNumber < len(cities)):
                neighbor = cities[cityNumber]
                distance = int(cities[cityNumber + 1])
                scenario[parentCity]["connectedCities"][neighbor] = distance
                cityNumber += 2
    return scenario

def provideOutput(parentCities,goalCity, calculateActualCost):
    path = []
    currentCity = goalCity
    while currentCity != None:
        path.append(currentCity)
        currentCity = parentCities[currentCity]
    print("Path:" , " -> ".join(path[::-1]) )
    print("Total Cost :", calculateActualCost[goalCity], "km")
    return None


def aStarAlgorithm(scenario, startCity,goalCity):
    if startCity not in scenario or goalCity not in scenario:
        print ("No Path Found")  #if the start or goal city is not in the scenario
        return None
    toExploreCities = []
    calculateActualCost = {startCity: 0}  #cost without heuristic
    parentCity = {startCity: None}
    heapq.heappush(toExploreCities,(scenario[startCity]["heuristic"],startCity))

    while toExploreCities:
        totalCost,currentCity = heapq.heappop(toExploreCities)
        if currentCity == goalCity:
            return provideOutput(parentCity,goalCity,calculateActualCost)

        for neighborCity, distance in scenario[currentCity]["connectedCities"].items():
            costFromStartCity = calculateActualCost[currentCity] + distance  #calculate the g(n) for the neighbor from start city
            
            if neighborCity not in calculateActualCost or costFromStartCity < calculateActualCost[neighborCity]:
                calculateActualCost[neighborCity] = costFromStartCity
                totalCost = costFromStartCity + scenario[neighborCity]["heuristic"]
                heapq.heappush(toExploreCities,(totalCost,neighborCity))
                parentCity[neighborCity] = currentCity
    print ("No Path Found")
    return None



start_Node = input("Enter the start city: ")
destination = input("Enter the destination city: ")

scenario = createScenario("input file.txt") #input file name
aStarAlgorithm(scenario,start_Node,destination)

