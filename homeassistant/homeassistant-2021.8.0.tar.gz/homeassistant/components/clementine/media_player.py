"""Support for Clementine Music Player as media player."""
from datetime import timedelta
import time

from clementineremote import ClementineRemote
import voluptuous as vol

from homeassistant.components.media_player import PLATFORM_SCHEMA, MediaPlayerEntity
from homeassistant.components.media_player.const import (
    MEDIA_TYPE_MUSIC,
    SUPPORT_NEXT_TRACK,
    SUPPORT_PAUSE,
    SUPPORT_PLAY,
    SUPPORT_PREVIOUS_TRACK,
    SUPPORT_SELECT_SOURCE,
    SUPPORT_VOLUME_SET,
    SUPPORT_VOLUME_STEP,
)
from homeassistant.const import (
    CONF_ACCESS_TOKEN,
    CONF_HOST,
    CONF_NAME,
    CONF_PORT,
    STATE_OFF,
    STATE_PAUSED,
    STATE_PLAYING,
)
import homeassistant.helpers.config_validation as cv

DEFAULT_NAME = "Clementine Remote"
DEFAULT_PORT = 5500

SCAN_INTERVAL = timedelta(seconds=5)

SUPPORT_CLEMENTINE = (
    SUPPORT_PAUSE
    | SUPPORT_VOLUME_STEP
    | SUPPORT_PREVIOUS_TRACK
    | SUPPORT_VOLUME_SET
    | SUPPORT_NEXT_TRACK
    | SUPPORT_SELECT_SOURCE
    | SUPPORT_PLAY
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_ACCESS_TOKEN): cv.positive_int,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Clementine platform."""

    host = config[CONF_HOST]
    port = config[CONF_PORT]
    token = config.get(CONF_ACCESS_TOKEN)

    client = ClementineRemote(host, port, token, reconnect=True)

    add_entities([ClementineDevice(client, config[CONF_NAME])])


class ClementineDevice(MediaPlayerEntity):
    """Representation of Clementine Player."""

    _attr_media_content_type = MEDIA_TYPE_MUSIC
    _attr_supported_features = SUPPORT_CLEMENTINE

    def __init__(self, client, name):
        """Initialize the Clementine device."""
        self._client = client
        self._attr_name = name

    def update(self):
        """Retrieve the latest data from the Clementine Player."""
        try:
            client = self._client

            if client.state == "Playing":
                self._attr_state = STATE_PLAYING
            elif client.state == "Paused":
                self._attr_state = STATE_PAUSED
            elif client.state == "Disconnected":
                self._attr_state = STATE_OFF
            else:
                self._attr_state = STATE_PAUSED

            if client.last_update and (time.time() - client.last_update > 40):
                self._attr_state = STATE_OFF

            volume = float(client.volume) if client.volume else 0.0
            self._attr_volume_level = volume / 100.0
            if client.active_playlist_id in client.playlists:
                self._attr_source = client.playlists[client.active_playlist_id]["name"]
            else:
                self._attr_source = "Unknown"
            self._attr_source_list = [s["name"] for s in client.playlists.values()]

            if client.current_track:
                self._attr_media_title = client.current_track["title"]
                self._attr_media_artist = client.current_track["track_artist"]
                self._attr_media_album_name = client.current_track["track_album"]
                self._attr_media_image_hash = client.current_track["track_id"]
            else:
                self._attr_media_image_hash = None

        except Exception:
            self._attr_state = STATE_OFF
            raise

    def select_source(self, source):
        """Select input source."""
        client = self._client
        sources = [s for s in client.playlists.values() if s["name"] == source]
        if len(sources) == 1:
            client.change_song(sources[0]["id"], 0)

    async def async_get_media_image(self):
        """Fetch media image of current playing image."""
        if self._client.current_track:
            image = bytes(self._client.current_track["art"])
            return (image, "image/png")

        return None, None

    def volume_up(self):
        """Volume up the media player."""
        newvolume = min(self._client.volume + 4, 100)
        self._client.set_volume(newvolume)

    def volume_down(self):
        """Volume down media player."""
        newvolume = max(self._client.volume - 4, 0)
        self._client.set_volume(newvolume)

    def mute_volume(self, mute):
        """Send mute command."""
        self._client.set_volume(0)

    def set_volume_level(self, volume):
        """Set volume level."""
        self._client.set_volume(int(100 * volume))

    def media_play_pause(self):
        """Simulate play pause media player."""
        if self.state == STATE_PLAYING:
            self.media_pause()
        else:
            self.media_play()

    def media_play(self):
        """Send play command."""
        self._attr_state = STATE_PLAYING
        self._client.play()

    def media_pause(self):
        """Send media pause command to media player."""
        self._attr_state = STATE_PAUSED
        self._client.pause()

    def media_next_track(self):
        """Send next track command."""
        self._client.next()

    def media_previous_track(self):
        """Send the previous track command."""
        self._client.previous()
