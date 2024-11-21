from scipy.signal import find_peaks
import numpy as np

data = np.sin(np.linspace(0, 10, 100)) + 0.5 * np.random.rand(100)
peaks, _ = find_peaks(data)
print(f"{len(peaks)} peaks found at: {peaks}")
