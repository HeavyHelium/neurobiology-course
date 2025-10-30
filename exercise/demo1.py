
# %%

import matplotlib.pyplot as plt
import nest
import nest.voltage_trace

nest.set_verbosity("M_WARNING")
nest.ResetKernel()

# %%

def plot_voltage_trace(voltmeter, name="voltage_trace"):
    nest.voltage_trace.from_device(voltmeter)
    plt.savefig(f"./plots/{name}.png")
    plt.show()

# %%

neuron = nest.Create("iaf_psc_alpha")
voltmeter = nest.Create("voltmeter")
neuron.I_e = 376.0

nest.Connect(voltmeter, neuron)
nest.Simulate(1000.0)
# %%
plot_voltage_trace(voltmeter, name="demo1_voltage_trace")

# %%