from typing import Optional, List
from pydantic import Field,BaseModel, validator



class ImageUrls(BaseModel):
    field_50x50: str = Field(..., alias='50x50')
    field_150x150: str = Field(..., alias='150x150')
    field_500x500: str = Field(..., alias='500x500')


class AudioUrls(BaseModel):
    field_96_KBPS: str = Field(..., alias='96_KBPS')
    field_160_KBPS: str = Field(..., alias='160_KBPS')
    field_320_KBPS: str = Field(..., alias='320_KBPS')


class Song(BaseModel):
    id: str = None
    title: str = None
    albumId: str = None
    albumTitle: str = None
    duration: str = None
    playCount: int = None
    year: str = None
    releaseDate: str = None
    language: str = None
    hasLyrics: str = None
    singers: str = None
    starring: str = None
    label: str = None
    music: str = None
    copyright: str = None
    musicId: str = None
    primaryArtists: str = None
    primaryArtistsId: str = None
    featuredArtists: str = None
    featuredArtistsId: str = None
    artistMap: dict = None
    url: str = None
    albumUrl: str = None
    labelUrl: str = None
    imageUrls: ImageUrls = None
    audioUrls: AudioUrls = None


class Album(BaseModel):
    id: str = None
    title: str = None
    name: str = None
    year: str = None
    url: str = None
    imageUrls: ImageUrls = None
    primaryArtists: str = None
    primaryArtistsId: str = None
    songs: List[dict] = None

class Playlist(BaseModel):
    id: str = None
    title: str = None 
    listCount: str = None
    followerCount: str = None
    url: str = None
    image: str = None
    songs: List[dict] = None

class Lyrics(BaseModel):
    lyrics: str = None
    lyrics_copyright: str = None
    snippet: str = None
