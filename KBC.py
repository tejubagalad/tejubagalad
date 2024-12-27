# List of questions, options, and correct answers
questions = [
    ["On which day Indian Constitution Day is celebrated?", "november1", "november26", "december26", "january 26", 2],
    ["Which of the following sites is considered the largest Indus Valley Civilization site discovered so far?", "Mohenjo-daro", "Harappa", "Rakhigarhi", "Dholavira", 3],
    ["What is the hardest natural substance on earth?", "Diamond", "Gold", "Silver", "Bronze", 1],
    ["What is the color of the sun?", "Red", "Yellow", "Orange", "Pink", 2],
    ["What is the shape with three sides?", "Triangle", "Square", "Rhombus", "Hexagon", 1],
    ["Largest continent in the world is:", "Asia", "Africa", "Australia", "Europe", 1],
    ["Who is the first European to attack India?", "Alexander", "Vasco da Gama", "Neil Armstrong", "Julius Caesar", 1],
    ["Where is Red Square situated?", "India", "Australia", "Moscow", "California", 3],
    ["Which is the fastest land animal?", "Tiger", "Cheetah", "Lion", "Falcon", 2],
    ["Which element has chemical symbol 'O'?", "Oxygen", "Ozone", "Oracle", "Uranium", 1],
    ["Which country is known as 'The Land of Rising Sun'?", "China", "USA", "Japan", "Vatican City", 3],
    ["Who painted the Mona Lisa?", "Leonardo da Vinci", "William Shakespeare", "Alexander", "Robert Bruce", 1],
    ["Who is known as the Iron Man of India?", "Gandhiji", "Subhash Chandra Bose", "Nehru", "Sardar Vallabhbhai Patel", 4],
    ["Which country is the largest coffee producer?", "India", "Brazil", "USA", "Canada", 2],
    ["Which is the longest river in India?", "Ganges", "Krishna", "Kaveri", "Tunga Bhadra", 1]
]

# Levels of money
levels = [1000, 2000, 4000, 8000, 10000, 24000, 50000, 100000, 200000, 320000, 640000, 1280000, 2400000, 5000000, 10000000]
money = 0

# Game loop
for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs: {levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}     b. {question[2]}")
    print(f"c. {question[3]}     d. {question[4]}")

    # Get user input
    reply = int(input("Enter your answer (1-4): "))

    if reply == question[-1]:
        print(f"Correct answer! You have won Rs: {levels[i]}")

        # Safe points
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer! Game over.")
        break

print(f"You walk away with Rs: {money}")
