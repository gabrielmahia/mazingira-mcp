"""MazingiraMCP — Kenya Environment and Climate Tools (5 tools). All data DEMO."""
from __future__ import annotations
from typing import Optional
from fastmcp import FastMCP
mcp = FastMCP(name="mazingira-mcp", instructions="Kenya environment: NEMA permits, climate data, conservation. DEMO.")

@mcp.tool(name="nema_permit_guide", description="NEMA environmental permit requirements and process in Kenya. DEMO.")
def nema_permit_guide(activity_type: str, county: Optional[str] = None) -> dict:
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
    data = next((v for k, v in PERMITS.items() if k in at or at in k), PERMITS["construction"])
    return {"source": "DEMO — nema.go.ke for official process", "activity": activity_type, "county": county,
            **data, "nema": "nema.go.ke | 020-2111088", "penalty": "Operating without EIA: KES 1M fine or 2 years prison"}

@mcp.tool(name="climate_data_guide", description="Kenya climate data sources: weather, drought, flood risk. DEMO.")
def climate_data_guide(data_type: str, county: Optional[str] = None) -> dict:
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

@mcp.tool(name="conservation_areas", description="Kenya conservation areas, national parks, and protected land zones. DEMO.")
def conservation_areas(county: Optional[str] = None, area_type: Optional[str] = None) -> dict:
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

@mcp.tool(name="environmental_rights_query", description="Environmental rights under Kenya Constitution 2010 Article 42. DEMO.")
def environmental_rights_query(topic: str) -> dict:
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

@mcp.tool(name="climate_adaptation_guide", description="Kenya climate adaptation resources for farmers and communities. DEMO.")
def climate_adaptation_guide(region: Optional[str] = None, sector: Optional[str] = "agriculture") -> dict:
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
