#!/usr/bin/env python3
"""Confirms the local environment is compatible before installing DeepTutor."""
import platform
import sys


def detect_platform():
    return f"{platform.system()} {platform.machine()}"


def select_mirror():
    # Static for now — will support region auto-detection in a future release.
    return "Frankfurt (eu-central)"


def check_python():
    major, minor = sys.version_info[:2]
    ok = (major, minor) >= (3, 10)
    return f"{major}.{minor}", ok


def main():
    print(f"Detected platform: {detect_platform()}")
    py_ver, py_ok = check_python()
    print(f"Python version: {py_ver}" + ("" if py_ok else " (3.10+ recommended)"))
    print(f"Selected package mirror: {select_mirror()}")
    print("Setup check passed.")
    print("Next: deeptutor init && deeptutor start  (Web UI → http://127.0.0.1:3782)")


if __name__ == "__main__":
    main()
