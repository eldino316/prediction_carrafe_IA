
class WaterJugProblem:
    def __init__(self,capicity_of_jug1,capacity_of_ju2,initial_jug1,initial_jug2,final_state_jug1,final_state_jug2):
        self.capj1 = capicity_of_jug1
        self.capj2 = capacity_of_ju2
        self.final_capj1 = final_state_jug1
        self.final_capj2 = final_state_jug2
        self.initialj1 = initial_jug1
        self.initialj2 = initial_jug2
        self.found_path = 0
        self.path_array = [(initial_jug1,initial_jug2)]
        #self.__findPath(self.initialj1,self.initialj2,0)
    
    def execute(self):
        self.__findPath(self.initialj1,self.initialj2,0)

        if self.found_path==0:
            return []
        else:
            return self.path_array

    def __findPath(self,current_capj1,current_capj2,current_depth):
        
        if current_depth>10:
            return 

        if (current_capj1,current_capj2)==(self.final_capj1,self.final_capj2):
            self.found_path = 1
            return 1 

        temp_states = self.__generateStates(current_capj1,current_capj2)
        for state in temp_states:
            if state not in self.path_array:
                self.path_array.append(state)
                a = self.__findPath(state[0],state[1],current_depth+1)
                #print(self.path_array,a)
                if a==1:
                    return 1
                else:
                    self.path_array.pop() 
        return

    def __generateStates(self,x,y):
        new_states = []

        if x>0:
            new_states.append((0,y))
        if y>0:
            new_states.append((x,0))
        if x<self.capj1:
            new_states.append((self.capj1,y))
        if y<self.capj2:
            new_states.append((x,self.capj2))
        if x+y<=self.capj1 and y>0:
            new_states.append((x+y,0))
        if x+y>=self.capj1 and y>0:
            new_states.append((self.capj1,y-(self.capj1-x)))
        if x+y<=self.capj2 and x>0:
            new_states.append((0,x+y))
        if x+y>=self.capj2 and x>0:
            new_states.append((x-(self.capj2-y),self.capj2))
        #print(x,y,new_states)
        return new_states
    def run_program(self):
        path=self.execute()
        if len(path)==0:
            return "NOT POSSIBLE"
        return path                

"""
start = WaterJugProblem(5,3,0,0,2,0)
path = start.execute()
if len(path)==0:
    print("NOT POSSIBLE")
else:
    for i in path:
        print(i)
"""