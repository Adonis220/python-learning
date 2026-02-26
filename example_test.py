points = 100
level = "gold" if points >= 100 else "silver"
result = "pass" if points >= 60 else "fail"
print(result)
print(level)

if level == "gold":
    print("Good Job")
else:
    print("try harder")



