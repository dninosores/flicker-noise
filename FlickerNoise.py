import math

# Length of animation
ANIMLENGTH = 581
# Set to random value for each shot, tweak to get peaks in the places you want
SEED = 77777
# select the node you want to affect and then put the name of the knob you want to add the noise to here
KNOB = 'position'
# Makes wave bigger/smaller (1 is max size)
# default 0.8
AMPLITUDE = 0.6
# Raises center of wave (0)
OFFSET = 0
# Lower values = messier, 0.1 default
NOISE_FREQ = 0.1
# Higher vales = faster, use OSC_FREQ for this though (0.8) default
NOISE_AMP = 0.8
# Lower values = slower, 0.07 default
OSC_FREQ = 0.07


def sawtooth(n):
    n = n % 2
    if n > 1:
        n = 1-(n-1)
    return 2 * (n - 0.5)

selected = nuke.selectedNodes()[0]
posn = selected[KNOB]
posn.setAnimated()

acc = 0
for frame in range(ANIMLENGTH):
    noise = nuke.expression(f"random({frame}*{NOISE_FREQ}, {SEED})") * NOISE_AMP
    acc += (noise)
    value = (((1+sawtooth(OSC_FREQ * acc))/2.0) * AMPLITUDE) + (1-AMPLITUDE)/2.0 + OFFSET
    #value = round(value, 1)
    #value = math.floor((value*10)/2)*2/10
    posn.setValueAt(value, frame)