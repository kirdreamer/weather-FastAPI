import configparser


DEFAULT_PROPERTY_PATH = "resources/config.properties"


class PropertiesManager:
    def __init__(self, file_path: str = DEFAULT_PROPERTY_PATH):
        self.properties = self.read_properties_file(file_path)
    
    def read_property(self, property_key: str) -> str:
        return self.properties.get("DEFAULT", property_key)

    @staticmethod
    def read_properties_file(file_path: str) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(file_path)
        return config
