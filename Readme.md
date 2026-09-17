# CombiFile

A minimal tool that merges multiple text files into one, separated by filename headers. Runs entirely in the browser — no install, no server.

🔗 **[Live Demo](https://adwait-more.github.io/CombiFile/)**

## Usage

Try the [live version](https://adwait-more.github.io/CombiFile/) or open [`index.html`](index.html) locally in any browser.

### Sidebar Controls

| Control | What it does |
|---------|-------------|
| **Add Files** | Queue files (click multiple times to add more) |
| **Clear All** | Remove everything from the list |
| **Sort** | Reorder by name (A→Z / Z→A) or by extension |
| **Select by name** | Type a substring → checks only matching files |
| **Select by extension** | Type an extension (e.g. `.cs`) → checks only files of that type |
| **All / None / Invert** | Bulk selection controls |
| **Merge & Download** | Combines checked files and downloads the result |

### Main Area

- Each file row has a **checkbox** (toggle include/exclude), an **extension badge**, and a **✕** button to remove it.
- Merge output follows the current sort order.

## Output format

```
--- [first_file.txt] ---

(contents of first_file.txt)


--- [second_file.txt] ---

(contents of second_file.txt)
```