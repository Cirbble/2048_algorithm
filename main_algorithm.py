"""
Eric Shi
2332400
Robert Vincent
Programming techniques and applications
"""


from board2048 import board2048

class future_board_states(object):
    #A tree like class to manage all possible future board states
    def __init__(self, root: board2048, depth: int, first=False):
        """Creates a future board state class, taking a board2048 object as a mandatory argument, and the depth as a mandatory argument
        Make sure to also specify first=True when starting this class
        The future board state class is basically a tree of trees, with the root being the inputed board2048
        """
        
        #Setting the input board as the root of the tree
        self.root=root
        
        #checking for user stupidity 
        self.depth=depth
        if type(depth)!=int:
            raise Exception("The depth is supposed to be an integer")
        if depth<=0:
            raise ValueError
        
        #creating all the variables
        self.tpoints=0
        self.wpoints=0
        self.apoints=0
        self.spoints=0
        self.dpoints=0
        self.answer=-1
        
        #getting all future possibilities
        temp=root.get_future()
        
        #assigning each one into its proper list
        
        self.w=[]
        for i in temp[0]:
            temp_board_dir=board2048(i[0])
            tempaaaa=(temp_board_dir,i[1])
            self.w.append(tempaaaa)

        self.a=[]
        for i in temp[1]:
            temp_board_dir=board2048(i[0])
            tempaaaa=(temp_board_dir,i[1])
            self.a.append(tempaaaa)
            
        self.s=[]
        for i in temp[2]:
            temp_board_dir=board2048(i[0])
            tempaaaa=(temp_board_dir,i[1])
            self.s.append(tempaaaa)

        self.d=[]    
        for i in temp[3]:
            temp_board_dir=board2048(i[0])
            tempaaaa=(temp_board_dir,i[1])
            self.d.append(tempaaaa)        

        #calculates the points based on the board2048 class
        #important to do this before generating the next level
        #since then the board2048 class gets turned into future_board_states class
        self.calc_points()
        if depth != 1: #while it isn't the lowest level
            self.generate_next_level(depth-1)

        if depth == 1: 
            pass #load bearing pass statment do not remove
        elif first==False:
            self.calc_partial_points()
        elif first==True:
            self.calc_gradient_decent()
        self.find_best_move()

    def __str__(self):
        """Turns the board class into a string"""
        #do not ever use this as a debug tool holy 
        #since everything is on different lines it's completely unreadable
        ans="w:\n"
        for i in self.w:
            ans+=str(i)
            ans+="\n"
        ans+="a\n"
        for i in self.a:
            ans+=str(i)
            ans+="\n"
        ans="s\n"
        for i in self.s:
            ans+=str(i)
            ans+="\n"
        ans="d\n"
        for i in self.d:
            ans+=str(i)
            ans+="\n"
        return(ans)
        pass
    def calc_points(self):
        """Calculates the point of any given future"""
        #if a 2 was generated, its points is weighted at 90%
        #if a 4 was generated, its points is weighted at 10%
        #so that combined, they add up to 100%
        
        for i in self.w:
            if i[1]==2:
                self.wpoints+=i[0].eval_self()*0.9
            if i[1]==4:
                self.wpoints+=i[0].eval_self()*0.1
        for i in self.a:
            if i[1]==2:
                self.apoints+=i[0].eval_self()*0.9
            if i[1]==4:
                self.apoints+=i[0].eval_self()*0.1
        for i in self.s:
            if i[1]==2:
                self.spoints+=i[0].eval_self()*0.9
            if i[1]==4:
                self.spoints+=i[0].eval_self()*0.1
        for i in self.d:
            if i[1]==2:
                self.dpoints+=i[0].eval_self()*0.9
            if i[1]==4:
                self.dpoints+=i[0].eval_self()*0.1

        #adding all the points together into tpoints
        self.tpoints=self.wpoints+self.apoints+self.spoints+self.dpoints
        
        pass
    def generate_next_level(self,depth):
        """Turns each potencial board into another future board state class
        Extends the tree another depth"""
        for i in range(len(self.w)):
            self.w[i]=future_board_states(self.w[i][0],depth)
        for i in range(len(self.a)):
            self.a[i]=future_board_states(self.a[i][0],depth)
        for i in range(len(self.s)):
            self.s[i]=future_board_states(self.s[i][0],depth)
        for i in range(len(self.d)):
            self.d[i]=future_board_states(self.d[i][0],depth)
        
        pass
    
    def calc_partial_points(self):
        """Calculates the points from each child
        Stores answer in tpoints as an int or float"""
        self.tpoints=0
        for i in self.a:
            self.tpoints+=i.tpoints
        for i in self.w:
            self.tpoints+=i.tpoints
        for i in self.s:
            self.tpoints+=i.tpoints
        for i in self.d:
            self.tpoints+=i.tpoints
        pass
    def calc_gradient_decent(self):
        """Calculates the points from each child
        Stores answer in respective point catagory
        Meant to only be used for root board"""
        self.wpoints=0
        self.apoints=0
        self.spoints=0
        self.dpoints=0
        for i in self.a:

            self.apoints+=i.tpoints
        for i in self.w:
            self.wpoints+=i.tpoints
        for i in self.s:
            self.spoints+=i.tpoints
        for i in self.d:
            self.dpoints+=i.tpoints
    
    def find_best_move(self):
        """Finds the best move from any given board, store the answer in self.answer"""
        """Uncomment the print to make it look cool"""
        #print(self.apoints, self.wpoints, self.spoints, self.dpoints)
        if self.apoints>=self.wpoints and self.apoints>=self.dpoints and self.apoints>=self.spoints:
            self.answer="a"
            pass
        elif self.spoints>=self.apoints and self.spoints>=self.dpoints and self.spoints>=self.wpoints:
            self.answer="s"
        elif self.dpoints>=self.spoints and self.dpoints>=self.apoints and self.dpoints >= self.wpoints:
            self.answer="d"
        elif self.wpoints>=self.apoints and self.wpoints>=self.spoints and self.wpoints >= self.dpoints:
            self.answer="w"
        else:
            self.answer=-1
            print("a very nice word that is not a swear word and would not get me refered to either HR or the dean")
          
        pass
    
    
    pass

class algor2048(object):
    def __init__(self, board=-1, sight=3):
        """Init creates the class
        Optional argument for a already played board
        Else it creates a new board
        Sight is how many moves into the future the system checks for"""
        #Note: it takes my around 10 seconds to calculate one iteration with sight 3, increase at your own risk
        if board==-1:
            self.boardstate=board2048()
        
        elif isinstance(board, board2048):
            self.boardstate=board2048(board.board)
            pass
        
        else:
            self.boardstate=board2048(board)
        self.sight=sight
    
    def __str__(self):
        """allows for nice printing"""
        return(str(self.boardstate))

    def export_boardstate(self):
        """Returns the board"""
        return(self.boardstate)
    
    def do_move(self,dir):
        """does the move to the boardstate"""
        result = self.boardstate.swipe(dir)
        return(result)

    def trouver_best_move(self):
        """Finds the best move"""
        #print(str(self.boardstate))
        temp=future_board_states((self.boardstate), self.sight, first=True)
        return(temp.answer)
        pass

    def make_best_move(self):
        """Does the best move avaible
        and then generates a new tile
        """
        #print(1)
        best_move=self.trouver_best_move()
        result=self.do_move(best_move)
        #print(best_move)
        if result == -1:
            raise Exception("welp, the best move doesn't exisit lol good luck figuring out the mistake future me <3")
        else:
            #print(self)
            #print(2)
            (self.boardstate.gen_new_tile())
            #print(3)
            pass


    
    
    pass

if __name__=="__main__": # a little bit of testing
    
    b=board2048()
    
    c = algor2048(b)
    print(type(b))
    print(type(c.boardstate))
    print(c)
    #print(c.find_best_move())
    c.make_best_move()
    print(c)
    