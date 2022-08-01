from fmpy import *
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + "//..//..//FMU_Connector")
sys.path.insert(0, dir_path + "//..//FMU_Connector")
from FMU_Connector import FMUConnector

print("simplemain.py")
print(os.getcwd())

print_logger = lambda s: print('[FMI] ' + s)
model_filepath = os.getcwd() + '/../samples/Aircraft_noParameters.fmu'
# simulate_fmu(filename = model_filepath, stop_time=100, debug_logging=True, fmi_call_logger=print_logger)


# [FMI] fmi2EnterInitializationMode(component=0x7ffa960140e0) -> OK
# [FMI] fmi2ExitInitializationMode(component=0x7ffa960140e0) -> OK
# [FMI] fmi2GetReal(component=0x7ffa960140e0, vr=[335544320, 335544321, 335544322, 335544323, 335544324, 335544325, 335544326], nvr=7, value=[0.0, 0.0, 1.5, 2.0, 0.0, -0.0, 0.0]) -> OK
# [FMI] fmi2GetInteger(component=0x7ffa960140e0, vr=[335544327], nvr=1, value=<fmpy.fmi2.c_long_Array_1 object at 0x000001A4AF1BA9C8>) -> OK
# [FMI] fmi2DoStep(component=0x7ffa960140e0, currentCommunicationPoint=0.0, communicationStepSize=0.2, noSetFMUStatePriorToCurrentPoint=1) -> OK

fmuconnector = FMUConnector(model_filepath, print_logger)
fmuconnector.initialize_model()
fmuconnector.reset({})
fmuconnector.run_step()

# pretend to be a new episode
fmuconnector.initialize_model()
fmuconnector.run_step()
