import logging

# logging.basicConfig(level=logging.INFO)

# def setup_logger(name: str):
#     """
#     Set up a logger with the specified name.
#     """
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)  # Or any other level

#     # Create a console handler and set level to debug
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.INFO)  # Or any other level

#     # Create formatter
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#     # Add formatter to ch
#     ch.setFormatter(formatter)

#     # Add ch to logger
#     if not logger.handlers:
#         logger.addHandler(ch)

#     return logger