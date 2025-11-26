scores = input("Enter scores separated by space: ").split()
scores = [float(x) for x in scores]

total = sum(scores)
avg = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", avg)
