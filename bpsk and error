import numpy as np
import matplotlib.pyplot as plt
message_frequency = 10
carrier_frequency = 20
sampling_frequency = 30 * carrier_frequency
t = np.arange(0, 4/carrier_frequency, 1/sampling_frequency)
message = np.sign(np.cos(2 * np.pi * message_frequency * t) +
np.random.normal(scale = 0.01, size = len(t)))
carrier = np.cos(2 * np.pi * sampling_frequency/carrier_frequency * t)
modulated_signal = carrier * message
plt.figure(figsize=(8, 6))
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal)
plt.show()
plt.plot(t, message)
plt.plot(t, modulated_signal, "--")
plt.plot(t, carrier, "-")
plt.show()
# # Monte Carlo Simulation
N = 500000
EbN0dB_list = np.arange(0, 50)
BER = []
for i in range(len(EbN0dB_list)):
EbN0dB = EbN0dB_list[i]
EbN0 = 10**(EbN0dB/10)
x = 2 * (np.random.rand(N) >= 0.5) - 1
noise = 1/np.sqrt(2 * EbN0)
channel = x + np.random.randn(N) * noise
received_x = 2 * (channel >= 0.5) - 1
errors = (x != received_x).sum()
BER.append(errors/N)
plt.plot(EbN0dB_list, BER, "-", EbN0dB_list, BER, "go")
plt.axis([0, 14, 1e-7, 0.1])
plt.xscale('linear')
plt.yscale('log')
plt.grid()
plt.xlabel("EbN0 in dB")
plt.ylabel("BER")
plt.title("BER in BPSK")
plt.show()
