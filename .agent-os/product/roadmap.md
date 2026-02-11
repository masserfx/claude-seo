# Product Roadmap

## Phase 0: Already Completed

The following features have been implemented:

- [x] Core orchestrator skill with routing to 12 sub-skills
- [x] Full site audit with 6 parallel subagents (`/seo audit`) `XL`
- [x] Deep single-page analysis (`/seo page`) `L`
- [x] Technical SEO analysis - 8 categories (`/seo technical`) `L`
- [x] Content & E-E-A-T assessment (`/seo content`) `M`
- [x] Schema markup detection, validation, generation - 50+ types (`/seo schema`) `L`
- [x] Image optimization analysis (`/seo images`) `M`
- [x] Sitemap analysis and generation with quality gates (`/seo sitemap`) `M`
- [x] AI search optimization / GEO (`/seo geo`) `L`
- [x] Strategic SEO planning with 6 industry templates (`/seo plan`) `L`
- [x] Programmatic SEO with quality safeguards (`/seo programmatic`) `M`
- [x] Competitor comparison page generation (`/seo competitor-pages`) `M`
- [x] International SEO / hreflang validation (`/seo hreflang`) `M`
- [x] Python utility scripts (fetch, parse, screenshot, visual analysis) `L`
- [x] Post-edit schema validation hook `S`
- [x] Reference files (CWV thresholds, schema types, E-E-A-T, quality gates) `M`
- [x] Complete documentation (architecture, commands, installation, MCP, troubleshooting) `L`
- [x] Install scripts (Unix + Windows) `S`

## Phase 1: Quality & Reliability

**Goal:** Improve detection accuracy and fill analysis gaps
**Success Criteria:** All TODO.md items resolved, zero false positives in core checks

### Features

- [ ] Fake freshness detection - Compare `datePublished` vs actual content changes `M`
- [ ] Mobile content parity check - Mobile vs desktop meta, schema, content equivalence `M`
- [ ] Discover optimization checks - Clickbait detection, content depth, E-E-A-T signals `M`
- [ ] Brand mention analysis implementation - Programmatic scoring for unlinked mentions `S`

### Dependencies

- Existing content analysis infrastructure
- E-E-A-T framework reference data

## Phase 2: AI Search Expansion

**Goal:** Deepen AI search optimization capabilities across emerging platforms
**Success Criteria:** Coverage of all major AI search platforms, measurable citability improvements

### Features

- [ ] Extended AI platform analysis - Cohere, ByteDance, emerging AI search engines `M`
- [ ] AI citation tracking - Monitor brand appearance in AI-generated answers `L`
- [ ] Passage optimization assistant - Rewrite content for optimal citability (134-167 words) `M`
- [ ] AI crawler management generator - Auto-generate robots.txt and llms.txt configs `S`
- [ ] AI search competitive analysis - Compare AI visibility vs competitors `L`

### Dependencies

- GEO skill foundation (completed)
- Access to AI platform APIs (optional, MCP)

## Phase 3: MCP Integrations

**Goal:** Connect with major SEO data providers for enriched analysis
**Success Criteria:** At least 3 MCP integrations operational with data flowing into reports

### Features

- [ ] Ahrefs MCP integration - Backlink data, domain rating, keyword rankings `L`
- [ ] Semrush MCP integration - Keyword research, position tracking, competitor data `L`
- [ ] Google Search Console integration - Real CTR, impressions, indexing status `M`
- [ ] PageSpeed Insights integration - Real CWV data instead of estimates `S`
- [ ] Google Trends integration - Search demand and trending topics `S`

### Dependencies

- MCP server infrastructure
- API credentials management

## Phase 4: Automation & Monitoring

**Goal:** Enable continuous SEO monitoring and automated workflows
**Success Criteria:** Scheduled audits running, alerting on SEO regressions

### Features

- [ ] Scheduled audit runs - Periodic automated site audits `L`
- [ ] SEO regression alerts - Detect and notify on score drops `M`
- [ ] Historical tracking - Track SEO Health Score over time `M`
- [ ] CI/CD integration - Pre-deploy SEO checks as pipeline step `L`
- [ ] Batch URL analysis - Process URL lists from CSV/sitemap `S`
- [ ] Custom report templates - User-defined report formats and sections `M`

### Dependencies

- Phase 3 integrations for real data
- Persistent storage for historical data

## Phase 5: Enterprise & Scale

**Goal:** Support large-scale enterprise SEO operations
**Success Criteria:** Handle 10k+ page sites, multi-team collaboration

### Features

- [ ] Large-scale crawling - Support for 10,000+ page sites `XL`
- [ ] Multi-site dashboard - Aggregate scores across multiple properties `L`
- [ ] Team collaboration - Shared audit results and task assignment `L`
- [ ] White-label reporting - Agency-branded PDF exports `M`
- [ ] API access - Programmatic access to audit results `L`

### Dependencies

- Phase 4 automation infrastructure
- Enterprise-grade data storage
