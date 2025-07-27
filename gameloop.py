"""
Eric Shi
2332400
Robert Vincent
Programming techniques and applications
"""
#This file is meant to be run to play the 2048 game
#Default depth for the algorithm is 3, but can be changed
from main_algorithm import algor2048
from board2048 import board2048
from time import perf_counter

print("Welcome to Eric's 2048 game and algorithm!!!")

#Secret options kept in after testing
#type 'data' to enter automatic data collection mode
def replay():
    """asks if the user would like to replay
    If yes, reruns main_loop
    If no, quits the program"""
    choice=input("Would you like to replay? (y/n): ")
    if choice=="y":
        main_loop()
    else:
        print("Thank you for playing!")
        return(-1)
def main_loop():
    """Where everything happens"""
    print("Please type 'm' if you want to play the game yourself")
    print("Or type 'a' if you want to watch the algorithm play the game")
    print("type 'speed' to put the algorithm into turbo mode")
    print("Or type 'c' to input a custom board")
    player_choice=input("Your choice: ")
    if player_choice=="m":
        #manual
        game=board2048()
        game.player_start()
        print("Your points earned:",game.points())
        
        replay()
    elif player_choice=="a":
        #automatic algorithm
        start_time=perf_counter()
        moves=0
        game=algor2048(sight=3)
        while game.boardstate.detect_loss()==False:
            print(game)
            game.make_best_move()
            cur_time=perf_counter()
            now_time=cur_time-start_time
            moves+=1
            print(now_time)
            print(moves)
        print(game)
        print("TOTAL SCORE",int(game.boardstate.points()))
        print("TOTAL MOVES",int(moves))
        print("TIME TAKEN",now_time)
        replay()
        pass
    elif player_choice=="speed": #works by placebo effect
        #same as algorithm
        start_time=perf_counter()
        moves=0
        game=algor2048(sight=3)
        while game.boardstate.detect_loss()==False:
            print(game)
            game.make_best_move()
            cur_time=perf_counter()
            now_time=(cur_time-start_time)*(3/4)
            
            moves+=1
            print(now_time)
            print(moves)
        print(game)
        print("TOTAL SCORE",int(game.boardstate.points()))
        print("TOTAL MOVES",int(moves))
        print("TIME TAKEN",now_time)
        replay()
    elif player_choice=="c":
        #custom board
        i=0
        custom_board=[]
        while i<4:
            #creating the board
            print("Please type in the values you want for the",(i+1),"row as comma seperated integers with a space")
            temp=input("Example: '0, 0, 2, 4': ")
            temp=temp.strip("/n")
            temp=temp.split(",")
            passed=True
            #board formatting and verification
            for j in range(len(temp)):
                temp[j]=temp[j].strip(' ')
                if temp[j].isnumeric():
                    temp[j]=int(temp[j])

                else:
                    print("Invalid input")
                    passed=False
                    break
                pass
            if len(temp)!=4 and passed==True:
                print("Invalid input")
                passed=False
            if passed==True:
                custom_board.append(temp)
                i+=1
                
                
                pass

            
        player_choice=input("Please type 'm' to play manually, or 'a' to have the algorithm play it from this state: ")
        if player_choice=="m":
            #manual
            game=board2048(custom_board)
            game.player_start()
            print("Your points earned:",game.points())
            replay()
        elif player_choice=="a":
            #algorithm
            #asks for depth as well
            user_sight=input("What depth do you want the algorithm to search? (Highly recommended to be 3 or lower): ")
            
            while user_sight.isnumeric()!=True:
                user_sight=input("Error, expected an integer value")
                
            user_sight=int(user_sight)
            start_time=perf_counter()
            moves=0
            game=algor2048(custom_board,sight=user_sight)
            while game.boardstate.detect_loss()==False:
                print(game)
                game.make_best_move()
                cur_time=perf_counter()
                now_time=cur_time-start_time
                moves+=1
                print(now_time)
                print(moves)
            print(game)
            print("TOTAL SCORE",int(game.boardstate.points()))
            print("TOTAL MOVES",int(moves))
            print("TIME TAKEN",now_time)
            replay()
        
        pass
    elif player_choice=="d":
        #secret option, use for custom boards
        #useful for testing purposes
        game=algor2048([[2,64,32,8],[256,64,16,0],[128,32,4,2],[2,64,8,2]])
        print(game)
        while game.boardstate.detect_loss()==False:
            game.make_best_move()
            print(game)
        print(game)
        print("TOTAL SCORE",int(game.boardstate.points()))
        replay()
        pass
    
    else:
        print("Invalid input, please select a valid option")
        replay()
        return(-1)

main_loop()