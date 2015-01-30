from datetime import datetime
from argparse import ArgumentParser

import sys
import logging
import logging.config

DATE_FORMAT = "%Y-%m-%d"
log = None

def date_type(val):
    return datetime.strptime(val, DATE_FORMAT)


def set_logger():
    global log
    format_str = ('%(asctime)s - %(levelname)s - {} - '
              '%(filename)s:%(funcName)s:%(lineno)d - %(message)s')
    logging.basicConfig(level=logging.INFO,
                        format=format_str.format("daq"),
                        datefmt=DATE_FORMAT + '-%H:%M:%S')
    log = logging.getLogger(__name__)


def main(argv=None):
    set_logger()
    argv = argv or sys.argv
    parser = ArgumentParser(description="Daq tool")

    parser.add_argument('--date',
                        help='event date - in YYYY-MM-DD format - PST/PDT',
                        dest='date',
                        type=date_type,
                        required=True)

    args = parser.parse_args(argv[1:])
    log.info('Args: {}'.format(args))

    # Simulation
    date = args.date.strftime(DATE_FORMAT)
    if (date == "2015-02-02"):
        log.info('Failed scenario')
        return 1
    elif (date == "2015-02-03"):
        log.info('Unhandled exception - scenario')
        i = 1/0

    return 0


if __name__ == '__main__':
    main()

