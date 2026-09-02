# mazingira-mcp

## Why This Exists

Kenyan projects stall or get fined because NEMA's permit thresholds, EIA requirements and environmental rights are hard to establish up front. Operating without an EIA carries serious penalties, so knowing which category a project falls into is worth more than knowing the law in general.

## Install

```bash
pip install mazingira-mcp
```

## Tools (5)

- **`nema_permit_guide`** — Return Kenya NEMA (National Environment Management Authority) permit requirements and application process.  
  <sub>args: activity_type, county</sub>
- **`climate_data_guide`** — Return Kenya climate data, rainfall patterns, and temperature ranges by region.  
  <sub>args: data_type, county</sub>
- **`conservation_areas`** — Return information on Kenya national parks, game reserves, and conservation areas.  
  <sub>args: county, area_type</sub>
- **`environmental_rights_query`** — Return Kenya citizen environmental rights and violation reporting procedures.  
  <sub>args: topic</sub>
- **`climate_adaptation_guide`** —   
  <sub>args: region, sector</sub>

## Example

```python
from mazingira_mcp.server import nema_permit_guide

result = nema_permit_guide(project_type='construction')
# permit type, threshold, fee basis, timeline, penalty exposure
```

## Claude Desktop Integration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mazingira-mcp": {
      "command": "python",
      "args": ["-m", "mazingira_mcp.server"]
    }
  }
}
```

## Data & Disclaimers

Thresholds, fees and penalties reflect NEMA guidance and the Environmental Management and Co-ordination Act. Verify current figures at nema.go.ke before budgeting or filing.

Every tool response carries a `source` field. Responses labelled `DEMO` are
illustrative reference data, not a live feed — verify against the authority
named in the response before acting on it.

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All 32 servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).

<!-- interconnect:v1 -->
## Part of the East Africa coordination stack

- **Install & run:** `pip install reli-cli && reli list` — 33 MCP servers on the [official MCP Registry](https://registry.modelcontextprotocol.io) under `io.github.gabrielmahia`
- **Evaluate any model on Swahili agent tasks:** [kipimo](https://github.com/gabrielmahia/kipimo) · [dataset](https://huggingface.co/datasets/gmahia/kipimo) · [leaderboard](https://huggingface.co/spaces/gmahia/kipimo-leaderboard)
- **Coordinate across servers:** [africa-coord-bus](https://pypi.org/project/africa-coord-bus/) — offline-first event bus with a built-in Kenya routing table
- **Datasets:** [huggingface.co/gmahia](https://huggingface.co/gmahia) · **Docs hub:** [nairobi-stack](https://github.com/gabrielmahia/nairobi-stack)

Model-agnostic by design: closed APIs, open-weight models, and small distilled models are all first-class citizens.
<!-- /interconnect:v1 -->
