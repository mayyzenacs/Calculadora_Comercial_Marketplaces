from mode import Calculator
import json
import os
from datetime import datetime


def saveHistory(precoPor, PrecoDe, Percent):
    history =  []

    if os.path.exists('history.json'): 
        with open('history.json', 'r') as archive: 
            try: 
                history = json.load(archive)
            except:
                history = []
                
    history.append({
        "data": datetime.now().strftime('%d/%m/%Y %H:%M'),
        "precoPor": precoPor,
        "precoDe": PrecoDe,
        "percent": Percent
})

    with open('history.json', 'w') as arq: 
        json.dump(history, arq, indent=4)

saveHistory(45.45, 56.56, '35%')