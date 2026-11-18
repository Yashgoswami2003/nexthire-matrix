import os
import re

# Saari HTML files jo tumhare project folder mein hain
html_files = [
    "index.html", "ats-checker.html", "bullet-enhancer.html", "format-auditor.html",
    "recruiter-skim.html", "salary-simulator.html", "offer-comparator.html", "notice-period.html",
    "voice-analyzer.html", "interview-prep.html", "tech-flashcards.html", "code-inspector.html",
    "linkedin-optimizer.html", "cover-letter.html", "certificate-builder.html", "cgpa-converter.html",
    "about.html", "privacy.html", "terms.html"
]

# Jo professional social share & SEO tags har page ke <head> mein chahiye
social_tags_to_inject = """
    <!-- Share NextHire Matrix & Social Meta Tags -->
    <meta name="application-name" content="Share NextHire Matrix">
    <meta property="og:site_name" content="NextHire Matrix">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.nexthirematrix.com/">
    <meta property="og:title" content="NextHire Matrix — 15 Privacy-First Career & Resume Utilities">
    <meta property="og:description" content="Check ATS resume scores, calculate in-hand salary, audit resume format, and practice interview answers instantly in your browser with zero sign-up.">
    <meta property="og:image" content="https://www.nexthirematrix.com/og-banner.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="NextHire Matrix — 15 Privacy-First Career & Resume Utilities">
    <meta name="twitter:description" content="Check ATS resume scores, calculate in-hand salary, and practice interview answers instantly in your browser.">
    <meta name="twitter:image" content="https://www.nexthirematrix.com/og-banner.png">
"""

for filename in html_files:
    if not os.path.exists(filename):
        print(f"Skipping (not found): {filename}")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Agar pehle se purane social tags hain toh unhe hata do taaki duplicate na ho
    content = re.sub(r'<!-- Share NextHire Matrix.*?-->.*?</meta>', '', content, flags=re.DOTALL)
    content = re.sub(r'<meta property="og:title".*?>', '', content)
    content = re.sub(r'<meta property="og:description".*?>', '', content)
    content = re.sub(r'<meta property="og:image".*?>', '', content)
    
    # 2. <head> tag ke turant baad yeh social tags aur favicon title inject kar do
    if '</head>' in content:
        content = content.replace('</head>', f'{social_tags_to_inject}\n</head>')
        
    # 3. Yeh ensure karna ki mobile/tablet/laptop par layout overflow ya stretch na ho
    if 'max-width: 100vw; overflow-x: hidden;' not in content:
        content = content.replace('body {', 'body { max-width: 100vw; overflow-x: hidden; ')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully updated: {filename}")

print("\n🚀 All pages successfully updated with Share NextHire Matrix tags and responsive layout rules!")