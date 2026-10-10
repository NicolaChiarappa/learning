# TASK (design): this code WORKS for the current use cases.
# 1. What is wrong with the design? Be specific.
# 2. Next month you must add the "xlsx" format and "zstd" compression. What happens to this code?
# 3. How would you restructure it? Describe the classes/functions and their responsibilities
#    (signatures and a few lines of pseudo-code are fine, no full implementation).
# 4. There are also at least two latent bugs unrelated to the class structure. Find them.

import csv
import gzip
import io
import json


""" 
    il problema che vedo è che all'aumentare degli exporter e dei compressor le combinazioni crescono e il numero di classi esplode, e quindi bisogna anche mantenere molte classi
    Una soluzione poterebbe essere implementare un Abstract Factory quindi avere su due assi indipendenti le due variabili ovvero l'exporter e il compressor
    
    oppure una soluzione più semplice sarebbe quella di dare come parametro del costruttore dell'exporter il tipo di compressor, ovviamente la classe Exporter che scrivo di seguito deve essere estesa per il Json e il csv
"""



class Exporter:

    compressor = None

    def __init__(self, compressor):
        self.compressor = compressor

    def _export(self, data):
        """
        qui mettiamo la logica di esportazione

        """
    def export(self):
        if self.compressor is None:
            self._export("dati non compressi")
        else:
            self._export(compressor.compress(data))





class Exporter:
    def export(self, rows):
        raise NotImplementedError


class CsvExporter(Exporter):
    def export(self, rows):
        buf = io.StringIO()
        writer = csv.writer(buf)
        for row in rows:
            writer.writerow(row.values())
        return buf.getvalue().encode()


class CsvExporterWithHeader(CsvExporter):
    def export(self, rows):
        rows = list(rows)
        header = ",".join(rows[0].keys()) + "\r\n"
        return header.encode() + super().export(rows)


class GzipCsvExporterWithHeader(CsvExporterWithHeader):
    def export(self, rows):
        return gzip.compress(super().export(rows))


class JsonExporter(Exporter):
    def export(self, rows):
        return json.dumps(list(rows)).encode()


class GzipJsonExporter(JsonExporter):
    def export(self, rows):
        return gzip.compress(super().export(rows))


def get_exporter(kind, header=False, compress=False):
    if kind == "csv" and header and compress:
        return GzipCsvExporterWithHeader()
    if kind == "csv" and header:
        return CsvExporterWithHeader()
    if kind == "csv" and compress:
        raise ValueError("not supported")
    if kind == "csv":
        return CsvExporter()
    if kind == "json" and compress:
        return GzipJsonExporter()
    return JsonExporter()
