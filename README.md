# zargonBackup
python backup script

# Syntax
./zgb.py SRC DEST [LINK-DEST]

- SRC - folder you want to backup
- DEST - folder to store backup
- LINK-DEST - path to one of the previous backup folders. Makes hardlinks to unchanged files.

# Usage example

1. Clone repo
2. Go to the repo folder 
3. Run: 
```shell
./zgb.py ~/Documents/ ~/backup/ 
```
or if you want to run incremental backup:
```shell
./zgb.py ~/Documents/ ~/backup/ ~/backup/20250510_124112/
```
