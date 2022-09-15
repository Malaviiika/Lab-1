# Pulse Code Modulation (PCM)
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
# Message signal generation
fm = 100
dc_offset = 2
t = np.arange(0, 5/fm, 0.0001)
x = np.sin(2 * pi * fm * t) + dc_offset
plt.figure(figsize = (8, 6))
plt.plot(t, x)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Message Signal")
plt.grid(True)
plt.show()
# Sampling
fs = 30 * fm
t = np.arange(0, 5/fm, 1/fs)
xSampled = np.sin(2 * pi * fm * t) + dc_offset
plt.plot(t, xSampled, "bo-")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sampled message Signal")
plt.grid(True)
plt.show()

# Quantization
L = 8
x_min = min(x)
x_max = max(x)
quantizationLevels = np.linspace(x_min, x_max, L)
xQuantized = []
qInput = np.linspace(x_min, x_max, 1000)
qOutput = []
for i in qInput:
for j in quantizationLevels:
if i <= j:
qOutput.append(j)
break
for i in xSampled:
for j in quantizationLevels:
if i <= j:
xQuantized.append(j)
break
plt.figure(figsize = (12, 6))
plt.subplot(1, 2, 1)
plt.plot(qInput, qOutput, "r-")
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Quantizer Characteristics L = 8")
plt.grid(True)
plt.subplot(1, 2, 2)
plt.plot(t, xQuantized, "bo-")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sampled and Quantized message Signal")
plt.grid(True)
plt.show()
qlevels = {}
bit_no = int(np.log2(L))
for i in range(L):
val = bin(i).replace('0b', "")
if len(val) != bit_no:
bin_str = "0" * (bit_no - len(val))
bin_str = bin_str + val
else:
bin_str = val
qlevels[quantizationLevels[i]] = bin_str
xTruncated = [qlevels[i] for i in xQuantized]
print("Pulse coded message : {}".format(xTruncated))
# Signal to Noise Ratio (SNR)
def power(lst):
P = 0
for i in lst:
P = P + i**2
return P/len(lst)
quantizationNoise = xQuantized - xSampled
plt.plot(t, quantizationNoise)
plt.xlabel("Time")
plt.ylabel("Noise")
plt.title("Quantization Noise")
plt.show()
snr = power(xSampled) / power(quantizationNoise)
snrdB = 20 * np.log10(snr)
step_size = (x_max - x_min)/L
noisePower = (step_size**2)/3
snrEqn = power(xSampled) / noisePower
snrEqndB = 20 * np.log10(snrEqn)
print("SNR : {}".format(snrdB))
print("SNR from equation : {} dB".format(snrEqndB))
