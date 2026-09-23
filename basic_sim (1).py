import random
import csv
import statistics

random.seed(123)

# Basic Monte Carlo simulation:
# 1,000 samples of size 100 from N(0,1)
means = []

for rep in range(1000):
    x = [random.gauss(0, 1) for _ in range(100)]
    means.append(statistics.mean(x))

with open("basic_sim_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["replicate", "sample_mean"])
    for i, value in enumerate(means, start=1):
        writer.writerow([i, value])

print("Simulation complete")
print("Replicates:", len(means))
print("Mean of sample means:", statistics.mean(means))
print("SD of sample means:", statistics.stdev(means))
print("Saved: basic_sim_results.csv")
