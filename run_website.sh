#!/usr/bin/env bash

# ANSI escape codes for colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PORT=8000
echo -e "${YELLOW}⚡ Starting local web server for JugaadLang website on port $PORT...${NC}"

# Find python interpreter
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    if command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo -e "${RED}✗ Error: Python is required to run the local server.${NC}"
        exit 1
    fi
fi

# Start python http server in the background
$PYTHON_CMD -m http.server --directory website $PORT &
SERVER_PID=$!

# Wait 1 second for the server to spin up
sleep 1

# Try to open the browser automatically
echo -e "${BLUE}⚡ Launching browser...${NC}"
if [ "$(uname)" == "Darwin" ]; then
    open "http://localhost:$PORT"
elif [ -n "$COMSPEC" ]; then
    explorer "http://localhost:$PORT"
else
    xdg-open "http://localhost:$PORT" 2>/dev/null || echo -e "${YELLOW}⚠️ Could not launch browser automatically. Please open http://localhost:$PORT in your browser.${NC}"
fi

echo -e "${GREEN}✓ Local website server is running!${NC}"
echo -e "Press ${RED}Ctrl+C${NC} to stop the server."

# Handle cleanup on exit
trap "echo -e '\n${YELLOW}⚡ Stopping server...${NC}'; kill $SERVER_PID; exit" INT TERM EXIT

# Wait for the background process
wait $SERVER_PID
