# CLAUDE.md — AI Assistant Guide for Plugin

## Project Overview

This is the **Plugin** repository for the `citoyendelmundo-ui` project. It is a newly initialized repository intended to house plugin functionality for the citoyendelmundo-ui ecosystem.

## Repository Status

- **State**: Newly initialized (empty repository)
- **Default branch**: `main`
- **Remote**: `citoyendelmundo-ui/plugin` on GitHub

## Development Workflow

### Branch Naming

- Feature branches: `feature/<short-description>`
- Bug fixes: `fix/<short-description>`
- Documentation: `docs/<short-description>`
- Claude-generated branches follow the pattern: `claude/<description>-<id>`

### Commit Conventions

- Use clear, descriptive commit messages
- Lead with a verb in imperative mood (e.g., "Add", "Fix", "Update", "Remove")
- Keep the subject line under 72 characters
- Add a blank line before extended description if needed

### Pull Requests

- PRs should target `main`
- Include a summary of changes and a test plan
- Keep PRs focused on a single concern

## Build & Test Commands

> **Note**: Build tooling has not yet been configured. Update this section as the project evolves.

```bash
# Placeholder — update once tooling is added
# npm install        # Install dependencies
# npm run build      # Build the project
# npm test           # Run tests
# npm run lint       # Run linter
```

## Project Structure

> **Note**: The directory structure will be documented here as the project takes shape.

```
Plugin/
├── CLAUDE.md          # This file — AI assistant guide
└── ...                # Project files to be added
```

## Code Conventions

- Follow consistent naming conventions established by the first contributors
- Prefer clear, self-documenting code over excessive comments
- Keep functions small and focused on a single responsibility
- Validate at system boundaries (user input, external APIs), trust internal code

## Key Guidelines for AI Assistants

1. **Read before writing** — Always read existing files before modifying them
2. **Minimal changes** — Only change what is necessary to complete the task; do not refactor surrounding code
3. **No speculative features** — Do not add error handling, abstractions, or features beyond what is requested
4. **Security first** — Never introduce command injection, XSS, SQL injection, or other OWASP Top 10 vulnerabilities
5. **No secrets in code** — Never commit `.env`, credentials, API keys, or other sensitive data
6. **Test your work** — Run the project's test suite after making changes
7. **Update this file** — When adding significant tooling, structure, or conventions, update CLAUDE.md to reflect the current state
