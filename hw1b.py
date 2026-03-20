#!/usr/bin/env python3 -B
"""hw1b.py: top() with pragmatic eps"""
import random, math, statistics
from stats import top

random.seed(1)

def weibull(n=20):
  shape = random.uniform(0.5, 3)
  scale = random.uniform(1, 4)
  return [min(10,
    scale*(-math.log(random.random()))**(1/shape)*2.5)
    for _ in range(n)]

sizes = []
for trial in range(50):
  rxs = {i: weibull() for i in range(20)}

  # baseline = pool all observations
  pooled = [v for rx in rxs.values() for v in rx]
  sd     = statistics.stdev(pooled)

  winners = top(rxs, eps=0.35 * sd)
  sizes.append(len(winners))

  w_means = [sum(rxs[w])/len(rxs[w]) for w in winners]
  spread  = max(w_means) - min(w_means) if w_means else 0

print(f"avg winners: {sum(sizes)/len(sizes):.1f}/20")
print(f"min winners: {min(sizes)}")
print(f"max winners: {max(sizes)}")

# Larger eps -> more winners, because the threshold for a "practically
# significant" difference grows, so more treatments are considered
# statistically indistinguishable from the best. Conversely, a smaller
# eps tightens the definition of "close enough" and produces fewer winners.