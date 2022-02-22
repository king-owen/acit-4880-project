from scipy import stats
import numpy as np
from math import *
t_value = (3.08-3.00)/(1.983/sqrt(2675))
p_value = stats.t.sf(np.abs(t_value),2675)
print(p_value)