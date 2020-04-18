# Block Formatter
Because writing a bunch of nested JSON gets unwieldy in your Slack Bots


# Example

From a template in the Block Kit Builder:
```
{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "You have a new request:\n*<google.com|Fred Enriquez - Time Off request>*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Type:*\nPaid time off\n*When:*\nAug 10-Aug 13\n*Hours:* 16.0 (2 days)\n*Remaining balance:* 32.0 hours (4 days)\n*Comments:* \"Family in town, going camping!\""
			},
			"accessory": {
				"type": "image",
				"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
				"alt_text": "computer thumbnail"
			}
		}
	]
}
```

You would have to pass in this JSON into your Blocks argument in the message call when using the python slack client. Instead you pass in:

```
template = [
    Section(
        text=Text(
            type="mrkdwn",
            text="You have a new request:\n*<google.com|Fred Enriquez - Time Off request>*",
        )
    ),
    Section(
        text=Text(
            type="mrkdwn",
            text="*Type:*\nPaid time off\n*When:*\nAug 10-Aug 13\n*Hours:* 16.0 (2 days)\n*Remaining balance:* 32.0 hours (4 days)\n*Comments:* \"Family in town, going camping!\""
        ),
        accessory=Image(
            type="image"
            image_url="https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
            alt_text="computer thumbnail"
        )
    )
]
```