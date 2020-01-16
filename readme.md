# DeCONZ TRADFRI Dimmer

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

_Smooth dimming functionality for TRADFRI Dimmer and lights connected through DeCONZ_

## Installation

Download the `remote_control` directory from inside the `apps` directory here to your local `apps` directory, then add the configuration to enable the `hacs` module.

## App configuration

### Basic configuration:
The behaviour is as follows:

* Fast turn right -> light turns on
* Fast turn left -> light turns off
* Slow turn right -> brightness increases smoothly
* Slow turn left  -> brightness decreases smoothly

##### Example config:

```yaml
remote_control:
  module: remote_control
  class: RemoteControl
  event: deconz_event
  id: tradfri_wireless_dimmer
  dimlight: group.banano
  step: 25
```
#### Configuration
key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | remote_control | The module name of the app.
`class` | False | string | RemoteControl | The name of the Class.
`event` | False | string | deconz_event | deconz event.

##### Entities
key | optional | type | default | description
-- | -- | -- | -- | --
`id` | False | string | | The id of the Tradfri Dimmer Switch.
`dimlight` | False | string | | The entitiy_id of the light.
`step` | False | number | | Amount of dimming.
