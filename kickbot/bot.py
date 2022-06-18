# kickbot - a maubot plugin to track user activity and remove inactive users from rooms/spaces.

from typing import Awaitable, Type, Optional, Tuple
import json
import time

from mautrix.client import Client
from mautrix.types import (Event, StateEvent, EventID, UserID, FileInfo, EventType,
                            MediaMessageEventContent, ReactionEvent, RedactionEvent)
from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper
from maubot import Plugin, MessageEvent
from maubot.handlers import command, event

# database table related things
from .db import upgrade_table



class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("exclusion_list")


class KickBot(Plugin):
    # database table related things
#   kickbot_t: Type[KickBot]
#   version: Type[Version]

    async def start(self) -> None:
        await super().start()
        self.config.load_and_update()
        
    @event.on(EventType.ROOM_MESSAGE)
    async def update_user_timestamp(self, evt: MessageEvent) -> None:
        excluded = evt.sender in self.config["exclusion_list"]
        q = """
            REPLACE INTO user_events(mxid, last_message_timestamp, ignore_inactivity) 
            VALUES ($1, $2, $3)
        """
        await self.database.execute(q, evt.sender, evt.timestamp, int(excluded))
        self.log.info("record added")

    #need a command to load/reload full space-member list to user_events table,
    #if not already in the table set last_message value to 0

    #need a command to return a list of users who are in the space member-list,
    #but have a last_message value greater than 30 and 60 days AND ignore_activity
    #value is set to 0
    #
    #memberlist = await self.client.get_joined_members(space_room_id)
    #self.log.info(memberlist.keys())
    #current_time = int(time.time() * 1000) # get current timestamp to match matrix datestamp formatting
    #30_days_ago = (current_time - 2592000000) # not useful now but will be when we compare timestamps
    #60_days_ago = (current_time - 5184000000) # not useful now but will be when we compare timestamps


    @classmethod
    def get_db_upgrade_table(cls) -> None:
        return upgrade_table

    @classmethod
    def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config
