import numpy as np
from scipy.io import wavfile
from sklearn.decomposition import FastICA

print("Start")
# Load the mixed signals
mix1_rate, mix1_data = wavfile.read('/mnt/home/boddutha/ITM801A_Tharun/Assignment/CSE801A_Spring2024_A2/mix_1.wav')
mix2_rate, mix2_data = wavfile.read('/mnt/home/boddutha/ITM801A_Tharun/Assignment/CSE801A_Spring2024_A2/mix_2.wav')
mix3_rate, mix3_data = wavfile.read('/mnt/home/boddutha/ITM801A_Tharun/Assignment/CSE801A_Spring2024_A2/mix_3.wav')
mix4_rate, mix4_data = wavfile.read('/mnt/home/boddutha/ITM801A_Tharun/Assignment/CSE801A_Spring2024_A2/mix_4.wav')
mix5_rate, mix5_data = wavfile.read('/mnt/home/boddutha/ITM801A_Tharun/Assignment/CSE801A_Spring2024_A2/mix_5.wav')

# Perform FastICA on the mixed signals
mix_data = np.column_stack((mix1_data, mix2_data, mix3_data, mix4_data, mix5_data))
ica = FastICA(n_components=5)
unmixed_data = ica.fit_transform(mix_data)

# Rescale the unmixed signals to a scale from -1 to 1
unmixed_data = unmixed_data / np.max(np.abs(unmixed_data))

# Write out the unmixed signals
wavfile.write('unmixed_1.wav', mix1_rate, unmixed_data[:, 0].astype(np.float32))
wavfile.write('unmixed_2.wav', mix2_rate, unmixed_data[:, 1].astype(np.float32))
wavfile.write('unmixed_3.wav', mix3_rate, unmixed_data[:, 2].astype(np.float32))
wavfile.write('unmixed_4.wav', mix4_rate, unmixed_data[:, 3].astype(np.float32))
wavfile.write('unmixed_5.wav', mix5_rate, unmixed_data[:, 4].astype(np.float32))

import matplotlib.pyplot as plt
import numpy as np

# Plot the time courses of the different unmixed songs
plt.figure(figsize=(10, 6))
for i in range(unmixed_data.shape[1]):
    plt.figure(figsize = (10, 6))
    plt.plot(np.arange(len(unmixed_data)), unmixed_data[:, i])
    # plt.title(f"Unmixed Signal {i + 1}")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    # plt.show()
plt.tight_layout()
# plt.show()
print("Completed")