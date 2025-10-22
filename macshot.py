#!/usr/bin/env python3
"""
macshot - Simple Mac Screenshot Tool

Two-mode operation for efficient screenshot workflows:

Mode 1 - Set Folder:
    macshot.py --set-folder
    Opens folder picker and saves selection for future screenshots

Mode 2 - Take Screenshot:
    macshot.py
    Takes single screenshot to previously selected folder

Workflow:
    1. Set folder once: macshot.py --set-folder
    2. Take many screenshots: macshot.py (repeat as needed)
    3. Change folder anytime: macshot.py --set-folder
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Store last selected folder path
FOLDER_CACHE = Path.home() / ".macshot_folder"


def select_folder():
    """Open macOS folder picker and return selected path"""
    try:
        result = subprocess.run(
            [
                "osascript",
                "-e",
                'POSIX path of (choose folder with prompt "Select folder to save screenshots:")'
            ],
            capture_output=True,
            text=True,
            check=True
        )

        folder_path = result.stdout.strip()
        return Path(folder_path) if folder_path else None

    except subprocess.CalledProcessError:
        # User cancelled folder selection
        return None


def save_folder_path(folder_path):
    """Save selected folder path to cache file"""
    FOLDER_CACHE.write_text(str(folder_path))


def load_folder_path():
    """Load previously selected folder path from cache"""
    if FOLDER_CACHE.exists():
        return Path(FOLDER_CACHE.read_text().strip())
    return None


def set_folder_mode():
    """Mode 1: Select and save destination folder"""
    print("macshot: Select destination folder...")

    folder_path = select_folder()

    if not folder_path:
        print("✗ No folder selected")
        return 1

    # Save for future use
    save_folder_path(folder_path)

    # Ensure folder exists
    folder_path.mkdir(parents=True, exist_ok=True)

    print(f"✓ Folder set: {folder_path}")
    print("  Now use macshot without --set-folder to take screenshots")
    return 0


def take_screenshot_mode():
    """Mode 2: Take single screenshot to saved folder"""

    # Load saved folder
    output_dir = load_folder_path()

    if not output_dir:
        print("✗ No folder configured. Run: macshot.py --set-folder")
        return 1

    if not output_dir.exists():
        print(f"✗ Folder not found: {output_dir}")
        print("  Run: macshot.py --set-folder")
        return 1

    # Generate timestamp filename
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot-{timestamp}.png"
    filepath = output_dir / filename

    try:
        # Use Mac's built-in screencapture with interactive selection
        result = subprocess.run(
            ["screencapture", "-i", str(filepath)],
            capture_output=True
        )

        # Check if file was created (user might have pressed ESC)
        if filepath.exists():
            print(f"✓ Screenshot saved: {filename}")
            print(f"  Location: {output_dir}")
            return 0
        else:
            print("✗ Screenshot cancelled (ESC pressed)")
            return 1

    except subprocess.CalledProcessError as e:
        print(f"✗ Error taking screenshot: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\n✗ Interrupted")
        return 1


def main():
    """Main entry point"""

    parser = argparse.ArgumentParser(
        description="macshot - Simple Mac Screenshot Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--set-folder",
        action="store_true",
        help="Select destination folder for screenshots"
    )

    args = parser.parse_args()

    if args.set_folder:
        return set_folder_mode()
    else:
        return take_screenshot_mode()


if __name__ == "__main__":
    sys.exit(main())
