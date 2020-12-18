# Pyinstall notes

## cmd line
python -OO -m PyInstaller --onefile --noconsole --version-file fixture\version.txt -a --icon=fixture\rns.ico %1

## Virus
- Scan type: Auto-Protect Scan
- Event: Risk Found!
- Security risk detected: Heur.AdvML.B
  - 2020.09.09
  - 2018.12.19

## Links
[Forum](https://python-forum.io/Thread-pyinstaller-generated-code-gets-flagged-by-NIS)
[Github](https://github.com/pyinstaller/pyinstaller/issues?utf8=%E2%9C%93&q=is%3Aissue+virus)
