# Technical Stack

## Runtime & Language

- **Language:** Python 3.8+
- **Package Manager:** pip (requirements.txt)
- **Execution Environment:** Claude Code Skill (runs inside Claude Code IDE)

## Core Dependencies

- **beautifulsoup4** >=4.12.0,<5.0.0 - HTML parsing and SEO element extraction
- **lxml** >=6.0.2,<7.0.0 - XML/HTML processing engine
- **requests** >=2.32.4,<3.0.0 - HTTP client for web page fetching
- **urllib3** >=2.6.3,<3.0.0 - HTTP library (critical CVE-2026-21441 fix)
- **Pillow** >=12.1.0,<13.0.0 - Image analysis (dimensions, format, file size)
- **validators** >=0.22.0,<1.0.0 - URL and email validation
- **playwright** >=1.56.0,<2.0.0 - Browser automation for screenshots (optional)

## Architecture

- **Platform:** Claude Code Skills framework
- **Pattern:** Orchestrator skill + 12 specialized sub-skills
- **Parallelism:** 6 subagents for concurrent site analysis
- **Data Format:** Markdown reports, JSON-LD schema, PNG screenshots

## Infrastructure

- **Installation Path:** ~/.claude/skills/seo/ (main skill)
- **Sub-skills Path:** ~/.claude/skills/seo-{name}/
- **Agents Path:** ~/.claude/agents/seo-{name}.md
- **Hooks Path:** ~/.claude/hooks/validate-schema.py

## External Integrations (Optional, via MCP)

- Ahrefs API
- Semrush API
- Google Search Console API

## Code Repository

- **URL:** https://github.com/AgriciDaniel/claude-seo
- **License:** MIT
- **Version:** 1.1.0

## Version Strategy

- Bounded version pinning (>=min,<next_major)
- Security-focused minimum versions
- Updated 2026-02-07 with critical CVE fixes
