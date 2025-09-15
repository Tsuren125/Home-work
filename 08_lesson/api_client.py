import requests


class YougileClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, payload):
        return requests.post(f"{self.base_url}/projects",
                             json=payload, headers=self.headers)

    def update_project(self, project_id, payload):
        return requests.put(f"{self.base_url}/projects/{project_id}",
                            json=payload, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.base_url}/projects/{project_id}",
                            headers=self.headers)
