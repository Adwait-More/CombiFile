# CombiFile

A brutally minimal tool that merges multiple text files into one, separated by filename headers.

Two versions included — use whichever fits your setup.

---

## Web Version (no install needed)

Open [`index.html`](index.html) in any modern browser. That's it.

- Select files → set output name → click Merge → file downloads automatically.
- Everything runs client-side. No server, no dependencies.

---

## Desktop Version (Python)

### Install

```bash
pip install -r requirements.txt
```

### Run

```bash
python combifile.py
```

---

## How it works

1. Click **Select Files** to queue text files.
2. Set the output filename (default: `combined_output.txt`).
3. Click **Merge**.
   - **Desktop:** prompts for an output folder, writes the file there.
   - **Web:** downloads the merged file directly.
4. Each file's content is written under a `--- [FILENAME] ---` header.

## Output format

```
--- [first_file.txt] ---

(contents of first_file.txt)


--- [second_file.txt] ---

(contents of second_file.txt)
```