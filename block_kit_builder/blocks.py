from dataclasses import dataclass
from .composition import Text
from typing import List

@dataclass
class Section:
    type: str = 'section'
    text: Text = None
    block_id: str = None
    fields: List[Text] = None
    accessory: str = None


@dataclass
class Divider:
    type: str = 'divider'
    block_id: str = None


@dataclass
class Image:
    type: str = 'image'
    image_url: str = None
    alt_text: str = None
    title: str = None
    block_id: str = None


@dataclass
class Actions:
    type: str
    elements: str
    block_id: str = None


@dataclass
class Context:
    type: str
    elements: str
    block_id: str = None


@dataclass
class Input:
    type: str
    label: str
    elements: str
    block_id: str = None
    hint: str = None
    optional: str = None


@dataclass
class File:
    type: str
    external_id: str
    source: str
    block_id: str = None

