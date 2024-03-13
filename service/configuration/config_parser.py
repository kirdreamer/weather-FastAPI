import configparser


DEFAULT_PROPERTY_PATH = "\weather-FastAPI\config.properties"


class PropertiesManager:
    def __init__(self, file_path: str = DEFAULT_PROPERTY_PATH):
        self.properties = self.read_properties_file(file_path)
    
    def read_property(self, property_key: str) -> str:
        return self.properties.get('DEFAULT', property_key)

    def read_properties_file(file_path: str) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(file_path)
        return config
