import appdaemon.plugins.hass.hassapi as hass


class RemoteControl(hass.Hass):
    def initialize(self):
        if "event" in self.args:
            self.listen_event(self.handle_event, self.args["event"])

    def handle_event(self, event_name, data, kwargs):
        if data["id"] == self.args["id"]:
            self.log(data["event"])
            if data["event"] == 1002:
                self.log("Fast Right - light on")
                self.call_service("light/turn_on", entity_id="light.comodinoci")
            elif data["event"] == 2002:
                if self.get_state("light.comodinoci") == "on":
                    current_brightness = self.get_state('light.comodinoci', attribute='brightness')
                    new_brightness = current_brightness + 25
                    if new_brightness > 254:
                        new_brightness=254
                    self.log("Slow Right - dim up (%i)",new_brightness )
                    self.call_service('light/turn_on', entity_id='light.comodinoci', brightness=new_brightness, transition=2)
            elif data["event"] == 3002:
                
                if self.get_state("light.comodinoci") == "on":
                    current_brightness = self.get_state('light.comodinoci', attribute='brightness')
                    new_brightness = current_brightness - 25
                    if new_brightness < 0:
                        new_brightness = 0
                    self.log("Slow Left - dim down (%i)", new_brightness)    
                    self.call_service('light/turn_on', entity_id='light.comodinoci', brightness=new_brightness, transition=2)
            elif data["event"] == 4002:
                self.log("Fast Left - light off")
                self.call_service("light/turn_off", entity_id="light.comodinoci"
