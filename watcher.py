import sys
import time
import subprocess
from pathlib import Path

input('wait for the game to start than press enter')
if len(sys.argv) > 1:
    LAST_KNOWN = sys.argv[1]
else:
    LAST_KNOWN = '446'

print(f'protecting {LAST_KNOWN} layer from being 0 please do not close this window when you playing or watcher dont save your choise')
print(f'and a litle warning this watcher dont protect title from other changes like other title than regular have respect to OMOCAT ))')
SAVE_PATH = Path("G:/SteamLibrary/steamapps/common/OMORI/www/save")
TITEL_PATH = SAVE_PATH / "TITLEDATA"

def is_game_running():
    result = subprocess.run(
        ['tasklist', '/FI', 'IMAGENAME eq OMORI.exe'],
        capture_output=True,
        text=True
    )
    return 'OMORI.exe' in result.stdout

try:
    while is_game_running():
        if TITEL_PATH.exists():
            current = TITEL_PATH.read_text().strip()
            if current == '0':
                TITEL_PATH.write_text(LAST_KNOWN)
        time.sleep(1)
except KeyboardInterrupt:
    pass