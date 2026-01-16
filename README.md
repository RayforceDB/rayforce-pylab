# Rayforce PyLab

Browser-based Python environment with rayforce-py, powered by Pyodide.

## Features

- rayforce-py running in the browser via WebAssembly
- Monaco Editor with Python syntax highlighting
- Real-time code execution with Shift+Enter

## Quick Start

```bash
# Start local server
python serve.py

# Open in browser
http://localhost:8080/rayforce-pylab/index.html
```

## Building the Wheel

Prerequisites:
- Emscripten SDK (emcc)
- Pyodide xbuildenv
- rayforce-wasm built with latest rayforce core

```bash
# Build rayforce-py C extension for Pyodide
make -f Makefile.pyodide
```

## Project Structure

```
rayforce-pylab/
├── index.html           # Main web application
├── serve.py             # Development server with CORS
├── Makefile.pyodide     # Build configuration for Pyodide
├── pyodide_compat.h     # C compatibility header
└── dist/
    └── rayforce-*.whl   # Pre-built Pyodide wheel
```

## Limitations

- Fluent query API (`.select().where().execute()`) has threading issues in WASM
- Use `eval_str()` with Rayfall syntax for queries as a workaround

## GitHub Pages Deployment

The project uses GitHub Actions to automatically:
1. Pull latest `rayforce` and `rayforce-py` from master
2. Build WASM with Emscripten
3. Create Pyodide wheel
4. Deploy to GitHub Pages

### Setup

1. Enable GitHub Pages in repository settings:
   - Go to Settings → Pages
   - Source: "GitHub Actions"

2. Push to master - deployment happens automatically

3. Manual rebuild: Actions → "Build and Deploy" → "Run workflow"

Daily rebuilds are scheduled at midnight UTC to catch upstream updates.

## Dependencies

- [Pyodide](https://pyodide.org/) 0.26.4 - Python 3.12 in WebAssembly
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) - Code editor
- [rayforce](https://github.com/RayforceDB/rayforce) - Core database
- [rayforce-py](https://github.com/RayforceDB/rayforce-py) - Python bindings
