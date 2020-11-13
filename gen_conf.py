import re
import os
import json


class JsonConfig:
    def __init__(self):
        self.file_path = "config_gitlab.json"
        self.data = dict()
        self.data_tile_list = list()
        self.gitlab_tile_list()

        self.data['version'] = "2.0"
        self.data['columns'] = 4
        self.data['tiles'] = self.data_tile_list
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)

    @staticmethod
    def create_sub_tile(label, tile_list):
        sub_tile = dict()
        sub_tile['type'] = 'GROUP'
        sub_tile['label'] = label
        sub_tile['rowSpan'] = 4
        sub_tile['tiles'] = tile_list
        return sub_tile

    def gitlab_tile_list(self):
        projects = {'app': 144, 'docs': 167, 'python': 235,
                    'rest-api': 135, 'cloud-aws': 87, 'react': 218, 'rails': 219,
                    'data-stream': 206, 'marketplace': 105, 'detector': 141,
                    'kakfa-boost': 109, 'mock-test': 104}

        branches = ['master', 'develop', 'integration', 'devel', 'fix', 'release', 'dev']

        for proj_name, proj_id in projects.items():
            gitlab_tile = list()
            for branch in branches:
                proj = dict()
                proj['type'] = 'GITLAB-PIPELINE'
                proj['label'] = proj_name
                proj['params'] = {'projectId': proj_id, 'ref': branch}
                gitlab_tile.append(proj)
            self.data_tile_list.append(self.create_sub_tile(f'{proj_name} - CI Jobs Running', gitlab_tile))


if __name__ == '__main__':
    JsonConfig()
