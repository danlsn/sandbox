import json

import yaml
import requests
from pyairtable import Api, Base, Table
from tqdm import tqdm


def get_token(config="../config.yaml"):
    with open(config, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)["airtable"]["token"]


def get_bases(auth_token=get_token()):
    url = "https://api.airtable.com/v0/meta/bases"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    bases = response.json()["bases"]
    return bases


def get_tables(base, auth_token=get_token()):
    base_id = base['id']
    url = f"https://api.airtable.com/v0/meta/bases/{base_id}/tables"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    tables = response.json()["tables"]
    # Add tables to base
    base['tables'] = tables
    return base


def get_base_records(base, auth_token=get_token()):
    base_id = base['id']
    tables = get_tables(base)['tables']
    ts = []
    for t in tables:
        table = Table(auth_token, base_id, t['name'])
        rows = table.all()
        t['rows'] = rows
        ts.append(t)
    base['tables'] = ts
    return base


def main():
    bases = get_bases()
    # all_bases_records = [get_base_records(base) for base in tqdm(bases)]
    # all_bases_tables = [get_tables(base) for base in tqdm(bases)]
    for _ in tqdm(bases):
        base = get_base_records(_)
        with open(f"../../data/{base['id']}_{base['name']}.json", "w") as f:
            json.dump(base, f, indent=4)
    # Write all_bases_tables to json file
    # with open("all-bases-w-tables.json", "w") as f:
    #     json_object = json.dumps(all_bases_records, indent=4)
    #     f.write(json_object)
    ...


if __name__ == "__main__":
    main()
