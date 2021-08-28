import matplotlib.pyplot as plt 
import numpy as np
import PyLTSpice.LTSpice_RawRead as sp
import PyLTSpice.LTSpiceBatch as ltCommander
from shutil import copyfile
import os

meAbsPath = os.path.dirname(os.path.realpath(__file__))
lTC = ltCommander.SimCommander("simulacion/tpN1.asc")

lTC.set_parameter('V_1',0)
lTC.set_parameter('V_2',1)

lTC.add_instructions(
   "; Simulation settings",
   ".ac dec 30 .1 100Meg"
)
# lTC.reset_netlist()  # This resets all the changes done to the checklist

lTC.run()

print(type(lTC.wait_completion()))

LTR = sp.LTSpiceRawRead("simulacion/tpN1_1.raw") 

print(LTR.get_trace_names())
# print(LTR.get_raw_property())

V01 = LTR.get_trace("V(vo1)")
x   = LTR.get_trace("frequency") # Gets the frequency axis
steps = LTR.get_steps()

print(V01.get_wave(0))
# print(np.real(V02.get_wave(0)[0]), np.imag(V02.get_wave(0)[0]))
# print(np.sqrt(np.real(V02.get_wave(0))**2+np.imag(V02.get_wave(0))**2))
for step in range(len(steps)):
    r,i = (np.real(V01.get_wave(0)), np.imag(V01.get_wave(0)))
    # print(r,i)
    mod   = np.sqrt(r**2+i**2)
    # print(mod)
    phase = np.arctan2(i,r)
    plt.plot(x.get_time_axis(step), mod, label=steps[step])
    plt.xscale('log');plt.grid()

plt.legend() # order a legend
plt.show()
