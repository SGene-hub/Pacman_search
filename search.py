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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    # from game import Directions

    # s = Directions.SOUTH
    # w = Directions.WEST
    # e = Directions.EAST
    # n = Directions.NORTH

    
    # directions_dic = {'West': w, 'East': e, 
    #                  'South': s, 'North': n}

    # keep track of both nodes visited
    visited = set()

    # initialise stack that will contain nodes to be visited. LILO structure will allow 
    # to visit every node in the subtree stemming from a sucessor of the root node before 
    # moving to the next subtree stemming from another successor of the root node
    
    visit = util.Stack()   
    start = problem.getStartState()

    # the stack will keep track of both nodes to be viisted and directions to be followed for that node 
    # doing so, the goal node when found will be in a tuple with the directions needed to get there directly 
    # from the root node

    visit.push((start, []))
   

    while not visit.isEmpty():
        
        current = visit.pop()

        if problem.isGoalState(current[0]):
            
            return current[1] 

        elif current[0] not in visited: 
            
            visited.add(current[0])

            successors = problem.getSuccessors(current[0])

            for successor in successors:
            
                if successor[0] not in visited:
                
                    visit.push((successor[0], current[1] + [successor[1]]))

                    


    ## keep track of both directions and nodes visited. you need to output direction list

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # from game import Directions

    # s = Directions.SOUTH
    # w = Directions.WEST
    # e = Directions.EAST
    # n = Directions.NORTH

    
    # directions_dic = {'West': w, 'East': e, 
    #                  'South': s, 'North': n}

    # keep track of both nodes visited
    visited = set()

    # initialise queue that will contain nodes to be visited. FILO structure will allow 
    # to visit every node at every level before mving onto the next level. All successors of
    # the root node will need to be visited before being able to visit any node on the lower 
    # levels, and so on. in the subtree stemming from a sucessor of the root node before 
    
    visit = util.Queue()   
    start = problem.getStartState()

    # the queue will keep track of both nodes to be visted and directions to be followed for that node.
    # doing so, the goal node when found will be in a tuple with the directions needed to get there directly 
    # from the root node

    visit.push((start, []))
   

    while not visit.isEmpty():
        
        current = visit.pop()

        if problem.isGoalState(current[0]):
            
            return current[1] 

        elif current[0] not in visited: 
            
            visited.add(current[0])

            successors = problem.getSuccessors(current[0])

            for successor in successors:
            
                if successor[0] not in visited:
                
                    visit.push((successor[0], current[1] + [successor[1]]))



def uniformCostSearch(problem):
      
    # from game import Directions

    # s = Directions.SOUTH
    # w = Directions.WEST
    # e = Directions.EAST
    # n = Directions.NORTH

    
    # directions_dic = {'West': w, 'East': e, 
    #                  'South': s, 'North': n}

    # keep track of both nodes visited
    visited = set()

    # initialise priority queue that will contain nodes to be visited. This willow allow 
    # to visit the node with the least cost associated out fo every successor of every node visited. 
    
    visit = util.PriorityQueue()   
    start = problem.getStartState()

    # the queue will keep track of both nodes to be visted and directions to be followed for that node,
    # as well as cost associated with theaction needed to reach that node. 

    visit.push((start, []), 0) # cost is zero as the game is initialised at that state
   

    while not visit.isEmpty():
        
        current = visit.pop()

        if problem.isGoalState(current[0]):
            
            return current[1] 

        elif current[0] not in visited: 
            
            visited.add(current[0])

            successors = problem.getSuccessors(current[0])

            for successor in successors:
            
                if successor[0] not in visited:

                    cost = problem.getCostOfActions(current[1] + [successor[1]])
                    visit.push((successor[0], current[1] + [successor[1]]), cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""


    # keep track of both nodes visited
    visited = set()

    # initialise priority queue that will contain nodes to be visited. This willow allow 
    # to visit the node with the least cost associated out fo every successor of every node visited. 
    
    visit = util.PriorityQueue()   
    start = problem.getStartState()

    # the queue will keep track of both nodes to be visted and directions to be followed for that node,
    # as well as cost associated with theaction needed to reach that node. 

    visit.push((start, []), 0 + heuristic(start, problem)) # cost + is zero as the game is initialised at that state

    while not visit.isEmpty():
        
        current = visit.pop()

        if problem.isGoalState(current[0]):
            
            return current[1] 

        elif current[0] not in visited: 
            
            visited.add(current[0])

            successors = problem.getSuccessors(current[0])

            for successor in successors:
            
                if successor[0] not in visited:

                    cost = problem.getCostOfActions(current[1] + [successor[1]])
                    visit.push((successor[0], current[1] + [successor[1]]), cost + heuristic(successor[0], problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
