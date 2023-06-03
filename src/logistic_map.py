import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np
from math import *


# The parametrized function to be plotted
def f(x, r):
    return r * x * (1 - x)


def calc_equilibrium(x, r):
    populations = [x]
    while True:
        x = f(x, r)
        for j in range(0, len(populations)):
            if abs(populations[j] - x) < 1e-5:
                return populations[j:]
        populations.append(x)


# Define initial parameters
growth_rate = 2.6
initial_population = 0.5

# x-axis
YEAR_SPAN = 30
time = np.linspace(0, YEAR_SPAN, YEAR_SPAN + 1)


# y-axis
def generate_population(initial_population, growth_rate):
    populations = [initial_population]
    for i in range(YEAR_SPAN):
        populations.append(f(populations[i], growth_rate))
    return populations


equilibrium_population = generate_population(initial_population, growth_rate)

# Create the figure and the line that we will manipulate
fig1, ax1 = plt.subplots()
line, = plt.plot(time, equilibrium_population, linewidth=2)
ax1.set_title('Population vs Time')
ax1.set_xlabel('Time')
ax1.set_xlim(0, YEAR_SPAN)
ax1.set_xticks(np.arange(0, YEAR_SPAN + 1, 2))
ax1.set_ylabel('Population')
ax1.set_ylim(0, 1)
ax1.set_yticks(np.arange(0, 1.1, 0.1))
ax1.grid(True)

# adjust the main plot to make room for the sliders
fig1.subplots_adjust(bottom=0.3)

# Make a slider to control the growth rate.
ax_growth_rate = fig1.add_axes([0.25, 0.1, 0.65, 0.03])
growth_rate_slider = widgets.Slider(
    ax=ax_growth_rate,
    label='Growth rate',
    valmin=0.1,
    valmax=5,
    valinit=growth_rate,
)

# Make a slider to control the initial population.
ax_initial_population = fig1.add_axes([0.25, 0.15, 0.65, 0.03])
initial_population_slider = widgets.Slider(
    ax=ax_initial_population,
    label='Initial population',
    valmin=0,
    valmax=1,
    valinit=initial_population,
)


# The function to be called anytime a slider's value changes
def update(val):
    populations = generate_population(initial_population_slider.val,
                                      growth_rate_slider.val)
    line.set_ydata(populations)
    fig1.canvas.draw_idle()


# register the update function with each slider
growth_rate_slider.on_changed(update)
initial_population_slider.on_changed(update)


# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
def reset_button_on_clicked(mouse_event):
    initial_population_slider.reset()
    growth_rate_slider.reset()


reset_button_ax = fig1.add_axes([0.8, 0.025, 0.1, 0.04])
reset_button = widgets.Button(reset_button_ax, 'Reset', hovercolor='0.975')
reset_button.on_clicked(reset_button_on_clicked)

# Bifurcation diagram
RATES_MIN = 0
RATES_MAX = 4
RATES_STEP = 0.01
fig2, ax2 = plt.subplots()
ax2.set_title('Bifurcations')
ax2.set_xlabel('Rate')
ax2.set_xlim(RATES_MIN, RATES_MAX)
ax2.set_ylabel('Equilibrium Population')
ax2.set_ylim(0, 1)

for rate in np.arange(RATES_MIN, RATES_MAX, RATES_STEP):
    equilibrium_population = calc_equilibrium(initial_population, rate)
    # print(rate, len(equilibrium_population))
    ax2.scatter([rate] * len(equilibrium_population),
                equilibrium_population,
                s=0.1,
                c='black')

plt.show()
