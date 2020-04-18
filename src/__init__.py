from dataclasses import asdict, is_dataclass
from json import JSONEncoder, dumps, loads
from blocks import Actions, Context, Fields, File, Image, Input, Section
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


def clean_dict(d):
   clean = {}
   for k, v in d.items():
      if isinstance(v, dict):
         nested = clean_dict(v)
         if len(nested.keys()) > 0:
            clean[k] = nested
      elif v is not None:
         clean[k] = v
   return clean


def slack_fmt(slackdataclass):
    json_fmt = dumps(example, cls=DataClass2JSON)
    return dumps(clean_dict(loads(json_fmt)))



example = Section(
    text=Text(
        type='mrkdwn',
        text='A message',
    )
)

print(example)
json_example = dumps(example, cls=DataClass2JSON)
print(slack_fmt(json_example))