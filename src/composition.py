from dataclasses import dataclass
from typing import List

@dataclass
class Text:
    type: str
    text: str
    emoji: bool = None
    verbatim: bool = None


@dataclass
class Confirmation:
    title: str
    text: Text
    confirm: str
    deny: str
    style: str = None


@dataclass
class Option:
    text: Text
    value: str
    description: str = None
    url: str = None


@dataclass
class OptionGroup:
    label: str
    options: List[Option]