# AI-Packman-Agent

In this project, your Pacman character navigates to a specific location and gathers food in an efficient spiral pattern. We construct broad search algorithms and implement them within the context of the Pacman game. To verify the accuracy of your algorithms through debugging and testing, you can run the subsequent command to view its specifics:

python autograder.py

## project structure

- Pacman Agent Algorithms: Navigating and Optimizing Food Collection
  - search.py : The document containing all our search algorithms.
  - searchAgents.py : The file where all the search agents are placed.
- Gameboard Dynamics: Visualization, Movement, and Logic of the Pacman World

  - pacman.py : The main file that runs Pacman games. This file describes the GameState class for the Pacman game that you use in this project.
  - The implemented logic for the Pacman world is in this file. It includes various classes like AgentState, Agent, Grid, and Direction.
  - util.py : Useful data structures for implementing search algorithms are located in this file.
  - graphicsDisplay.py : Graphics for the Pacman game are implemented in this file.
  - graphicsUtils.py : Provides assistance for the graphical aspects of the game.
  - textDispaly.py : Offers ASCII-based graphics for the Pacman game.
  - ghostAgent.py : Manages the behavior of the ghost characters.
  - layout.py : Program to read map files and save their information.

The project has more files in it, but the main focus is on search.py and searchAgents.py.

## Finding a food using Depth-first search

You can find the fully implemented SearchAgent class in the searchAgents.py file. make sure that SearchAgent is working properly by running the following commands:

```
python pacman.py -l tinyMaze -p SearchAgent
```

```
python pacman.py -l mediumMaze -p SearchAgent
```

```
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

The Pacman screen shows the states that have been explored and the order in which they were explored (the brighter the red, the earlier it was explored).

## Finding a food using Breadth-first search

After implementing BFS function in search.py file, We test our code similar to the depth first search algorithm.

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

```
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

## Changing the cost function

While BFS finds the shortest path to the goal, we might also want to find the best path in other ways. Think about two mazes, mediumDottedMaze and mediumScaryMaze. By adjusting the cost function, we can guide Pacman to explore different paths. For instance, we could make moving in ghost-filled areas more costly or less costly in food-rich areas. The UCS graph search algorithm is available in the uniformCostSearch function within the search.py file. Now, you should be able to observe the agents' successful behaviors in the three maps below. In all scenarios, the agents are UCS agents, varying only in the cost function they apply.

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```

```
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```

```
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

## Finding a food using A\* search

Implement the AStar search algorithm in the aStarSearch function in the search.py file.
A\* takes a heuristic function as an input argument. Heuristic functions have two input arguments:

1. The current situation in the search problem
2. The search problem itself.

In this section, you can test your implemented A\* algorithm on the problem of finding the path inside the maze to a specific point, using the Manhattan distance heuristic:

```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

After running the code with this algorithm, you will see that the A\* algorithm finds the optimal solution faster than the UCS algorithm.

## Finding all corners

The real strength of the A\* algorithm becomes apparent when tackling more complex search challenges. Now, we're introducing a new puzzle and creating a complex heuristic for it.

Imagine a maze with four dots located at each corner. Our goal is to find the quickest route through the maze that visits all four corners, no matter if there's food in one corner or not. It's important to note that in some mazes, like tinyCorners, the quickest route doesn't always start with the nearest food.
now our agent can solve the following two problems:

```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

```
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

## Heuristics for the corners problem

As you know, heuristics are functions that take a search condition as input and return a number as output. The estimated output number shows the nearest target.
The code can solve the following problem:

```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

## Eating all the points

In this part, we're tackling a tough search problem: eating all the Pacman foods in the fewest steps possible. To do this, we need to create a new search problem that sets up the food collecting challenge. For this, the FoodSearchProblem class is created in the searchAgents.py file. A good solution is a path that lets Pacman collect all the food items in the Pacman world. For now, our solutions don't worry about souls or power pellets. The answers depend only on where the walls, food, and Pacman are. (Of course, ghosts can mess up the solution We'll tackle that in the next project.)

```
python pacman.py -l testSearch -p AStarFoodSearchAgent
```
