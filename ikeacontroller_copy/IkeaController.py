from pytradfri import Gateway
from pytradfri.api.libcoap_api import APIFactory
from pytradfri.error import PytradfriError
from pytradfri.util import load_json, save_json

import uuid
import argparse


class IkeaController:
    CONFIG_FILE = 'tradfri_standalone_psk.conf'
    IP = '192.168.1.155'

    def __init__(self):
        conf = load_json(self.CONFIG_FILE)

        try:
            identity = conf[self.IP].get('identity')
            psk = conf[self.IP].get('key')
            api_factory = APIFactory(host=self.IP, psk_id=identity, psk=psk)
        except KeyError:
            identity = uuid.uuid4().hex
            api_factory = APIFactory(host=self.IP, psk_id=identity)

            try:
                psk = api_factory.generate_psk('5Ja2eJM13hSQhnPt')
                print('Generated PSK: ', psk)

                conf[self.IP] = {'identity': identity,
                                'key': psk}
                save_json(self.CONFIG_FILE, conf)
            except AttributeError:
                raise PytradfriError("Please provide the 'Security Code' on the "
                                    "back of your Tradfri gateway using the "
                                    "-K flag.")

        self.api = api_factory.request

        gateway = Gateway()

        devices_command = gateway.get_devices()
        devices_commands = self.api(devices_command)
        self.devices = self.api(devices_commands)
        print(self.devices)

        self.lights = [dev for dev in self.devices if dev.has_light_control]
        sockets = [dev for dev in self.devices if dev.has_socket_control]
        self.oven = [socket for socket in sockets if socket.name == 'Oven'][0]

    def turn_on_oven(self):
        self.api(self.oven.socket_control.set_state(True))

    def turn_off_oven(self):
        self.api(self.oven.socket_control.set_state(True))

    def get_oven_state(self):
        return self.oven.socket_control.sockets[0].state

    def get_light_state(self, index):
        return self.lights[index].light_control.lights[0].state

    def get_light_dimmer(self, index):
        return self.lights[index].light_control.lights[0].dimmer

    def turn_light_on(self, index):
        self.api(self.lights[index].light_control.set_state(True))
    
    def turn_light_off(self, index):
        self.api(self.lights[index].light_control.set_state(False))
    
    def set_light_dimmer(self, index, dim):
        bit = max(min(254, round(dim * 254 / 100)), 0)
        print('Set light %d to %s%%' % (index, max(min(100, dim), 0)))
        self.api(self.lights[index].light_control.set_dimmer(bit))

    def set_light_color(self, index, color):
        if color == 'warm':
            c = 'efd275'
        elif color == 'cold':
            c = 'f5faf6'
        else:
            c = 'f1e0b5'
        print('Set light %d to %s color' % (index, color))
        self.api(self.lights[index].light_control.set_hex_color(c))
