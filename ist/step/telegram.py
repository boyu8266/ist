import io
from datetime import datetime
from typing import Any, Callable

import matplotlib.pyplot as plt
import telebot
from matplotlib import gridspec
from tpdp import Step

from ist.config import Config
from ist.state import IstState


class TelegramSendTextInfo(Step):
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


class TelegramSendChart(Step):
    def __get_buf(self, df) -> io.BytesIO:
        fig = plt.figure()
        gs = gridspec.GridSpec(3, 1, height_ratios=[2, 1, 1])
        ax0 = plt.subplot(gs[0])
        df['close'].tail(60).plot(ax=ax0)
        ax1 = plt.subplot(gs[1], sharex=ax0)
        df[['k', 'd']].tail(60).plot(ax=ax1, color=['#DF3D2E', '#21C49C'])
        ax2 = plt.subplot(gs[2], sharex=ax0)
        df[['macd', 'dif']].tail(60).plot(ax=ax2, color=['#F8CD9E', '#FB9D7E'])

        plt.subplots_adjust(hspace=.0)
        ax0.grid()
        ax1.grid()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        return buf

    def run(self, state: IstState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> IstState:
        config = Config.from_config_file()
        token = config.telegram_token
        userid = config.telegram_userid

        bot = telebot.TeleBot(token)
        list_item = []
        if not state.rawdataframe.empty:
            list_item.append(state.rawdataframe)
        list_item.append(state.dataframe)

        for item in list_item:
            buf = self.__get_buf(item)
            bot.send_photo(userid, buf)
        return state
