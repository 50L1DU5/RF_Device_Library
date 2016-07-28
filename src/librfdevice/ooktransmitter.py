# Base class for OOK transmitters

from rflib import *


class OOKTransmitter(object):

    # The constant for On Off Key transmitters is the
    # method of modulation.
    modulation = MOD_ASK_OOK

    # Every subclass of OOK transmitters will most likely
    # have these things.
    description = 'Base class for On-Off Keying transmitter types.'
    frequency = None
    baud = None
    key_sequence = "\x00"

    def __init__(self, frequency, baud, key_sequence):
        self.frequency = int(frequency)
        self.baud = int(baud)
        self.key_sequence = key_sequence
        self.configure()

    def configure(self):
        d.setFreq(self.frequency)
        d.setMdmModulation(self.modulation)
        d.setMdmDRate(self.baud)

    def set_baud(self, new_baud):
        self.baud = int(new_baud)

    def set_frequency(self, new_freq):
        self.frequency = int(new_freq)

    def set_key_sequence(self, new_key_sequence):
        self.key_sequence = new_key_sequence

    def repeat_key_sequence(self, n, seq=None):
        return (seq or self.key_sequence) * int(n)

    def send_key_sequence(self, n=1, seq=None):
        self.configure()
        d.RFxmit(self.repeat_key_sequence(n, seq or self.key_sequence))

