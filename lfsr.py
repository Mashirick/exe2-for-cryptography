from pylfsr import LFSR
import matplotlib.pyplot as plt

L1 = LFSR(initstate='random',fpoly=[19,18,17,14],counter_start_zero=False)
L2 = LFSR(initstate='random',fpoly=[22,21],counter_start_zero=False)
L3 = LFSR(initstate='random',fpoly=[23,22,21,8],counter_start_zero=False)

fig1, ax1 = plt.subplots(figsize=(8,3))
for _ in range(35):
  ax1.clear()
  L1.Viz(ax=ax1, title='')
  plt.ylim([-0.1,None])
  L1.next()
  fig1.canvas.draw()
  plt.pause(0.1)
  
fig2, ax2 = plt.subplots(figsize=(8,3))
for _ in range(35):
  ax2.clear()
  L2.Viz(ax=ax2, title='R2')
  plt.ylim([-0.1,None])
  L2.next()
  fig2.canvas.draw()
  plt.pause(0.1)
  
fig3, ax3 = plt.subplots(figsize=(8,3))    
for _ in range(35):
  ax3.clear()
  L3.Viz(ax=ax3, title='R3')
  plt.ylim([-0.1,None])
  L3.next() 
  fig3.canvas.draw()
  plt.pause(0.1)
  
  