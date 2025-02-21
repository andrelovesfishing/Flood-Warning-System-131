import numpy as np
import matplotlib as plt

def polyfit(dates, levels, p):
    true_dates = plt.dates.date2num(dates)
    poly = np.polyfit(true_dates, levels, p)
    d0 = np.mean(true_dates)
    return (poly,d0)