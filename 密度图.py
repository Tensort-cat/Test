import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123)

x1 = np.random.normal(-10, 5, 1000)
x2 = np.random.normal(5, 10, 1000)
df = pd.DataFrame({"x1": x1, "x2": x2})

fig, ax = plt.subplots(figsize=(10, 7))
df.plot(kind="density", ax=ax, linewidth=3, title="Density Plot", alpha=0.7)
df.plot(kind="hist", ax=ax, density=True, legend=False, alpha=0.8)
plt.show()
