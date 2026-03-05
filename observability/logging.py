"""
Logging module for AgentForge
"""

import logging
import sys


def setup_logging(level=logging.INFO):
    """Setup logging configuration"""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


# Default logger
logger = logging.getLogger("agentforge")


def get_logger(name):
    """Get a logger for a specific module"""
    return logging.getLogger(f"agentforge.{name}")
