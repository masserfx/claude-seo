# Product Mission

## Pitch

Claude SEO is an enterprise-grade SEO analysis skill for Claude Code that helps developers, SEO specialists, and marketing agencies perform comprehensive website audits, content optimization, and AI search readiness analysis directly from their IDE.

## Users

### Primary Customers

- **Web Developers**: Need SEO audit capabilities integrated into their development workflow without switching tools
- **SEO Specialists**: Want fast, comprehensive analysis with actionable recommendations and structured data output
- **Marketing Agencies**: Require scalable SEO auditing across multiple client websites with consistent methodology

### User Personas

**Developer Dan** (25-40 years old)
- **Role:** Full-stack web developer
- **Context:** Building and maintaining websites, needs to ensure SEO best practices during development
- **Pain Points:** Switching between IDE and separate SEO tools, manual checking of meta tags and schema markup, keeping up with Google algorithm changes
- **Goals:** Catch SEO issues before deployment, generate proper schema markup, ensure Core Web Vitals compliance

**Agency Anna** (28-45 years old)
- **Role:** SEO consultant at a digital agency
- **Context:** Auditing multiple client websites, creating SEO strategies, reporting on optimization progress
- **Pain Points:** Time-consuming manual audits, inconsistent audit methodologies, expensive SaaS SEO tools
- **Goals:** Fast comprehensive audits, standardized reporting, AI search readiness assessment for clients

**Marketer Max** (30-50 years old)
- **Role:** In-house marketing manager
- **Context:** Managing company website SEO, content optimization, competing for AI search visibility
- **Pain Points:** Limited technical SEO knowledge, unclear prioritization of fixes, no visibility into AI search optimization
- **Goals:** Understand SEO health at a glance, get prioritized action plans, optimize for Google AI Overviews and ChatGPT

## The Problem

### SEO Tools Are Disconnected from Development

Developers must switch between their IDE and external SEO tools (Screaming Frog, Ahrefs, Semrush) to check optimization. This context-switching reduces productivity and means SEO issues are often caught too late.

**Our Solution:** Claude SEO brings comprehensive SEO analysis directly into Claude Code, enabling developers to audit and fix issues without leaving their workflow.

### AI Search Optimization Is a Blind Spot

With the rise of AI Overviews, ChatGPT, and Perplexity, traditional SEO tools don't address AI search visibility. Brand mentions are 3x more important than backlinks for AI citations, yet no tool optimizes for this.

**Our Solution:** The GEO (Generative Engine Optimization) skill analyzes AI crawler access, passage-level citability, and brand mention opportunities across all major AI platforms.

### Programmatic SEO Creates Quality Risks

Scaling content through programmatic SEO often leads to thin content penalties and index bloat. Google's March 2024 Scaled Content Abuse policy makes this especially risky.

**Our Solution:** Built-in quality gates (30+ pages warning, 50+ hard stop for location pages), thin content detection, and doorway page pattern identification prevent penalties before they happen.

## Differentiators

### IDE-Native SEO Analysis

Unlike standalone tools like Screaming Frog or web-based platforms like Ahrefs, Claude SEO runs directly inside Claude Code with natural language interaction. This eliminates context-switching and enables real-time fix verification. Developers can audit, fix, and re-check in a single workflow.

### AI Search Readiness (GEO)

Unlike traditional SEO tools that focus solely on Google organic results, Claude SEO includes comprehensive AI search optimization covering Google AI Overviews, ChatGPT, Perplexity, and other AI platforms. This includes AI crawler management, llms.txt detection, and passage-level citability scoring based on February 2026 research.

### Parallel Subagent Architecture

Unlike sequential audit tools, Claude SEO deploys 6 specialized subagents simultaneously for site audits, dramatically reducing analysis time. Each subagent focuses on its domain (technical, content, schema, sitemap, performance, visual) and results are aggregated into a unified SEO Health Score.

## Key Features

### Core Analysis Features

- **Full Site Audit** (`/seo audit`): Crawl up to 500 pages with 6 parallel subagents producing a unified SEO Health Score (0-100)
- **Deep Page Analysis** (`/seo page`): Comprehensive single-page analysis covering on-page, content, technical, schema, images, and CWV potential
- **Technical SEO** (`/seo technical`): 8-category analysis including crawlability, indexability, security headers, Core Web Vitals, and JS rendering
- **Content Assessment** (`/seo content`): E-E-A-T evaluation, readability metrics, word count validation, and AI citation readiness scoring

### Optimization Features

- **Schema Markup** (`/seo schema`): Detection, validation, and generation for 50+ schema types with deprecation tracking
- **Image Optimization** (`/seo images`): Alt text analysis, format recommendations (WebP/AVIF), responsive images, and lazy loading checks
- **Sitemap Management** (`/seo sitemap`): Analysis, validation, and generation with quality gates for location pages
- **AI Search Optimization** (`/seo geo`): Brand mention analysis, AI crawler management, llms.txt detection, platform-specific optimization

### Strategic Features

- **SEO Planning** (`/seo plan`): Strategic planning with 6 industry templates (SaaS, local, ecommerce, publisher, agency, generic)
- **Programmatic SEO** (`/seo programmatic`): Data quality assessment, template planning, thin content safeguards
- **Competitor Pages** (`/seo competitor-pages`): Comparison page generation with feature matrices and schema markup
- **International SEO** (`/seo hreflang`): Hreflang validation, language code checks, i18n SEO analysis
