# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for mazingira-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/mazingira-mcp"
LABEL org.opencontainers.image.description="mazingira-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir mazingira-mcp

CMD ["mazingira-mcp"]
