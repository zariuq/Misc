from operator import itemgetter
import pygame

# To be solved via A*


board2 = [1,5,3,2,8,4,6,7,0] # no solution
board4 = [1,0,2,4,5,3,6,7,8]
win = [0,1,2,3,4,5,6,7,8]

# first we need a heuristic. I'll use the manhattan distance

coordinates = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
# originally (s1,s2), but I'll assume one goal-state :P
def man_distance(s1): 
    sum = 0
    for i in range(0,9): #Fucking colon!
        ideal = coordinates[win[i]]
        current = coordinates[s1[i]] #I had board[i] instead of s1[i]
        sum +=  abs(ideal[0] - current[0]) + abs(ideal[1] -current[1])
    return sum
    
#print (man_distance(board))
# I tried making the boards tuples, but non-mutability is a bitch. So tuple it to hash it~
print (hash(tuple(board)))
print (hash(tuple(win)))
    
# f_score = h + step-distance from initial_state
# (node, f_score) may be enough?

def get_adjacent(index):
    if index == 0:
        return [1,3]
    if index == 1:
        return [0,2,4]
    if index == 2:
        return [1,5]
    if index == 3:
        return [0,4,6]
    if index == 4:
        return [1,3,5,7]
    if index == 5:
        return [2,4,8]
    if index == 6:
        return [3,7]
    if index == 7:
        return [4,6,8]
    if index == 8:
        return [5,7]
    return []

def get_neighbors(state):
    neighbors = []
    #print(state) # I had passed in the (state,f_score)
    zero_loc = state.index(0)
    next_moves = get_adjacent(zero_loc)
    for m in next_moves:
        to_add = list(state) #Fuck, normal equal is like passing a pointer around :< I should be using Haskell...
        to_add[zero_loc] = to_add[m]
        to_add[m] = 0
        neighbors += [to_add]
    return neighbors

# >_> I thought the order of the path would be reversed! Odd...
# well, it IS backwards in a sense
def reconscructPath(came,cur):
    path = [cur]
    cur_h = hash(tuple(cur))
    while cur_h in came:
        cur = came[cur_h]
        path.append(cur)
        #path += [cur]
        cur_h = hash(tuple(cur))
    path.reverse()
    return path

def aStar(initial_state, goal):

    fringe = [(initial_state, man_distance(initial_state))]
    openSet = {}
    openSet[hash(tuple(initial_state))] = initial_state
    closedNodes = {} # to keep track of visited states
    cameFrom = {} # to keep track of prior states
    g_score = {}
    g_score[hash(tuple(initial_state))] = 0

    while fringe != []: 
        current = fringe.pop() #the last element has the smallest f_score
        current_hash = hash(tuple(current[0]))
        if current[0] == win:
            return reconscructPath(cameFrom,current[0]) # reconscruct path
        closedNodes[current_hash] = current[0]
        del openSet[current_hash]
        
        neighbor_nodes = get_neighbors(current[0])
        for neighbor in neighbor_nodes:
            neighbor_hash = hash(tuple(neighbor))
            if neighbor_hash in closedNodes: # forgot colon again
                continue
            temp_g_score = g_score[current_hash] + 1 #no real difference :D
            
            if neighbor_hash not in openSet:
                cameFrom[neighbor_hash] = current[0]
                g_score[neighbor_hash] = temp_g_score
                openSet[neighbor_hash] = neighbor
                fringe += [(neighbor, man_distance(neighbor) + temp_g_score)]
                #sorted(fringe, key=itemgetter[0], reverse=True) # sort by f_score, min at end for .pop 
                fringe.sort(key=lambda s: s[1], reverse=True) #so the itemgetter shit didn't work.. lambda ftw!
            elif neighbor_hash in g_score:
                if temp_g_score < g_score[neighbor_hash]:
                    cameFrom[neighbor_hash] = current[0]
                    g_score[neighbor_hash] = temp_g_score
                    openSet[neighbor_hash] = neighbor
                    #f_score?
        print (len(fringe))
                
        
    return []
    
solution = aStar(board4,win)

print(solution)









