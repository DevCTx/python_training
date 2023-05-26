import os
import sys

sys.path.append(os.path.join('..', 'modules'))

import module

ones = [1 for i in range(5)]
print(module.suml(ones))
print(module.prodl(ones))