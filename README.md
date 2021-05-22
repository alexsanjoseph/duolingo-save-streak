# duolingo-save-streak

Save Duolingo Streak by buying streak freeze if possible

## Installation and Running

1. clone the packjage
2. Run `main.py` with the appropriate env vars

### Example

Command:

```sh

usernames='username1,username2' passwords='pass1,pass2' python3 main.py
```

Output:

```text
Processing username1
Item: streak_freeze Already Equipped
Item: rupee_wager Already Equipped
Processing username2
Trying to Buy streak_freeze for usernam2
Bought streak_freeze for username2

```

## Deployment

### As a Cron Job

You can run the above command by adding it your cron expression if you have an already running server

### Using AWS Lambda

Upload this as an AWS lambda function - Trigger daily by using Cloudwatch monitoring.
