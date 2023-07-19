import argparse
from datetime import datetime

from logging_service import LoggingService

from ist import config, sleep
from ist.custom import *
from ist.pipeline import (DayDataPipeline, MonthDataPipeline,
                          PeriodDataPipeline, WeekDataPipeline)
from ist.strategy import Strategy


def main():
    parser = argparse.ArgumentParser(description="IST Data Pipeline")

    parser.add_argument("--number", "-n", type=str, help="Number parameter")
    parser.add_argument("--strategy", "-s", type=str, help="Strategy parameter")
    parser.add_argument("--period", "-p", type=str, help="Period parameter")
    parser.add_argument("--start-date", "-sd", type=str, help="Start date parameter")
    parser.add_argument("--end-date", "-ed", type=str, help="End date parameter")
    parser.add_argument("--timeout", "-t", type=int, help="Timeout parameter")

    args = parser.parse_args()

    number: str = args.number
    strategy: str = args.strategy
    period: str = args.period
    start_date: str = args.start_date
    end_date: str = args.end_date
    timeout: int = args.timeout

    if not any([number, strategy, period, start_date, end_date, timeout]):
        numbers: list = config.numbers
        strategys: list = config.strategies
        periods: list = config.periods
        for i in range(len(numbers)):
            n = numbers[i]
            s: Strategy = globals()[strategys[i]]()
            p = periods[i]

            exec(n, s, p, start_date, end_date, timeout)

            sleep()

    else:
        s: Strategy = globals()[strategy]()
        exec(number, s, period, start_date, end_date, timeout)


def exec(number: str, strategy: Strategy, period: str, start_date: str, end_date: str, timeout: int):
    LoggingService().info(f'period: {period}')

    start_date = start_date or '1997-01-01'
    end_date = end_date or datetime.now().strftime("%Y-%m-%d")
    timeout = timeout or 30

    pipeline: PeriodDataPipeline = None
    if period != None and period.lower() == 'month':
        pipeline = MonthDataPipeline('month data pipeline')
    elif period != None and period.lower() == 'week':
        pipeline = WeekDataPipeline('week data pipeline')
    else:
        pipeline = DayDataPipeline('day data pipeline')

    pipeline.run(number, strategy, start_date, end_date, timeout)


if __name__ == "__main__":
    main()
