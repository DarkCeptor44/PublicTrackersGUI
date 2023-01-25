# PublicTrackersGUI
A GUI to get Public trackers from the [trackerslist](https://github.com/ngosang/trackerslist) repository.

## How to use

* Clone it locally and install dependencies with:
```
pip install -r requirements.txt
```

* Start the GUI by running the `main.py` script:
```
python main.py
```

And that's it! You can make a `bat` file which does the above command in the folder and create a shortcut to it anywhere.

Or you can install PyInstaller with `pip install pyinstaller` and use this command to build an exe:
```
pyinstaller --add-data "gui.ui;." -w -n PublicTrackersGUI -F main.py
```