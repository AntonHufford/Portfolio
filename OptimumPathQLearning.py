#a q-learning algorithm that finds the optimum path 
#through a maze, animated with pygame, showing the 
#updated path every 100 iterations

import numpy as np
import pygame
import sys
import time
pygame.init()

epsilon = 0.9
discount_factor = 0.9
learning_rate = 0.9

width = 1000
height = 500
total = 0
env_x = 25
env_y = 50
steps = 0
x = 0
y = 0
agent_x = 0
agent_y = 100

color = (66, 135, 245)
pygame.display.set_caption("optimum path")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

q_values = np.random.random((env_x, env_y, 4))

rewards = np.full((25, 50), -1)
drawn = np.zeros((25, 50))

#definition of path walls

rewards[22][39] = 75

rewards[7:12, 10] = -100
rewards[7:12, 14] = -100
rewards[11, 11:15] = -100
rewards[7, 11:15] = -100

rewards[16:19, 12] = -100
rewards[16:19, 21] = -100
rewards[16, 12:22] = -100
rewards[19, 12:22] = -100

rewards[6, 30:36] = -100

rewards[19:24, 14] = -100
rewards[23, 2:14] = -100
rewards[17, 38:44] = -100
rewards[14, 38:44] = -100
rewards[14:18, 37] = -100
rewards[14:18, 44] = -100

rewards[4:14, 22] = -100

rewards[21:25, 45] = -100
rewards[21, 46:49] = -100

rewards[12:22, 27] = -100
rewards[12:23, 34] = -100
rewards[12, 27:34] = -100
rewards[22, 27:34] = -100

rewards[12, 27:50] = -100
rewards[14:21, 48] = -100

rewards[11, 0:10] = -100
rewards[12:18, 7] = -100
rewards[18, 22:27] = -100
rewards[10, 14:22] = -100
rewards[2:10, 39] = -100
rewards[2:12, 44] = -100

rewards[10, 22:40] = -100
rewards[17:23, 4] = -100

def episode_complete(current_row_index, current_col_index):
    if rewards[current_row_index][current_col_index] == 75:
        return True
    
def get_next_action(current_row_index, current_col_index, epsilon):
    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row_index, current_col_index])
    else:
        return np.random.randint(4)
    
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


for episode in range(1201):
    drawn.fill(0)
    screen.fill((0, 0, 0))
    
    if 1000 < episode:
        epsilon = 0.95
    elif 100 < episode:
        epsilon = 0.9
    else:
        epsilon = 0.2
    
    for i in range(len(rewards)):
        for j in range(len(rewards[i])):
            if rewards[i][j] == -100:
                pygame.draw.rect(screen, (42, 163, 127), (x, y, 20, 20), 5)
            x += 20
        x = 0
        if y == 480:
            y = 0
        else:
            y += 20

    total += steps
    steps = 0
    row_index = 5
    col_index = 0
    
    if episode == 1200:
        color = (180, 202, 237)
        avg = total / episode
        print("Average steps = ",avg)
        epsilon = 1
        
    while not episode_complete(row_index, col_index):
        
        
        action_index = get_next_action(row_index, col_index, epsilon)

        
        old_row_index, old_col_index = row_index, col_index
        row_index, col_index = get_next_location(row_index, col_index, action_index)
        reward = rewards[row_index, col_index]
        old_q_value = q_values[old_row_index, old_col_index, action_index]
        temporal_difference = reward + (discount_factor * np.max(q_values[row_index, col_index])) - old_q_value            
        new_q_value = old_q_value + (learning_rate * temporal_difference)
        q_values[old_row_index, old_col_index, action_index] = new_q_value
        

        if steps > 9999:
            break
        
        steps += 1
        agent_x = (col_index * 20)
        agent_y = (row_index * 20)
            
        if drawn[row_index][col_index] == 0 and episode % 100 == 0:


            pygame.draw.rect(screen, color, (agent_x, agent_y, 20, 20), 2)
            pygame.draw.rect(screen, (117, 240, 117), (780, 440, 20, 20))
            pygame.draw.rect(screen, (255, 255, 255), (0, 100, 20, 20))
        

            pygame.display.flip()
        drawn[row_index][col_index] = 1
           
    if episode % 100 == 0:
        print(episode, steps)
    episode += 1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
time.sleep(20)
pygame.quit()
sys.exit()

        
    
