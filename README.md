# macshot

**Simple Mac Screenshot Tool**

A minimal, sovereign screenshot utility for macOS that captures screenshots and saves them with timestamps to user-selected folders.

## Features

- **Two-mode workflow**: Set folder once, take many screenshots
- Interactive screenshot capture (select area on screen)
- Auto-saves with timestamp: `YYYYMMDD-HHMMSS.png`
- Custom folder selection via native macOS dialog
- Zero dependencies (pure Python 3 + Mac built-ins)
- Perfect for documenting slides, tutorials, or remote work
- Foundation for future AI preprocessing

## Requirements

- macOS (uses built-in `screencapture` command)
- Python 3.9+ (managed via `uv`)
- [uv](https://docs.astral.sh/uv/) - Modern Python package manager

## Installation

### Using uv (Recommended)

```bash
# Install uv if you don't have it
brew install uv

# Clone the repository
git clone https://github.com/yourusername/macshot.git
cd macshot

# Python version is managed by .python-version file
# uv will automatically use Python 3.12

# Make executable
chmod +x macshot.py
```

### Manual Installation

```bash
# Clone or download
cd /path/to/macshot

# Make executable
chmod +x macshot.py

# Ensure Python 3.9+ is installed
python3 --version
```

## Usage

### Two-Mode Workflow

**macshot** uses a two-mode workflow for efficient screenshot capture:

#### Mode 1: Set Folder (once per session)

```bash
# Set destination folder via macOS folder picker
uv run macshot.py --set-folder
```

This opens a native macOS folder selection dialog. The selected folder is saved for future screenshots.

#### Mode 2: Take Screenshot (repeat as needed)

```bash
# Take screenshot to previously selected folder
uv run macshot.py
```

Takes a single screenshot with interactive area selection and saves it to the folder you set in Mode 1.

---

### Typical Workflow Example

```bash
# 1. Set folder once (e.g., for Athora work screenshots)
uv run macshot.py --set-folder
> [Select: ~/projects/athora/screenshots]

# 2. Take multiple screenshots (repeat as needed)
uv run macshot.py  # Screenshot 1
uv run macshot.py  # Screenshot 2
uv run macshot.py  # Screenshot 3
# ... continue as needed

# 3. Change folder when switching context (e.g., to Bitvocation)
uv run macshot.py --set-folder
> [Select: ~/projects/bitvocation/screenshots]

# 4. Take more screenshots to new location
uv run macshot.py  # Screenshot in new folder
```

**Cancel**: Press `ESC` during screenshot selection to cancel

**Note**: `uv run` automatically manages the Python version specified in `.python-version` (3.12), downloading it if needed.

---

### Keyboard Shortcuts (Highly Recommended)

For maximum efficiency, set up **two keyboard shortcuts**:

1. **Set Folder**: `Ctrl+Cmd+Shift+S` (use occasionally)
2. **Take Screenshot**: `Ctrl+Cmd+S` (use frequently)

See: [docs/mac-shortcuts-setup.md](docs/mac-shortcuts-setup.md) for detailed setup instructions.

## Output

Screenshots are saved to your selected folder with timestamp-only filenames:
```
[your-selected-folder]/YYYYMMDD-HHMMSS.png
```

Example: `20251022-103045.png`

The selected folder path is stored in `~/.macshot_folder` and persists between sessions.

## Project Structure

```
macshot/
├── README.md              # This file
├── macshot.py             # Main script
├── screenshots/           # Output folder (gitignored)
│   └── .gitkeep
├── .gitignore             # Git configuration
└── docs/
    └── mac-shortcuts-setup.md  # Keyboard shortcut setup guide
```

## Use Cases

- **Documenting presentations/slides**: Set folder once, capture many slides
- **Remote work screenshots**: Capture Windows/RDP environments efficiently
- **Tutorial/guide creation**: Organize screenshots by topic/section
- **Bug reporting**: Quick visual documentation
- **Visual note-taking**: Timestamped reference images
- **Multi-project workflows**: Switch folders between different contexts

## Philosophy

**Sovereign tooling**: Simple, transparent, zero-dependency tools that you own and control. No cloud services, no tracking, no complexity.

## License

MIT License - See LICENSE file

## Contributing

Contributions welcome! This is a simple tool by design, but improvements to core functionality are appreciated.

---

**macshot** - Part of the sovereign data toolkit
