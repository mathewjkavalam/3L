#!/usr/bin/python3
from browser import document
from datetime import datetime
now = datetime.now()
document["mainText"].textContent = str(now).split(' ')[1]