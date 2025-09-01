#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def subplots():
    fig, ax = plt.subplots(2, 1, gridspec_kw={"hspace": 0}, figsize=[9.6, 4.3], layout="tight")
    return fig, ax

def savefig(path):
    ax[0].set_ylabel("QPS [count/s]")
    ax[0].legend()
    ax[0].minorticks_on()
    ax[0].grid()
    ax[0].grid(which="minor", alpha=0.2)
    ax[0].set_xlim(1, 120)

    ax[1].set_ylabel("Latency [ms]")
    ax[1].minorticks_on()
    ax[1].grid()
    ax[1].grid(which="minor", alpha=0.2)
    ax[1].set_xlim(1, 120)

    plt.xlabel("Concurrency")

    plt.savefig(path)

nagle = pd.read_csv("data/1tokio-rayon-nagle.csv")
vs = pd.read_csv("data/1tokio-rayon-vs.csv")

fig, ax = subplots()
ax[0].plot(nagle["Concurrency"], nagle["QPS"], label="scylla")
ax[1].plot(nagle["Concurrency"], nagle["P99"], label="scylla")
savefig("nagle-scylla.png")


fig, ax = subplots()
ax[0].plot(nagle["Concurrency"], nagle["QPS"], label="scylla")
ax[1].plot(nagle["Concurrency"], nagle["P99"], label="scylla")
ax[0].plot(vs["Concurrency"], vs["QPS"], label="vector-store")
ax[1].plot(vs["Concurrency"], vs["P99"], label="vector-store")
savefig("nagle-scylla-vs.png")

quorum = pd.read_csv("data/1tokio-rayon-quorum.csv")

fig, ax = subplots()
ax[0].plot(nagle["Concurrency"], nagle["QPS"], label="scylla+nagle")
ax[1].plot(nagle["Concurrency"], nagle["P99"], label="scylla+nagle")
ax[0].plot(quorum["Concurrency"], quorum["QPS"], label="scylla")
ax[1].plot(quorum["Concurrency"], quorum["P99"], label="scylla")
ax[0].plot(vs["Concurrency"], vs["QPS"], label="vector-store")
ax[1].plot(vs["Concurrency"], vs["P99"], label="vector-store")
savefig("nagle-quorum-scylla-vs.png")

fig, ax = subplots()
ax[0].plot(quorum["Concurrency"], quorum["QPS"], label="scylla")
ax[1].plot(quorum["Concurrency"], quorum["P99"], label="scylla")
ax[0].plot(vs["Concurrency"], vs["QPS"], label="vector-store")
ax[1].plot(vs["Concurrency"], vs["P99"], label="vector-store")
savefig("quorum-scylla-vs.png")

scylla = pd.read_csv("data/1tokio-rayon.csv")

fig, ax = subplots()
ax[0].plot(quorum["Concurrency"], quorum["QPS"], label="scylla+cl=quorum")
ax[1].plot(quorum["Concurrency"], quorum["P99"], label="scylla+cl=quorum")
ax[0].plot(scylla["Concurrency"], scylla["QPS"], label="scylla+cl=one")
ax[1].plot(scylla["Concurrency"], scylla["P99"], label="scylla+cl=one")
ax[0].plot(vs["Concurrency"], vs["QPS"], label="vector-store")
ax[1].plot(vs["Concurrency"], vs["P99"], label="vector-store")
savefig("quorum-one-scylla-vs.png")

a1s4_vs = pd.read_csv("data/a1s4-vs.csv")
a1s4_sc = pd.read_csv("data/a1s4-sc.csv")
a4s4_vs = pd.read_csv("data/a4s4-vs.csv")
a4s4_sc = pd.read_csv("data/a4s4-sc.csv")
a4s0_vs = pd.read_csv("data/a4s0-vs.csv")
a4s0_sc = pd.read_csv("data/a4s0-sc.csv")

fig, ax = subplots()
ax[0].plot(a1s4_vs["Concurrency"], a1s4_vs["QPS"], label="a1s4")
ax[1].plot(a1s4_vs["Concurrency"], a1s4_vs["P99"], label="a1s4")
ax[0].plot(a4s4_vs["Concurrency"], a4s4_vs["QPS"], label="a4s4")
ax[1].plot(a4s4_vs["Concurrency"], a4s4_vs["P99"], label="a4s4")
ax[0].plot(a4s0_vs["Concurrency"], a4s0_vs["QPS"], label="a4s0")
ax[1].plot(a4s0_vs["Concurrency"], a4s0_vs["P99"], label="a4s0")
savefig("thread-layout-vs.png")

fig, ax = subplots()
ax[0].plot(a1s4_sc["Concurrency"], a1s4_sc["QPS"], label="a1s4")
ax[1].plot(a1s4_sc["Concurrency"], a1s4_sc["P99"], label="a1s4")
ax[0].plot(a4s4_sc["Concurrency"], a4s4_sc["QPS"], label="a4s4")
ax[1].plot(a4s4_sc["Concurrency"], a4s4_sc["P99"], label="a4s4")
ax[0].plot(a4s0_sc["Concurrency"], a4s0_sc["QPS"], label="a4s0")
ax[1].plot(a4s0_sc["Concurrency"], a4s0_sc["P99"], label="a4s0")
savefig("thread-layout-sc.png")


fig, ax = subplots()
ax[0].plot(a1s4_vs["Concurrency"], a1s4_vs["QPS"], label="a1s4-vector-store")
ax[1].plot(a1s4_vs["Concurrency"], a1s4_vs["P99"], label="a1s4-vector-store")
ax[0].plot(a1s4_sc["Concurrency"], a1s4_sc["QPS"], label="a1s4-scylla")
ax[1].plot(a1s4_sc["Concurrency"], a1s4_sc["P99"], label="a1s4-scylla")
savefig("a1s4.png")

fig, ax = subplots()
ax[0].plot(a4s4_vs["Concurrency"], a4s4_vs["QPS"], label="a4s4-vector-store")
ax[1].plot(a4s4_vs["Concurrency"], a4s4_vs["P99"], label="a4s4-vector-store")
ax[0].plot(a4s4_sc["Concurrency"], a4s4_sc["QPS"], label="a4s4-scylla")
ax[1].plot(a4s4_sc["Concurrency"], a4s4_sc["P99"], label="a4s4-scylla")
savefig("a4s4.png")

fig, ax = subplots()
ax[0].plot(a4s0_vs["Concurrency"], a4s0_vs["QPS"], label="a4s0-vector-store")
ax[1].plot(a4s0_vs["Concurrency"], a4s0_vs["P99"], label="a4s0-vector-store")
ax[0].plot(a4s0_sc["Concurrency"], a4s0_sc["QPS"], label="a4s0-scylla")
ax[1].plot(a4s0_sc["Concurrency"], a4s0_sc["P99"], label="a4s0-scylla")
savefig("a4s0.png")
