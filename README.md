# macshot

**Simple Mac Screenshot Tool**

A minimal, sovereign screenshot utility for macOS that captures screenshots and saves them with timestamps to a predefined folder.

## Features

- Interactive screenshot capture (select area on screen)
- Auto-saves with timestamp: `screenshot-YYYYMMDD-HHMMSS.png`
- Zero dependencies (pure Python 3 + Mac built-ins)
- Simple, focused, fast
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

### Basic Usage

```bash
# Using uv (recommended - auto-manages Python version)
uv run macshot.py

# Or direct Python (requires Python 3.12+ installed)
python3 macshot.py
```

The script will:
1. Prompt you to select an area on screen
2. Save the screenshot to `screenshots/` folder
3. Print the saved file path

**Cancel**: Press `ESC` during selection to cancel

**Note**: `uv run` automatically manages the Python version specified in `.python-version` (3.12), downloading it if needed.

### Keyboard Shortcut (Recommended)

For the best experience, bind `macshot.py` to a keyboard shortcut using Mac's **Shortcuts app**.

See: [docs/mac-shortcuts-setup.md](docs/mac-shortcuts-setup.md) for detailed instructions.

## Output

Screenshots are saved to:
```
macshot/screenshots/screenshot-YYYYMMDD-HHMMSS.png
```

Example: `screenshot-20251022-103045.png`

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

- Quick documentation capture for work (remote environments, etc.)
- Visual note-taking
- Bug reporting
- Tutorial/guide creation
- Reference image collection

## Future Extensions

Planned enhancements (not implemented yet):
- Custom output folder configuration
- AI-powered screenshot preprocessing
- Multiple format support (PNG, JPG, PDF)
- Annotation capabilities
- OCR integration

## Philosophy

**Sovereign tooling**: Simple, transparent, zero-dependency tools that you own and control. No cloud services, no tracking, no complexity.

## License

MIT License - See LICENSE file

## Contributing

Contributions welcome! This is a simple tool by design, but improvements to core functionality are appreciated.

---

**macshot** - Part of the sovereign data toolkit
