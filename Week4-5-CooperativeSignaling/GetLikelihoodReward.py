
class GetLikelihoodReward(object):
    def __init__(self, transitionTable, goalPolicies):
        self.transitionTable = transitionTable
        self.goalPolicies  = goalPolicies #can be dictionary of form goal:goal policy or a list, but trueGoal should link to the correct policy here

    def __call__(self, trueGoal, originalReward, alpha):
    	######################################
    	###### Your Code Here ################
    	######################################
        return(newReward)
    



# Parameters across all goals and environments
convergenceThreshold = 10e-7
gamma = .9
beta = 2
alpha = 5



"""
	Environment specifications
	gridWidth = 7
	gridHeight = 6
	allActions = [(1,0), (0,1), (-1,0), (0,-1), (0,0)]
	trapStates = [(3,0), (3,1), (3,3)]
	goalA = (6,1)
	goalB = (6,4)
	goalC = (1,5)
"""

transition = {(0, 0): {(1, 0): {(1, 0): 1},(0, 1): {(0, 1): 1},(-1, 0): {(0, 0): 1},(0, -1): {(0, 0): 1},(0, 0): {(0, 0): 1}},(0, 1): {(1, 0): {(1, 1): 1},(0, 1): {(0, 2): 1},(-1, 0): {(0, 1): 1},(0, -1): {(0, 0): 1},(0, 0): {(0, 1): 1}},(0, 2): {(1, 0): {(1, 2): 1},(0, 1): {(0, 3): 1},(-1, 0): {(0, 2): 1},(0, -1): {(0, 1): 1},(0, 0): {(0, 2): 1}},(0, 3): {(1, 0): {(1, 3): 1},(0, 1): {(0, 4): 1},(-1, 0): {(0, 3): 1},(0, -1): {(0, 2): 1},(0, 0): {(0, 3): 1}},(0, 4): {(1, 0): {(1, 4): 1},(0, 1): {(0, 5): 1},(-1, 0): {(0, 4): 1},(0, -1): {(0, 3): 1},(0, 0): {(0, 4): 1}},(0, 5): {(1, 0): {(1, 5): 1},(0, 1): {(0, 5): 1},(-1, 0): {(0, 5): 1},(0, -1): {(0, 4): 1},(0, 0): {(0, 5): 1}},(1, 0): {(1, 0): {(2, 0): 1},(0, 1): {(1, 1): 1},(-1, 0): {(0, 0): 1},(0, -1): {(1, 0): 1},(0, 0): {(1, 0): 1}},(1, 1): {(1, 0): {(2, 1): 1},(0, 1): {(1, 2): 1},(-1, 0): {(0, 1): 1},(0, -1): {(1, 0): 1},(0, 0): {(1, 1): 1}},(1, 2): {(1, 0): {(2, 2): 1},(0, 1): {(1, 3): 1},(-1, 0): {(0, 2): 1},(0, -1): {(1, 1): 1},(0, 0): {(1, 2): 1}},(1, 3): {(1, 0): {(2, 3): 1},(0, 1): {(1, 4): 1},(-1, 0): {(0, 3): 1},(0, -1): {(1, 2): 1},(0, 0): {(1, 3): 1}},(1, 4): {(1, 0): {(2, 4): 1},(0, 1): {(1, 5): 1},(-1, 0): {(0, 4): 1},(0, -1): {(1, 3): 1},(0, 0): {(1, 4): 1}},(1, 5): {(1, 0): {(2, 5): 1},(0, 1): {(1, 5): 1},(-1, 0): {(0, 5): 1},(0, -1): {(1, 4): 1},(0, 0): {(1, 5): 1}},(2, 0): {(1, 0): {(3, 0): 1},(0, 1): {(2, 1): 1},(-1, 0): {(1, 0): 1},(0, -1): {(2, 0): 1},(0, 0): {(2, 0): 1}},(2, 1): {(1, 0): {(3, 1): 1},(0, 1): {(2, 2): 1},(-1, 0): {(1, 1): 1},(0, -1): {(2, 0): 1},(0, 0): {(2, 1): 1}},(2, 2): {(1, 0): {(3, 2): 1},(0, 1): {(2, 3): 1},(-1, 0): {(1, 2): 1},(0, -1): {(2, 1): 1},(0, 0): {(2, 2): 1}},(2, 3): {(1, 0): {(3, 3): 1},(0, 1): {(2, 4): 1},(-1, 0): {(1, 3): 1},(0, -1): {(2, 2): 1},(0, 0): {(2, 3): 1}},(2, 4): {(1, 0): {(3, 4): 1},(0, 1): {(2, 5): 1},(-1, 0): {(1, 4): 1},(0, -1): {(2, 3): 1},(0, 0): {(2, 4): 1}},(2, 5): {(1, 0): {(3, 5): 1},(0, 1): {(2, 5): 1},(-1, 0): {(1, 5): 1},(0, -1): {(2, 4): 1},(0, 0): {(2, 5): 1}},(3, 0): {(1, 0): {(4, 0): 1},(0, 1): {(3, 1): 1},(-1, 0): {(2, 0): 1},(0, -1): {(3, 0): 1},(0, 0): {(3, 0): 1}},(3, 1): {(1, 0): {(4, 1): 1},(0, 1): {(3, 2): 1},(-1, 0): {(2, 1): 1},(0, -1): {(3, 0): 1},(0, 0): {(3, 1): 1}},(3, 2): {(1, 0): {(4, 2): 1},(0, 1): {(3, 3): 1},(-1, 0): {(2, 2): 1},(0, -1): {(3, 1): 1},(0, 0): {(3, 2): 1}},(3, 3): {(1, 0): {(4, 3): 1},(0, 1): {(3, 4): 1},(-1, 0): {(2, 3): 1},(0, -1): {(3, 2): 1},(0, 0): {(3, 3): 1}},(3, 4): {(1, 0): {(4, 4): 1},(0, 1): {(3, 5): 1},(-1, 0): {(2, 4): 1},(0, -1): {(3, 3): 1},(0, 0): {(3, 4): 1}},(3, 5): {(1, 0): {(4, 5): 1},(0, 1): {(3, 5): 1},(-1, 0): {(2, 5): 1},(0, -1): {(3, 4): 1},(0, 0): {(3, 5): 1}},(4, 0): {(1, 0): {(5, 0): 1},(0, 1): {(4, 1): 1},(-1, 0): {(3, 0): 1},(0, -1): {(4, 0): 1},(0, 0): {(4, 0): 1}},(4, 1): {(1, 0): {(5, 1): 1},(0, 1): {(4, 2): 1},(-1, 0): {(3, 1): 1},(0, -1): {(4, 0): 1},(0, 0): {(4, 1): 1}},(4, 2): {(1, 0): {(5, 2): 1},(0, 1): {(4, 3): 1},(-1, 0): {(3, 2): 1},(0, -1): {(4, 1): 1},(0, 0): {(4, 2): 1}},(4, 3): {(1, 0): {(5, 3): 1},(0, 1): {(4, 4): 1},(-1, 0): {(3, 3): 1},(0, -1): {(4, 2): 1},(0, 0): {(4, 3): 1}},(4, 4): {(1, 0): {(5, 4): 1},(0, 1): {(4, 5): 1},(-1, 0): {(3, 4): 1},(0, -1): {(4, 3): 1},(0, 0): {(4, 4): 1}},(4, 5): {(1, 0): {(5, 5): 1},(0, 1): {(4, 5): 1},(-1, 0): {(3, 5): 1},(0, -1): {(4, 4): 1},(0, 0): {(4, 5): 1}},(5, 0): {(1, 0): {(6, 0): 1},(0, 1): {(5, 1): 1},(-1, 0): {(4, 0): 1},(0, -1): {(5, 0): 1},(0, 0): {(5, 0): 1}},(5, 1): {(1, 0): {(6, 1): 1},(0, 1): {(5, 2): 1},(-1, 0): {(4, 1): 1},(0, -1): {(5, 0): 1},(0, 0): {(5, 1): 1}},(5, 2): {(1, 0): {(6, 2): 1},(0, 1): {(5, 3): 1},(-1, 0): {(4, 2): 1},(0, -1): {(5, 1): 1},(0, 0): {(5, 2): 1}},(5, 3): {(1, 0): {(6, 3): 1},(0, 1): {(5, 4): 1},(-1, 0): {(4, 3): 1},(0, -1): {(5, 2): 1},(0, 0): {(5, 3): 1}},(5, 4): {(1, 0): {(6, 4): 1},(0, 1): {(5, 5): 1},(-1, 0): {(4, 4): 1},(0, -1): {(5, 3): 1},(0, 0): {(5, 4): 1}},(5, 5): {(1, 0): {(6, 5): 1},(0, 1): {(5, 5): 1},(-1, 0): {(4, 5): 1},(0, -1): {(5, 4): 1},(0, 0): {(5, 5): 1}},(6, 0): {(1, 0): {(6, 0): 1},(0, 1): {(6, 1): 1},(-1, 0): {(5, 0): 1},(0, -1): {(6, 0): 1},(0, 0): {(6, 0): 1}},(6, 1): {(1, 0): {(6, 1): 1},(0, 1): {(6, 2): 1},(-1, 0): {(5, 1): 1},(0, -1): {(6, 0): 1},(0, 0): {(6, 1): 1}},(6, 2): {(1, 0): {(6, 2): 1},(0, 1): {(6, 3): 1},(-1, 0): {(5, 2): 1},(0, -1): {(6, 1): 1},(0, 0): {(6, 2): 1}},(6, 3): {(1, 0): {(6, 3): 1},(0, 1): {(6, 4): 1},(-1, 0): {(5, 3): 1},(0, -1): {(6, 2): 1},(0, 0): {(6, 3): 1}},(6, 4): {(1, 0): {(6, 4): 1},(0, 1): {(6, 5): 1},(-1, 0): {(5, 4): 1},(0, -1): {(6, 3): 1},(0, 0): {(6, 4): 1}},(6, 5): {(1, 0): {(6, 5): 1},(0, 1): {(6, 5): 1},(-1, 0): {(5, 5): 1},(0, -1): {(6, 4): 1},(0, 0): {(6, 5): 1}}}
rewardForGoalA = {(0, 0): {(1, 0): {(1, 0): -1},(0, 1): {(0, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(0, 0): -1},(0, 0): {(0, 0): -0.1}},(0, 1): {(1, 0): {(1, 1): -1},(0, 1): {(0, 2): -1},(-1, 0): {(0, 1): -1},(0, -1): {(0, 0): -1},(0, 0): {(0, 1): -0.1}},(0, 2): {(1, 0): {(1, 2): -1},(0, 1): {(0, 3): -1},(-1, 0): {(0, 2): -1},(0, -1): {(0, 1): -1},(0, 0): {(0, 2): -0.1}},(0, 3): {(1, 0): {(1, 3): -1},(0, 1): {(0, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(0, 2): -1},(0, 0): {(0, 3): -0.1}},(0, 4): {(1, 0): {(1, 4): -1},(0, 1): {(0, 5): -1},(-1, 0): {(0, 4): -1},(0, -1): {(0, 3): -1},(0, 0): {(0, 4): -0.1}},(0, 5): {(1, 0): {(1, 5): -1},(0, 1): {(0, 5): -1},(-1, 0): {(0, 5): -1},(0, -1): {(0, 4): -1},(0, 0): {(0, 5): -0.1}},(1, 0): {(1, 0): {(2, 0): -1},(0, 1): {(1, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(1, 0): -1},(0, 0): {(1, 0): -0.1}},(1, 1): {(1, 0): {(2, 1): -1},(0, 1): {(1, 2): -1},(-1, 0): {(0, 1): -1},(0, -1): {(1, 0): -1},(0, 0): {(1, 1): -0.1}},(1, 2): {(1, 0): {(2, 2): -1},(0, 1): {(1, 3): -1},(-1, 0): {(0, 2): -1},(0, -1): {(1, 1): -1},(0, 0): {(1, 2): -0.1}},(1, 3): {(1, 0): {(2, 3): -1},(0, 1): {(1, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(1, 2): -1},(0, 0): {(1, 3): -0.1}},(1, 4): {(1, 0): {(2, 4): -1},(0, 1): {(1, 5): -1},(-1, 0): {(0, 4): -1},(0, -1): {(1, 3): -1},(0, 0): {(1, 4): -0.1}},(1, 5): {(1, 0): {(2, 5): -1},(0, 1): {(1, 5): -1},(-1, 0): {(0, 5): -1},(0, -1): {(1, 4): -1},(0, 0): {(1, 5): -0.1}},(2, 0): {(1, 0): {(3, 0): -1},(0, 1): {(2, 1): -1},(-1, 0): {(1, 0): -1},(0, -1): {(2, 0): -1},(0, 0): {(2, 0): -0.1}},(2, 1): {(1, 0): {(3, 1): -1},(0, 1): {(2, 2): -1},(-1, 0): {(1, 1): -1},(0, -1): {(2, 0): -1},(0, 0): {(2, 1): -0.1}},(2, 2): {(1, 0): {(3, 2): -1},(0, 1): {(2, 3): -1},(-1, 0): {(1, 2): -1},(0, -1): {(2, 1): -1},(0, 0): {(2, 2): -0.1}},(2, 3): {(1, 0): {(3, 3): -1},(0, 1): {(2, 4): -1},(-1, 0): {(1, 3): -1},(0, -1): {(2, 2): -1},(0, 0): {(2, 3): -0.1}},(2, 4): {(1, 0): {(3, 4): -1},(0, 1): {(2, 5): -1},(-1, 0): {(1, 4): -1},(0, -1): {(2, 3): -1},(0, 0): {(2, 4): -0.1}},(2, 5): {(1, 0): {(3, 5): -1},(0, 1): {(2, 5): -1},(-1, 0): {(1, 5): -1},(0, -1): {(2, 4): -1},(0, 0): {(2, 5): -0.1}},(3, 0): {(1, 0): {(4, 0): -100},(0, 1): {(3, 1): -100},(-1, 0): {(2, 0): -100},(0, -1): {(3, 0): -100},(0, 0): {(3, 0): -100}},(3, 1): {(1, 0): {(4, 1): -100},(0, 1): {(3, 2): -100},(-1, 0): {(2, 1): -100},(0, -1): {(3, 0): -100},(0, 0): {(3, 1): -100}},(3, 2): {(1, 0): {(4, 2): -1},(0, 1): {(3, 3): -1},(-1, 0): {(2, 2): -1},(0, -1): {(3, 1): -1},(0, 0): {(3, 2): -0.1}},(3, 3): {(1, 0): {(4, 3): -100},(0, 1): {(3, 4): -100},(-1, 0): {(2, 3): -100},(0, -1): {(3, 2): -100},(0, 0): {(3, 3): -100}},(3, 4): {(1, 0): {(4, 4): -1},(0, 1): {(3, 5): -1},(-1, 0): {(2, 4): -1},(0, -1): {(3, 3): -1},(0, 0): {(3, 4): -0.1}},(3, 5): {(1, 0): {(4, 5): -1},(0, 1): {(3, 5): -1},(-1, 0): {(2, 5): -1},(0, -1): {(3, 4): -1},(0, 0): {(3, 5): -0.1}},(4, 0): {(1, 0): {(5, 0): -1},(0, 1): {(4, 1): -1},(-1, 0): {(3, 0): -1},(0, -1): {(4, 0): -1},(0, 0): {(4, 0): -0.1}},(4, 1): {(1, 0): {(5, 1): -1},(0, 1): {(4, 2): -1},(-1, 0): {(3, 1): -1},(0, -1): {(4, 0): -1},(0, 0): {(4, 1): -0.1}},(4, 2): {(1, 0): {(5, 2): -1},(0, 1): {(4, 3): -1},(-1, 0): {(3, 2): -1},(0, -1): {(4, 1): -1},(0, 0): {(4, 2): -0.1}},(4, 3): {(1, 0): {(5, 3): -1},(0, 1): {(4, 4): -1},(-1, 0): {(3, 3): -1},(0, -1): {(4, 2): -1},(0, 0): {(4, 3): -0.1}},(4, 4): {(1, 0): {(5, 4): -1},(0, 1): {(4, 5): -1},(-1, 0): {(3, 4): -1},(0, -1): {(4, 3): -1},(0, 0): {(4, 4): -0.1}},(4, 5): {(1, 0): {(5, 5): -1},(0, 1): {(4, 5): -1},(-1, 0): {(3, 5): -1},(0, -1): {(4, 4): -1},(0, 0): {(4, 5): -0.1}},(5, 0): {(1, 0): {(6, 0): -1},(0, 1): {(5, 1): -1},(-1, 0): {(4, 0): -1},(0, -1): {(5, 0): -1},(0, 0): {(5, 0): -0.1}},(5, 1): {(1, 0): {(6, 1): -1},(0, 1): {(5, 2): -1},(-1, 0): {(4, 1): -1},(0, -1): {(5, 0): -1},(0, 0): {(5, 1): -0.1}},(5, 2): {(1, 0): {(6, 2): -1},(0, 1): {(5, 3): -1},(-1, 0): {(4, 2): -1},(0, -1): {(5, 1): -1},(0, 0): {(5, 2): -0.1}},(5, 3): {(1, 0): {(6, 3): -1},(0, 1): {(5, 4): -1},(-1, 0): {(4, 3): -1},(0, -1): {(5, 2): -1},(0, 0): {(5, 3): -0.1}},(5, 4): {(1, 0): {(6, 4): -1},(0, 1): {(5, 5): -1},(-1, 0): {(4, 4): -1},(0, -1): {(5, 3): -1},(0, 0): {(5, 4): -0.1}},(5, 5): {(1, 0): {(6, 5): -1},(0, 1): {(5, 5): -1},(-1, 0): {(4, 5): -1},(0, -1): {(5, 4): -1},(0, 0): {(5, 5): -0.1}},(6, 0): {(1, 0): {(6, 0): -1},(0, 1): {(6, 1): -1},(-1, 0): {(5, 0): -1},(0, -1): {(6, 0): -1},(0, 0): {(6, 0): -0.1}},(6, 1): {(1, 0): {(6, 1): 9},(0, 1): {(6, 2): 9},(-1, 0): {(5, 1): 9},(0, -1): {(6, 0): 9},(0, 0): {(6, 1): 9.9}},(6, 2): {(1, 0): {(6, 2): -1},(0, 1): {(6, 3): -1},(-1, 0): {(5, 2): -1},(0, -1): {(6, 1): -1},(0, 0): {(6, 2): -0.1}},(6, 3): {(1, 0): {(6, 3): -1},(0, 1): {(6, 4): -1},(-1, 0): {(5, 3): -1},(0, -1): {(6, 2): -1},(0, 0): {(6, 3): -0.1}},(6, 4): {(1, 0): {(6, 4): -1},(0, 1): {(6, 5): -1},(-1, 0): {(5, 4): -1},(0, -1): {(6, 3): -1},(0, 0): {(6, 4): -0.1}},(6, 5): {(1, 0): {(6, 5): -1},(0, 1): {(6, 5): -1},(-1, 0): {(5, 5): -1},(0, -1): {(6, 4): -1},(0, 0): {(6, 5): -0.1}}}
rewardForGoalB = {(0, 0): {(1, 0): {(1, 0): -1},(0, 1): {(0, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(0, 0): -1},(0, 0): {(0, 0): -0.1}},(0, 1): {(1, 0): {(1, 1): -1},(0, 1): {(0, 2): -1},(-1, 0): {(0, 1): -1},(0, -1): {(0, 0): -1},(0, 0): {(0, 1): -0.1}},(0, 2): {(1, 0): {(1, 2): -1},(0, 1): {(0, 3): -1},(-1, 0): {(0, 2): -1},(0, -1): {(0, 1): -1},(0, 0): {(0, 2): -0.1}},(0, 3): {(1, 0): {(1, 3): -1},(0, 1): {(0, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(0, 2): -1},(0, 0): {(0, 3): -0.1}},(0, 4): {(1, 0): {(1, 4): -1},(0, 1): {(0, 5): -1},(-1, 0): {(0, 4): -1},(0, -1): {(0, 3): -1},(0, 0): {(0, 4): -0.1}},(0, 5): {(1, 0): {(1, 5): -1},(0, 1): {(0, 5): -1},(-1, 0): {(0, 5): -1},(0, -1): {(0, 4): -1},(0, 0): {(0, 5): -0.1}},(1, 0): {(1, 0): {(2, 0): -1},(0, 1): {(1, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(1, 0): -1},(0, 0): {(1, 0): -0.1}},(1, 1): {(1, 0): {(2, 1): -1},(0, 1): {(1, 2): -1},(-1, 0): {(0, 1): -1},(0, -1): {(1, 0): -1},(0, 0): {(1, 1): -0.1}},(1, 2): {(1, 0): {(2, 2): -1},(0, 1): {(1, 3): -1},(-1, 0): {(0, 2): -1},(0, -1): {(1, 1): -1},(0, 0): {(1, 2): -0.1}},(1, 3): {(1, 0): {(2, 3): -1},(0, 1): {(1, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(1, 2): -1},(0, 0): {(1, 3): -0.1}},(1, 4): {(1, 0): {(2, 4): -1},(0, 1): {(1, 5): -1},(-1, 0): {(0, 4): -1},(0, -1): {(1, 3): -1},(0, 0): {(1, 4): -0.1}},(1, 5): {(1, 0): {(2, 5): -1},(0, 1): {(1, 5): -1},(-1, 0): {(0, 5): -1},(0, -1): {(1, 4): -1},(0, 0): {(1, 5): -0.1}},(2, 0): {(1, 0): {(3, 0): -1},(0, 1): {(2, 1): -1},(-1, 0): {(1, 0): -1},(0, -1): {(2, 0): -1},(0, 0): {(2, 0): -0.1}},(2, 1): {(1, 0): {(3, 1): -1},(0, 1): {(2, 2): -1},(-1, 0): {(1, 1): -1},(0, -1): {(2, 0): -1},(0, 0): {(2, 1): -0.1}},(2, 2): {(1, 0): {(3, 2): -1},(0, 1): {(2, 3): -1},(-1, 0): {(1, 2): -1},(0, -1): {(2, 1): -1},(0, 0): {(2, 2): -0.1}},(2, 3): {(1, 0): {(3, 3): -1},(0, 1): {(2, 4): -1},(-1, 0): {(1, 3): -1},(0, -1): {(2, 2): -1},(0, 0): {(2, 3): -0.1}},(2, 4): {(1, 0): {(3, 4): -1},(0, 1): {(2, 5): -1},(-1, 0): {(1, 4): -1},(0, -1): {(2, 3): -1},(0, 0): {(2, 4): -0.1}},(2, 5): {(1, 0): {(3, 5): -1},(0, 1): {(2, 5): -1},(-1, 0): {(1, 5): -1},(0, -1): {(2, 4): -1},(0, 0): {(2, 5): -0.1}},(3, 0): {(1, 0): {(4, 0): -100},(0, 1): {(3, 1): -100},(-1, 0): {(2, 0): -100},(0, -1): {(3, 0): -100},(0, 0): {(3, 0): -100}},(3, 1): {(1, 0): {(4, 1): -100},(0, 1): {(3, 2): -100},(-1, 0): {(2, 1): -100},(0, -1): {(3, 0): -100},(0, 0): {(3, 1): -100}},(3, 2): {(1, 0): {(4, 2): -1},(0, 1): {(3, 3): -1},(-1, 0): {(2, 2): -1},(0, -1): {(3, 1): -1},(0, 0): {(3, 2): -0.1}},(3, 3): {(1, 0): {(4, 3): -100},(0, 1): {(3, 4): -100},(-1, 0): {(2, 3): -100},(0, -1): {(3, 2): -100},(0, 0): {(3, 3): -100}},(3, 4): {(1, 0): {(4, 4): -1},(0, 1): {(3, 5): -1},(-1, 0): {(2, 4): -1},(0, -1): {(3, 3): -1},(0, 0): {(3, 4): -0.1}},(3, 5): {(1, 0): {(4, 5): -1},(0, 1): {(3, 5): -1},(-1, 0): {(2, 5): -1},(0, -1): {(3, 4): -1},(0, 0): {(3, 5): -0.1}},(4, 0): {(1, 0): {(5, 0): -1},(0, 1): {(4, 1): -1},(-1, 0): {(3, 0): -1},(0, -1): {(4, 0): -1},(0, 0): {(4, 0): -0.1}},(4, 1): {(1, 0): {(5, 1): -1},(0, 1): {(4, 2): -1},(-1, 0): {(3, 1): -1},(0, -1): {(4, 0): -1},(0, 0): {(4, 1): -0.1}},(4, 2): {(1, 0): {(5, 2): -1},(0, 1): {(4, 3): -1},(-1, 0): {(3, 2): -1},(0, -1): {(4, 1): -1},(0, 0): {(4, 2): -0.1}},(4, 3): {(1, 0): {(5, 3): -1},(0, 1): {(4, 4): -1},(-1, 0): {(3, 3): -1},(0, -1): {(4, 2): -1},(0, 0): {(4, 3): -0.1}},(4, 4): {(1, 0): {(5, 4): -1},(0, 1): {(4, 5): -1},(-1, 0): {(3, 4): -1},(0, -1): {(4, 3): -1},(0, 0): {(4, 4): -0.1}},(4, 5): {(1, 0): {(5, 5): -1},(0, 1): {(4, 5): -1},(-1, 0): {(3, 5): -1},(0, -1): {(4, 4): -1},(0, 0): {(4, 5): -0.1}},(5, 0): {(1, 0): {(6, 0): -1},(0, 1): {(5, 1): -1},(-1, 0): {(4, 0): -1},(0, -1): {(5, 0): -1},(0, 0): {(5, 0): -0.1}},(5, 1): {(1, 0): {(6, 1): -1},(0, 1): {(5, 2): -1},(-1, 0): {(4, 1): -1},(0, -1): {(5, 0): -1},(0, 0): {(5, 1): -0.1}},(5, 2): {(1, 0): {(6, 2): -1},(0, 1): {(5, 3): -1},(-1, 0): {(4, 2): -1},(0, -1): {(5, 1): -1},(0, 0): {(5, 2): -0.1}},(5, 3): {(1, 0): {(6, 3): -1},(0, 1): {(5, 4): -1},(-1, 0): {(4, 3): -1},(0, -1): {(5, 2): -1},(0, 0): {(5, 3): -0.1}},(5, 4): {(1, 0): {(6, 4): -1},(0, 1): {(5, 5): -1},(-1, 0): {(4, 4): -1},(0, -1): {(5, 3): -1},(0, 0): {(5, 4): -0.1}},(5, 5): {(1, 0): {(6, 5): -1},(0, 1): {(5, 5): -1},(-1, 0): {(4, 5): -1},(0, -1): {(5, 4): -1},(0, 0): {(5, 5): -0.1}},(6, 0): {(1, 0): {(6, 0): -1},(0, 1): {(6, 1): -1},(-1, 0): {(5, 0): -1},(0, -1): {(6, 0): -1},(0, 0): {(6, 0): -0.1}},(6, 1): {(1, 0): {(6, 1): -1},(0, 1): {(6, 2): -1},(-1, 0): {(5, 1): -1},(0, -1): {(6, 0): -1},(0, 0): {(6, 1): -0.1}},(6, 2): {(1, 0): {(6, 2): -1},(0, 1): {(6, 3): -1},(-1, 0): {(5, 2): -1},(0, -1): {(6, 1): -1},(0, 0): {(6, 2): -0.1}},(6, 3): {(1, 0): {(6, 3): -1},(0, 1): {(6, 4): -1},(-1, 0): {(5, 3): -1},(0, -1): {(6, 2): -1},(0, 0): {(6, 3): -0.1}},(6, 4): {(1, 0): {(6, 4): 9},(0, 1): {(6, 5): 9},(-1, 0): {(5, 4): 9},(0, -1): {(6, 3): 9},(0, 0): {(6, 4): 9.9}},(6, 5): {(1, 0): {(6, 5): -1},(0, 1): {(6, 5): -1},(-1, 0): {(5, 5): -1},(0, -1): {(6, 4): -1},(0, 0): {(6, 5): -0.1}}}
rewardForGoalC = {(0, 0): {(1, 0): {(1, 0): -1},(0, 1): {(0, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(0, 0): -1},(0, 0): {(0, 0): -0.1}},(0, 1): {(1, 0): {(1, 1): -1},(0, 1): {(0, 2): -1},(-1, 0): {(0, 1): -1},(0, -1): {(0, 0): -1},(0, 0): {(0, 1): -0.1}},(0, 2): {(1, 0): {(1, 2): -1},(0, 1): {(0, 3): -1},(-1, 0): {(0, 2): -1},(0, -1): {(0, 1): -1},(0, 0): {(0, 2): -0.1}},(0, 3): {(1, 0): {(1, 3): -1},(0, 1): {(0, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(0, 2): -1},(0, 0): {(0, 3): -0.1}},(0, 4): {(1, 0): {(1, 4): -1},(0, 1): {(0, 5): -1},(-1, 0): {(0, 4): -1},(0, -1): {(0, 3): -1},(0, 0): {(0, 4): -0.1}},(0, 5): {(1, 0): {(1, 5): -1},(0, 1): {(0, 5): -1},(-1, 0): {(0, 5): -1},(0, -1): {(0, 4): -1},(0, 0): {(0, 5): -0.1}},(1, 0): {(1, 0): {(2, 0): -1},(0, 1): {(1, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(1, 0): -1},(0, 0): {(1, 0): -0.1}},(1, 1): {(1, 0): {(2, 1): -1},(0, 1): {(1, 2): -1},(-1, 0): {(0, 1): -1},(0, -1): {(1, 0): -1},(0, 0): {(1, 1): -0.1}},(1, 2): {(1, 0): {(2, 2): -1},(0, 1): {(1, 3): -1},(-1, 0): {(0, 2): -1},(0, -1): {(1, 1): -1},(0, 0): {(1, 2): -0.1}},(1, 3): {(1, 0): {(2, 3): -1},(0, 1): {(1, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(1, 2): -1},(0, 0): {(1, 3): -0.1}},(1, 4): {(1, 0): {(2, 4): -1},(0, 1): {(1, 5): -1},(-1, 0): {(0, 4): -1},(0, -1): {(1, 3): -1},(0, 0): {(1, 4): -0.1}},(1, 5): {(1, 0): {(2, 5): 9},(0, 1): {(1, 5): 9},(-1, 0): {(0, 5): 9},(0, -1): {(1, 4): 9},(0, 0): {(1, 5): 9.9}},(2, 0): {(1, 0): {(3, 0): -1},(0, 1): {(2, 1): -1},(-1, 0): {(1, 0): -1},(0, -1): {(2, 0): -1},(0, 0): {(2, 0): -0.1}},(2, 1): {(1, 0): {(3, 1): -1},(0, 1): {(2, 2): -1},(-1, 0): {(1, 1): -1},(0, -1): {(2, 0): -1},(0, 0): {(2, 1): -0.1}},(2, 2): {(1, 0): {(3, 2): -1},(0, 1): {(2, 3): -1},(-1, 0): {(1, 2): -1},(0, -1): {(2, 1): -1},(0, 0): {(2, 2): -0.1}},(2, 3): {(1, 0): {(3, 3): -1},(0, 1): {(2, 4): -1},(-1, 0): {(1, 3): -1},(0, -1): {(2, 2): -1},(0, 0): {(2, 3): -0.1}},(2, 4): {(1, 0): {(3, 4): -1},(0, 1): {(2, 5): -1},(-1, 0): {(1, 4): -1},(0, -1): {(2, 3): -1},(0, 0): {(2, 4): -0.1}},(2, 5): {(1, 0): {(3, 5): -1},(0, 1): {(2, 5): -1},(-1, 0): {(1, 5): -1},(0, -1): {(2, 4): -1},(0, 0): {(2, 5): -0.1}},(3, 0): {(1, 0): {(4, 0): -100},(0, 1): {(3, 1): -100},(-1, 0): {(2, 0): -100},(0, -1): {(3, 0): -100},(0, 0): {(3, 0): -100}},(3, 1): {(1, 0): {(4, 1): -100},(0, 1): {(3, 2): -100},(-1, 0): {(2, 1): -100},(0, -1): {(3, 0): -100},(0, 0): {(3, 1): -100}},(3, 2): {(1, 0): {(4, 2): -1},(0, 1): {(3, 3): -1},(-1, 0): {(2, 2): -1},(0, -1): {(3, 1): -1},(0, 0): {(3, 2): -0.1}},(3, 3): {(1, 0): {(4, 3): -100},(0, 1): {(3, 4): -100},(-1, 0): {(2, 3): -100},(0, -1): {(3, 2): -100},(0, 0): {(3, 3): -100}},(3, 4): {(1, 0): {(4, 4): -1},(0, 1): {(3, 5): -1},(-1, 0): {(2, 4): -1},(0, -1): {(3, 3): -1},(0, 0): {(3, 4): -0.1}},(3, 5): {(1, 0): {(4, 5): -1},(0, 1): {(3, 5): -1},(-1, 0): {(2, 5): -1},(0, -1): {(3, 4): -1},(0, 0): {(3, 5): -0.1}},(4, 0): {(1, 0): {(5, 0): -1},(0, 1): {(4, 1): -1},(-1, 0): {(3, 0): -1},(0, -1): {(4, 0): -1},(0, 0): {(4, 0): -0.1}},(4, 1): {(1, 0): {(5, 1): -1},(0, 1): {(4, 2): -1},(-1, 0): {(3, 1): -1},(0, -1): {(4, 0): -1},(0, 0): {(4, 1): -0.1}},(4, 2): {(1, 0): {(5, 2): -1},(0, 1): {(4, 3): -1},(-1, 0): {(3, 2): -1},(0, -1): {(4, 1): -1},(0, 0): {(4, 2): -0.1}},(4, 3): {(1, 0): {(5, 3): -1},(0, 1): {(4, 4): -1},(-1, 0): {(3, 3): -1},(0, -1): {(4, 2): -1},(0, 0): {(4, 3): -0.1}},(4, 4): {(1, 0): {(5, 4): -1},(0, 1): {(4, 5): -1},(-1, 0): {(3, 4): -1},(0, -1): {(4, 3): -1},(0, 0): {(4, 4): -0.1}},(4, 5): {(1, 0): {(5, 5): -1},(0, 1): {(4, 5): -1},(-1, 0): {(3, 5): -1},(0, -1): {(4, 4): -1},(0, 0): {(4, 5): -0.1}},(5, 0): {(1, 0): {(6, 0): -1},(0, 1): {(5, 1): -1},(-1, 0): {(4, 0): -1},(0, -1): {(5, 0): -1},(0, 0): {(5, 0): -0.1}},(5, 1): {(1, 0): {(6, 1): -1},(0, 1): {(5, 2): -1},(-1, 0): {(4, 1): -1},(0, -1): {(5, 0): -1},(0, 0): {(5, 1): -0.1}},(5, 2): {(1, 0): {(6, 2): -1},(0, 1): {(5, 3): -1},(-1, 0): {(4, 2): -1},(0, -1): {(5, 1): -1},(0, 0): {(5, 2): -0.1}},(5, 3): {(1, 0): {(6, 3): -1},(0, 1): {(5, 4): -1},(-1, 0): {(4, 3): -1},(0, -1): {(5, 2): -1},(0, 0): {(5, 3): -0.1}},(5, 4): {(1, 0): {(6, 4): -1},(0, 1): {(5, 5): -1},(-1, 0): {(4, 4): -1},(0, -1): {(5, 3): -1},(0, 0): {(5, 4): -0.1}},(5, 5): {(1, 0): {(6, 5): -1},(0, 1): {(5, 5): -1},(-1, 0): {(4, 5): -1},(0, -1): {(5, 4): -1},(0, 0): {(5, 5): -0.1}},(6, 0): {(1, 0): {(6, 0): -1},(0, 1): {(6, 1): -1},(-1, 0): {(5, 0): -1},(0, -1): {(6, 0): -1},(0, 0): {(6, 0): -0.1}},(6, 1): {(1, 0): {(6, 1): -1},(0, 1): {(6, 2): -1},(-1, 0): {(5, 1): -1},(0, -1): {(6, 0): -1},(0, 0): {(6, 1): -0.1}},(6, 2): {(1, 0): {(6, 2): -1},(0, 1): {(6, 3): -1},(-1, 0): {(5, 2): -1},(0, -1): {(6, 1): -1},(0, 0): {(6, 2): -0.1}},(6, 3): {(1, 0): {(6, 3): -1},(0, 1): {(6, 4): -1},(-1, 0): {(5, 3): -1},(0, -1): {(6, 2): -1},(0, 0): {(6, 3): -0.1}},(6, 4): {(1, 0): {(6, 4): -1},(0, 1): {(6, 5): -1},(-1, 0): {(5, 4): -1},(0, -1): {(6, 3): -1},(0, 0): {(6, 4): -0.1}},(6, 5): {(1, 0): {(6, 5): -1},(0, 1): {(6, 5): -1},(-1, 0): {(5, 5): -1},(0, -1): {(6, 4): -1},(0, 0): {(6, 5): -0.1}}}




