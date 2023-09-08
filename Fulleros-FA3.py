import numpy as np

# Sample or test scores data
scores = [88, 45, 53, 86, 33, 86, 85, 30, 89, 53, 41, 96, 56, 38, 62, 71, 51, 86, 68, 29, 28, 47, 33, 37, 25, 36, 33, 94, 73, 46, 42, 34, 79, 72, 88, 99, 82, 62, 57, 42, 28, 55, 67, 62, 60, 96, 61, 57, 75, 93, 34, 75, 53, 32, 28, 73, 51, 69, 91, 35]

# Calculate descriptive measures
q1 = np.percentile(scores, 25)    # Q1 (25th percentile)
q2 = np.median(scores)            # Q2 (50th percentile)
q3 = np.percentile(scores, 75)    # Q3 (75th percentile)
d9 = np.percentile(scores, 90)    # D9 (90th percentile)
p95 = np.percentile(scores, 95)  # P95 (95th percentile)

# Display the results
print("Q1 (25th percentile):", q1)
print("Q2 (50th percentile):", q2)
print("Q3 (75th percentile):", q3)
print("D9 (90th percentile):", d9)
print("P95 (95th percentile):", p95)