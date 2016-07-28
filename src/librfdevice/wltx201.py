#!/usr/bin/env python

# File that can be used as an import into RFcat
# As such, rflib and RFcat must be installed

from rfdevlib.ooktransmitter import OOKTransmitter, d


class WLTX201(OOKTransmitter):

    # Info about the HeathCo-Zenith TX unit, aka
    # the WLTX-201
    MODEL = 'WLTX-201'
    FCCID = 'BJ4-WLTX201'
    description = ('The WLTX-201 is a HeathCo-Zenith doorbell transmitter. The unit has a single button and a "jumper" '
                   'circuit that controls the ring pattern of the doorbell itself. Without the jumper the chime goes, '
                   '"ding-dong," and with the jumper the chime goes, "ding."')

    # This unit's frequency is pretty stable at 315e6 MHz
    frequency = 315000000

    # In the fccid.io database, the test report
    # claims that .32ms of signal is a single digital "1"
    # so baud is calculated (1bit / .32ms) * (1000ms / 1 second) = (bits / second)
    baud = 3125

    # There are two key sequences this transmitter supports
    jumper_sequence = "\x12\x5b\x24\xb6\x5b"
    nojumper_sequence = "\x12\x5b\x24\xb2\xdb"

    # @param: jumper (optional) - Indicates whether the jumper should be simulated.
    #                             The door bell is  "ding-dong" without the jumper, and
    #                             "ding" with it.
    # @param: padding (optional) - How many "null bytes" to pad with end of the data with.
    #                              Perhaps useful for timing.
    def __init__(self, jumper=False, padding=3):
        super(WLTX201, self).__init__(self.frequency, self.baud, None)
        self.padding = padding
        self.jumper = jumper
        self.update_key_sequence()

    # Sets the bit-data based on the presence of
    # the jumper
    def update_key_sequence(self):
        if self.jumper:
            self.key_sequence = self.jumper_sequence
        else:
            self.key_sequence = self.nojumper_sequence

        self.key_sequence += ("\x00" * self.padding)

    # Returns True if the jumper is set, and False if the
    # jumper is not set.
    def has_jumper(self):
        return self.jumper

    # Remove the jumper from the unit
    def remove_jumper(self):
        self.jumper = False
        self.update_key_sequence()

    # Put the jumper in the unit. There is only one jumper on this TX unit,
    # so repeating this method will not have any affect.
    def add_jumper(self):
        self.jumper = True
        self.update_key_sequence()

    # The WLTX-201 only has one button, which is used to
    # send the On-Off Key sequence.
    def button(self, num_times=1):
        self.send_key_sequence(num_times)

    # Set the padding (trailing null-bytes) and update the key sequence
    def set_padding(self, n):
        self.padding = int(n)
        self.update_key_sequence()

    # Add a couple configuration options
    def configure(self):
        super(WLTX201, self).configure()
        d.setPktPQT(0)
        d.setMdmSyncWord(0x125b)
        d.makePktFLEN(5)

