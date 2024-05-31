from config import load_config, save_config

class TestConfig:

    def test_save_and_load_config(temp_config_filex):
        # Override the global CONFIG_FILE path
        global CONFIG_FILE
        CONFIG_FILE = temp_config_filex

        # Test save_config
        test_config = {"new_key": "new_value"}
        save_config(test_config)
        
        # Test load_config
        loaded_config = load_config()
        assert loaded_config == test_config