from configparser import ConfigParser
from pathlib import Path


class ConnConfig:
    def __init__(self, **kwargs):
        """Fields:ADAPP_SERVER = localhost"""

        self.adapp_server = kwargs.pop("adapp_server")
        self.repeater_ip = kwargs.pop("repeater_ip")
        self.repeater_port = kwargs.pop("repeater_port")
        self.adapp_port = kwargs.pop("adapp_port")
        self.adapp_tokenvalidation_url = kwargs.pop(
            "adapp_tokenvalidation_url")

    def get_repeater_url(self):
        return f"{self.repeater_ip}:{self.repeater_port}"

    def get_adapp_url(self):
        return f"{self.adapp_server}:{self.adapp_port}"

    def get_adapp_tokenvalidation_url(self):
        return f"{self.adapp_server}:{self.adapp_port}{self.adapp_tokenvalidation_url}"

    def display_config(self):
        print(f"ADAPP_SERVER: {self.adapp_server}")
        print(f"REPEATER_IP: {self.repeater_ip}")
        print(f"REPEATER_PORT: {self.repeater_port}")
        print(f"ADAPP_PORT: {self.adapp_port}")
        print(f"ADAPP_TOKENVALIDATION_URL: {self.adapp_tokenvalidation_url}")


def read_config():
    """Read the configuration for the AuthServer plugin."""

    FILE_NAME = "adconfig.ini"
    file_path = Path(__file__).resolve().parents[2] / FILE_NAME
    print(file_path)
    config = ConfigParser()
    config.read(file_path)
    print(config.sections())
    return ConnConfig(**config["adconfig_dev"])


class ConfigFiles(StrEnum):
    """Definition of configuration file paths for different environments."""

    PROD = "/etc/my-websockify/ad_config.ini"
    DEV = "ad_config.ini"
    TEST = "/etc/my-websockify/ad_config_test.ini"


class ConnConfig:
    """Configuration structure to connections"""

    def __init__(self, **kwargs):
        """Assign configuration values from keyword arguments."""

        self.adapp_server = kwargs.pop("adapp_server")
        self.repeater_ip = kwargs.pop("repeater_ip")
        self.repeater_port = kwargs.pop("repeater_port")
        self.adapp_port = kwargs.pop("adapp_port")
        self.adapp_tokenvalidation_url = kwargs.pop(
            "adapp_tokenvalidation_url")

    def get_repeater_url(self):
        return f"{self.repeater_ip}:{self.repeater_port}"

    def get_adapp_url(self):
        return f"{self.adapp_server}:{self.adapp_port}"

    def get_adapp_tokenvalidation_url(self):
        return f"{self.adapp_server}:{self.adapp_port}{self.adapp_tokenvalidation_url}"

    def display_config(self):
        print(f"ADAPP_SERVER: {self.adapp_server}")
        print(f"REPEATER_IP: {self.repeater_ip}")
        print(f"REPEATER_PORT: {self.repeater_port}")
        print(f"ADAPP_PORT: {self.adapp_port}")
        print(f"ADAPP_TOKENVALIDATION_URL: {self.adapp_tokenvalidation_url}")


class ADConnectionManager(ABC):
    """Class to manage connection to the Asset Digitization application."""

    @abstractmethod
    def load_config(self):
        """Load the configuration for the Asset Digitization application
        This is a placeholder implementation, replace with actual config loading logic"""
        pass

    @abstractmethod
    def get_config(self):
        """Return the loaded configuration"""
        pass

    @abstractmethod
    def create_loader(self) -> ConfigLoader:
        """Create and return a configuration loader"""
        pass

    @abstractmethod
    def get_repeater_pars(self):
        """Return the repeater configuration"""
        pass


class RegistryConfigFile:
    """Class to manage the registry of configuration files."""

    _registry_ini_files = {
        ConfigEnv.PROD: "/etc/my-websockify/config.ini",
        ConfigEnv.DEV: "config_dev.ini",
        ConfigEnv.TEST: "/etc/my-websockify/config_test.ini"
    }

    @classmethod
    def get_ini_file(cls, exec_profile: ConfigEnv):
        """Return the config file for the given execution profile."""
        return cls._registry_ini_files.get(exec_profile)


class ConfigLoader(ABC):
    """Interface for configuration loaders."""

    @abstractmethod
    def load_config(self) -> ConnConfig:
        """Return the configuration setted"""
        pass


class INIConfigLoader(ConfigLoader):
    """Concrete implementation for load from Ini file"""

    def __init__(self, exec_profile: ConfigEnv):
        self.exec_profile = exec_profile
        self.ini_file = RegistryConfigFile.get_ini_file(exec_profile)

    def load_config(self):
        """Load the configuration from the INI file."""

        config = ConfigParser()
        config.read(self.ini_file)
        config_set = ConnConfig(**config["local"])
        return config_set


class ADDFOConnectionManager(ADConnectionManager):
    """Class to manage connections to the Asset Digitization DFO application."""

    config_loader: ConfigLoader
    exec_profile: ConfigEnv

    def __init__(self):
        """Start connection manager for DFO"""
        # create get the config loader from the catory loader
        self.exec_profile = self.get_exec_profile()

    def load_config(self):
        # Load the configuration for the Asset Digitization DFO application
        # This is a placeholder implementation, replace with actual config loading logic
        # check the execution profile and load the appropriate configuration
        self.config =
        return

    def get_config(self):
        """Get the configuration for the Asset Digitization DFO application."""
        pass

    def get_exec_profile(self) -> ConfigEnv:
        """Get the execution profile for the Asset Digitization DFO application."""
        return get_current_env()


class AD3DConnectionManager(ADConnectionManager):
    """Class to manage connections to the Asset Digitization 3D application."""

    def __init__(self, config_loader: ConfigLoader):
        self.config_loader = config_loader

    def load_config(self):
        # Load the configuration for the Asset Digitization 3D application
        # This is a placeholder implementation, replace with actual config loading logic
        pass


class ADConnectionManagerLocalTest(ADConnectionManager):
    """Class to manage connections to the Asset Digitization application for local testing."""

    def __init__(self, exec_profile: ConfigEnv):
        """Start connection manager for local testing"""
        self.exec_profile = exec_profile
        self.config = self.get_config()

    def load_config(self):
        # Load the configuration for local testing
        # This is a placeholder implementation, replace with actual config loading logic
        pass

    def get_config(self):
        """Get the configuration for local testing."""

        self.loader_config = self.create_loader()
        self.config = self.loader_config.load_config()
        self.repeater_ip = self.config.get("repeater_ip")
        return self.config

    def create_loader(self) -> ConfigLoader:
        """Create the loader for the local test configuration."""

        self.config_loader = INIConfigLoader(self.exec_profile)

        return self.config_loader

    def get_repeater_pars(self):
        """Get the repeater parameters."""

    def get_validation_url(self):
        """Return the url for validation token"""

        # http://localhost:8088/system/webdev/uvnc_Dev/dev/token_validation
        return f"http://{ADAPP_SERVER}:{ADAPP_PORT}{ADAPP_TOKENVALIDATION_URL}"


class ConnectionFactory():
    """Factory for the connection"""

    _REGISTRY = {
        "LOCAL": ADConnectionManagerLocalTest,
        "PROD": ADDFOConnectionManager,
        "TEST": ADDFOConnectionManager,
        "DEV": ADDFOConnectionManager,
    }

    @classmethod
    def get_connection_manager(cls, env: str) -> ADConnectionManager:
        """Return the connection manager for the specified environment."""
        manager_class = cls._REGISTRY.get(env.upper())
        if not manager_class:
            raise ValueError(f"Unknown environment: {env}")
        return manager_class()


class FactoryConfigFile():

    _REGISTRY_CONFIG_FILE = {
        ConfigEnv.DEV: "adconfig.ini",
        ConfigEnv.PROD: "adconfig.ini",
        ConfigEnv.TEST: "adconfig.ini"
    }

    @classmethod
    def get_cfg_file(cls, env: ConfigEnv) -> str:
        return cls._REGISTRY_CONFIG_FILE.get(env, "adconfig.ini")


class ConfigLoader(ABC):

    @abstractmethod
    def load_config(self) -> dict:
        pass


class INIConfigLoader(ConfigLoader):
    """Handle the load config from ini custom file"""

    def __init__(self, env: ConfigEnv):
        self.env = env

    def load_config(self) -> dict:
        """Load config for ini file"""
        # Determine the configuration file path based on the environment

        file_name = FactoryConfigFile.get_cfg_file(self.env)
        file_path = None
        if self.env == ConfigEnv.DEV:
            path = Path(__file__).parent / file_name
            file_path = os.path.join(os.path.dirname(__file__), file_name)
        if self.env == ConfigEnv.PROD:
            path = Path(__file__).parent / file_name
            file_path = Path("/etc/websockify") / file_name
        if self.env == ConfigEnv.TEST:
            path = Path(__file__).parent / file_name
            file_path = Path("/etc/websockify") / file_name

        # config = ConfigParser()
        # config.read(file_path)
        return {"file_name": str(file_name), "file_path": str(file_path)}


if __name__ == "__main__":
    connection_config = read_config()
    connection_config.display_config()
