import json
from itertools import cycle


def annonate_with_subject_ids(input_file: str, subject_ids: list):
    with open(input_file, 'r') as inputfile:
        data = json.load(inputfile)
        cycle_list = cycle(subject_ids)
        for specimen in data["entry"]:
            specimen["resource"]["subject"] = {
                "reference": f"Patient/{next(cycle_list)}"
            }

        with open('annotated_output.json', 'w') as output:
            output.write(json.dumps(data, indent=2))
            print('Done.')
