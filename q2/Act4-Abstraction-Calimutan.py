from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def __init__(self, name):
        super().__init__(name)

    def get_reading(self):
        print(f"[{self.get_name()}] Reading: 7.2 pH (Neutral)")

class TempSensor(Sensor):
    def __init__(self, name):
        super().__init__(name)

    def get_reading(self):
        print(f"[{self.get_name()}] Reading: 24.5°C")

print("--- Lab Inventory System ---")

s1 = PHSensor("pH Sensor")
s2 = TempSensor("Temperature Sensor")

for sensor in [s1, s2]:
    sensor.get_reading()

print("\n----------------------------\n")

print("Attempting to instantiate Sensor directly...")