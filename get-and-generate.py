import argparse
import json
import requests


def get_files(change_id: str):
    """Get image files from a Gerrit change"""
    headers = {"Accept": "application/json"}
    resp = requests.get(
        f"https://gerrit.wikimedia.org/r/changes/{change_id}/revisions/current/files/",
        headers=headers,
    )
    data = resp.content[4:]
    json_data = json.loads(data)
    images = []

    for key, value in json_data.items():
        if key.endswith(".png") or key.endswith(".svg"):
            images.append(key)
    return images


def generate_commands(change_id: str, images: str):
    """Generate purge commands for a list of images"""
    commands = []
    for image in images:
        command = f"echo 'https://en.wikipedia.org/{image}' | mwscript purgeList.php &&"
        commands.append(command)
    commands.append(f"echo 'Purged all images in change {change_id}'")
    return commands


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get images from a Gerrit change and generate purge commands"
    )
    parser.add_argument(
        "--change-id",
        type=str,
        action="store",
        required=True,
    )

    args = parser.parse_args()
    change_id = args.change_id
    images = get_files(change_id)
    commands = generate_commands(change_id, images)
    print(f"Generated purge commands for https://gerrit.wikimedia.org/r/c/{change_id}:")
    for command in commands:
        print(command)
