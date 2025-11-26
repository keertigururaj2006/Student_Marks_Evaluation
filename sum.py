import sys

# Check if arguments were passed
if len(sys.argv) < 2:
    print("Usage: python scores_main.py <s1> <s2> <s3> ...")
    sys.exit(1)

# Convert arguments to numbers
scores = [float(x) for x in sys.argv[1:]]

total = sum(scores)
avg = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", avg)
