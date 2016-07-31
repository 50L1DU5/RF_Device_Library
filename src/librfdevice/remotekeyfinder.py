#!/usr/bin/env python

from librfdevice.ooktransmitter import OOKTransmitter


class RemoteKeyFinder(OOKTransmitter):

    # Information about this unit can be found by
    # looking up this FCC ID at fccid.io
    FCCID = 'SF8KDVR1301'

    description = ('This transmitter unit is part of a Sharper Image product that allows a user to '
            'find their keys. The recieving unit is placed on the user\'s keychain and when the '
            'transmitter\'s button is pushed it emits a signal that causes the keyfob to produce a sound. '
            'The transmitting unit has two buttons, corresponding to two different receivers.')

    frequency = 315000000
    baud = 5000

    button1_seq = "\x0f\xf9\xe0\x9e\x09\xff\x3c\x13\xc1\x3f\xe7\x82\x78\x27\xfc\xf0\x4f\x04"
    button2_seq = "\x0f\xf9\xe0\x9e\x09\xff\x3c\x13\xc1\x3f\xe7\x82\x78\x27\xfc\xf0\x4f\x04"

    def __init__(self):
        super(RemoteKeyFinder, self).__init__(self.frequency, self.baud, None)

    def button_1(self, n=20):
        self.send_key_sequence(n, self.button1_seq)

    def button_2(self, n=20):
        self.send_key_sequence(n, self.button2_seq)
