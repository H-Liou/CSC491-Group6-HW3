#!/usr/bin/env python3 -B
"""hw1a.py: accuracy under class imbalance"""
import random
from stats import Confuse, confuse, confused

random.seed(1)

RATIOS = [              # (num_pos, num_neg)
  (50,  50),
  (10,  90),
  (5,   95),
  (1,   99),
  (1,   999)]

TP_RATE = 0.70          # classifier catches 70% of +
FP_RATE = 0.05          # classifier false-alarms 5%

print(f"{'ratio':>10} {'acc':>5} {'pd':>5}"
      f" {'pf':>5} {'prec':>5}")
print("-" * 40)

for n_pos, n_neg in RATIOS:
  cf = Confuse()
  for _ in range(n_pos):
    got = "pos" if random.random() < TP_RATE else "neg"
    confuse(cf, "pos", got)
  for _ in range(n_neg):
    got = "pos" if random.random() < FP_RATE else "neg"
    confuse(cf, "neg", got)
  summary = confused(cf, summary=True)
  ratio = f"{n_pos}:{n_neg}"
  print(f"{ratio:>10} {summary.acc:>5} {summary.pd:>5} {summary.pf:>5} {summary.prec:>5}")

"""
     ratio   acc    pd    pf  prec
----------------------------------------
     50:50    80    80    20    80
     10:90    91    91     9    91
      5:95    93    93     7    93
      1:99    96    96     4    96
     1:999    95    95     4    95

The classifier never changed as it always catches 70% of positives and
false-alarms 5% of negatives. But accuracy climbs from 80% to 96% as the
negative class grows, because the large pool of true negatives dominates
the calculation. A model that predicts "negative" for everything would score
even higher, yet catch zero positives. This is why pd and pf are more
informative for rare-class problems: they measure performance within each
class independently, so class imbalance cannot inflate them.
"""