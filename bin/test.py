import json
from ..historia import Historia

with open('/Users/kaelan/www/hexgen/bin/export.json') as map_file
    gen = Historia(json.load(map_file))
    gen.step()
    gen.report()
