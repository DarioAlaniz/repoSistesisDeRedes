import matplotlib.pyplot as plt 
import numpy as np
import PyLTSpice.LTSpice_RawRead as sp
import PyLTSpice.LTSpiceBatch as ltCommander
from shutil import copyfile
import os


meAbsPath = os.path.dirname(os.path.realpath(__file__))
lTC = ltCommander.SimCommander("ejercicios/ejer1_17/ejer1_17.asc")
vin=2

lTC.set_parameter('R',10000)
# for i in vin:
lTC.set_parameter('Vin',vin)
lTC.set_component_values(V2="SINE(0 {Vin} 1k)")
#se debe crear este comando de simulacion antes en ltspice!!!!
lTC.add_instructions(
    "; Simulation settings",
    # ".op",
    # ".step param Vin -1 1 0.5"
    ".tran 0 1m 0 0.1m"
)
#se debe llamar a esta funcion con las ruta de las .net originales para actualizarlas ya que 
# add_instruccion trabaja sobre una copia, no funciona correctamente!!!! 
lTC.write_netlist("ejercicios/ejer1_17/1_17.net")
lTC.run()
while(lTC.wait_completion() != None):
    print('Simulando.....')


# lTC.reset_netlist()  # This resets all the changes done to the checklist

LTR = sp.LTSpiceRawRead("ejercicios/ejer1_17/ejer1_17_1.raw") 

# print(LTR.get_trace_names())
# print(LTR.get_raw_property())

Vo      = LTR.get_trace("V(vo)")
vin     = LTR.get_trace("V(vin)")
time    = LTR.get_trace("time") # Gets the time axis
steps   = LTR.get_steps()
for step in range(len(steps)):
    print(step)
    plt.plot(vin.get_wave(step), Vo.get_wave(step), label=steps[step])
    # plt.plot(time.get_time_axis(step), Vo.get_wave(step), label=steps[step])
    plt.grid()

plt.legend() # order a legend
plt.show()
