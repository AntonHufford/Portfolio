import numpy as np
import pygame
import sys
import time
#module I wrote to keep maze wall definitions in, also in the github portfolio:
import rw

pygame.init()

epsilon = 0.9            
discount_factor = 0.9
learning_rate = 0.9

width = 1000
height = 500
steps = 0
total = 0
env_x = 25
env_y = 50

#drawing coordinates:
x = 0
y = 0
agent_x = 0
agent_y = 100
color = (66, 135, 245)

iterations = 1200
max_steps = 10000
delay = 5

pygame.display.set_caption("optimum path")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

#3d tensor of q values based on location and 4 possible actions
q_values = np.random.random((env_x, env_y, 4))

#to avoid redrawing squares:
drawn = np.zeros((25, 50)) 

#did agent reach the goal?
def episode_complete(current_row_index, current_col_index):
    if rw.rewards[current_row_index][current_col_index] == 75:
        return True
    
#what to do next? act on experience or explore?   
def get_next_action(current_row_index, current_col_index, epsilon):
    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row_index, current_col_index])
    else:
        return np.random.randint(4)

#update location
def get_next_location(current_row_index, current_col_index, action_index):
    new_row_index = current_row_index
    new_col_index = current_col_index
    if action_index == 0 and current_row_index > 0:
        new_row_index -= 1
    elif action_index == 1 and current_col_index < 49:
        new_col_index += 1
    elif action_index == 2 and current_row_index < 24:
        new_row_index += 1
    elif action_index == 3 and current_col_index > 0:
        new_col_index -= 1
    return new_row_index, new_col_index

#the final iteration will be with epsilon = 1, and hence reveal optimum path (no randomness). 
for episode in range((iterations + 1)): 

    drawn.fill(0)
    screen.fill((0, 0, 0))
    
    #how experience vs explore is decided. explore a lot at the beginning and act on experience later
    if 1000 < episode:
        epsilon = 0.95
    elif 100 < episode:
        epsilon = 0.9
    else:
        epsilon = 0.2
        
    #drawing loop
    for i in range(len(rw.rewards)):
        for j in range(len(rw.rewards[i])):
            if (rw.rewards[i][j] == -100) and (episode % 100 == 0):
                pygame.draw.rect(screen, (42, 163, 127), (x, y, 20, 20), 5)
            x += 20
        x = 0
        if y == 480:
            y = 0
        else:
            y += 20

    total += steps
    steps = 0
    
    #return to starting point
    row_index = 5
    col_index = 0
    
    if episode == iterations:
        color = (180, 202, 237)
        avg = round(total / episode, 2)
        epsilon = 1
        
    while not episode_complete(row_index, col_index):
        
        action_index = get_next_action(row_index, col_index, epsilon)
        old_row_index, old_col_index = row_index, col_index
        row_index, col_index = get_next_location(row_index, col_index, action_index)
        #receive reward for current loction
        reward = rw.rewards[row_index, col_index]
        #save old q value before updating
        old_q_value = q_values[old_row_index, old_col_index, action_index]
        #how much should the q value change?
        temporal_difference = reward + (discount_factor * np.max(q_values[row_index, col_index])) - old_q_value            
        #update q value for current location
        new_q_value = old_q_value + (learning_rate * temporal_difference)
        q_values[old_row_index, old_col_index, action_index] = new_q_value
        
        if steps == max_steps:
            break
        
        steps += 1
        
        #drawing coordinates
        agent_x = (col_index * 20)
        agent_y = (row_index * 20)
        
        #update best path drawing every 100 iterations, make sure not to redraw squares
        if drawn[row_index][col_index] == 0 and episode % 100 == 0:

            pygame.draw.rect(screen, color, (agent_x, agent_y, 20, 20), 2)
            pygame.draw.rect(screen, (117, 240, 117), (780, 440, 20, 20))
            pygame.draw.rect(screen, (255, 255, 255), (0, 100, 20, 20))
            pygame.display.flip()
            
        drawn[row_index][col_index] = 1
        
    if episode % 100 == 0:
        print(episode, steps)

    if episode == (iterations):
        print("Average steps =", avg)
        print("Optimum path is", steps, "steps.")
        
    episode += 1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
time.sleep(delay)
pygame.quit()
sys.exit()

        
    
