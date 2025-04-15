import logging

def get_logger(name='factor_lake_logger', level=logging.INFO):
    logger = logging.getLogger(name)
    
    # Avoid adding multiple handlers in interactive environments or re-runs
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')  # Clean format for CLI
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)
    return logger


def set_log_level(level):
    """Map the user input level to a logging level."""
    levels = {
        1: logging.WARNING,  # Only show high-level messages
        2: logging.INFO,     # Yearly summaries and basic details
        3: logging.DEBUG,    # Full detailed logs
    }
    return levels.get(level, logging.INFO)  # Default to INFO if level is invalid


# Function to log stock details for each year
def log_stock_details(year, stock_data):
    if log_level >= logging.DEBUG:
        # Level 3: Detailed breakdown with all stocks
        for stock, prices in stock_data.items():
            logger.debug(f"{stock} details for {year}: {prices[year-2022]}")

    if log_level == logging.INFO:
        # Level 2: Yearly summaries, only include stocks available from the start
        for stock, prices in stock_data.items():
            if year - 2022 < len(prices):  # If the stock was available in this year
                logger.info(f"{stock} summary for {year}: {prices[year-2022]}")

    if log_level == logging.WARNING:
        # Level 1: Only high-level rebalancing information, no stock details
        logger.warning(f"Year {year}: Portfolio rebalanced.")

# Simulate some yearly operations
for year in range(2022, 2025):
    log_stock_details(year, stocks)
