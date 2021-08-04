# -*- coding: utf-8 -*-

import logging
from starlette.applications import Starlette
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from ruteni import configuration

logger = logging.getLogger(__name__)

RUTENI_SCHEDULER_WAIT = configuration.get("RUTENI_SCHEDULER_WAIT", default=False)

scheduler = AsyncIOScheduler()


async def startup(app: Starlette) -> None:
    scheduler.start()
    logger.info("started")


async def shutdown(app: Starlette) -> None:
    # @todo modules that import `scheduler` should not be able to shut it down
    scheduler.shutdown(wait=RUTENI_SCHEDULER_WAIT)
    logger.info("stopped")


configuration.add_service("scheduler", startup, shutdown)

logger.info("loaded")
