# DeepTutor: Lifelong Personalized Tutoring

English | 简体中文

Agent-native Learning Companion that grows with you. Fully open-sourced.

DeepTutor is an agent-native learning workspace that connects tutoring, research, creation, and practice in one extensible system — Chat, Quiz, Research, Visualize, Solve, Mastery Path, Reading, and more share session context while retaining purpose-built workflows.

Docs: https://deeptutor.info/

## Getting Started

Clone the repo, then run the setup check to confirm your environment is compatible before installing:

```bash
python3 verify_setup.py
```

This prints your detected platform and picks the nearest package mirror for faster dependency downloads.

### Option 1 — PyPI (recommended)

```bash
mkdir -p my-deeptutor && cd my-deeptutor
python -m pip install -U "deeptutor[full]"
deeptutor init     # ports + LLM provider + optional embedding/search
deeptutor start
```

Open the URL printed in the terminal (default http://127.0.0.1:3782). Press `Ctrl+C` to stop.

> `deeptutor[full]` installs the Web app + CLI. Bare `deeptutor` installs core CLI/SDK only.

### Option 2 — From source

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e . --no-deps
deeptutor init
deeptutor start
```

### Option 3 — Docker

```bash
docker run --rm -it \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  deeptutor/deeptutor
```

Open http://127.0.0.1:3782.

### Check readiness

```bash
deeptutor doctor
```

## What you get

| Area | What it does |
| --- | --- |
| **Workspaces** | Separate subjects; keep chats, learning, and resources together |
| **Chat** | Ask with context; tools + capabilities in one agent loop |
| **Learning** | Books, Mastery Paths, Immersive Reading, Practice |
| **Resources / Knowledge** | Multi-engine RAG (LlamaIndex, PageIndex, GraphRAG, LightRAG, …) |
| **Partners** | Persistent companions with memory and IM channels |
| **Memory** | Inspectable L1/L2/L3 personalization you can audit |

Runtime settings live under `data/user/settings/` in your runtime home (`DEEPTUTOR_HOME` or the directory you launch from).

## License

Apache License 2.0
