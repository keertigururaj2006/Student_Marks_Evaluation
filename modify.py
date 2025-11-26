import sys

if len(sys.argv) < 2:
    print("Usage: python scores_local.py <s1> <s2> <s3> ...")
    sys.exit(1)

scores = [float(x) for x in sys.argv[1:]]

print("Scores:", scores)
print("Sum:", sum(scores))
print("Average:", sum(scores) / len(scores))
print("Maximum:", max(scores))
print("Minimum:", min(scores))
