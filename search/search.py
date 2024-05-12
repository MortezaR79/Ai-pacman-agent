# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class visitedClass:
    def __init__(self, node,NSEW , cost):
        self.node = node
        self.NSEW = NSEW
        self.cost = cost


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """Search the deepest nodes in the search tree first."""
    stack = util.Stack()
    firstNode = problem.getStartState()
    directionArr = []
    visitedClassObject = []
    visited = []
    tmp = []
    appendedDirection = []
    visitedClassObject = visitedClass(firstNode, directionArr, 0)
    stack.push(visitedClassObject)

    while not stack.isEmpty():
        stackTop = stack.pop()
        currentNode = stackTop.node
        directionArr = stackTop.NSEW

        if not (currentNode in [x.node for x in visited]):
            visited.append(visitedClass(currentNode, directionArr, 0))

            if problem.isGoalState(currentNode):
                return directionArr
            if not (problem.isGoalState(currentNode)):
                successors = problem.getSuccessors(currentNode)
                for i in range(len(successors)):
                    Node,Direction,cost = successors[i]
                    appendedDirection = directionArr + [Direction]
                    newNodeDirection = visitedClass(Node, appendedDirection,0)
                    stack.push(newNodeDirection)

    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    stack = util.Queue()
    firstNode = problem.getStartState()
    directionArr = []
    visitedClassObject = []
    visited = []
    tmp = []
    appendedDirection= []
    visitedClassObject = visitedClass(firstNode, directionArr, 0)
    stack.push(visitedClassObject)

    while not stack.isEmpty():
        stackTop = stack.pop()
        currentNode = stackTop.node
        directionArr = stackTop.NSEW

        if not (currentNode in [x.node for x in visited]):
            visited.append(visitedClass(currentNode, directionArr, 0))
            if problem.isGoalState(currentNode):
                return directionArr
            if not (problem.isGoalState(currentNode)):
                successors = problem.getSuccessors(currentNode)
                for i in range(len(successors)):
                    Node,Direction,cost = successors[i]
                    appendedDirection = directionArr + [Direction]
                    newNodeDirection = visitedClass(Node, appendedDirection,0)
                    stack.push(newNodeDirection)
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    stack = util.PriorityQueue()
    firstNode = problem.getStartState()
    directionArr = []
    visitedClassObject = []
    visited = []
    tmp = []
    a = 1
    b = True
    appendedDirection= []
    visitedClassObject = visitedClass(firstNode, directionArr, 0)
    stack.push(visitedClassObject, 0)


    while not stack.isEmpty():
        stackTop = stack.pop()
        currentNode = stackTop.node
        directionArr = stackTop.NSEW
        currentCost = stackTop.cost
        b = True
        while(b == True):
            # print(currentCost)
            b = False
            a = a + 1

        if not (currentNode in [x.node for x in visited]) :
            visited.append(visitedClass(currentNode, directionArr, currentCost))

            if problem.isGoalState(currentNode):
                return directionArr
            if not (problem.isGoalState(currentNode)):
                successors = problem.getSuccessors(currentNode)
                # print(successors)
                for i in range(len(successors)):
                    Node , Direction, cost = successors[i]
                    appendedDirection = directionArr + [Direction]
                    updatedCost = currentCost + cost
                    # print("cost ", cost)

                    newNodeDirection = visitedClass(Node, appendedDirection,updatedCost)
                    stack.push(newNodeDirection, updatedCost)
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    stack = util.PriorityQueue()
    firstNode = problem.getStartState()
    directionArr = []
    import random
    visitedClassObject = []
    visited = []
    tmp = []
    appendedDirection= []
    visitedClassObject = visitedClass(firstNode, directionArr, 0)
    h = heuristic(firstNode,problem)
    stack.push(visitedClassObject,  0)

    while not stack.isEmpty():
        stackTop = stack.pop()
        currentNode = stackTop.node
        directionArr = stackTop.NSEW
        currentCost = stackTop.cost
        tmpcost = currentCost + heuristic(currentNode,problem)
        if not (currentNode in [x.node for x in visited]):
             visited.append(visitedClass(currentNode, directionArr, tmpcost))

        # visited.append(visitedClass(currentNode, directionArr, tmpcost))
        if problem.isGoalState(currentNode):
             return directionArr
        if not (problem.isGoalState(currentNode)):
             successors = problem.getSuccessors(currentNode)
             # print(successors)
             for i in range(len(successors)):
                Node , Direction, cost = successors[i]
                appendedDirection = directionArr + [Direction]
                # updatedCost = currentCost + cost + heuristic(Node, problem)
                updatedCost = problem.getCostOfActions(appendedDirection) + heuristic(Node, problem)
                newNodeDirection = visitedClass(Node, appendedDirection, updatedCost)
                #stack.push(newNodeDirection, updatedCost)
                if not (Node in [x.node for x in visited]):
                    stack.update(newNodeDirection, updatedCost)
                    visited.append(newNodeDirection)

                for i in range(len(visited)):
                    N = visited[i].node
                    D = visited[i].NSEW
                    C = visited[i].cost
                    if N == Node and updatedCost < C:

                        stack.update(newNodeDirection, updatedCost)

    return directionArr








# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
