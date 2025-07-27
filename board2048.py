"""
Eric Shi
2332400
Robert Vincent
Programming techniques and applications
"""
#documentation and comments goes against  my job security 
#NEED TO DO:
"""

"""

from random import randint
class board2048(object):
    def __init__(self, pre=-1, width=4, height=4):
        #creates the board
        #if pre is -1, it randomly generates a board
        #else, it uses the pre defined board
        #eventually width and hight will do something
        if pre==-1:
            self.board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #makes the empty board
            self.gen_new_tile() #puts two random tiles on the board
            self.gen_new_tile()
            """a=[randint(0,3),randint(0,3)]
            b=[randint(0,3),randint(0,3)]
            while a==b:
                b=[randint(0,3),randint(0,3)]
            self.board[a[0]][a[1]]=2
            self.board[b[0]][b[1]]=2"""
        else:
            self.board=pre    #uses the pre-made board
            pass

    def player_start(self):
        """Starts the main loop for playing the game
        This option is meant for a human player to play the game"""
        while self.detect_loss() == False: 
            #asks the player to make a move
            #then checks if the move was valid, 
            #if yes, then does the move, if no it doesn't
            #then it reasks until the board is full
            print(self)
            player_move=input("Your move (wasd): ")
            
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
        for i in self.board: #simple check to see if there's a free tile
            for j in i:
                if j==0:
                    loss=False
        if loss==True: #more complex check to see if any of the 4 directions can be merged into
            if self.verify_a()!=-1:
                return(False)
            if self.verify_s()!=-1:
                return(False)
            if self.verify_d()!=-1:
                return(False)
            if self.verify_w()!=-1:
                return(False)
            else:
                return(True)
            pass
        
        return(False)
        
    def gen_new_tile(self):
        """Finds an empty space, then places either a 2 or a 4 on that tile"""
        
        if self.detect_loss()==True: #if it detects a loss, it'll return -1, prevents infinite loops
            return(-1)
        temp=[randint(0,3),randint(0,3)] #chooses a random tile in the board
        while self.board[temp[0]][temp[1]] != 0: #checking if the random choosen tile is empty
            temp=[randint(0,3),randint(0,3)] #reruns the generation until it's free
            pass
        random_value=randint(1,10)
        if random_value==10: #chooses weather to place a 4 or a 2, at a 10% and 90% respectivly
            self.board[temp[0]][temp[1]]=4
        else:
            self.board[temp[0]][temp[1]]=2
        return(1)
        pass

    def swipe(self,in_dir):
        """
        Swipes the board, w for up, s for down, a for left, and d for right
        This is used for manual player controlled gameplay
        """
        #it first verifies the input to make sure that it's was or d
        #then checks if the direction can be swiped in
        #then it swips
        #if at any point something goes wrong, it returns -1
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
        """does as the name implies, creates a copy of itself
        returns an arrary of arrays"""
        temp=[]
        for i in self.board:
            temp.append(i.copy())
        return(temp)
        pass
    
    def verify_w(self):
        """
        Checks to see if the swipe direction is valid
        Returns 1 if valid, -1 if not valid
        """
        #Done by checking to see if after a swipe if the board has changed at all
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
        Returns 1 if valid, -1 if not valid
        """
        #Done by checking to see if after a swipe if the board has changed at all
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
        Returns 1 if valid, -1 if not valid
        """
        #Done by checking to see if after a swipe if the board has changed at all
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
        Returns 1 if valid, -1 if not valid
        """
        #Done by checking to see if after a swipe if the board has changed at all
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
        # read documentation for how this is done
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

    def find_future(self):
        """finds all the possible random boards that could be generated
        returns an array of tuples([the board], tile added)"""
        all_possible=[]
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    temp2 = self.copy_board()
                    temp2[i][j] = 2
                    temp22=(temp2,2)
                    all_possible.append(temp22)
                
                    temp4 = self.copy_board()
                    temp4[i][j] = 4
                    temp44=(temp4,4)
                    all_possible.append(temp44)
        return(all_possible)

    def points(self):
        """Returns how many points are on the board"""
        points=0
        for i in self.board:
            #print(i)
            for j in i:
                #print(j)
                points+=j
        return(points)

    def find_local_mul(self,y,x,height,width):
        """finds if there is a tile with the same value nearby,
        if no, then finds the largest value"""
        local_val=int(self.board[y][x])
        local_mul=1
        list_nearby=[]

        #checks nearby tiles to see if they're valid, then adding the value to the list_nearby
        if y-1 != -1:
            list_nearby.append(self.board[y-1][x])
            
        if y+1 != height+1:
            list_nearby.append(self.board[y+1][x])
            
            pass
        if x-1 != -1:
            list_nearby.append(self.board[y][x-1])
            
            pass
        if x+1 != width+1:
            list_nearby.append(self.board[y][x+1])
            
            pass
        

        
        for i in list_nearby:
            if i==local_val:
                local_mul+= i/100*2.5
                break
            elif local_mul<(1+i/100):
                local_mul=1+i/100

        return(local_mul)
        pass

    def eval_self(self):
        """Evaluates the board state and returns an int as a measure of how good it is """
        #I'm actually gonna explain this one well cause I'll need to tweak it in the future lol
        #The eval is going to have 2 distinct phases, one calculating the multiplier and on the base value
        # The base value is going to be the points avaible on the board
        # Giving a small bonues in points for bigger tiles
        # to incentivize having a lot of bigger numbers on the board when possible
        # As well as giving a smaller local mul to each tile if it's hugging a wall
        # Those two together should incentive the algorithm to prioritize making big numbers and placing them on the side
        # 
        # maybe look to eventually add an adjacancy bonus for big numbers next to big numbers

        if self.detect_loss()==True: #disencentives dead boards by a lot
            
            return(0)

        #Calculating general mul for empty spaces, each one gives a 3% bonues
        gen_mul=1
        for i in self.board:
            for j in i:
                if j == 0:
                    gen_mul+=0.03
                pass
        
        gen_chips=0


        #calcuates the point for all individual tiles
        board_hori=len(self.board[0])-1
        board_verti=len(self.board)-1 
        for i in range(len(self.board)): #i is y pos
            for j in range(len(self.board[0])): #j is x pos
                temp = self.board[i][j]*1.1
                temp_mul=1
                if temp != 0:
                    #finds the wall hugging bonues
                    if (i==0 or i == board_verti) and (j==0 or j==board_hori): #in a corner (x3 big combo bonues)
                        temp_mul+=6942000000000
                    if i==0 or i == board_verti: #touching top wall
                        temp_mul+=6942000000000
                    if j==0 or j==board_hori: #touching side wall
                        temp_mul+=6942000000000
                    #finding the largest nearby number bonues
                    temp_local_mul=self.find_local_mul(i,j,board_verti,board_hori)
                    temp=temp*temp_mul*temp_local_mul
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
    
    def find_highest_tile(self):
        """finds the single highest value tile"""
        highest=0
        for i in self.board:
            for j in i:
                if j>highest:
                    highest=j
        return(highest)

if __name__ == "__main__": # little bit of testing, feel free to play with it
    a=board2048([[0,0,1,1],[10,1,1,1],[1,1,1,1],[1,1,1,1]])
    print(a.find_highest_tile())
    #print(a)
    #print(a.find_future())
    #c=board2048()
    #c.player_start()
