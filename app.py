import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load one audio file
file_path = "/home/prakhar/Documents/GitHub/Classify/Data/genres_original/blues/blues.00000.wav"
signal, sample_rate = librosa.load(file_path, sr=22050) # Load at standard SR

# Explore it
print(f"Signal Shape: {signal.shape}")
print(f"Sample Rate: {sample_rate}")
print(f"Duration: {len(signal)/sample_rate} seconds")

# Extract MFCCs
mfccs = librosa.feature.mfcc(y=signal, sr=sample_rate, n_mfcc=13)
print(f"MFCCs Shape: {mfccs.shape}") # (13 coefficients, time frames)

# Visualize
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time', sr=sample_rate)
plt.colorbar()
plt.title('MFCC')
plt.show()
