from typing import Dict, List
import pandas as pd

class StrategyExecutor:
    def __init__(self):
        pass  # Initialize any required parameters here

    def execute(self, data: pd.DataFrame) -> Dict:
        """Execute trading strategy and return signal."""
        # Example: Simple Moving Average Strategy
        short_period = 14
        long_period = 28
        
        df = data.copy()
        df['短期MA'] = df.close.rolling(short_period).mean()
        df['长期MA'] = df.close.rolling(long_period).mean()

        last_close = df.iloc[-1].close
        short_ma = df.iloc[-1]['短期MA']
        long_ma = df.iloc[-1]['长期MA']

        if last_close > short_ma and last_close > long_ma:
            return {'signal': 'BUY', 'price': round(last_close * 1.005, 2)}
        elif last_close < short_ma and last_close < long_ma:
            return {'signal': 'SELL', 'price': round(last_close * 0.995, 2)}
        else:
            return None