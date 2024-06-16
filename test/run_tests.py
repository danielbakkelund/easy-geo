

def get_cmd_arg(prefix,default=None):
    '''
    get_cmd_arg('--logLevel','INFO')
    checks for command line arguments like --logLevel:DEBUG and
    returns 'DEBUG', or if nothing is found, 'INFO'.
    '''
    import sys

    start = prefix + ':'

    for arg in sys.argv:
        if arg.startswith(start):
            return arg[len(start):]

    return default


def run_tests():
    import logging
    import unittest

    # Configure logging
    log_level = getattr(logging,get_cmd_arg('--logLevel', 'WARNING').upper())
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Load all tests
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='./test')

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
