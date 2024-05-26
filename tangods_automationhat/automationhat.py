from tango import AttrWriteType, DispLevel, DevState, DevBoolean, DevFloat
from tango.server import Device, attribute, command, device_property
import automationhat as ahat


class AutomationHAT(Device):    

    def init_device(self):
        Device.init_device(self)
        self.initialize_dynamic_attributes()
        self.set_state(DevState.ON)

    def initialize_dynamic_attributes(self):
        # relays
        for i in range(3):
            attr = attribute(
                name=f"relay_{i+1}",
                label=f"Relay {i+1}",
                dtype=DevBoolean,
                access=AttrWriteType.READ_WRITE,
                fget=self.relay_read,
                fset=self.relay_write,
            )
            self.add_attribute(attr)

        # inputs
        for i in range(3):
            attr = attribute(
                name=f"input_{i+1}",
                label=f"Input {i+1}",
                dtype=DevBoolean,
                access=AttrWriteType.READ,
                fget=self.input_read,
            )
            self.add_attribute(attr)        

        # outputs
        for i in range(3):
            attr = attribute(
                name=f"output_{i+1}",
                label=f"Output {i+1}",
                dtype=DevBoolean,
                access=AttrWriteType.READ_WRITE,
                fget=self.output_read,
                fset=self.output_write,
            )
            self.add_attribute(attr)

        # ADCs
        for i in range(4):
            attr = attribute(
                name=f"adc_{i+1}",
                label=f"ADC {i+1}",
                dtype=DevFloat,
                unit="V",
                access=AttrWriteType.READ,
                fget=self.adc_read,
            )
            self.add_attribute(attr)  

    def relay_read(self, attr):
        id = int(attr.get_name().split('_')[1])-1

        return ahat.relay[id].is_on()

    def relay_write(self, attr):
        id = int(attr.get_name().split('_')[1])-1
            
        value = attr.get_write_value()

        if value:
            ahat.relay[id].on()
        else:            
            ahat.relay[id].off()

    def input_read(self, attr):
        id = int(attr.get_name().split('_')[1])-1

        return ahat.input[id].read()

    def output_read(self, attr):
        id = int(attr.get_name().split('_')[1])-1

        return ahat.output[id].is_on()

    def output_write(self, attr):
        id = int(attr.get_name().split('_')[1])-1
            
        value = attr.get_write_value()

        if value:
            ahat.output[id].on()
        else:            
            ahat.output[id].off()

    def adc_read(self, attr):
        id = int(attr.get_name().split('_')[1])-1

        return ahat.analog[id].read()
