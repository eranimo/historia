import json
from historia import Historia

if __name__ == "__main__":
    file_path = '/Users/kaelan/www/hexgen/bin/export.json'

    with open(file_path) as fobj:
        gen = Historia(json.load(fobj))
        gen.start()
        gen.export('./bin/export.json')
