Given a change ID (e.g. 1063916), fetch images from https://gerrit.wikimedia.org/r/changes/{change_id}/revisions/current/files and then generate purge commands.

# Example
```bash
(venv) ➜  purge-logos-from-patch git:(main) python get-and-generate.py --change-id 1063916
Generated purge commands for https://gerrit.wikimedia.org/r/c/1063916:
echo 'https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-wordmark-igl.svg' | mwscript purgeList.php &&
echo 'https://en.wikipedia.org/static/images/project-logos/iglwiki-1.5x.png' | mwscript purgeList.php &&
echo 'https://en.wikipedia.org/static/images/project-logos/iglwiki.png' | mwscript purgeList.php &&
echo 'https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-tagline-igl.svg' | mwscript purgeList.php &&
echo 'https://en.wikipedia.org/static/images/project-logos/iglwiki-2x.png' | mwscript purgeList.php &&
echo 'Purged all images in change 1063916'
```