# Mac Shortcuts Setup Guide

How to set up **two keyboard shortcuts** for `macshot` using macOS Shortcuts app.

**Requirements**: macOS Monterey (12.0) or later

---

## Overview

**macshot** uses a two-mode workflow that requires **two separate keyboard shortcuts**:

1. **Set Folder** - Opens folder picker to select destination (use occasionally)
2. **Take Screenshot** - Captures screenshot to selected folder (use frequently)

---

## Setup Shortcut 1: Set Folder

### Step 1: Create "macshot - Set Folder" Shortcut

1. Open **Shortcuts** app (`Cmd+Space` → "Shortcuts")
2. Click **"+"** button (top right)
3. Name it: **"macshot - Set Folder"**

### Step 2: Add Shell Script Action

1. Search for: **"Run Shell Script"**
2. Drag it into your shortcut
3. Paste this command:

```bash
cd /Users/main/dev/projects/sovereign-data/macshot && /Users/main/.local/bin/uv run macshot.py --set-folder
```

**Important**: Replace paths with your actual installation:
- `cd /path/to/macshot` - Your macshot directory
- `/path/to/uv` - Find with: `which uv`

### Step 3: Assign Keyboard Shortcut

1. Click the **ⓘ (info icon)**
2. Click **"Add Keyboard Shortcut"**
3. Press: **`Ctrl+Cmd+Shift+S`** (Shift = Setup/Select)
4. Click **"Done"**

---

## Setup Shortcut 2: Take Screenshot

### Step 1: Create "macshot - Take Screenshot" Shortcut

1. In Shortcuts app, click **"+"** again
2. Name it: **"macshot - Take Screenshot"** or just **"macshot"**

### Step 2: Add Shell Script Action

1. Search for: **"Run Shell Script"**
2. Drag it into your shortcut
3. Paste this command:

```bash
cd /Users/main/dev/projects/sovereign-data/macshot && /Users/main/.local/bin/uv run macshot.py
```

**Note**: Same paths as Shortcut 1, but **without** `--set-folder` flag

### Step 3: Assign Keyboard Shortcut

1. Click the **ⓘ (info icon)**
2. Click **"Add Keyboard Shortcut"**
3. Press: **`Ctrl+Cmd+S`** (S = Screenshot)
4. Click **"Done"**

---

## Workflow

Once both shortcuts are set up:

### Initial Setup (once per session)
1. Press **`Ctrl+Cmd+Shift+S`** (Set Folder)
2. Select destination folder in dialog
3. Folder is saved for future screenshots

### Taking Screenshots (repeat as needed)
1. Press **`Ctrl+Cmd+S`** (Take Screenshot)
2. Select area on screen
3. Screenshot saved to folder you set earlier
4. Repeat step 1-3 for more screenshots

### Switching Contexts
- Press **`Ctrl+Cmd+Shift+S`** again to pick a new folder
- Future screenshots go to the new location

---

## Example: Documenting Slides

```
1. Press Ctrl+Cmd+Shift+S → Select folder: ~/Documents/presentation-slides
2. Display slide 1
3. Press Ctrl+Cmd+S → Capture slide 1
4. Display slide 2
5. Press Ctrl+Cmd+S → Capture slide 2
6. Display slide 3
7. Press Ctrl+Cmd+S → Capture slide 3
... continue for all slides
```

All screenshots are automatically saved with timestamps in the selected folder.

---

## Troubleshooting

### "command not found: uv"

The Shortcuts app can't find `uv`. Use the full path:

```bash
which uv
# Output: /Users/main/.local/bin/uv
# Use this full path in your shortcuts
```

### "No folder configured" Error

You need to run **Set Folder** mode first:
- Press `Ctrl+Cmd+Shift+S` to select destination folder
- Then use `Ctrl+Cmd+S` to take screenshots

### Shortcut Not Working

1. Check **System Settings** → **Privacy & Security** → **Accessibility**
2. Ensure **Shortcuts** app has permission
3. May need to grant **Terminal** access as well
4. Test manually first:
   ```bash
   cd /path/to/macshot
   uv run macshot.py --set-folder  # Test set folder
   uv run macshot.py               # Test take screenshot
   ```

### Wrong Folder Selected

Simply press `Ctrl+Cmd+Shift+S` again to choose a different folder.

---

## Keyboard Shortcut Reference

| Shortcut | Action | When to Use |
|----------|--------|-------------|
| `Ctrl+Cmd+Shift+S` | Set Folder | Once per session or when switching contexts |
| `Ctrl+Cmd+S` | Take Screenshot | Repeatedly for each screenshot |

---

## Tips

- **Set folder first** before taking screenshots
- Choose shortcuts that don't conflict with existing Mac shortcuts
- The selected folder path persists even after restarting macOS
- Press **ESC** during screenshot selection to cancel

---

**You're all set!** Enjoy efficient, organized screenshot workflows with macshot.
