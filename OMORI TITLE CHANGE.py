import os
from pathlib import Path
import subprocess

print("=== RUNNING DIAGNOSTIC ===")
print(f"Current directory: {os.getcwd()}")

options = ['444', '445', '446', '447', '448']
game_path = Path(os.getcwd())
www_path = game_path / "www"
save_path = www_path / "save"
title_data = save_path / 'TITLEDATA'
watcher = game_path / "watcher.py"
# === ИЩЕМ ЛЮБОЙ .exe ФАЙЛ ===
exe_files = list(game_path.glob("*.exe"))
game_exe = None
for exe in exe_files:
    if "OMORI" in exe.name or "Game" in exe.name:
        game_exe = exe
        break

if not game_exe and exe_files:
    game_exe = exe_files[0]  # берём первый попавшийся

print(f"Game path: {game_path}")
print(f"www path: {www_path}")
print(f"www exists: {www_path.exists()}")
print(f"save path: {save_path}")
print(f"save exists: {save_path.exists()}")
print(f"Found .exe: {game_exe}")
print(f".exe exists: {game_exe.exists() if game_exe else False}")

if not www_path.exists() or not game_exe or not game_exe.exists():
    print("ERROR: www folder or game executable not found!")
    print("Make sure you're running this from the OMORI game folder.")
else:
    print("✅ Everything looks good!")


if title_data.exists():
    print('TITLEDATA is exist can title can be changed')
    print('choose from this options:')
    print('444 - black space\n'
          '445 - red space\n'
          '446 - white space\n'
          '447 - good ending\n'
          '448 - bad ending'
          )
    answer = input('input here:')

    if answer in options:
        with open(title_data, 'w') as f:
            f.write(str(answer))

        if watcher.exists():
            print(f'activating watcher for best expirience')
            subprocess.Popen( ['python', str(watcher), str(answer)],
    creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            print(f'watcher does not exist')

        print(f'seccessfully changed title hooray! now opening game')
        import webbrowser
        webbrowser.open("steam://rungameid/1150690")
    else:
        print(f'{answer} is not a valid option idi nahui')
        input("\nPress Enter to exit...")



