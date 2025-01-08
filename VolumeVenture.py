import ctypes
import comtypes
from ctypes import wintypes
import pycaw.pycaw as pycaw

# Initialize the COM library
ctypes.windll.ole32.CoInitialize(None)

class AudioManager:
    def __init__(self):
        self.devices = {}
        self.enumerate_audio_devices()

    def enumerate_audio_devices(self):
        device_enumerator = comtypes.CoCreateInstance(
            pycaw.CLSID_MMDeviceEnumerator, 
            pycaw.MMDeviceEnumerator, 
            comtypes.CLSCTX_INPROC_SERVER
        )
        collection = device_enumerator.EnumAudioEndpoints(
            pycaw.eRender, pycaw.DEVICE_STATE_ACTIVE
        )
        count = collection.GetCount()

        for i in range(count):
            device = collection.Item(i)
            volume = device.Activate(
                pycaw.IAudioEndpointVolume._iid_, 
                comtypes.CLSCTX_INPROC_SERVER, 
                None
            )
            self.devices[device.GetId()] = volume

    def set_volume(self, device_id, level):
        if device_id in self.devices:
            self.devices[device_id].SetMasterVolumeLevelScalar(level, None)
        else:
            print(f"Device ID {device_id} not found.")

    def get_volume(self, device_id):
        if device_id in self.devices:
            return self.devices[device_id].GetMasterVolumeLevelScalar()
        return None

    def list_audio_devices(self):
        return list(self.devices.keys())

def main():
    audio_manager = AudioManager()
    print("Available Audio Devices:")
    devices = audio_manager.list_audio_devices()
    for idx, device in enumerate(devices):
        current_volume = audio_manager.get_volume(device)
        print(f"[{idx}] Device ID: {device}, Current Volume: {current_volume:.2f}")

    try:
        device_index = int(input("Select device index to change volume: "))
        new_volume = float(input("Enter new volume level (0.0 to 1.0): "))
        selected_device = devices[device_index]
        audio_manager.set_volume(selected_device, new_volume)
        print(f"Volume set to {new_volume:.2f} for device ID: {selected_device}")
    except (IndexError, ValueError):
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()