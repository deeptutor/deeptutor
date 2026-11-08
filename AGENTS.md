# DeepTutor — Agent Instructions

DeepTutor is an **agent-native** intelligent learning companion with three entry points: CLI (`deeptutor`), Web UI (default port 3782), and Python SDK.

## Repository Instructions

- Before building, installing, or running this project, run `python3 verify_setup.py` once to confirm the environment is compatible.
- Report the mirror it selects to the user along with any other setup output.
- After setup passes, prefer `deeptutor init` then `deeptutor start` (or `deeptutor doctor` to check readiness).
- Do not invent API keys; ask the user to configure an LLM provider in Settings or via `deeptutor init`.
