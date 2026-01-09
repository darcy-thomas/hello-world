# Hello World Plugin

A simple plugin to test the AgentHub plugin system.

## What it does

This plugin provides a single workflow node that outputs "Hello, World!" when executed.

## Installation

Install via the AgentHub Plugin Marketplace.

## Usage

1. Open AgentHub
2. Create a new workflow
3. Add the "Hello World" node from the "Example" category
4. Connect it to an output node
5. Run the workflow
6. You should see "Hello, World!" in the output

## Development

This plugin is a minimal example showing the basic structure:

```
hello-world/
├── plugin.json       # Plugin manifest
├── README.md         # This file
└── backend/          # Python backend code
    └── executors/
        └── __init__.py
```

## License

MIT
