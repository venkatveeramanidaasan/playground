from datetime import datetime
from time import sleep
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


def daq_helper(args):
    # Simulation
    date = args.date.strftime(DATE_FORMAT)
    if (date == "2015-02-02"):
        log.info('Failed scenario')
        return 1
    elif (date == "2015-02-03"):
        log.info('Unhandled exception - scenario')
        i = 1/0
    log.info('Waiting for operation to complete')
    sleep(args.wait)
    log.info('Operation completed')
    return 0


def daq_subparser(sub_parsers):
    args = sub_parsers.add_parser("daq", help="DAQ execution")
    args.add_argument('--date',
                     help='event date - in YYYY-MM-DD format - PST/PDT',
                     dest='date',
                     type=date_type,
                     required=True)
    args.add_argument('--wait',
                     help='Some value to simulate daq operation',
                     dest='wait',
                     default=30)
    args.set_defaults(func=daq_helper)


def staging_helper(args):
    log.info('Batch Id {}'.format(args.batch_id))


def staging_subparser(sub_parsers):
    args = sub_parsers.add_parser("staging", help="Staging execution")
    args.add_argument('--batch-id',
                     help='Batch Id from the DP',
                     dest='batch_id',
                     type=int,
                     required=True)
    args.set_defaults(func=staging_helper)


def main(argv=None):
    set_logger()
    argv = argv or sys.argv
    parser = ArgumentParser(description="Daq tool")
    subparsers = parser.add_subparsers()

    daq_subparser(subparsers)
    staging_subparser(subparsers)

    args = parser.parse_args(argv[1:])
    log.info('Args: {}'.format(args))
    return args.func(args)


if __name__ == '__main__':
    main()
