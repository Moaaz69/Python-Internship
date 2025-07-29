import random
from datetime import datetime

# Predefined word list
word_list = [
    "python", "developer", "keyboard", "internet", "function",
    "variable", "machine", "learning", "weather", "program",
    "debug", "syntax", "script", "object", "module"
]

# Shuffle and pick 10 unique words
random.shuffle(word_list)
selected_words = word_list[:10]

print("🔤 Welcome to the Word Scramble Game!")
player_name = input("🎮 Enter your name: ").strip().title()

print(f"\n👋 Hello, {player_name}! Get ready to unscramble 10 words!\n")

score = 0

for i, original_word in enumerate(selected_words, 1):
    scrambled = ''.join(random.sample(original_word, len(original_word)))
    
    print(f"\nWord {i} of 10")
    print(f"🔀 Scrambled: {scrambled}")
    
    guess = input("✏️  Your guess: ").strip().lower()
    
    if guess == original_word:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct word was: {original_word}")

# Final score display
print("\n🎉 Game Over!")
print(f"📊 {player_name}, you scored {score} out of 10.")

# Save score to file
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
entry = f"{timestamp},{player_name},{score}\n"

with open("scores.txt", "a") as file:
    file.write(entry)

print("📝 Your score has been saved to scores.txt.")

# top 5 leaderboard
print("\n🏆 Leaderboard (Top 5 Scores):")
try:
    with open("scores.txt", "r") as file:
        entries = [line.strip().split(',') for line in file.readlines()]
        sorted_entries = sorted(entries, key=lambda x: int(x[2]), reverse=True)
        
        print("\n┌─────┬────────────┬──────────────┬───────┐")
        print("│  #  │ Timestamp  │ Player       │ Score │")
        print("├─────┼────────────┼──────────────┼───────┤")
        
        for i, (ts, name, sc) in enumerate(sorted_entries[:5], 1):
            print(f"│ {i:<3} │ {ts[:10]} │ {name:<12} │  {sc}/10 │")
        
        print("└─────┴────────────┴──────────────┴───────┘")

except FileNotFoundError:
    print("No scores found yet.")
