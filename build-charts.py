#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(3, 120, num=40)

qps_a1s4 = np.linspace(200, 4000, num=40)
p99_a1s4 = np.linspace(2, 30, num=40)

qps_a4s4 = np.linspace(300, 3500, num=40)
p99_a4s4 = np.linspace(3, 40, num=40)

qps_a1s3 = np.linspace(400, 4500, num=40)
p99_a1s3 = np.linspace(3.5, 37, num=40)

qps_a2s2 = np.linspace(450, 4700, num=40)
p99_a2s2 = np.linspace(3.2, 47, num=40)

qps_a4s0 = np.linspace(550, 6700, num=40)
p99_a4s0 = np.linspace(4.2, 57, num=40)

fig, ax = plt.subplots(2, 1, gridspec_kw={"hspace": 0})

ax[0].set_ylabel("QPS [count/s]")
ax[0].plot(x, qps_a1s4, label="a1s4")
ax[0].plot(x, qps_a4s4, label="a4s4")
ax[0].plot(x, qps_a1s3, label="a1s3")
ax[0].plot(x, qps_a2s2, label="a2s2")
ax[0].plot(x, qps_a4s0, label="a4s0")
ax[0].grid()
ax[0].legend()

ax[1].set_ylabel("Latency [ms]")
ax[1].plot(x, p99_a1s4, label="a1s4")
ax[1].plot(x, p99_a4s4, label="a4s4")
ax[1].plot(x, p99_a1s3, label="a1s3")
ax[1].plot(x, p99_a2s2, label="a2s2")
ax[1].plot(x, p99_a4s0, label="a4s0")
ax[1].grid()
ax[1].legend()

plt.xlabel("Concurrency")

plt.show()
