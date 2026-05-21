import random

# Random number
secret = random.randint(1, 100)

tries = 0

print("🎮 Welcome to the Number Guessing Game 🎮")
print("------------------------------------------------")
print("🤖 I have selected a number between 1 and 100.")
print("🎯 Your mission is to guess it!")
print("------------------------------------------------")

while True:
    tries += 1

    guess = int(input("\n🔢 Enter your guess: "))

    if guess == secret:
        print("\n🎉 Congratulations!!!")
        print(f"🏆 You guessed the number in {tries} tries.")
        print("👏 You Win!")
        break

    elif guess > secret:
        print("📉 Too high! Try a smaller number.")

    else:
        print("📈 Too low! Try a bigger number.")
