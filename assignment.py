age = input("Are you a cigarette addict older than 75 years old? Variable Yes/No")
chronic = input("Do you have a severe chronic disease? Yes/No")
immune = input("Is your immune system too weak?Yes/No")
if (age == "Yes" and chronic == "Yes" and immune == "Yes"):
    print("You are in risky group")
else:
    print("You are not in risky group")