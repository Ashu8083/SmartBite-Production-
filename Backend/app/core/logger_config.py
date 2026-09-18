import logging

logging.basicConfig(level=logging.INFO, 
                    format="%(levelname)s | %(messages)s",
                    force=True)

logger = logging.getLogger("app")