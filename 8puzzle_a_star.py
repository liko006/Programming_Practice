'''
1. current state 가 정답인지 확인 -> 정답이면 정답 정리하고 종료
2. current state 에서 할 수 있는 action 들을 이용하여 next state 들을 만들기
3. next state 들을 f(n) 값이 작은 순서대로 위치하도록 queue 에추가
4. queue 에서다음 state 를가져오기
5. 1로 돌아가서 반복

f(n) = g(n) + h(n) = 시작 state 부터의 경로(path) 수 + 정답과 다른 숫자 개수
'''
# "initial" -> "012345678"
import copy
import random
import time

# define State class to have current state and its current cost
class State:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost
        
    def getState(self):
        return self.state
    
    def getCost(self):
        return self.cost

def is_goal(state) -> bool:
    if state == "012345678":
        return True
    else:
        return False

# state needs to be in 1x9 array shape
def getInvCount(state):

    inv_count = 0; 
    for i in range(9):
        for j in range(i+1,9):
            if state[i] > state[j] and state[i] != 0 and state[j] != 0: 
                 inv_count += 1 
    return inv_count 
  
# whether state is solvable or not
def is_solvable(state): 

    # Count inversions in given 8 puzzle 
    invCount = getInvCount(state); 
  
    # return true if inversion count is even. 
    return (invCount%2 == 0); 
    
def change_states(state, i, j):
    
    new_state = copy.deepcopy(state)
    new_state[i], new_state[j] = state[j], state[i]
    
    return "".join(new_state)    

# functions to help calculating h(n)
def moves_need(n, p):
    
    m = 0
    if n == 0:
        if p == 1 or p == 3:
            m = 1
        if p == 2 or p == 4 or p == 6:
            m = 2
        if p == 5 or p == 7:
            m = 3
        if p == 8:
            m = 4
            
    if n == 1:
        if p == 0 or p == 2 or p == 4:
            m = 1
        if p == 3 or p == 5 or p == 7:
            m = 2
        if p == 6 or p == 8:
            m = 3  
            
    if n == 2:
        if p == 1 or p == 5:
            m = 1
        if p == 0 or p == 4 or p == 8:
            m = 2
        if p == 3 or p == 7:
            m = 3
        if p == 6:
            m = 4
            
    if n == 3:
        if p == 0 or p == 4 or p == 6:
            m = 1
        if p == 1 or p == 5 or p == 7:
            m = 2
        if p == 2 or p == 8:
            m = 3 
            
    if n == 4:
        if p == 1 or p == 3 or p == 5 or p == 7:
            m = 1
        if p == 0 or p == 2 or p == 4 or p == 8:
            m = 2
            
    if n == 5:
        if p == 2 or p == 4 or p == 8:
            m = 1
        if p == 1 or p == 3 or p == 7:
            m = 2
        if p == 0 or p == 6:
            m = 3 

    if n == 6:
        if p == 3 or p == 7:
            m = 1
        if p == 0 or p == 4 or p == 8:
            m = 2
        if p == 1 or p == 5:
            m = 3
        if p == 2:
            m = 4
            
    if n == 7:
        if p == 6 or p == 4 or p == 8:
            m = 1
        if p == 1 or p == 3 or p == 5:
            m = 2
        if p == 0 or p == 2:
            m = 3 
            
    if n == 8:
        if p == 5 or p == 7:
            m = 1
        if p == 2 or p == 4 or p == 6:
            m = 2
        if p == 1 or p == 3:
            m = 3
        if p == 0:
            m = 4
    
    return m

# function for computing expected cost for next step
def hn(next_state):
    
    goal = '012345678'
    cnt = 0
    
    for i in range(9):
        if goal[i] != next_state[i]:
            cnt += 1
            cnt += moves_need(int(next_state[i]), i)
    
    return cnt

# function for creating next states
def next_states(state):  
    
    # g(n) is 1 for all moves
    cost = state.cost + 1
    
    current_state = list(state.state)
    
    result = []
    
    if current_state[0] == '0':
        result.append([State(change_states(current_state, 0, 1), cost + hn(change_states(current_state, 0, 1))), state])
        result.append([State(change_states(current_state, 0, 3), cost + hn(change_states(current_state, 0, 3))), state])
    if current_state[1] == '0':
        result.append([State(change_states(current_state, 1, 0), cost + hn(change_states(current_state, 1, 0))), state])
        result.append([State(change_states(current_state, 1, 2), cost + hn(change_states(current_state, 1, 2))), state])
        result.append([State(change_states(current_state, 1, 4), cost + hn(change_states(current_state, 1, 4))), state])
    if current_state[2] == '0':
        result.append([State(change_states(current_state, 2, 1), cost + hn(change_states(current_state, 2, 1))), state])
        result.append([State(change_states(current_state, 2, 5), cost + hn(change_states(current_state, 2, 5))), state])
    if current_state[3] == '0':
        result.append([State(change_states(current_state, 3, 0), cost + hn(change_states(current_state, 3, 0))), state])
        result.append([State(change_states(current_state, 3, 4), cost + hn(change_states(current_state, 3, 4))), state])
        result.append([State(change_states(current_state, 3, 6), cost + hn(change_states(current_state, 3, 6))), state])
    if current_state[4] == '0':
        result.append([State(change_states(current_state, 4, 1), cost + hn(change_states(current_state, 4, 1))), state])
        result.append([State(change_states(current_state, 4, 3), cost + hn(change_states(current_state, 4, 3))), state])
        result.append([State(change_states(current_state, 4, 5), cost + hn(change_states(current_state, 4, 5))), state])
        result.append([State(change_states(current_state, 4, 7), cost + hn(change_states(current_state, 4, 7))), state])
    if current_state[5] == '0':
        result.append([State(change_states(current_state, 5, 2), cost + hn(change_states(current_state, 5, 2))), state])
        result.append([State(change_states(current_state, 5, 4), cost + hn(change_states(current_state, 5, 4))), state])
        result.append([State(change_states(current_state, 5, 8), cost + hn(change_states(current_state, 5, 8))), state])
    if current_state[6] == '0':
        result.append([State(change_states(current_state, 6, 3), cost + hn(change_states(current_state, 6, 3))), state])
        result.append([State(change_states(current_state, 6, 7), cost + hn(change_states(current_state, 6, 7))), state])
    if current_state[7] == '0':
        result.append([State(change_states(current_state, 7, 6), cost + hn(change_states(current_state, 7, 6))), state])
        result.append([State(change_states(current_state, 7, 4), cost + hn(change_states(current_state, 7, 4))), state])
        result.append([State(change_states(current_state, 7, 8), cost + hn(change_states(current_state, 7, 8))), state])
    if current_state[8] == '0':
        result.append([State(change_states(current_state, 8, 7), cost + hn(change_states(current_state, 8, 7))), state])
        result.append([State(change_states(current_state, 8, 5), cost + hn(change_states(current_state, 8, 5))), state])
    
    return result    


# compare the expected cost and insert the states in ascending order
def comp_fn(state_list, nxt_st):
    
    length = len(state_list)
    left = 0 
    right = length-1

    while left<=right:
        mid = (left+right)//2
        if state_list[mid][0].cost == nxt_st[0].cost:
            state_list.insert(mid, nxt_st)
            break
        elif state_list[mid][0].cost > nxt_st[0].cost:
            right = mid-1
            if state_list[right][0].cost < nxt_st[0].cost:
                state_list.insert(right, nxt_st)
                break
        elif state_list[mid][0].cost < nxt_st[0].cost:
            if state_list[right][0].cost <= nxt_st[0].cost:
                state_list.append(nxt_st)
                break
            left = mid+1
    
    return state_list


# make random array from 0-8
temp = random.sample(range(0,9),9)

for i in range(9):
    temp[i] = str(temp[i])

# save the random array as strings
temp = "".join(temp)

# create instance with random state and initial cost
initial = State(temp, 0)

state_list = []
initial_state = [initial, ]

state_list.append(initial_state)
state_dic = {initial_state[0].state:""}

# save starting time
start_t = time.time()

if is_solvable(temp):
    
    i = 0
    while True:
        current_state = state_list[i]

        if is_goal(current_state[0].state):
        
            print("goal!!!")
            # print time spent
            print('time: ', time.time()-start_t)
            # print the # of iteration
            print(i)
            # print the cost need to reach the goal
            print(current_state[0].cost)

            path = [current_state[0].state]
            
            j = 0
            while j >=0 : 
                
                if j == 0:
                    current_path = [current_state[1].state, state_dic[current_state[1].state]]
                
                path.insert(0, current_path[0])
            
                if current_path[1] == "":
                    print(path)
                    break
                
                current_path = [current_path[1], state_dic[current_path[1]]]
                
                j += 1
                
            break
        
        next_state_list = next_states(current_state[0])
               
        for state in next_state_list:
            if state[0].state not in state_dic:
                state_dic[state[0].state] = state[1].state
                # order the states by lowest expected cost (f(n))
                state_list = comp_fn(state_list, state)
                
        
        # if the program takes too long to get the answer, break and notice
        if time.time() > (start_t + 20):
            print('takes too long')
            break
    
        i = i+1
        if i == len(state_list):
            break
            
else:
    print('Not Solvable')
