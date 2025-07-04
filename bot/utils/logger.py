import logging

GREEN, RED, YELLOW, BLUE, MAGENTA, CYAN, RESET = (
    "\033[92m", "\033[91m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[0m"
)

class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: CYAN,
        logging.INFO: GREEN,
        logging.WARNING: YELLOW,
        logging.ERROR: RED,
        logging.CRITICAL: MAGENTA,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, RESET)
        record.levelname = f"{color}{record.levelname}{RESET}"
        record.msg = f"{color}{record.getMessage()}{RESET}"
        return super().format(record)

logger = logging.getLogger("Calculator")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)
