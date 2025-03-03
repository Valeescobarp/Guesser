import random

class Number_Guesser:
    def __init__(self, number, max_guesses=4, max_hints=3):
        self.number = number
        self.remaining_guesses = max_guesses
        self.remaining_hints = max_hints
        self.hints_given = 0
    
    def get_factors(self):
        return [i for i in range(1, self.number + 1) if self.number % i == 0]
    
    def get_multiples(self):
        return [self.number * i for i in range(2, 9)]  
    
    def get_larger_smaller(self, lower=1, upper=50):
        if self.number - 1 > lower:
            return f"Guess a number smaller than {self.number}"
        if self.number + 1 < upper:
            return f"Guess a number larger than {self.number}"
    
    def get_parity(self):
        return "The number is even." if self.number % 2 == 0 else "The number is odd."
    
    def get_hint(self):
        if self.remaining_hints <= 0:
            return "You have used all your hints. Make a guess."
        
        hint_type = random.choice(['a', 'b', 'c'])
        if hint_type == 'a':
            if random.choice([True, False]) and self.get_factors():
                hint = f"One factor of the number is {random.choice(self.get_factors())}."
            else:
                hint = f"One multiple of the number is {random.choice(self.get_multiples())}."
        elif hint_type == 'b':
            hint = self.get_larger_smaller()
        else:
            hint = self.get_parity()
        
        self.remaining_hints -= 1
        return hint

def chatbot():
    number = random.randint(1, 50)
    game = Number_Guesser(number)
    
    print("Hello! I've guessed a number between 1 and 50")
    print(f"You have {game.remaining_guesses} guesses!")
    print("You can ask for 3 hints by typing 'hint'")
    
    while game.remaining_guesses > 0:
        user_input = input("Enter your guess or type 'hint': ")
        
        if user_input.lower() == "hint":
            print(game.get_hint())
        else:
            guess = int(user_input)
            if guess == game.number:
                print(guess)
                print("Congratulations! You win!")
                return
            else:
                print("Wrong guess. Try again!")
                game.remaining_guesses -= 1
        
        print(f"Guesses remaining: {game.remaining_guesses}, Hints remaining: {game.remaining_hints}")
    
    print(f"You've run out of guesses. The number was {game.number}.")

chatbot()
