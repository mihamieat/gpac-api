# -*- coding: utf-8 -*-
"""logger module."""

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:    \033[35m[DEV]\033[0m %(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)
