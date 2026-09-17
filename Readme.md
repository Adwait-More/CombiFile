# CombiFile

A minimal tool that merges multiple text files into one, separated by filename headers. Runs entirely in the browser — no install, no server.

## Usage

Open [`index.html`](index.html) in any browser.

1. **Add Files** — queue files (click multiple times to add more).
2. **Sort** — reorder by name (A→Z / Z→A) or by extension.
3. **Filter** — type a substring and click **Select** (or press Enter) to check only matching files.
4. **Checkboxes** — toggle individual files on/off. Use **Check All** / **Uncheck All** for bulk control.
5. **✕** — remove a file from the list entirely.
6. **Merge** — combines only the checked files (in the current sort order) and downloads the result.

## Output format

```
--- [first_file.txt] ---

(contents of first_file.txt)


--- [second_file.txt] ---

(contents of second_file.txt)
```