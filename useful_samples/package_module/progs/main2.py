import sys
import os

# extra_pack can be added directly as zip (easier to send or archive)
sys.path.append(os.path.join('..', 'packages', 'extra_pack.zip'))
  
import extra.good.best.sigma as sig

from extra.good.best.tau import funT

print(sig.funS())
print(funT())