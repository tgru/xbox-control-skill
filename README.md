# <img src='https://rawgithub.com/FortAwesome/Font-Awesome/master/advanced-options/raw-svg/solid/gamepad.svg' card_color='#22a7f0' width='50' height='50' style='vertical-align:bottom'/> Xbox Control

Lets you control your Xbox One by voice.

## Description

This is a skill for the Mycroft AI voice assistant, which enables you to control your Xbox One with voice commands.

## Setup

### Installation

At the moment this skill requires an [Xbox Smartglass REST server](https://github.com/OpenXbox/xbox-smartglass-rest-python) from OpenXbox running somewhere. In case the server is not running on the same device the URL and port of this server can be configured in the skill settings, since the default setting is `localhost:5557`.

Apart from this, a normal skill installation by cloning this repository can be done.

### Configuration

On first startup the skill can scan your network for Xbox One devices if you ask Mycroft to do this (*Find my Xbox*) and will add it automatically if found one. In case the skill does not find any Xbox or multiple ones, the IP address and Live ID of your device must be added manually in the skill settings, which are accesible through [home.mycroft.ai](home.mycroft.ai).

## Examples

 - "Power on the Xbox"
 - "Switch the Xbox off"

## Features

### Power

| Function  | Example             |
|-----------|---------------------|
| Power On  | Turn on the Xbox    |
| Power off | Switch the Xbox off |

### Media Control

| Function | Example                        |
|----------|--------------------------------|
| Play     | Play music on the Xbox         |
| Pause    | Pause the song on the Xbox     |
| Stop     | Stop Xbox media                |
| Next     | Skip the track on the Xbox     |
| Previous | Play the last song on the Xbox |

### Miscellaneous

| Function       | Example                            |
|----------------|------------------------------------|
| Auto Detection | Find my Xbox                       |

## Credits

@tgru

## Disclaimer

Xbox, Xbox One, Smartglass and Xbox Live are trademarks of Microsoft Corporation. This project is in no way endorsed by or affiliated with Microsoft Corporation, or any associated subsidiaries, logos or trademarks.
