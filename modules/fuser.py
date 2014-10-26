from config import load_project_properties
from filehelper import find_python_files_in_project
from authormapper import get_contributors_for_file
from filehelper import convert_file_to_json
import os
import json

class Fuser():

    config = {}

    def __init__(self):
        self.config = load_project_properties()

    def generate_project_object(self, project_location):
        project_object = []
        files = find_python_files_in_project(str(project_location))
        for file in files:
            if file != '':
                file_dict = convert_file_to_json(file)
                file_path = os.path.dirname(file)
                authors = get_contributors_for_file(file_path, file)
                for key in file_dict[file].keys():
                    file_dict[file][key]['author'] = authors[key]

                project_object.append(file_dict)
        if self.config['debug'] == 'on':
            with open('data.json', 'w') as outfile:
                json.dump(project_object, outfile, sort_keys = True, indent = 4)
        return project_object

if __name__ == '__main__':
    fuser = Fuser()
    project = fuser.generate_project_object(fuser.config['jason']['plumbum'])
    for item in project:
        print item
