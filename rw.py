import numpy as np
rewards = np.full((25, 50), -1)

#module for wall definitions
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

    
    
    

    
        
        
        

        
        

            


        

           
        

        
    

