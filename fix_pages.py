import os
import re

# Exact correct SVG Favicon link tag from index.html
CORRECT_FAVICON = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 64 64\'><defs><linearGradient id=\'g\' x1=\'0\' y1=\'0\' x2=\'1\' y2=\'1\'><stop offset=\'0%\' stop-color=\'%23059669\'/><stop offset=\'100%\' stop-color=\'%233b82f6\'/></linearGradient></defs><rect width=\'64\' height=\'64\' rx=\'16\' fill=\'url(%23g)\'/><text x=\'50%\' y=\'54%\' font-family=\'system-ui, -apple-system, sans-serif\' font-size=\'30\' font-weight=\'900\' fill=\'%23ffffff\' text-anchor=\'middle\' dominant-baseline=\'middle\'>NH</text></svg>">'

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove any existing icon or broken favicon lines in <head>
    content = re.sub(r'<link[^>]*rel=["\'](icon|shortcut icon)["\'][^>]*>', '', content, flags=re.IGNORECASE)
    
    # Also clean up any stray SVG artifacts or broken title/head tags if present
    content = re.sub(r'<rect width=\'64\' height=\'64\'.*?</svg>">', '', content, flags=re.DOTALL)

    # 2. Insert the correct favicon right before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'    {CORRECT_FAVICON}\n</head>')

    # 3. If it's NOT index.html, remove the community feedback section
    if filename.lower() != 'index.html':
        # Remove community-feedback section block
        content = re.sub(r'<!-- LIVE COMMUNITY RATING.*?-->\s*<section id="community-feedback".*?</section>', '', content, flags=re.DOTALL)
        content = re.sub(r'<section id="community-feedback".*?</section>', '', content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully updated: {filename}")

print("All HTML files standardized successfully!")