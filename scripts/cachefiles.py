#! python3

# Get all files from the export 

import json
export = json.load(open('./dist/-/export.json'))

file_set = set()

for key, item in export['files'].items():
    file_set.add('"/'+item['url']+'"')
    for link in item['links']:
        try:
            more = link.get('resolvedRelTarget')['contents']
            if isinstance(more, list):
                file_set.add('"/'+more[1]+'"')
            else:
                file_set.add('"/'+more+'"')
        except KeyError:
            pass


print(",\n".join(list(file_set)))

