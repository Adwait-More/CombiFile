# CombiFile

A brutally minimal tool that merges multiple text files into one, separated by filename headers.

## Usage

Open [`index.html`](index.html) in any browser. No install, no server, no dependencies.

1. Click **Add Files** to queue files (can be clicked multiple times to add more).
2. Use **checkboxes** to include/exclude individual files from the merge.
3. Use the **✕** button to remove a file from the list entirely.
4. Set the output filename (default: `combined_output.txt`).
5. Click **Merge** — only checked files are merged and downloaded.

Everything runs client-side in the browser.

## Output format

```
--- [first_file.txt] ---

(contents of first_file.txt)


--- [second_file.txt] ---

(contents of second_file.txt)
```