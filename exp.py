import asyncio
from bleak import BleakScanner

def calculate_distance(rssi):
    txPower = -59  # one meter away RSSI
    if rssi == 0:
        return -1.0
    ratio = rssi * 1.0 / txPower
    if ratio < 1.0:
        return ratio ** 10
    else:
        return 0.89976 * ratio ** 7.7095 + 0.111

async def main():
    scanner = BleakScanner()
    devices = await scanner.discover()
    for device in devices:
        distance = calculate_distance(device.rssi)
        print(f"Device: {device.name}, RSSI: {device.rssi}, Estimated Distance: {distance} m")

asyncio.run(main())