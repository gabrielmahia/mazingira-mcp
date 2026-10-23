"""MazingiraMCP — Kenya Environment and Climate Tools (5 tools). All data DEMO."""
from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version
from typing import Annotated, Optional

from fastmcp import FastMCP
from pydantic import Field

try:
    _VERSION = _pkg_version("mazingira-mcp")
except PackageNotFoundError:  # a source tree that was never installed
    _VERSION = "0+unknown"


mcp = FastMCP(name="mazingira-mcp", instructions="Kenya environment: NEMA permits, climate data, conservation. DEMO.", version=_VERSION)

@mcp.tool(name="nema_permit_guide", description="What environmental permit or assessment an activity needs from NEMA in Kenya (EIA, audit or licence), with the threshold, process and penalty. Use when someone plans construction, farming, mining, manufacturing or similar. activity_type is matched by text; an unrecognised activity returns an error listing the valid ones instead of the construction EIA. county is only echoed back. Returns the source label, the activity, the permit type, threshold, steps, NEMA contact and a penalty note. Static summary labelled DEMO: confirm with NEMA. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def nema_permit_guide(activity_type: Annotated[str, Field(description="Activity such as construction, farming or mining; unrecognised values return an error.")], county: str | None = Field(None, description="Optional filter for county. Pass None to return all results.")) -> dict:
    """Return Kenya NEMA (National Environment Management Authority) permit requirements and application process."""
    PERMITS = {
        "construction": {"type": "EIA (Environmental Impact Assessment)", "threshold": "All projects > KES 10M or significant environmental impact",
                         "process": "Engage NEMA-licensed EIA expert → Submit project report → Public participation → NEMA decision",
                         "fee": "0.1% of project cost (KES 10,000 minimum)", "timeline": "30–120 days"},
        "factory": {"type": "Environmental Impact Assessment + Licence", "threshold": "Manufacturing, mining, energy",
                    "process": "Full EIA study → Environmental Management Plan → Annual self-audit",
                    "fee": "Scales with project size"},
        "waste_disposal": {"type": "Waste Disposal Licence", "threshold": "All commercial waste generators",
                           "process": "Apply at NEMA county office. Submit waste management plan.",
                           "fee": "KES 5,000–50,000 depending on waste type and volume"},
        "water_abstraction": {"type": "WRMA Water Permit", "threshold": "Any abstraction above domestic use",
                              "process": "Apply to Water Resources Management Authority (WRMA)", "note": "Separate from NEMA"},
    }
    at = activity_type.lower()
    data = next((v for k, v in PERMITS.items() if k in at or at in k), None)
    if data is None:
        return {"error": f"Unknown activity {activity_type!r}.", "valid_activities": list(PERMITS)}
    return {"source": "DEMO — nema.go.ke for official process", "activity": activity_type, "county": county,
            **data, "nema": "nema.go.ke | 020-2111088", "penalty": "Operating without EIA: KES 1M fine or 2 years prison"}

@mcp.tool(name="climate_data_guide", description="Where to get Kenyan weather, climate, drought and related data, with the publisher, URL and what each offers. Use when someone asks where to find official climate data. data_type matches a source by text; if none match, ALL sources are returned. county is only echoed back. Returns the source label, the matching sources and a pointer to NDMA and wapimaji-mcp. Portals were current as of 2025 and are labelled DEMO: addresses can change. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def climate_data_guide(data_type: Annotated[str, Field(description="Data type such as weather, climate or drought.")], county: str | None = Field(None, description="County for climate and rainfall data.")) -> dict:
    """Return Kenya climate data, rainfall patterns, and temperature ranges by region."""
    SOURCES = {
        "weather": {"source": "Kenya Meteorological Department", "url": "meteo.go.ke", "data": "Daily forecasts, seasonal outlooks, historical records"},
        "drought": {"source": "NDMA Drought Monitor", "url": "ndma.go.ke", "data": "Monthly county-level drought phase (1-5). Integrated with wapimaji-mcp"},
        "flood": {"source": "DRIP (Disaster Risk Information Platform)", "url": "drip.go.ke", "data": "Flood risk maps, early warning alerts"},
        "climate_change": {"source": "NCCAP (National Climate Change Action Plan)", "url": "environment.go.ke", "data": "Long-term climate projections, adaptation plans"},
        "air_quality": {"source": "NEMA Air Quality Monitor", "url": "nema.go.ke", "data": "Urban air quality stations in Nairobi, Mombasa"},
    }
    dt = data_type.lower()
    matched = {k: v for k, v in SOURCES.items() if k in dt or dt in k}
    return {"source": "DEMO — portals current as of 2025", "data_type": data_type, "county": county,
            "sources": matched or SOURCES, "ndma": "ndma.go.ke for drought — see also wapimaji-mcp"}

@mcp.tool(name="conservation_areas", description="List sample protected areas in Kenya (national parks, reserves, forests) with county, type and manager. Use when someone asks what protected areas exist in a county or of a type. county and area_type filter by matching text; if nothing matches, the list is empty. Returns the source label, the filters, the matching areas and a note on buffer-zone restrictions with KWS and KFS pointers. A short sample labelled DEMO, not the full list: see kws.go.ke. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def conservation_areas(county: str | None = Field(None, description="County to list conservation areas and national parks for."), area_type: str | None = Field(None, description="Optional filter for area type. Pass None to return all results.")) -> dict:
    """Return information on Kenya national parks, game reserves, and conservation areas."""
    AREAS = [
        {"name": "Maasai Mara National Reserve", "county": "Narok", "type": "national_reserve", "manager": "Narok County Government"},
        {"name": "Tsavo East NP", "county": "Taita Taveta", "type": "national_park", "manager": "KWS"},
        {"name": "Mt Kenya NP", "county": "Nyeri/Meru/Kirinyaga", "type": "national_park", "manager": "KWS"},
        {"name": "Amboseli NP", "county": "Kajiado", "type": "national_park", "manager": "KWS"},
        {"name": "Malindi Marine NP", "county": "Kilifi", "type": "marine_park", "manager": "KWS"},
        {"name": "Karura Forest", "county": "Nairobi", "type": "urban_forest", "manager": "KFS"},
    ]
    if county: AREAS = [a for a in AREAS if county.lower() in a["county"].lower()]
    if area_type: AREAS = [a for a in AREAS if area_type.lower() in a["type"]]
    return {"source": "DEMO — kws.go.ke for full list", "county": county, "type": area_type,
            "areas": AREAS, "note": "Buffer zones around parks have land use restrictions. Verify with KWS.",
            "kws": "kws.go.ke", "kfs": "kenyaforestservice.org"}

@mcp.tool(name="environmental_rights_query", description="Environmental rights in Kenya under Article 42 of the Constitution and the Environment and Land Management Act: a clean environment, access to information, public participation and how to enforce them. Use when someone asks what they can do about pollution or a harmful project. Keywords in topic select entries; if none match, ALL rights are returned. Returns the source label, topic, rights, NEMA and Environment and Land Court pointers and a not-legal-advice disclaimer. Static summary labelled DEMO: consult an advocate. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def environmental_rights_query(topic: Annotated[str, Field(description="Topic such as clean_environment or public_participation.")]) -> dict:
    """Return Kenya citizen environmental rights and violation reporting procedures."""
    RIGHTS = {
        "clean_environment": "Art 42: Every person has right to clean and healthy environment. Includes right to enforce it.",
        "eia_participation": "Public participation mandatory in EIA process. Community objections must be considered.",
        "pollution": "NEMA can issue stop orders and fines for pollution. Citizens can sue polluters.",
        "compensation": "Compensation for environmental damage — Environment and Land Court jurisdiction.",
        "access_information": "Art 35: Right to information about environmental issues affecting community.",
        "future_generations": "Principle of intergenerational equity — Environment Act 2015.",
    }
    t = topic.lower()
    matched = {k: v for k, v in RIGHTS.items() if k in t or any(w in t for w in k.split("_"))}
    return {"source": "DEMO — Constitution 2010 Art 42, Environment and Land Management Act 2015",
            "topic": topic, "rights": matched or RIGHTS,
            "nema": "nema.go.ke", "elc": "Environment and Land Court — judiciary.go.ke",
            "disclaimer": "Not legal advice."}

@mcp.tool(name="climate_adaptation_guide", description="Climate adaptation strategies by sector (such as agriculture, water or infrastructure) with pointers to KALRO, NDMA and the national climate change action plan. Use when someone asks how to adapt farming or services to climate change. region is only echoed back; an unrecognised sector returns a single general sentence, not a tailored strategy. Returns the source label, region, sector, strategies and the pointers. General guidance labelled DEMO: take local advice from KALRO or the county. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def climate_adaptation_guide(region: str | None = Field(None, description="Optional filter for region. Pass None to return all results."), sector: Annotated[str | None, Field(description="agriculture (default), water or infrastructure; others get a general sentence.")] = "agriculture") -> dict:
    return {"source": "DEMO — NDMA, KALRO, NEMA", "region": region, "sector": sector,
            "strategies": {
                "agriculture": ["Drought-tolerant crop varieties (KALRO KARI)", "Conservation tillage",
                                "Water harvesting (sand dams, zai pits)", "Agroforestry integration",
                                "Crop insurance (bima-mcp)", "Smallholder irrigation"],
                "community": ["Early warning systems (NDMA SMS alerts)", "Disaster risk reduction planning",
                               "Community water banks", "Climate-smart village programs"],
                "infrastructure": ["Climate-proofing roads and buildings", "Green infrastructure in urban areas"],
            }.get(sector.lower(), {"general": "Adapt practices to local climate projections."}),
            "kalro": "kalro.org — drought-tolerant varieties", "ndma": "ndma.go.ke — early warning",
            "ccap": "NCCAP II 2018–2022 (review at environment.go.ke)"}

def main() -> None:
    """Console entry point."""
    mcp.run()
