from twopilabs.utils.scpi import *
from .x1000_base import SenseX1000Base


class ScpiInitiate(object):
    """Class containing SCPI commands concerning the INITIATE subsystem"""

    def __init__(self, device: ScpiDevice) -> None:
        self.device = device

    def immediate(self):
        """Immediately initiates (arms) the device for triggering"""
        self.device.execute("INIT:IMM")
        self.device.raise_error()

    def immediate_and_receive(self) -> SenseX1000Base.Acquisition:
        """Immediately initiates (arms) the device for triggering and returns the acquisition object"""
        stream = self.device.execute("INIT:IMM; *WAI; CALC:DATA?", result=ScpiArbStream)
        return SenseX1000Base.Acquisition.from_stream(stream)
