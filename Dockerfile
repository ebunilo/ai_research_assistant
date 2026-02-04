# Dockerfile for AI Research Assistant
# Multi-stage build for optimized production image

FROM python:3.11-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.11-slim AS runtime

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY research_assistant/ ./research_assistant/

# Create .adk directory for ADK agent discovery
RUN mkdir -p /app/.adk

# Create directory for reports
RUN mkdir -p /app/reports

# Expose port for ADK web interface
EXPOSE 8020

# Health check - verify ADK web server is responding
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -sf http://localhost:8020/ || exit 1

# Run the ADK agent server with explicit path to agent directory
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8020", "--agent-path", "/app/research_assistant"]
