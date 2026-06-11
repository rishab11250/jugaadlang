#!/usr/bin/env bash

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <new_version>"
  echo "Example: $0 1.0.3"
  exit 1
fi

NEW_VERSION=$1
echo "🚀 Updating version to $NEW_VERSION across all components..."

# 1. Update pyproject.toml
python3 -c "
import re
with open('pyproject.toml', 'r') as f: content = f.read()
content = re.sub(r'version = \"[0-9.]+\"', f'version = \"$NEW_VERSION\"', content, count=1)
with open('pyproject.toml', 'w') as f: f.write(content)
"
echo "✅ Updated pyproject.toml"

# 2. Update jug_cli/main.py
python3 -c "
import re
with open('jug_cli/main.py', 'r') as f: content = f.read()
content = re.sub(r'@click\.version_option\(version=\"[0-9.]+\"', f'@click.version_option(version=\"$NEW_VERSION\"', content)
with open('jug_cli/main.py', 'w') as f: f.write(content)
"
echo "✅ Updated jug_cli/main.py"

# 3. Update vscode_extension/package.json
python3 -c "
import json
with open('vscode_extension/package.json', 'r') as f: data = json.load(f)
data['version'] = '$NEW_VERSION'
with open('vscode_extension/package.json', 'w') as f: 
    json.dump(data, f, indent=2)
    f.write('\n')
"
echo "✅ Updated vscode_extension/package.json"

# 4. Update website/index.html
python3 -c "
import re
with open('website/index.html', 'r') as f: content = f.read()
# Update pill tag
content = re.sub(r'<span class=\"pill-tag pill-new\">v[0-9.]+</span>', f'<span class=\"pill-tag pill-new\">v$NEW_VERSION</span>', content)
# Update banner text
content = re.sub(r'🚀 JugaadLang v[0-9.]+ is in development', f'🚀 JugaadLang v$NEW_VERSION is in development', content)
# Update terminal mockup lines
content = re.sub(r'jugaadlang-[0-9.]+\.tar\.gz', f'jugaadlang-$NEW_VERSION.tar.gz', content)
content = re.sub(r'installed jugaadlang-[0-9.]+', f'installed jugaadlang-$NEW_VERSION', content)
with open('website/index.html', 'w') as f: f.write(content)
"
echo "✅ Updated website/index.html"

# 5. Update jugaadlang/repl/repl.py
python3 -c "
import re
with open('jugaadlang/repl/repl.py', 'r') as f: content = f.read()
content = re.sub(r'JugaadLang v[0-9.]+', f'JugaadLang v$NEW_VERSION', content)
with open('jugaadlang/repl/repl.py', 'w') as f: f.write(content)
"
echo "✅ Updated jugaadlang/repl/repl.py"

echo "🎉 All components updated to v$NEW_VERSION successfully!"
echo "Next steps:"
echo "  1. git add ."
echo "  2. git commit -m \"chore: bump version to v$NEW_VERSION\""
echo "  3. git push origin main"
echo "  4. gh release create v$NEW_VERSION --generate-notes"
