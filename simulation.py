from audioop import avg
import trial002
import statistics
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def Simulate(Nsim):
    number_player =  []
    for i in range(1,Nsim):
        number_player.append(trial002.Poker())
    return (
        statistics.mean(number_player),
        min(number_player),
        st.t.interval(alpha=0.025, loc = np.mean(number_player), scale = st.sem(number_player), df = len(number_player)-1 ),
        max(number_player)
    )

print(Simulate(Nsim = 9999))