from dataclasses import dataclass
from composition import Text, Option, Confirmation
from typing import List

@dataclass
class Button:
    type: str
    text: Text
    action_id: str
    url: str = None
    value: str = None
    style: str = None
    confirm: str = None


@dataclass
class Checkbox:
    type: str
    action_id: str
    options: List[Option]
    initial_options: List[Option] = None
    confirm: Confirmation = None


@dataclass
class DatePicker:
    type: str
    action_id: str
    placeholder: Text = None
    initial_date: str = None
    confirm: Confirmation = None


@dataclass
class Image:
    type: str
    image_url: str
    alt_text: str