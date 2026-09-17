# CombiFile

A brutally minimal desktop tool that merges multiple text files into one, separated by filename headers.

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python combifile.py
```

## How it works

1. Click **Select Files** to queue text files.
2. Set the output filename (default: `combined_output.txt`).
3. Click **Merge** and pick an output folder.
4. Each file's content is written under a `--- [FILENAME] ---` header.
