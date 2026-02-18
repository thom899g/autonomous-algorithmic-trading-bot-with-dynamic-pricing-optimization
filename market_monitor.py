from typing import Dict, List
import pandas as pd
from dataCollector import DataCollector

class MarketMonitor:
    def __init__(self):
        self.data_collector = DataCollector()

    def watch_market(self, symbol: str, data: pd.DataFrame):
        # Monitor for volume spikes or price gaps
        last_data_point = data.iloc[-1]
        if len(data) > 2:
            prev_volume = data.iloc[-2].volume
            curr_volume = last_data_point.volume
            
            if curr_volume > (prev_volume * 3):
                self._handle_volume_spike(symbol, last_data_point.close)
                
            # Check for price gaps