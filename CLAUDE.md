# CLAUDE.md - AI Assistant Guide for VQS Repository

**Last Updated:** 2025-12-09
**Repository:** VQS (VQS system)
**Owner:** KevinHe (kevin.itsz@gmail.com)
**License:** Apache License 2.0

---

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Current Project State](#current-project-state)
3. [Development Workflow](#development-workflow)
4. [Git Conventions](#git-conventions)
5. [Code Structure Guidelines](#code-structure-guidelines)
6. [AI Assistant Guidelines](#ai-assistant-guidelines)
7. [Future Development Checklist](#future-development-checklist)

---

## Repository Overview

### Project Purpose
VQS is a system currently in its early initialization phase. The specific purpose, architecture, and implementation details are yet to be defined.

### Technology Stack
**Status:** To be determined

The project has not yet selected its technology stack. When choosing technologies, consider:
- Project requirements and use cases
- Team expertise and preferences
- Long-term maintenance and community support
- Performance and scalability needs

### Repository Structure
```
VQS/
├── .git/                 # Git version control
├── LICENSE              # Apache License 2.0
├── README.md            # Project overview (minimal)
└── CLAUDE.md            # This file - AI assistant guide
```

---

## Current Project State

### Status: Early Initialization

The repository is in its foundational stage with:
- ✅ Git repository initialized
- ✅ Apache 2.0 license established
- ✅ Basic README created
- ❌ No source code yet
- ❌ No build system configured
- ❌ No testing framework setup
- ❌ No development dependencies

### What Exists
- **LICENSE**: Apache License 2.0 - permissive open-source license
- **README.md**: Minimal project description
- **Git Configuration**:
  - GPG signing enabled (SSH key-based)
  - Remote repository configured
  - Branch structure established

### What's Missing
Everything else! The project awaits:
- Programming language selection
- Framework and library choices
- Directory structure
- Build and development tooling
- Testing infrastructure
- Documentation
- Source code implementation

---

## Development Workflow

### Branch Strategy

**Current Branch:** `claude/claude-md-miylbfjpj4668sdz-01WfCYFJFmq3VMzpdYWzGRCZ`

#### Branch Naming Convention
- **Feature branches**: `feature/<descriptive-name>`
- **Bug fix branches**: `bugfix/<descriptive-name>`
- **Claude AI branches**: `claude/<session-identifier>`
- **Main branch**: TBD (typically `main` or `master`)

#### Workflow Steps
1. Create or checkout appropriate branch
2. Make changes with clear, atomic commits
3. Test changes (once testing infrastructure exists)
4. Push to remote with `-u` flag: `git push -u origin <branch-name>`
5. Create pull request for review (when applicable)

---

## Git Conventions

### Commit Message Guidelines

Follow these conventions for clear, meaningful commit messages:

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Commit Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Build process, tooling, dependencies

#### Examples
```bash
feat(api): add user authentication endpoint

Implements JWT-based authentication with refresh tokens.
Includes middleware for protected routes.

Closes #123
```

```bash
docs(readme): update installation instructions

Add detailed steps for different operating systems
and troubleshooting section.
```

### Git Push Strategy

**CRITICAL**: Always use the full push command with upstream tracking:
```bash
git push -u origin <branch-name>
```

**Branch Requirements:**
- Claude branches MUST start with `claude/` and end with matching session ID
- Push failures with 403 errors indicate branch naming issues

**Network Retry Policy:**
- Retry up to 4 times on network failures
- Use exponential backoff: 2s, 4s, 8s, 16s
- Applies to: `git push`, `git fetch`, `git pull`

### Git Operations Best Practices

```bash
# Fetching specific branches (preferred)
git fetch origin <branch-name>

# Pulling with explicit branch
git pull origin <branch-name>

# Checking status
git status

# Viewing diff before commit
git diff
git diff --staged

# Viewing commit history
git log --oneline -10
```

---

## Code Structure Guidelines

### Recommended Directory Structure

When the project begins development, consider this structure:

```
VQS/
├── .git/                    # Git version control
├── .github/                 # GitHub-specific files
│   ├── workflows/          # CI/CD workflows
│   └── ISSUE_TEMPLATE/     # Issue templates
├── docs/                    # Documentation
│   ├── api/                # API documentation
│   ├── architecture/       # Architecture diagrams and docs
│   └── guides/             # User and developer guides
├── src/                     # Source code
│   ├── core/               # Core functionality
│   ├── utils/              # Utility functions
│   └── config/             # Configuration files
├── tests/                   # Test files
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── e2e/                # End-to-end tests
├── scripts/                 # Build and utility scripts
├── .gitignore              # Git ignore patterns
├── LICENSE                 # Apache License 2.0
├── README.md               # Project overview
├── CLAUDE.md               # This file
├── CONTRIBUTING.md         # Contribution guidelines
└── <build-config>          # package.json, setup.py, etc.
```

### File Naming Conventions

**To be established** based on chosen language and framework. Common patterns:

- **camelCase**: `userService.js`, `dataValidator.ts`
- **PascalCase**: `UserModel.py`, `AuthController.java`
- **kebab-case**: `user-service.js`, `data-validator.ts`
- **snake_case**: `user_service.py`, `data_validator.rb`

### Code Style

**To be established** - Consider using:
- Linters (ESLint, Pylint, RuboCop, etc.)
- Formatters (Prettier, Black, rustfmt, etc.)
- Pre-commit hooks for automated checking
- EditorConfig for consistent IDE settings

---

## AI Assistant Guidelines

### When Working on This Repository

#### 1. Always Read Before Modifying
- Read existing files before making changes
- Understand the context and existing patterns
- Don't assume - verify file contents and structure

#### 2. Maintain Consistency
- Follow existing naming conventions
- Match current code style and formatting
- Respect established architectural patterns
- Use the same dependency versions

#### 3. Minimal, Focused Changes
- Make changes directly related to the task
- Avoid over-engineering or premature optimization
- Don't add features beyond what's requested
- Keep solutions simple and maintainable

#### 4. Documentation Standards
- Update documentation when changing functionality
- Add comments only where logic isn't self-evident
- Include examples for complex features
- Keep CLAUDE.md updated with new conventions

#### 5. Testing Requirements
- Write tests for new features (once framework exists)
- Ensure existing tests pass before committing
- Don't skip test execution
- Update tests when modifying functionality

#### 6. Security Considerations
- Never commit secrets, credentials, or API keys
- Validate input at system boundaries
- Follow OWASP security best practices
- Be mindful of common vulnerabilities:
  - SQL injection
  - XSS (Cross-Site Scripting)
  - Command injection
  - Path traversal
  - CSRF

#### 7. Git Workflow for AI
1. Verify current branch: `git status`
2. Ensure on correct feature branch
3. Make changes using appropriate tools (Read, Edit, Write)
4. Review changes: `git diff`
5. Stage relevant files: `git add <files>`
6. Create descriptive commit: `git commit -m "..."`
7. Push with tracking: `git push -u origin <branch-name>`

#### 8. When to Use Tools
- **Read**: Always before editing files
- **Edit**: For modifying existing files (preferred over Write)
- **Write**: Only for creating new files
- **Grep/Glob**: For searching code (prefer Task tool for complex searches)
- **Bash**: For git operations, builds, tests, and system commands
- **Task**: For complex, multi-step operations or thorough codebase exploration

#### 9. Communication Style
- Be concise and clear
- Avoid unnecessary emojis (unless requested)
- Focus on technical accuracy
- Provide objective analysis over validation
- Include file paths with line numbers: `file.js:123`

#### 10. Error Handling
- If encountering errors, analyze and fix them
- Don't mark tasks complete if tests fail
- Report blockers clearly
- Suggest solutions based on error context

---

## Future Development Checklist

### Phase 1: Project Foundation
- [ ] Define project requirements and goals
- [ ] Choose programming language and framework
- [ ] Set up package manager and dependency management
- [ ] Create directory structure
- [ ] Configure linting and formatting tools
- [ ] Set up EditorConfig

### Phase 2: Development Infrastructure
- [ ] Configure build system
- [ ] Set up testing framework
- [ ] Create CI/CD pipeline (GitHub Actions, etc.)
- [ ] Add pre-commit hooks
- [ ] Configure code coverage tools
- [ ] Set up development environment documentation

### Phase 3: Code Standards
- [ ] Define code style guidelines
- [ ] Create coding conventions document
- [ ] Set up automated code review tools
- [ ] Establish pull request template
- [ ] Create issue templates

### Phase 4: Documentation
- [ ] Expand README.md with:
  - Installation instructions
  - Usage examples
  - Configuration options
  - Troubleshooting guide
- [ ] Create CONTRIBUTING.md
- [ ] Set up API documentation (if applicable)
- [ ] Create architecture documentation
- [ ] Add inline code documentation

### Phase 5: Quality Assurance
- [ ] Achieve test coverage targets
- [ ] Set up integration testing
- [ ] Configure performance testing
- [ ] Implement security scanning
- [ ] Add dependency vulnerability scanning

### Phase 6: Deployment
- [ ] Create deployment scripts
- [ ] Set up containerization (Docker, etc.)
- [ ] Configure production environment
- [ ] Create deployment documentation
- [ ] Set up monitoring and logging

---

## Project-Specific Notes

### Current State Notes
- Repository is in early initialization phase
- No code has been written yet
- Technology decisions pending
- This is the perfect time to establish conventions!

### Decision Log
_(Document major technical decisions here as they're made)_

| Date | Decision | Rationale |
|------|----------|-----------|
| 2025-12-09 | Apache License 2.0 selected | Permissive open-source license suitable for wide adoption |

### Known Issues
None currently - project hasn't begun implementation.

### Performance Considerations
To be documented once implementation begins.

### Security Notes
To be documented based on chosen technologies and architecture.

---

## Updates and Maintenance

### Updating This Document
This document should be updated when:
- Project structure changes significantly
- New conventions are established
- Technology stack is chosen or modified
- Development workflow changes
- New tools are integrated

### Review Frequency
- Review quarterly or after major milestones
- Update immediately when conventions change
- Keep synchronized with actual codebase state

---

## Resources

### Git
- [Git Documentation](https://git-scm.com/doc)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

### Security
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Security Best Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)

### General
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- [Semantic Versioning](https://semver.org/)

---

## Contact and Support

**Repository Owner:** KevinHe (kevin.itsz@gmail.com)

For questions, issues, or contributions, please follow the standard GitHub workflow:
1. Check existing issues
2. Create a new issue if needed
3. Submit pull requests for contributions

---

*This document is a living guide and should evolve with the project. Keep it updated and accurate!*
