import copy

class State():
    def __init__(self, value=[0,0,0,0,0,0,0,0,0], turn=1):
        self.value = value
        self.turn = turn

    def get_cost(self):
        
        # is_win, is_lose, is_draw 함수가 필요해서 State class 에도 동일한 함수를 추가
        if self.is_win():
            return 1
        elif self.is_lose():
            return -1
        elif self.is_draw():
            return 0

        # turn에 따라 cost를 max or min 하기
        if self.turn == 1:
            cost = max([next_state.get_cost() for next_state in self.next_states()])
        
        elif self.turn == -1:
            cost = min([next_state.get_cost() for next_state in self.next_states()])

        return cost
    
    # 가로 세로 대각선 값을 더해서 어느 줄이건 3 나오면 승리
    def is_win(self):
        d_sum1 = 0
        d_sum2 = 0

        for i in range(3):
            h_sum = 0
            v_sum = 0
            for j in range(3):
                h_sum = h_sum + self.value[i + j*3]
                v_sum = v_sum + self.value[i*3 + j]
                
            if h_sum == 3 or v_sum == 3:
                return True
            
            d_sum1 = d_sum1 + self.value[i*4]
            d_sum2 = d_sum2 + self.value[i*2 + 2]

        if d_sum1 == 3 or d_sum2 == 3:
            return True

    # 가로 세로 대각선 값을 더해서 어느 줄이건 -3 나오면 패배
    def is_lose(self):
        d_sum1 = 0
        d_sum2 = 0

        for i in range(3):
            h_sum = 0
            v_sum = 0
            for j in range(3):
                h_sum = h_sum + self.value[i + j*3]
                v_sum = v_sum + self.value[i*3 + j]
                
            if h_sum == -3 or v_sum == -3:
                return True
            
            d_sum1 = d_sum1 + self.value[i*4]
            d_sum2 = d_sum2 + self.value[i*2 + 2]

        if d_sum1 == -3 or d_sum2 == -3:
            return True

    # 데이터에 0이 하나라도 있으면 게임 진행중
    def is_draw(self):
        full = True
        for i in range(9):
            if self.value[i] == 0:
                full = False
                break

        return full
    
    # 현재 state 에서 i번째 자리를 채워서 새 state 만듦
    def new_state(self, i):
        data = copy.deepcopy(self.value)
        data[i] = self.turn
        next_turn = 1
        if self.turn == 1:
            next_turn = -1
            
        return State(data, next_turn)
        
    # 현재 state 에서 만들 수 있는 state list 만듦
    def next_states(self):        
        candidates = [i for i,one in enumerate(self.value) if one == 0]

        result = [self.new_state(index) for index in candidates]

        return result


class Game():
    def __init__(self, value=[0,0,0,0,0,0,0,0,0], turn=1):
        self.game_state = State(value=value, turn=turn)

    def reset(self):
        self.game_state = State()

    # 보기 편하게 출력 - 값에 따라 1은 'X', 0은 '-', -1은 'O'로 표시
    # X--
    # -O-
    # ---
    def print_state(self):
        symbol_dict = {1:'X', 0:'-', -1:'O'}
            
        for i in range(3):
            for j in range(3):
                value = self.game_state.value[i*3+j]
                symbol = symbol_dict[value]
                print(symbol, end='')
            print('')
        print('')

    # 가로 세로 대각선 값을 더해서 어느 줄이건 3 나오면 승리
    def is_win(self):
        d_sum1 = 0
        d_sum2 = 0

        for i in range(3):
            h_sum = 0
            v_sum = 0
            for j in range(3):
                h_sum = h_sum + self.game_state.value[i + j*3]
                v_sum = v_sum + self.game_state.value[i*3 + j]
                
            if h_sum == 3 or v_sum == 3:
                return True
            
            d_sum1 = d_sum1 + self.game_state.value[i*4]
            d_sum2 = d_sum2 + self.game_state.value[i*2 + 2]

        if d_sum1 == 3 or d_sum2 == 3:
            return True

    # 가로 세로 대각선 값을 더해서 어느 줄이건 -3 나오면 패배
    def is_lose(self):
        d_sum1 = 0
        d_sum2 = 0

        for i in range(3):
            h_sum = 0
            v_sum = 0
            for j in range(3):
                h_sum = h_sum + self.game_state.value[i + j*3]
                v_sum = v_sum + self.game_state.value[i*3 + j]
                
            if h_sum == -3 or v_sum == -3:
                return True
            
            d_sum1 = d_sum1 + self.game_state.value[i*4]
            d_sum2 = d_sum2 + self.game_state.value[i*2 + 2]

        if d_sum1 == -3 or d_sum2 == -3:
            return True

    # 데이터에 0이 하나라도 있으면 게임 진행중
    def is_draw(self):
        full = True
        for i in range(9):
            if self.game_state.value[i] == 0:
                full = False
                break

        return full

    # row 입력 받기
    def input_row(self):
        row = input('input row index: ')
        if not row.isnumeric():
            print('input is not a number')
            row = self.input_row()

        row = int(row)
        if row<0 or row>2:
            print('input should be from 0 to 2')
            row = self.input_row()

        return row

    # column 입력 받기
    def input_column(self):
        column = input('input column index: ')
        if not column.isnumeric():
            print('input is not a number')
            column = self.input_column()

        column = int(column)
        if column<0 or column>2:
            print('input should be from 0 to 2')
            column = self.input_column()

        return column

    # row, column 입력 받기
    def input_row_column(self):
        row = self.input_row()
        column = self.input_column()
        if self.game_state.value[row*3 + column] != 0:
            print('The position is used already')
            row, column = self.input_row_column()
        
        return row, column

    # 다음 단계로
    def next_step(self):
        
        # 플레이어의 차례이면 놓을 자리를 입력 받아 state를 만들고 출력     
        if self.game_state.turn == 1:
            row, column = self.input_row_column()
            self.game_state = self.game_state.new_state(row*3 + column)
            self.print_state()
            
        # PC의 차례이면 cost 가 min 되는 state를 찾아 해당 state를 만들고 출력
        elif self.game_state.turn == -1:

            pos_states = self.game_state.next_states()
            
            mincost = min([state.get_cost() for state in pos_states])
            
            for state in pos_states:
                if state.get_cost() == mincost:
                    self.game_state = state
                    self.print_state()
                    break

        else:
            print('')
            
    # 이기거나 지거나 비길 때까지 플레이
    def play(self):
        while True:
            if self.is_win():
                print("You win!")
                break
            if self.is_lose():
                print("You lose!")
                break
            if self.is_draw():
                print("It is a draw.")
                break

            self.next_step()


tictactoe = Game([0,0,0,0,0,0,0,0,0], 1)
tictactoe.play()

