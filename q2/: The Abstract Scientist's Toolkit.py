from abc import ABC, abstractmethod
class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")

class TempSensor(Sensor):
    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")

print("--- Lab Inventory System ---")
for sensor in [PHSensor(), TempSensor()]:
    sensor.get_reading()
print()
print("-" * 28)

my_sensor = Sensor()