from tango import AttrWriteType, DispLevel, DevState
from tango.server import Device, attribute, command, device_property
import automation-hat as ahat


class AutomationHAT(Device):
    

    def init_device(self):
        Device.init_device(self)
        self.set_state(DevState.ON)
