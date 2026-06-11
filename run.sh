#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# ANSI escape codes for colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

function show_help() {
    echo -e "${BLUE}JugaadLang Development Script${NC}"
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  test    - Run test suite using pytest"
    echo "  build   - Build source (sdist) and binary (wheel) distributions"
    echo "  install - Install local package in editable mode with all optional dependencies"
    echo "  web     - Serve the landing website locally and open it in browser"
    echo "  all     - Run tests, build the package, and install it"
    echo "  help    - Show this help message"
}

function run_test() {
    echo -e "${YELLOW}⚡ Ensuring dependencies are installed...${NC}"
    uv pip install -e .[all]
    echo -e "${YELLOW}⚡ Running test suite...${NC}"
    python3 -m pytest
    echo -e "${GREEN}✓ Tests completed successfully!${NC}"
}

function run_build() {
    echo -e "${YELLOW}⚡ Building JugaadLang package...${NC}"
    # Ensure build package is installed
    uv pip install --upgrade build
    # Clean previous build artifacts
    rm -rf build/ dist/ *.egg-info
    # Build package
    python3 -m build
    echo -e "${GREEN}✓ Package built successfully (artifacts in dist/)${NC}"
}

function run_install() {
    echo -e "${YELLOW}⚡ Installing JugaadLang locally...${NC}"
    uv pip install -e .[all]
    echo -e "${GREEN}✓ Package installed successfully in editable mode!${NC}"
    echo -e "You can now run '${BLUE}jug${NC}' command from anywhere!"
}

# Check command line arguments
case "$1" in
    test)
        run_test
        ;;
    build)
        run_build
        ;;
    install)
        run_install
        ;;
    web|website)
        ./run_website.sh
        ;;
    all|"")
        run_test
        run_build
        run_install
        ;;
    help|*)
        show_help
        ;;
esac
