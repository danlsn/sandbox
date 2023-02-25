import json


def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def main():
    base = load_json("../../data/appy2YuxSfezbNyKj_ProjectFS.json")
    print(base)
    ...


if __name__ == "__main__":
    main()
