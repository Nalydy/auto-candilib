# auto-candilib

:construction: ***Currently as Work In Progress*** :construction:

Part 1:
- [X] Request token from candilib
- [X] Retrieve token from email

Part 2:
- [X] Scrap targeted exam centers
- [ ] Find an exam to book
- [ ] Find a way to by-pass the anti-bot for the confirmation
  - [ ] Buster: Captcha Solver for Humans

Part 3 (optional):
- [ ] Deploy
- [ ] Make it user friendly

## Requirements

### Requirements.txt

```
pip install requirements.txt
```

### Chrome

```
sudo apt-get update
sudo apt-get --only-upgrade install google-chrome-stable
```

### Config

Create a file `config.json` in the `ressources` directory following the example: [config_example.json](ressources/config_example.json)

## Usage

```
python3 src/main.py
```

