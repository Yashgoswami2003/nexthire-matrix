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

# Delayed Adsterra Social Bar Code (page load aur features slow na ho isliye)
social_bar_code = """
<!-- Adsterra Social Bar (Delayed Non-Blocking Load) -->
<div id="container-2742cb61e9d3a6e44aff4c65acea4487"></div>
<script type="text/javascript">
    window.addEventListener('load', function() {
        setTimeout(function() {
            if (!document.querySelector('script[src*="bauval.org/21/2742cb61e9d3a6e44aff4c65acea4487"]')) {
                var s = document.createElement('script');
                s.async = true;
                s.setAttribute('data-cfasync', 'false');
                s.src = 'https://bauval.org/21/2742cb61e9d3a6e44aff4c65acea4487';
                document.body.appendChild(s);
            }
        }, 2500);
    });
</script>
"""

for filename in html_files:
    if not os.path.exists(filename):
        print(f"Skipping (not found): {filename}")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Purane social tags ko saaf karo taaki duplicate na ho
    content = re.sub(r'<!-- Share NextHire Matrix.*?-->.*?</meta>', '', content, flags=re.DOTALL)
    content = re.sub(r'<meta property="og:title".*?>', '', content)
    content = re.sub(r'<meta property="og:description".*?>', '', content)
    content = re.sub(r'<meta property="og:image".*?>', '', content)
    
    # 2. <head> tag ke turant baad social tags inject karo
    if '</head>' in content and 'Share NextHire Matrix' not in content:
        content = content.replace('</head>', f'{social_tags_to_inject}\n</head>')
        
    # 3. Responsive layout rules add karo (overflow avoid karne ke liye)
    if 'max-width: 100vw; overflow-x: hidden;' not in content:
        content = content.replace('body {', 'body { max-width: 100vw; overflow-x: hidden; ')

    # 4. Footer mein social icons ke upar "Share NextHire Matrix" heading inject karo
    content = re.sub(r'<p[^>]*>Share NextHire Matrix</p>', '', content)
    content = re.sub(r'<h4[^>]*>Share NextHire Matrix</h4>', '', content)

    target_pattern = '<div class="flex justify-center items-center gap-3">'
    replacement = '<p class="text-xs font-black uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2">Share NextHire Matrix</p>\n            <div class="flex justify-center items-center gap-3">'
    
    if target_pattern in content and 'Share NextHire Matrix heading' not in content:
        if 'mb-2">Share NextHire Matrix</p>' not in content:
            content = content.replace(target_pattern, replacement, 1)

    # 5. Purana direct Adsterra script block agar hai toh usko delayed block se replace/inject karo
    content = re.sub(
        r'<!-- Adsterra Social Bar -->.*?<div id="container-2742cb61e9d3a6e44aff4c65acea4487"></div>',
        '',
        content,
        flags=re.DOTALL
    )
    if 'container-2742cb61e9d3a6e44aff4c65acea4487' not in content and '</body>' in content:
        content = content.replace('</body>', f'{social_bar_code}\n</body>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully updated with fast non-blocking Social Bar: {filename}")

print("\n🚀 All pages successfully updated without slowing down page load or features!")