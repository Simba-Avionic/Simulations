import yaml
from rocketpy import GnssReceiver, Accelerometer, Barometer, Gyroscope, Rocket
import numpy as np

class R7Sensors:
    def __init__(self, yaml_path: str, save_path: str):
        self.yaml_path = yaml_path
        self.save_path  = save_path
        self.gyros: list[Gyroscope] = []
        self.accels: list[Accelerometer] = []
        self.baros: list[Barometer] = []
        self.gps: list[GnssReceiver] = []

    def save_sensors_data(self):
        all_sensors = self.accels + self.gyros + self.baros + self.gps
        for sensor in all_sensors:
            if getattr(sensor, "measured_data", None) and len(sensor.measured_data) > 0:
                sensor.export_measured_data(f"{self.save_path}/{sensor.name}.csv")

    def load_sensors(self):
        with open(self.yaml_path, 'r') as file:
            data = yaml.safe_load(file)
        if not data["enabled"]:
            return False
        sensor_loaders = {
            "Accel": self.__load_accels_sensors,
            "Gyro": self.__load_gyro_sensors,
            "Gps": self.__load_gps_sensors,
            "Barometer": self.__load_baro_sensors,
        }

        for key, loader in sensor_loaders.items():
            settings = data.get(key, [])
            if settings:
                loader(settings)

        return True

    def __load_baro_sensors(self, data):
        for baro_settings in data:
            self.baros.append(
                Barometer(
                    sampling_rate=baro_settings.get("sampling_rate", 0),
                    measurement_range=baro_settings.get("measurement_range", float('inf')),
                    resolution=baro_settings.get("resolution", 0),
                    noise_density=baro_settings.get("noise_density", 0),
                    noise_variance=baro_settings.get("noise_variance", 1),
                    random_walk_density=baro_settings.get("random_walk_density", 0),
                    random_walk_variance=baro_settings.get("random_walk_variance", 1),
                    constant_bias=baro_settings.get("constant_bias", 0),
                    operating_temperature=baro_settings.get("operating_temperature", 25),
                    temperature_bias=baro_settings.get("temperature_bias", 0),
                    temperature_scale_factor=baro_settings.get("temperature_scale_factor", 0),
                    name=baro_settings.get("name", "Barometer")
                )
            )

    def __load_gps_sensors(self, data):
        for gps_settings in data:
            self.gps.append(
                GnssReceiver(
                    sampling_rate=gps_settings["sampling_rate"],
                    position_accuracy=gps_settings.get("position_accuracy", 0),
                    altitude_accuracy=gps_settings.get("altitude_accuracy", 0),
                    name=gps_settings["name"]
                )
            )

    def __load_accels_sensors(self, data):
        for accel_settings in data:
            self.accels.append(
                Accelerometer(
                    sampling_rate=accel_settings["sampling_rate"],
                    consider_gravity=accel_settings.get("consider_gravity",False),
                    orientation=accel_settings.get("orientation",[0, 0, 0]),
                    measurement_range=accel_settings.get("measurement_range", np.inf),
                    resolution=accel_settings.get("resolution", 0),
                    noise_density=accel_settings.get("noise_density", 0),
                    random_walk_density=accel_settings.get("random_walk_density", 0),
                    constant_bias=accel_settings.get("constant_bias", 0),
                    name=accel_settings.get("name")
                )
            )
    def __load_gyro_sensors(self, data):
        for gyro_settings in data:
            self.gyros.append(
                Gyroscope(
                    sampling_rate=gyro_settings["sampling_rate"],
                    resolution=gyro_settings.get("resolution", 0),
                    orientation=gyro_settings.get("orientation", (0, 0, 0)),
                    noise_density=gyro_settings.get("noise_density", 0),
                    noise_variance=gyro_settings.get("noise_variance", 1),
                    random_walk_density=gyro_settings.get("random_walk_density", 0),
                    random_walk_variance=gyro_settings.get("random_walk_variance", 1),
                    constant_bias=gyro_settings.get("constant_bias", 0),
                    operating_temperature=gyro_settings.get("operating_temperature", 298.15),
                    temperature_bias=gyro_settings.get("temperature_bias", 0),
                    temperature_scale_factor=gyro_settings.get("temperature_scale_factor", 0),
                    cross_axis_sensitivity=gyro_settings.get("cross_axis_sensitivity", 0),
                    acceleration_sensitivity=gyro_settings.get("acceleration_sensitivity", 0),
                    name=gyro_settings.get("name")
                )
            )

if __name__ == "__main__":
    sens = R7Sensors("sensors.yaml", "sesors")
    sens.load_sensors()
    print(sens.gps)
    sens.save_sensors_data()