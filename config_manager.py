from typing import Dict, Optional
import yaml
from pathlib import Path

class ConfigManager:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.config_data = self._load_config()

    def _load_config(self) -> Dict:
        with open(Path(__file__).parent / self.config_file, 'r') as f:
            return yaml.safe_load(f)

    def get_symbol(self) -> str:
        return self.config_data['symbol']

    def get_timeframe(self) -> str:
        return self.config_data['time_frame']

    def is_alpaca(self) -> bool:
        return self.config_data['exchange'] == 'alpaca'

    def get_api_key(self, key_name: str) -> Optional[str]:
        return self.config_data.get('api_keys').get(key_name)