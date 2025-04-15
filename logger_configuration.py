import logging

def get_logger(name='factor_lake_logger', level=logging.INFO):
    logger = logging.getLogger(name)

    # Avoid adding multiple handlers in interactive environments or re-runs
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')  # Keep it clean for CLI
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)
    return logger
