#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def subplots():
    fig, ax = plt.subplots(2, 1, gridspec_kw={"hspace": 0}, figsize=[9.6, 4.3], layout="tight")
    return fig, ax

def savefig(path, xmin=1, xmax=120, legend="top"):
    ax[0].set_ylabel("QPS [count/s]")
    if legend=="top":
        ax[0].legend()
    ax[0].minorticks_on()
    ax[0].grid()
    ax[0].grid(which="minor", alpha=0.2)

    ax[1].set_ylabel("P99 Latency [ms]")
    if legend=="bottom":
        ax[1].legend()
    ax[1].minorticks_on()
    ax[1].grid()
    ax[1].grid(which="minor", alpha=0.2)

    xticks = ax[1].get_xticks()
    ax[0].set_xticks(xticks, labels=[])

    ax[0].set_xlim(xmin, xmax)
    ax[1].set_xlim(xmin, xmax)

    plt.xlabel("Concurrency")

    plt.savefig(path, transparent=True)
    #plt.close()

colors = (
        ('#3763C9', '#C0E13F', '#E9562F'),
        ('#07D0D8', '#42DBA0', '#071027'),
)

nagle = pd.read_csv("data/1tokio-rayon-nagle.csv")
vs = pd.read_csv("data/1tokio-rayon-vs.csv")

fig, ax = subplots()
ax[0].plot(nagle["Concurrency"], nagle["QPS"], color=colors[0][0], label="scylla")
ax[1].plot(nagle["Concurrency"], nagle["P99"], color=colors[0][0], label="scylla")
savefig("nagle-scylla.png")


fig, ax = subplots()
ax[0].plot(nagle["Concurrency"], nagle["QPS"], color=colors[0][0], label="scylla")
ax[1].plot(nagle["Concurrency"], nagle["P99"], color=colors[0][0], label="scylla")
ax[0].plot(vs["Concurrency"], vs["QPS"], color=colors[0][1], label="vector-store")
ax[1].plot(vs["Concurrency"], vs["P99"], color=colors[0][1], label="vector-store")
savefig("nagle-scylla-vs.png")

quorum = pd.read_csv("data/1tokio-rayon-quorum.csv")

fig, ax = subplots()
ax[0].plot(nagle["Concurrency"], nagle["QPS"], color=colors[0][0], label="scylla+nagle")
ax[1].plot(nagle["Concurrency"], nagle["P99"], color=colors[0][0], label="scylla+nagle")
ax[0].plot(quorum["Concurrency"], quorum["QPS"], color=colors[0][2], label="scylla")
ax[1].plot(quorum["Concurrency"], quorum["P99"], color=colors[0][2], label="scylla")
ax[0].plot(vs["Concurrency"], vs["QPS"], color=colors[0][1], label="vector-store")
ax[1].plot(vs["Concurrency"], vs["P99"], color=colors[0][1], label="vector-store")
savefig("nagle-quorum-scylla-vs.png")

fig, ax = subplots()
ax[0].plot(quorum["Concurrency"], quorum["QPS"], color=colors[0][0], label="scylla")
ax[1].plot(quorum["Concurrency"], quorum["P99"], color=colors[0][0], label="scylla")
ax[0].plot(vs["Concurrency"], vs["QPS"], color=colors[0][1], label="vector-store")
ax[1].plot(vs["Concurrency"], vs["P99"], color=colors[0][1], label="vector-store")
savefig("quorum-scylla-vs.png")

scylla = pd.read_csv("data/1tokio-rayon.csv")

fig, ax = subplots()
ax[0].plot(quorum["Concurrency"], quorum["QPS"], color=colors[0][0], label="scylla+cl=quorum")
ax[1].plot(quorum["Concurrency"], quorum["P99"], color=colors[0][0], label="scylla+cl=quorum")
ax[0].plot(scylla["Concurrency"], scylla["QPS"], color=colors[0][2], label="scylla+cl=one")
ax[1].plot(scylla["Concurrency"], scylla["P99"], color=colors[0][2], label="scylla+cl=one")
ax[0].plot(vs["Concurrency"], vs["QPS"], color=colors[0][1], label="vector-store")
ax[1].plot(vs["Concurrency"], vs["P99"], color=colors[0][1], label="vector-store")
savefig("quorum-one-scylla-vs.png")

a1s4_vs = pd.read_csv("data/a1s4-vs.csv")
a1s4_sc = pd.read_csv("data/a1s4-sc.csv")
a1s4_1_vs = pd.read_csv("data/a1s4-1-vs.csv")
a1s4_2_vs = pd.read_csv("data/a1s4-2-vs.csv")
a1s4_3_vs = pd.read_csv("data/a1s4-3-vs.csv")

fig, ax = subplots()
ax[0].plot(a1s4_vs["Concurrency"], a1s4_vs["QPS"], label="a1s4-vector-store")
ax[1].plot(a1s4_vs["Concurrency"], a1s4_vs["P99"], label="a1s4-vector-store")
ax[0].plot(a1s4_1_vs["Concurrency"], a1s4_1_vs["QPS"], label="a1s4-vector-store-1")
ax[1].plot(a1s4_1_vs["Concurrency"], a1s4_1_vs["P99"], label="a1s4-vector-store-1")
ax[0].plot(a1s4_2_vs["Concurrency"], a1s4_2_vs["QPS"], label="a1s4-vector-store-2")
ax[1].plot(a1s4_2_vs["Concurrency"], a1s4_2_vs["P99"], label="a1s4-vector-store-2")
ax[0].plot(a1s4_3_vs["Concurrency"], a1s4_3_vs["QPS"], label="a1s4-vector-store-3")
ax[1].plot(a1s4_3_vs["Concurrency"], a1s4_3_vs["P99"], label="a1s4-vector-store-3")
savefig("a1s4-3-vs-1.png")

a1s4_ext_vs = pd.read_csv("data/a1s4-ext-vs.csv")

fig, ax = subplots()
ax[0].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["QPS"], color=colors[0][1], label="vector-store")
ax[1].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["P99"], color=colors[0][1], label="vector-store")
ax[1].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["P99_0"], color=colors[0][0], label="vector-store node 1")
ax[1].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["P99_1"], color=colors[1][0], label="vector-store node 2")
ax[1].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["P99_2"], color=colors[1][1], label="vector-store node 3")
savefig("a1s4-div.png", legend="bottom")

fig, ax = subplots()
ax[0].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["QPS"], color=colors[0][1], label="vector-store")
ax[1].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["P99"], color=colors[0][1], label="vector-store")
ax[1].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["P99_0"], color=colors[0][0], label="vector-store node 1")
ax[1].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["P99_1"], color=colors[1][0], label="vector-store node 2")
ax[1].plot(a1s4_ext_vs["Concurrency"], a1s4_ext_vs["P99_2"], color=colors[1][1], label="vector-store node 3")
ax[1].plot(a1s4_1_vs["Concurrency"]*3, a1s4_1_vs["P99"], label="vector-store only node 1")
ax[1].plot(a1s4_2_vs["Concurrency"]*3, a1s4_2_vs["P99"], label="vector-store only node 2")
ax[1].plot(a1s4_3_vs["Concurrency"]*3, a1s4_3_vs["P99"], label="vector-store only node 3")
savefig("a1s4-div-3.png", legend="bottom")

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

a1s3_1_vs = pd.read_csv("data/a1s3-1-vs.csv")
a4s4_1_vs = pd.read_csv("data/a4s4-1-vs.csv")
a4s0_1_vs = pd.read_csv("data/a4s0-1-vs.csv")

fig, ax = subplots()
ax[0].plot(a1s4_1_vs["Concurrency"], a1s4_1_vs["QPS"], label="a1s4-vector-store-1")
ax[1].plot(a1s4_1_vs["Concurrency"], a1s4_1_vs["P99"], label="a1s4-vector-store-1")
ax[0].plot(a1s3_1_vs["Concurrency"], a1s3_1_vs["QPS"], label="a1s3-vector-store-1")
ax[1].plot(a1s3_1_vs["Concurrency"], a1s3_1_vs["P99"], label="a1s3-vector-store-1")
ax[0].plot(a4s4_1_vs["Concurrency"], a4s4_1_vs["QPS"], label="a4s4-vector-store-1")
ax[1].plot(a4s4_1_vs["Concurrency"], a4s4_1_vs["P99"], label="a4s4-vector-store-1")
ax[0].plot(a4s0_1_vs["Concurrency"], a4s0_1_vs["QPS"], label="a4s0-vector-store-1")
ax[1].plot(a4s0_1_vs["Concurrency"], a4s0_1_vs["P99"], label="a4s0-vector-store-1")
savefig("thread-layout-vs-1.png", xmax=42)

a1s4_1_cstate_vs = pd.read_csv("data/a1s4-1-cstate-vs.csv")
a1s3_1_cstate_vs = pd.read_csv("data/a1s3-1-cstate-vs.csv")
a4s4_1_cstate_vs = pd.read_csv("data/a4s4-1-cstate-vs.csv")
a4s0_1_cstate_vs = pd.read_csv("data/a4s0-1-cstate-vs.csv")
a4s0_1_cstate_yield_vs = pd.read_csv("data/a4s0-1-cstate-yield-vs.csv")

fig, ax = subplots()
ax[0].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["QPS"], color=colors[0][1], label="a1s4")
ax[1].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["P99"], color=colors[0][1], label="a1s4")
ax[0].plot(a1s3_1_cstate_vs["Concurrency"], a1s3_1_cstate_vs["QPS"], color=colors[0][0], label="a1s3")
ax[1].plot(a1s3_1_cstate_vs["Concurrency"], a1s3_1_cstate_vs["P99"], color=colors[0][0], label="a1s3")
ax[0].plot(a4s4_1_cstate_vs["Concurrency"], a4s4_1_cstate_vs["QPS"], color=colors[1][0], label="a4s4")
ax[1].plot(a4s4_1_cstate_vs["Concurrency"], a4s4_1_cstate_vs["P99"], color=colors[1][0], label="a4s4")
ax[0].plot(a4s0_1_cstate_vs["Concurrency"], a4s0_1_cstate_vs["QPS"], color=colors[1][1], label="a4s0")
ax[1].plot(a4s0_1_cstate_vs["Concurrency"], a4s0_1_cstate_vs["P99"], color=colors[1][1], label="a4s0")
savefig("thread-layout-cstate-vs-1.png", xmax=42)
savefig("thread-layout-cstate-vs-1-head.png", xmax=12)
savefig("thread-layout-cstate-vs-1-tail.png", xmin=12, xmax=42)

fig, ax = subplots()
ax[0].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["QPS"], color=colors[0][1], label="a1s4")
ax[1].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["P99"], color=colors[0][1], label="a1s4")
ax[0].plot(a1s3_1_cstate_vs["Concurrency"], a1s3_1_cstate_vs["QPS"], color=colors[0][0], label="a1s3")
ax[1].plot(a1s3_1_cstate_vs["Concurrency"], a1s3_1_cstate_vs["P99"], color=colors[0][0], label="a1s3")
ax[0].plot(a4s4_1_cstate_vs["Concurrency"], a4s4_1_cstate_vs["QPS"], color=colors[1][0], label="a4s4")
ax[1].plot(a4s4_1_cstate_vs["Concurrency"], a4s4_1_cstate_vs["P99"], color=colors[1][0], label="a4s4")
ax[0].plot(a4s0_1_cstate_vs["Concurrency"], a4s0_1_cstate_vs["QPS"], color=colors[1][1], label="a4s0")
ax[1].plot(a4s0_1_cstate_vs["Concurrency"], a4s0_1_cstate_vs["P99"], color=colors[1][1], label="a4s0")
ax[0].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["QPS"], color=colors[0][2], label="a4s0-yield")
ax[1].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["P99"], color=colors[0][2], label="a4s0-yield")
savefig("thread-layout-cstate-yield-vs-1.png", xmax=42)
savefig("thread-layout-cstate-yield-vs-1-head.png", xmax=12)
savefig("thread-layout-cstate-yield-vs-1-tail.png", xmin=12, xmax=42)

fig, ax = subplots()
ax[0].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["QPS"], color=colors[0][1], label="a1s4")
ax[1].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["P99"], color=colors[0][1], label="a1s4")
ax[0].plot(a1s3_1_cstate_vs["Concurrency"], a1s3_1_cstate_vs["QPS"], color=colors[0][0], label="a1s3")
ax[1].plot(a1s3_1_cstate_vs["Concurrency"], a1s3_1_cstate_vs["P99"], color=colors[0][0], label="a1s3")
savefig("thread-layout-cstate-vs-a1s4-a1s3.png", xmax=42)

fig, ax = subplots()
ax[0].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["QPS"], color=colors[0][1], label="a1s4")
ax[1].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["P99"], color=colors[0][1], label="a1s4")
ax[0].plot(a4s4_1_cstate_vs["Concurrency"], a4s4_1_cstate_vs["QPS"], color=colors[1][0], label="a4s4")
ax[1].plot(a4s4_1_cstate_vs["Concurrency"], a4s4_1_cstate_vs["P99"], color=colors[1][0], label="a4s4")
savefig("thread-layout-cstate-vs-a1s4-a4s4.png", xmax=42)

fig, ax = subplots()
ax[0].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["QPS"], color=colors[0][1], label="a1s4")
ax[1].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["P99"], color=colors[0][1], label="a1s4")
ax[0].plot(a4s0_1_cstate_vs["Concurrency"], a4s0_1_cstate_vs["QPS"], color=colors[1][1], label="a4s0")
ax[1].plot(a4s0_1_cstate_vs["Concurrency"], a4s0_1_cstate_vs["P99"], color=colors[1][1], label="a4s0")
savefig("thread-layout-cstate-vs-a1s4-a4s0.png", xmax=42)

fig, ax = subplots()
ax[0].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["QPS"], color=colors[0][1], label="a1s4")
ax[1].plot(a1s4_1_cstate_vs["Concurrency"], a1s4_1_cstate_vs["P99"], color=colors[0][1], label="a1s4")
ax[0].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["QPS"], color=colors[0][2], label="a4s0-yield")
ax[1].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["P99"], color=colors[0][2], label="a4s0-yield")
savefig("thread-layout-cstate-vs-a1s4-a4s0-yield.png", xmax=42)

fig, ax = subplots()
ax[0].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["QPS"], color=colors[0][2], label="a4s0-yield")
ax[1].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["P99"], color=colors[0][2], label="a4s0-yield")
ax[0].plot(a4s0_1_cstate_vs["Concurrency"], a4s0_1_cstate_vs["QPS"], color=colors[1][1], label="a4s0")
ax[1].plot(a4s0_1_cstate_vs["Concurrency"], a4s0_1_cstate_vs["P99"], color=colors[1][1], label="a4s0")
savefig("thread-layout-cstate-vs-a4s0-yield-a4s0.png", xmax=42)

fig, ax = subplots()
ax[0].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["QPS"], color=colors[0][2], label="a4s0-yield")
ax[1].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["P99"], color=colors[0][2], label="a4s0-yield")
ax[0].plot(a1s3_1_cstate_vs["Concurrency"], a1s3_1_cstate_vs["QPS"], color=colors[0][0], label="a1s3")
ax[1].plot(a1s3_1_cstate_vs["Concurrency"], a1s3_1_cstate_vs["P99"], color=colors[0][0], label="a1s3")
savefig("thread-layout-cstate-vs-a4s0-yield-a1s3.png", xmax=42)

fig, ax = subplots()
ax[0].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["QPS"], color=colors[0][2], label="a4s0-yield")
ax[1].plot(a4s0_1_cstate_yield_vs["Concurrency"], a4s0_1_cstate_yield_vs["P99"], color=colors[0][2], label="a4s0-yield")
ax[0].plot(a4s4_1_cstate_vs["Concurrency"], a4s4_1_cstate_vs["QPS"], color=colors[1][0], label="a4s4")
ax[1].plot(a4s4_1_cstate_vs["Concurrency"], a4s4_1_cstate_vs["P99"], color=colors[1][0], label="a4s4")
savefig("thread-layout-cstate-vs-a4s0-yield-a4s4.png", xmax=42)

fig, ax = subplots()
ax[0].plot(a1s4_sc["Concurrency"], a1s4_sc["QPS"], color=colors[0][0], label="scylla")
ax[1].plot(a1s4_sc["Concurrency"], a1s4_sc["P99"], color=colors[0][0], label="scylla")
ax[0].plot(a1s4_vs["Concurrency"], a1s4_vs["QPS"], color=colors[0][1], label="vector-store")
ax[1].plot(a1s4_vs["Concurrency"], a1s4_vs["P99"], color=colors[0][1], label="vector-store")
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

a1s4_aws_4_sc = pd.read_csv("data/a1s4-aws-4-scylla.csv")

fig, ax = subplots()
ax[0].plot(a1s4_aws_4_sc["Concurrency"], a1s4_aws_4_sc["QPS"], color=colors[0][0], label="a1s4 k=100 recall~=95.3%")
ax[1].plot(a1s4_aws_4_sc["Concurrency"], a1s4_aws_4_sc["P99"], color=colors[0][0], label="a1s4 k=100 recall~=95.3%")
savefig("a1s4-aws-4.png")

a1s4_aws_16_sc = pd.read_csv("data/a1s4-aws-16-scylla.csv")
a1s4_aws_16_10_sc = pd.read_csv("data/a1s4-aws-16-10-scylla.csv")

fig, ax = subplots()
ax[0].plot(a1s4_aws_16_10_sc["Concurrency"], a1s4_aws_16_10_sc["QPS"], color=colors[0][0], label="a1s4 k=10 recall~=99.2")
ax[1].plot(a1s4_aws_16_10_sc["Concurrency"], a1s4_aws_16_10_sc["P99"], color=colors[0][0], label="a1s4 k=10 recall~=99.2")
ax[0].plot(a1s4_aws_16_sc["Concurrency"], a1s4_aws_16_sc["QPS"], color=colors[0][1], label="a1s4 k=100 recall~=95.3%")
ax[1].plot(a1s4_aws_16_sc["Concurrency"], a1s4_aws_16_sc["P99"], color=colors[0][1], label="a1s4 k=100 recall~=95.3%")
savefig("a1s4-aws-16.png", xmax=480)

a4s0_aws_100m_10_sc = pd.read_csv("data/a4s0-aws-100m-10-scylla.csv")
a4s0_aws_100m_100_sc = pd.read_csv("data/a4s0-aws-100m-100-scylla.csv")

fig, ax = subplots()
ax[0].plot(a4s0_aws_100m_10_sc["Concurrency"], a4s0_aws_100m_10_sc["QPS"], color=colors[0][0], label="a4s0 k=10 recall~=97.2%")
ax[1].plot(a4s0_aws_100m_10_sc["Concurrency"], a4s0_aws_100m_10_sc["P99"], color=colors[0][0], label="a4s0 k=10 recall~=97.2%")
ax[0].plot(a4s0_aws_100m_100_sc["Concurrency"], a4s0_aws_100m_100_sc["QPS"], color=colors[0][1], label="a4s0 k=100 recall~=98.4%")
ax[1].plot(a4s0_aws_100m_100_sc["Concurrency"], a4s0_aws_100m_100_sc["P99"], color=colors[0][1], label="a4s0 k=100 recall~=98.4%")
savefig("a4s0-aws-100m.png", xmax=480)

xtask = [
    0,
    1,
    1,
    2,
    2,
    4,
    4,
    5,
    5,
    6,
    6,
    10,
    10,
    20,
    20,
    120,
    120,
    123,
    123,
    124,
    124,
    130,
    130,
    131,
    131,
    134,
    134,
    135,
]

ytask1 = [
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
]

fig, ax = plt.subplots(1, 1, figsize=[9.6, 4.3], layout="tight")
ax.plot(xtask, ytask1, color=colors[0][0], label="ideal task")
ax.yaxis.set_visible(False)
plt.ylabel("CPU Usage")
plt.xlabel("Time")
plt.savefig("task-scheduling-single.png", transparent=True)

xtask = [
    0,
    1,
    1,
    2,
    2,
    4,
    4,
    5,
    5,
    6,
    6,
    10,
    10,
    20,
    20,
    120,
    120,
    123,
    123,
    124,
    124,
    130,
    130,
    131,
    131,
    231,
    231,
    234,
    234,
    236,
    236,
    238,
    238,
    240,
]

ytask1 = [
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
]

ytask2 = [
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    3,
    2,
    2,
    3,
    3,
    2,
    2,
    3,
    3,
    2,
    2,
    3,
    3,
    2,
    2,
    3,
    3,
]

fig, ax = plt.subplots(1, 1, figsize=[9.6, 4.3], layout="tight")
ax.plot(xtask, ytask1, color=colors[0][0], label="task1")
ax.plot(xtask, ytask2, color=colors[0][1], label="task2")
ax.yaxis.set_visible(False)
plt.ylabel("CPU Usage")
plt.xlabel("Time")
plt.savefig("task-scheduling-two.png", transparent=True)

