# poetry-typer
Automatic Poetry Typer for MacOS

## Install
```
git clone git@github.com:BDraff/poetry-typer.git
```

### Install Packages
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Usage
```
python3 typer.py <poem-path>
```

#### Example
```
python3 typer.py poems/inventing-dinner.md
```


## Granting permission in system preferences

![Accessibility for Terminal](docs/01-accessibility-hyper.png "Step One: approve permission for your terminal app")

![Privacy and Security Window](docs/02-privacy-and-security.png "Step Two: privacy and security settings")

![Enable Radio Button in Settings](docs/03-radio-button.png "Step Three: enable radio button in settings")

![Enabled permissions in Settings](docs/04-enabled-permissions.png "Step Four: Accessibility is enabled for terminal app")
