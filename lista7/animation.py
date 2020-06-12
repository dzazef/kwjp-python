import numpy as np
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation

class Animation:

    def __init__(self, name_, x_, y_snapshots_, epochs_, anim_steps_, xlim, ylim):
        self.x = x_
        self.y_snapshots = y_snapshots_
        self.epochs = epochs_
        self.anim_step = anim_steps_
        self.fig = plt.figure()
        # self.axes = plt.axes()
        self.axes = plt.axes(xlim=xlim, ylim=ylim)
        self.scatter = self.axes.scatter([], [])
        self.text = self.axes.text(2.5, 1.15, '', fontsize=15)
        self.name = name_

    def update(self, i_):
        """Update plot values"""
        self.scatter.set_offsets(np.concatenate((self.x, self.y_snapshots[i_]),
                                                axis=1))
        self.text.set_text(f'Step {i_ * self.anim_step}')
        return self.scatter, self.text,

    def draw(self):
        """Create animation"""
        anim = FuncAnimation(self.fig, self.update,
                             frames=(self.epochs // self.anim_step),
                             interval=40, blit=True)
        anim.save(f'{self.name}.gif', writer='imagemagick')
