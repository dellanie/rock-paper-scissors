#creating rock paper scissors
#assign variables to rock paper and scissors

def game():

    print("Welcome to rock paper scissors")

    import random

    cpuwins = 0
    playerwins = 0


    game_on = ["s","r","p"]

    while game_on:
        computer = random.choice(game_on)

       # for i in game_on:

        #    if 1 == 1 or 2 == 2 or 3 ==3 :

         #       print("Draw")

         #   elif 1 == 3 or 3 == 1:
          #      print ("Rock Wins")

           # elif 1 == 2 or 2 == 1:
            #    print("Paper Wins")

            #elif 2==3 or 3==2:
             #   print("Scissors Wins")

              #  break

        start_play = ""

        Player1 = input("Please insert (s or r or t):")

        #player2 = input("Please insert (1-3):")

        start_play = Player1 == computer in game_on

        if (Player1 == "s" ) and (computer == "s"):
              print("Draw")

        elif (Player1 == "r" ) and (computer == "r"):
            print ("Draw")

        elif (Player1 == "p" ) and (computer == "p"):
            print("Draw")

        elif (Player1 == "s" ) and (computer == "p"):
            print ("Scissors wins")

        elif (Player1 == "r" ) and (computer == "p"):
            print("Paper wins")
            
        elif (Player1 == "s" ) and (computer == "r"):
            print("Rock Wins")
            
            

        for n in Player1:
            if n not in ("srt"):

                print ("Please try again")

            else:
                return

            

        #for p in player2:
         #   if p not in ("0123"):

          #      print ("Please try again")

          #      break


lets_go = game()

print (lets_go)

                
