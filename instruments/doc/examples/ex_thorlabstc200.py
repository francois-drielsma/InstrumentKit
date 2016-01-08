#Thorlabs Temperature Controller example

import instruments as ik
import quantities
tc = ik.thorlabs.TC200.open_serial('/dev/tc200', 115200)

tc.p = 200
print("The current p gain is: ", tc.p)

tc.temperature = 70*quantities.degF
print("The current temperature is: ", tc.temperature)
'''
tc.mode = tc.Mode.normal
print("The current mode is: ", tc.mode)

tc.enable = True
print("The current enabled state is: ", tc.enable)

tc.i = 2
print("The current i gain is: ", tc.i)

tc.d = 2
print("The current d gain is: ", tc.d)

tc.degrees = quantities.degF
print("The current degrees settings is: ", tc.degrees)

tc.sensor = tc.Sensor.PTC100
print("The current sensor setting is: ", tc.sensor)

tc.beta = 3900
print("The current beta settings is: ", tc.beta)

tc.max_temperature = 150*quantities.degC
print("The current max temperature setting is: ", tc.max_temperature)

tc.max_power = 1000*quantities.mW
print("The current max power setting is: ", tc.max_power)
'''

