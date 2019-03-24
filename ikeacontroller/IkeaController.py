from pytradfri import Gateway
from pytradfri.api.libcoap_api import APIFactory
from pytradfri.error import PytradfriError
from pytradfri.util import load_json, save_json

import uuid


class IkeaController:
    CONFIG_FILE = './tradfri_standalone_psk.conf'
    IP = '192.168.1.155'

    def __init__(self):
        conf = load_json(self.CONFIG_FILE)

        try:
            # identity = conf[self.IP].get('identity')
            # psk = conf[self.IP].get('key')
            identity = 'cfbdd372f82a4ffdbbca0644cc3aa304'
            psk = '5Ja2eJM13hSQhnPt'
            api_factory = APIFactory(host=self.IP, psk_id=identity, psk=psk)
        except KeyError:
            identity = uuid.uuid4().hex
            api_factory = APIFactory(host=self.IP, psk_id=identity)

            try:
                psk = api_factory.generate_psk(conf[self.IP].key)
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

    def list_all_components(self):
        print(self.devices)
        return self.devices

    def get_component(self, component_id):
        try:
            return [dev for dev in self.devices if dev.id == component_id][0]
        except IndexError:
            raise PytradfriError("Component does not exist")

    def get_socket_state(self, socket_id):
        socket = self.get_component(socket_id)
        return socket.socket_control.sockets[0].state

    def toggle_socket(self, socket_id, state):
        socket = self.get_component(socket_id)
        self.api(socket.socket_control.set_state(state))

    def get_light_state(self, light_id):
        light = self.get_component(light_id)
        return light.light_control.lights[0].state

    def get_light_dimmer(self, light_id):
        light = self.get_component(light_id)
        return light.light_control.lights[0].dimmer
    
    def toggle_light(self, light_id, state):
        light = self.get_component(light_id)
        self.api(light.light_control.set_state(state))
    
    def set_light_dimmer(self, light_id, dim):
        light = self.get_component(light_id)
        bit = max(min(254, round(dim * 254 / 100)), 0)
        self.api(light.light_control.set_dimmer(bit))

    def set_light_color(self, light_id, color):
        light = self.get_component(light_id)
        if color == 'warm':
            c = 'efd275'
        elif color == 'cold':
            c = 'f5faf6'
        else:
            c = 'f1e0b5'
        self.api(light.light_control.set_hex_color(c))


ikea = IkeaController()
