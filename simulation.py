from audioop import avg
import trial002
import statistics
import numpy as np
import matplotlib.pyplot as plt

def Simulate(Nsim):
    number_player =  []
    for i in range(1,Nsim):
        number_player.append(trial002.Poker())
    return statistics.mean(number_player)

print(Simulate(Nsim = 99999))