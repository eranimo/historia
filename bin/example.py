import os
import json
from historia import Historia

if __name__ == "__main__":
    file_path = os.path.join(os.path.expanduser('~'), 'hexgen.json')
    output_path = os.path.join(os.path.expanduser('~'), 'historia.json')
    print('Output: {}'.format(output_path))

    with open(file_path) as fobj:
        gen = Historia(json.load(fobj), debug=False, params={
            'run_days': 100
        })
        gen.start()
        gen.export(output_path)
