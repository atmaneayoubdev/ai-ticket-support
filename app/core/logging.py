import logging

# Initialize a logger for application code
app_logger = logging.getLogger("app")
app_logger.setLevel(logging.INFO)

# Avoid duplicate handlers in case of repeated initialization
if not app_logger.hasHandlers():
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    app_logger.addHandler(ch)

# Function to retrieve the logger


def get_logger():
    return app_logger
