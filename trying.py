import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, CheckButtons
import math
import numpy as np

# Initials values
MU_init = 25
SIGMA_init = 7.5
LENG = 1000
Black_win = 1
mu_negro = 25
sigma_negro = 7.5

# Animation controls
interval = 100 # ms, time between animation frames
loop_len = 5.0 # seconds per loop
scale = interval / 1000 / loop_len

def gaussian(x_data):
    global mu_negro, sigma_negro
    y = np.zeros(LENG)
    for i in range(LENG):
        y[i] = 1/(math.sqrt(2*math.pi)*sigma_negro)*math.exp(-(x_data[i]-mu_negro)**2/(2*sigma_negro**2))
    return y

fig, ax = plt.subplots()
# Initialize
x_data = np.linspace(MU_init-3*SIGMA_init, MU_init+3*SIGMA_init, LENG)
y_data = gaussian(x_data)
ax.set(xlim=(x_data[0], x_data[-1]), ylim=(0,0.5))
line, = plt.plot(x_data, y_data, color="steelblue", label="Prior Negro")

# Slider
axmu = plt.axes([0.25, .04, 0.50, 0.02])
axsigma = plt.axes([0.25, .01, 0.450, 0.02])
slider_mu = Slider(axmu, r'$\mu$', 0, 2*MU_init, valinit=MU_init)
slider_sigma = Slider(axsigma, r'$\sigma$', 1, SIGMA_init/2, valinit=SIGMA_init)

# CheckButtons
col = (0,0.2,0.7,0.2)
rax = plt.axes([0.15, 0.65, 0.2, 0.2], facecolor=col , alpha=0.1)
origState = (True, False)

check = CheckButtons(rax, ('Black_win', 'White_win'), origState)

def update_slider_mu(mu):
    global mu_negro
    mu_negro = mu
    line.set_ydata(gaussian(x_data))
    # redraw canvas while idle
    fig.canvas.draw_idle()
    
def update_slider_sigma(sigma):
    global sigma_negro
    sigma_negro = sigma
    line.set_ydata(gaussian(x_data))
    # redraw canvas while idle
    fig.canvas.draw_idle()
    

def animate(num):
    val = slider_mu.val
    slider_mu.set_val(val)
    val2 = slider_sigma.val 
    slider_sigma.set_val(val2)
    check.on_clicked(func)
    return line,

# call update function on slider value change
slider_mu.on_changed(update_slider_mu)
slider_sigma.on_changed(update_slider_sigma)

def func(label):
    global Black_win
    if label == 'Black_win':
        Black_win = 1    
    elif label == 'White_win':
        Black_win = 0
    plt.draw()

ani = animation.FuncAnimation(fig, animate, interval=interval, blit=False)
ax.legend()
plt.show()