# TASK (design): this function WORKS and has been in production for a year.
# 1. List the problems in order of importance (most important first), each with a one-line "why it matters".
# 2. For the 3 most important, describe how you would restructure: modules/functions/classes,
#    signatures, names. No full implementation; signatures and short pseudo-code are fine.
# 3. How would you test the restructured version? What would you mock, and what not?
# 4. If you could change only ONE thing today, what would it be and why?

import json
import smtplib
from datetime import datetime

DB = {}
processed = 0


"""
    lista dei problemi:
    - OVVIAMENTE IL DB NON PUò ESSERE TRATTATO COME UNA VARIABILE
    - funzione che fa più cose
    - se il csv è formattato male non ce ne accorgiamo
    - invece di printare bad format facciamo un raise
    - posso passare un csv ma scrivere dentro fmt "json" e si rompe tutto
"""


class Processor:

    def __init__(self, data):
        self.data = data
        self.d = {}
        #self.db = connessione al db


    def to_dict(self):
        raise NotImplementedError

    def validate_dict(self):
        """Logica di validazione del dizionario"""

    def save(self):
        """Deve salvare nel DB quindi usare un ORM non in una variabile
            questo gestisce anche il progressivo processed sempre nel db
        """



    def send(self):
        """invia una mail al cliente"""


    def process(self, data, send=True):
        self.d=self.to_dict()
        self.validate_dict()
        t = 0
        for i in d["items"]:
            t += i["price"] * i["qty"]
        if t > 100:
            t = t * 0.9
        logger.debug("total.....")
        self.save()
        if send:
            self.send()

class CsvProcessor(Processor):
    def to_dict(self):
        """
            qui inserirei la logica di conversione da csv a dict, considerando casi limite ecc

        """

class JsonProcessor(Processor):
    def to_dict(self):
        """
           qui inserirei la logica di conversione da csv a dict, considerando casi limite ecc

       """

class ProcessorFactory:
    def get_processor(self, data):
        """
        se il data è csv ritorni un CSVProcessor, se Json un JSON Processor altrimenti raise Exception...
        """


def process(data, send=True, fmt="json", debug=False):
    global processed
    if fmt == "json":
        d = json.loads(data)
    elif fmt == "csv":
        parts = data.split(",")
        d = {"id": parts[0], "email": parts[1], "items": [{"price": float(parts[2]), "qty": int(parts[3])}]}
    else:
        print("bad format")
        return
    t = 0
    for i in d["items"]:
        t += i["price"] * i["qty"]
    if t > 100:
        t = t * 0.9
    if debug:
        print("total", t)
    DB[d["id"]] = {"email": d["email"], "total": t, "at": datetime.now()}
    processed += 1
    if send:
        s = smtplib.SMTP("localhost")
        s.sendmail("shop@example.com", d["email"], f"Your total is {t}")
        s.quit()
    return t
