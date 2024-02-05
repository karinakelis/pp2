


def guess_game():
    #random number betweer 1  and 20
    secret_num = random.randint(1,20)
    print("Hello! What is your name?")
    print("Well, KBTU, I am thinking of a number between 1 and 20. Take a guess.")
    attempt = 0
    while True:
        attempt += 1
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
       
        except  ValueError:
            print("Please enter a valid number")
            break
   
        attempt += 1
        if guess == secret_num:
            print("Good job, KBTU! You guessed my number in {attempt} attempts")
            break
        elif guess < secret_num:
            print("Too low. Try again.")
        elif guess > secret_num:
            print("Too high. Try again.")

guess_game()
            
              
            
        
    
     
     
            
        

   


        
        
    