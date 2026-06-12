# Use standard lightweight python image
FROM python:3.14-slim

# Set work directory
WORKDIR /app

# Copy package config
COPY pyproject.toml README.md ./

# Install packages
RUN pip install --no-cache-dir .

# Copy source
COPY jugaadlang/ ./jugaadlang/
COPY jug_cli/ ./jug_cli/

# Install editable mode to register CLI
RUN pip install --no-cache-dir -e .

# Expose web framework port
EXPOSE 5000

# Set entry point to launch the REPL
ENTRYPOINT ["jug", "repl"]
