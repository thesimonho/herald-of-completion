# Herald of Completion

Hark! The herald of completion has arrived ... to let you know when your long-running tasks are done.

## Installation

```
pip install herald-of-completion
```

## Usage

Wrap the `@herald` decorator around the function you want to be notified about.

Some messengers require credentials. Store these in a `.env` file at the root of your project.

### .env settings

```
# Discord settings
WEBHOOK_URL="http://google.com"

# Email settings
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
SMTP_STARTTLS=True
SMTP_USER="user@gmail.com"
SMTP_PASSWORD="password"
```

## Contribution

Formatter: `black`

Tests: `pytest`
