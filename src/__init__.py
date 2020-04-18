from dataclasses import asdict, is_dataclass
from json import JSONEncoder, dumps, loads
from blocks import Actions, Context, Divider, File, Image, Input, Section
from composition import Confirmation, Option, OptionGroup, Text
from elements import Button, Checkbox, DatePicker, Image


class DataClass2JSON(JSONEncoder):
    ''' Implement subclass of JSONEncoder
    https://docs.python.org/3/library/json.html#json.JSONEncoder.default '''
    def default(self, o):
        try:
            if is_dataclass(o):
                return asdict(o)
        except TypeError:
            raise
        else:
            return super().default(o)


def clean_json(value):
    if isinstance(value, list):
        return [clean_json(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {
            key: clean_json(val)
            for key, val in value.items()
            if val is not None
        }
    else:
        return value


def slack_fmt(slackdataclass):
    blocks = []
    for s in slackdataclass:
        json_fmt = dumps(s, cls=DataClass2JSON)
        # this is ugly
        blocks.append(dumps(clean_json(loads(json_fmt))))

    return blocks



example = [
    Section(
        text=Text(
            type='mrkdwn',
            text='A message',
        ),
        fields=[
            Text(
                type='mrkdwn',
                text='A message',
            )
        ]
    ),
    Divider()
]

print(example)
print(slack_fmt(example))