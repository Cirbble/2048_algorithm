#documentation and comments goes against  my job security 
#NEED TO DO:

from random import randint
class board2048(object):
    def __init__(self, pre=-1):
        if pre==-1:
            self.board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            a=[randint(0,3),randint(0,3)]
            b=[randint(0,3),randint(0,3)]
            while a==b:
                b=[randint(1,4),randint(1,4)]
            self.board[a[0]][a[1]]=2
            self.board[b[0]][b[1]]=2
        else:
            self.board=pre    
            pass

    def player_start(self):
        """Starts the main loop for playing the game
        This option is meant for a human player to play the game"""
        while self.check_fail() == False:
            print(self)
            player_move=input("Your move (wasd): ")
            if player_move=="p":
                print("PAUSED")
                return(2)
                break
            if self.swipe(player_move) == 1:
                self.gen_new_tile()
            else:
                print("invalid move")
        
        print(self)
        print("Game has finished")
        return(-1)
        
    def __str__(self):
        """String representation of the board state
        formatted to look pretty <3
        Can only print up to 4 digits long, use raw_print() if expecting bigger numbers
        """
        result="_____________________\n"
        for i in self.board:
            #temp="|{i[0]:4i}|{i[1]:4i}|{i[2]:4i}|{i[3]:4i}|\n"
            temp="|{:4}|{:4}|{:4}|{:4}|\n".format(i[0],i[1],i[2],i[3])
            result+=temp
            result+="_____________________\n"
            pass
        #result+="_____________________"
        return(result)
        pass
    
    def raw_print(self):
        """returns the board state as a string
        no formatting, can show numbers larger than 4 digits"""
        result=""

        for i in self.board:
            temp=""
            for j in i:
                temp+=str(j)
                temp+=", "
            result+=temp
            result+="\n"
        return(result)
        pass

    def detect_loss(self):
        """Detects if the board is unplayable
        Accomplished by seeing if there is any tile that is empty
        """
        loss=True
        for i in self.board:
            for j in i:
                if j==0:
                    loss=False
        if loss==True:
            return(True)
        if loss==False:
            return(False)
        
    def gen_new_tile(self): #make this more efficent if program is taking too long
        """Finds an empty space, then places either a 2 or a 4 on that tile"""
        temp=[randint(0,3),randint(0,3)]
        while self.board[temp[0]][temp[1]] != 0:
            temp=[randint(0,3),randint(0,3)]
            pass
        random_value=randint(1,10)
        if random_value==10:
            self.board[temp[0]][temp[1]]=4
        else:
            self.board[temp[0]][temp[1]]=2
        pass

    def swipe(self,in_dir):
        """
        Swipes the board, w for up, s for down, a for left, and d for right
        This is used for manual player controlled gameplay
        """
        if in_dir!= "w" and in_dir!="s" and in_dir!="a" and in_dir!="d":
            return(-1)
        if in_dir=="a":
            if self.verify_a() == -1:
                return(-1)
            self.merge_left()
            return(1)
        if in_dir=="d":
            if self.verify_d() == -1:
                return(-1)
            self.merge_right()
            return(1)
        if in_dir=="w":
            if self.verify_w() == -1:
                return(-1)
            self.merge_up()
            return(1)
        if in_dir=="s":
            if self.verify_s() == -1:
                return(-1)
            self.merge_down()
            return(1)
        return(-1)
        
    def copy_board(self):
        """does as the name implies, creates a copy of itself"""
        temp=[]
        for i in self.board:
            temp.append(i.copy())
        return(temp)
        pass
    
    def verify_w(self):
        """
        Checks to see if the swipe direction is valid
        """
        temp_board = self.copy_board()
        temp_board=board2048(temp_board)
        temp_board.merge_up()
        if temp_board.board==self.board:
            return(-1)
            pass
        else:
            return(1)

    def verify_a(self):
        """
        Checks to see if the swipe direction is valid
        """
        temp_board = self.copy_board()
        temp_board=board2048(temp_board)
        temp_board.merge_left()
        if temp_board.board==self.board:
            return(-1)
            pass
        else:
            return(1)
        
    def verify_s(self):
        """
        Checks to see if the swipe direction is valid
        """
        temp_board = self.copy_board()
        temp_board=board2048(temp_board)
        temp_board.merge_down()
        if temp_board.board==self.board:
            return(-1)
            pass
        else:
            return(1)
        
    def verify_d(self):
        """
        Checks to see if the swipe direction is valid
        """
        temp_board = self.copy_board()
        temp_board=board2048(temp_board)
        temp_board.merge_right()
        if temp_board.board==self.board:
            return(-1)
            pass
        else:
            return(1)

    def merge_left(self):
        """merges left"""
        new_board=[]
        for i in self.board:
            temp=[0,0,0,0]
            curr=0
            
            for j in i:
                if j != 0:
                    if temp[curr] == 0:
                        temp[curr] = j
                        
                    elif temp[curr] == j:
                        temp[curr]= j*2
                        curr+=1
                    else:
                        curr+=1
                        temp[curr]=j 
            new_board.append(temp)
                
            pass
        self.board=new_board
        
        pass

    def merge_right(self):
        """merges right"""
        new_board=[]
        for i in self.board:
            temp=[0,0,0,0]
            curr=3
            
            for j in i[::-1]:
                if j != 0:
                    if temp[curr] == 0:
                        temp[curr] = j
                        
                    elif temp[curr] == j:
                        temp[curr]= j*2
                        curr-=1
                    else:
                        curr-=1
                        temp[curr]=j 
            new_board.append(temp)
                
            pass
        self.board=new_board
        
        pass
    
    def merge_up(self):
        """merges up"""
        new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        len_board=len(self.board[0])
        for i in range(len_board): #i represents y
            curr=0
            for j in range(len_board): #j represents x
                if self.board[j][i] !=0:
                    if new[curr][i] == 0:
                        new[curr][i] = self.board[j][i]
                    elif new[curr][i] == self.board[j][i]:
                        new[curr][i]=int(self.board[j][i])*2
                        curr+=1
                    else:
                        curr+=1
                        new[curr][i]= self.board[j][i]
                        pass
                    pass
                pass
            pass
        pass
        self.board=new
        
    def merge_down(self):
        """merges down"""
        new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        len_board=len(self.board[0])
        temp=[]
        for i in range(len_board):
            temp.append(i)
        temp.reverse()
        for i in temp: #i represents y
            curr=temp[0]
            #print(curr)
            for j in temp: #j represents x
                if self.board[j][i] !=0:
                    #print("SPOTTED")
                    if new[curr][i] == 0:
                        new[curr][i] = self.board[j][i]
                        #print(10)
                        #print(new)
                    elif new[curr][i] == self.board[j][i]:
                        new[curr][i]=int(self.board[j][i])*2
                        curr-=1
                        #print(20)
                    else:
                        curr-=1
                        new[curr][i]= self.board[j][i]
                        #print(30)
                        pass
                    pass
                pass
            pass
        pass
        self.board=new
        
    def check_fail(self):
        failed=True
        for i in self.board:
            for j in i:
                if j==0:
                    failed=False
                pass
        return(failed)
    
    def find_future(self):
        all_possible=[]
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    temp2 = self.copy_board()
                    temp2[i][j] = 2
                    all_possible.append(temp2)
                
                    temp4 = self.copy_board()
                    temp4[i][j] = 4
                    all_possible.append(temp4)
        return(all_possible)
        pass
    
    def points(self):
        """Returns how many points are on the board"""
        points=0
        for i in self.board:
            #print(i)
            for j in i:
                #print(j)
                points+=j
        return(points)

    def eval_self(self):
        """Evaluates the board state and returns an int as a measure of how good it is """
        #I'm actually gonna explain this one well cause I'll need to tweak it in the future lol
        #The eval is going to have 2 distinct phases, one calculating the multiplier and on the base value
        # Inspired by Balatro
        # The base value is going to be the points avaible on the board
        # Giving a small bonues in points for bigger tiles
        # to incentivize having a lot of bigger numbers on the board when possible
        # As well as giving a smaller local mul to each tile if it's hugging a wall
        # Those two together should incentive the algorithm to prioritize making big numbers and placing them on the side
        # 
        # maybe look to eventually add an adjacancy bonus for big numbers next to big numbers

        if self.detect_loss()==True: #disencentives dead boards by a lot, might cause problems in the future
            #if it does look to normalize it somehow
            return(0)

        #Calculating general mul for empty spaces, each one gives a 3% bonues
        gen_mul=1
        for i in self.board:
            for j in i:
                if j == 0:
                    gen_mul+=0.03
                pass
        
        gen_chips=0

        board_hori=len(self.board[0])-1
        board_verti=len(self.board)-1 #Big number bonus has not been implemented yet
        for i in range(len(self.board)): #i is y pos
            for j in range(len(self.board[0])): #j is x pos
                temp = self.board[i][j]
                temp_mul=1
                if temp != 0:
                    if i==0 or i == board_verti:
                        temp_mul+=0.05
                    if j==0 or j==board_hori:
                        temp_mul+=0.05
                    temp=temp*temp_mul
                    gen_chips+=temp
                    
                    
                    pass

                pass
        total=gen_chips*gen_mul
        return(total)
        pass

    def get_future(self):
        """Returns a list of all future possibilities from each swipe actions
        The list will have length 4, 
        pos 0 is w, pos 1 is a, pos 2 is s, and pos 3 is d
        Each pos is another list of each possibility"""
        #note I moved this from the algorithm class
        next_move_possibility=[]
        wboard=board2048(self.board)
        if wboard.swipe("w") != -1:
            next_move_possibility.append(wboard.find_future())
        else:
            next_move_possibility.append([])
        aboard=board2048(self.board)
        
        if aboard.swipe("a") != -1:
            next_move_possibility.append(aboard.find_future())
        else:
            next_move_possibility.append([])

        sboard=board2048(self.board)
        if sboard.swipe("s") != -1:
            next_move_possibility.append(sboard.find_future())
        else:
            next_move_possibility.append([])

        dboard=board2048(self.board)
        if dboard.swipe("d") != -1:
            next_move_possibility.append(dboard.find_future())
        else:
            next_move_possibility.append([])
        
        return(next_move_possibility)

#a=board2048([[0,0,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
#print(a)
#print(a.find_future())
if __name__ == "__main__":
    c=board2048()
    c.player_start()
