import pygame
from eightpuzzlesolver import aStar

pygame.init()
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
clock = pygame.time.Clock()

# Switch for human or playthrough
HUMAN = False

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Find centers
centers = []
box_w = WIDTH // 3
box_h = HEIGHT // 3
for j in range(1,4): # switched i and j to make numbers ordered horizontally.
    for i in range(1,4): #remember the colon!
        centers = centers + [( (i * box_w + (i-1) * box_w) // 2 , (j * box_h + (j-1) * box_h) // 2 )]
#print (centers)

# Render numbers
font = pygame.font.Font(None, 36)
numbers = []
for i in range(0,9): # Don't forget the colon, damnit!
    numbers = numbers + [font.render(str(i), True, BLUE)]

# Default board position (to be randomized eventually)
board2 = [1,5,3,2,8,4,6,7,0] # no solution?
board4 = [1,0,2,4,5,3,6,7,8]
win = [0,1,2,3,4,5,6,7,8]

# Surely there's a better way to do this. It reeks of a succinct pattern...
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

coordinates = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
# originally (s1,s2), but I'll assume one goal-state :P
def man_distance(s1): 
    sum = 0
    for i in range(0,9): #Fucking colon!
        ideal = coordinates[win[i]]
        current = coordinates[s1[i]] #I had board[i] instead of s1[i]
        sum +=  abs(ideal[0] - current[0]) + abs(ideal[1] -current[1])
    return sum


if HUMAN == True:

    while not done:
        nearest_center = -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN: #need to check this or .key produces an error
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                posi = event.pos
                print (posi)
                # find nearest center -- should totally be a function of its own :p
                dis = []
                px = posi[0]
                py = posi[1]
                for i in range(0,9):
                    dis = dis + [(px-centers[i][0])**2 + (py-centers[i][1])**2] # powers are with **, not ^
                nearest_center = dis.index(min(dis))
                print ("The position is: " + str(board[nearest_center]))    
                    
        # perform swap if next to 0.
        if nearest_center != -1:
            zero_loc = board.index(0)
            adjacents = get_adjacent(nearest_center)
            if zero_loc in adjacents:
                board[zero_loc] = board[nearest_center]
                board[nearest_center] = 0
                print("The Manhattan distance is: " + str(man_distance(board)))
            else:
                screen.fill(RED) # red doesn't
                pygame.time.wait(500) # wait works
            if win == board: # works, but just closing is ugly
                done = True #doing anything else without more modular code seems icky :p
            
        screen.fill(WHITE)
        
        # Draw the grid
        for i in range(1,3): # range(1,2) only drew one line!
            pygame.draw.line(screen, BLACK, [i * (WIDTH // 3), 0], [i * (WIDTH // 3),HEIGHT], 5)
            pygame.draw.line(screen, BLACK, [0, i * (HEIGHT // 3)], [WIDTH, i * (HEIGHT // 3)],5)
        
        # Draw 'numbers'
        for i in range(0,9):
            p = board[i]
            if p != 0:
                screen.blit(numbers[p], (centers[i][0] - numbers[p].get_width() // 2, centers[i][1] - numbers[p].get_height() // 2))
            #pygame.draw.circle(screen, BLUE, centers[i], 10)
            
        pygame.display.flip()
            
        clock.tick(60)
        
else: 
    solution = aStar(board4,win)
    print("Length = " + str(len(solution)))
    print("Solution = " + str(solution))
    for step in solution:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN: #need to check this or .key produces an error
                if event.key == pygame.K_ESCAPE:
                    done = True
                    
        screen.fill(WHITE)
        
        # Draw the grid
        for i in range(1,3): # range(1,2) only drew one line!
            pygame.draw.line(screen, BLACK, [i * (WIDTH // 3), 0], [i * (WIDTH // 3),HEIGHT], 5)
            pygame.draw.line(screen, BLACK, [0, i * (HEIGHT // 3)], [WIDTH, i * (HEIGHT // 3)],5)
        
        # Draw 'numbers'
        for i in range(0,9):
            p = step[i]
            if p != 0:
                screen.blit(numbers[p], (centers[i][0] - numbers[p].get_width() // 2, centers[i][1] - numbers[p].get_height() // 2))
            #pygame.draw.circle(screen, BLUE, centers[i], 10)
            
        pygame.display.flip()
        
        pygame.time.wait(350)
        clock.tick(60)
    

pygame.time.wait(1500)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
