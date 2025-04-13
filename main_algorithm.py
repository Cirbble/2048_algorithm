from board2048 import board2048

class future_board_states(object):
    #A class to store future board states as a big tree, allows for easy manipulation of data
    # at least I hope so :)
    def __init__(self, root: board2048, depth: int, first=False):
        self.root=root
        temp=root.get_future()
        self.depth=depth
        
        self.tpoints=0
        self.points=0
        self.wpoints=0
        self.apoints=0
        self.spoints=0
        self.dpoints=0
        
        self.w=[]
        for i in temp[0]:
            i=board2048(i)
            self.w.append(i)

        self.a=[]
        for i in temp[1]:
            i=board2048(i)
            self.a.append(i)
            
        self.s=[]
        
        for i in temp[2]:
            i=board2048(i)
            self.s.append(i)

        self.d=[]    
        for i in temp[3]:
            i=board2048(i)
            self.d.append(i)        
        

        #calculates the points based on the board2048 class
        #important to do this before generating the next level
        #since then the board2048 class gets turned into future_board_states class
        self.calc_points()

        if depth != 1: #while it isn't the lowest level
            self.generate_next_level(depth-1)
        pass
        
        
        if depth == 1: 
            pass
        elif first==False:
            self.calc_partial_points()
            pass
        else:
            self.calc_gradient_decent()
            pass

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
        for i in self.w:
            self.wpoints+=i.eval_self()
        for i in self.a:
            self.apoints+=i.eval_self()
        for i in self.s:
            self.spoints+=i.eval_self()
        for i in self.d:
            self.dpoints+=i.eval_self()
        self.points=self.wpoints+self.apoints+self.spoints+self.dpoints
        pass
    def generate_next_level(self,depth):
        for i in range(len(self.w)):
            self.w[i]=future_board_states(self.w[i],depth-1)
        for i in range(len(self.a)):
            self.a[i]=future_board_states(self.a[i],depth-1)
        for i in range(len(self.s)):
            self.s[i]=future_board_states(self.s[i],depth-1)
        for i in range(len(self.d)):
            self.d[i]=future_board_states(self.d[i],depth-1)
        
        pass
    
    def calc_partial_points(self):
        self.tpoints=0
        for i in self.a:
            #print(type(i))
            self.tpoints+=i.tpoints
        for i in self.w:
            self.tpoints+=i.tpoints
        for i in self.s:
            self.tpoints+=i.tpoints
        for i in self.d:
            self.tpoints+=i.tpoints
        pass
    def calc_gradient_decent(self):
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
        max_num=max(self.apoints,self.spoints,self.dpoints,self.wpoints)
        print(self.apoints,self.spoints,self.dpoints,self.wpoints)
        pass

    pass


class algor2048(object):
    def __init__(self, board=-1, sight=5):
        """Init creates the class
        Optional argument for a already played board
        Else it creates a new board
        Sight is how many moves into the future the system checks for"""
        if board==-1:
            self.boardstate=board2048()
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
        self.boardstate.swipe(dir)
    
    def get_future(self):
        """Returns a list of all future possibilities from each swipe actions
        The list will have length 4, 
        pos 0 is w, pos 1 is a, pos 2 is s, and pos 3 is d
        Each pos is another list of each possibility"""
        next_move_possibility=[]
        wboard=board2048(self.boardstate.copy_board())
        if wboard.swipe("w") != -1:
            next_move_possibility.append(wboard.find_future())
        else:
            next_move_possibility.append([])
        aboard=board2048(self.boardstate.copy_board())
        
        if aboard.swipe("a") != -1:
            next_move_possibility.append(aboard.find_future())
        else:
            next_move_possibility.append([])

        sboard=board2048(self.boardstate.copy_board())
        if sboard.swipe("s") != -1:
            next_move_possibility.append(sboard.find_future())
        else:
            next_move_possibility.append([])

        dboard=board2048(self.boardstate.copy_board())
        if dboard.swipe("d") != -1:
            next_move_possibility.append(dboard.find_future())
        else:
            next_move_possibility.append([])
        
        return(next_move_possibility)
        pass
    def turn_into_points(self, possible):
        """Temp is a list of all possible board states
        It is meant to be the list generated by get_future()"""
        points=[]
        for i in range(len(possible)):
            temppoints=0
            if len(possible[i])!=0:

                for j in range(len(possible[i])):
                    
                    #print(possible[i][j])
                    tempboard=board2048(possible[i][j])
                    tempval=tempboard.eval_self()
                    temppoints+=tempval

                    
                    pass
            else: 
                temppoints=-1
            points.append(temppoints)
        avg=0
        avg_div=0
        for i in points:
            if i != -1:
                avg+=i
                avg_div+=1
        if avg_div==0: #nvm solved it, this case happens when the board is in a dead state
            return([0,0,0,0])
            return("wait what the fuck?")
        avg=avg/avg_div
        for i in range(len(points)):
            if points[i] ==-1:
                points[i]=avg
        return(points)
    pass


#a=algor2048()
#a=algor2048([[2,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
#a=algor2048([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#print(a)
#aba=a.get_future()
#print(len(aba))
#print(len(aba[0]))
#print(aba)
#print(len(aba[0][0]))
#print(aba)
#print (a.turn_into_points(aba))
b=board2048()
print(b)
c=future_board_states(b,5)
c.find_best_move()
