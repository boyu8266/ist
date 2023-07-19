from datetime import datetime
from typing import Any, Callable

import telebot
from tpdp import Step

from ist.config import Config
from ist.state import IstState


class TelegramNotify(Step):
    def run(self, state: IstState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> IstState:
        config = Config.from_config_file()
        token = config.telegram_token
        userid = config.telegram_userid

        df = state.dataframe

        bot = telebot.TeleBot(token)
        date = df.index[-1].strftime('%Y-%m-%d') if isinstance(df.index[-1], datetime) else df.index[-1]
        message_text = f"""
[{state.stock} - {state.period}]
Data Date: {date}
-----
Close: {round(df.close[-1], 3)}
-----
K: {round(df.k[-1], 3)}
D: {round(df.d[-1], 3)}
-----
MACD: {round(df.macd[-1], 3)}
DIF: {round(df.dif[-1], 3)}
OSC: {round(df.osc[-1], 3)}
-----
Buy: {state.buy}
Sell: {state.sell}
"""
        bot.send_message(userid, message_text)
        return state
