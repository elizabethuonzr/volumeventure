# VolumeVenture

VolumeVenture is a Python-based utility that allows for dynamic control of audio volumes across various applications on Windows. It utilizes the Windows Core Audio APIs to manage audio levels on different audio devices.

## Features

- List all active audio output devices.
- Get the current volume level of a selected audio device.
- Set a new volume level for a selected audio device.

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Install the required packages by running:

   ```bash
   pip install pycaw comtypes
   ```

## Usage

1. Run the script with:

   ```bash
   python VolumeVenture.py
   ```

2. The script will list all available audio devices and their current volume levels.
3. Enter the index of the device you want to adjust the volume for.
4. Enter a new volume level between 0.0 and 1.0.

## Notes

- The application uses the `pycaw` library, which is a Python wrapper for the Windows Core Audio API.
- Make sure you have the necessary permissions to change system settings on your Windows machine.

## Contributing

Contributions to VolumeVenture are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.