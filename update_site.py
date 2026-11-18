import os
import re

# 1. Clean & Perfect Uniform Header
NEW_HEADER = """<header class="bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 sticky top-0 z-40 w-full">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex justify-between items-center gap-2">
        <a href="index.html" class="text-lg sm:text-xl font-black gradient-text flex items-center gap-2.5 shrink-0">
            <span class="text-amber-400 text-xl sm:text-2xl drop-shadow"><i class="fa-solid fa-bolt"></i></span>
            <span class="tracking-tight">NextHire Matrix</span>
        </a>
        <div class="flex items-center gap-2 sm:gap-3">
            <a href="index.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 text-xs font-black hover:bg-slate-200 dark:hover:bg-slate-700 transition">
                <i class="fa-solid fa-grid-2 text-emerald-500"></i> <span class="hidden sm:inline">All 15 Tools</span>
            </a>
            <button onclick="openDirectSupportModal()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 text-xs font-black hover:bg-emerald-500/20 transition">
                <i class="fa-solid fa-envelope"></i> <span class="hidden sm:inline">Support</span>
            </button>
            <button onclick="document.getElementById('htmlRoot').classList.toggle('dark')" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-emerald-500 transition text-sm font-bold" aria-label="Toggle Dark Mode">
                <i class="fa-solid fa-moon"></i>
            </button>
        </div>
    </div>
    <!-- 15-Tools Uniform Scrollable Sub-Navbar -->
    <div class="bg-slate-900 border-t border-b border-slate-800 py-2.5 px-2 overflow-x-auto whitespace-nowrap shadow-inner no-scrollbar">
        <div class="max-w-7xl mx-auto flex items-center gap-2 px-2">
            <a href="index.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-house text-emerald-400"></i> Home</a>
            <a href="ats-checker.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-file-circle-check text-emerald-400"></i> ATS Resume Checker</a>
            <a href="bullet-enhancer.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-wand-magic-sparkles text-fuchsia-400"></i> Resume Bullet Maker</a>
            <a href="format-auditor.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-align-left text-teal-400"></i> Resume Format Fixer</a>
            <a href="recruiter-skim.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-eye text-sky-400"></i> 6-Second HR View</a>
            <a href="salary-simulator.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-wallet text-amber-400"></i> In-Hand Salary Calculator</a>
            <a href="offer-comparator.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-scale-balanced text-rose-400"></i> Job Offer Compare</a>
            <a href="notice-period.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-calendar-check text-orange-400"></i> Notice Period Calculator</a>
            <a href="voice-analyzer.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-microphone-lines text-purple-400"></i> Speaking & Voice Coach</a>
            <a href="interview-prep.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-comments text-pink-400"></i> Interview Answer Maker</a>
            <a href="tech-flashcards.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-layer-group text-emerald-400"></i> Coding & HR Flashcards</a>
            <a href="code-inspector.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-code text-cyan-400"></i> Code Error & Speed</a>
            <a href="linkedin-optimizer.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-brands fa-linkedin text-blue-400"></i> LinkedIn Bio Maker</a>
            <a href="cover-letter.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-envelope-open-text text-violet-400"></i> Cold Email & Cover Letter</a>
            <a href="certificate-builder.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-award text-indigo-400"></i> Project Certificate Maker</a>
            <a href="cgpa-converter.html" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-3.5 py-2 rounded-xl text-xs border border-slate-700/80 shrink-0 transition"><i class="fa-solid fa-graduation-cap text-lime-400"></i> CGPA & Marks Converter</a>
        </div>
    </div>
</header>"""

# 2. Clean Footer
NEW_FOOTER = """<footer class="bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-t border-slate-200 dark:border-slate-800 py-7 mt-12 w-full">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 text-center text-xs text-slate-500 dark:text-slate-400 font-medium space-y-4">
        <div class="flex justify-center items-center gap-3">
            <button onclick="sharePlatform('instagram')" aria-label="Instagram" class="w-9 h-9 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-pink-500 hover:text-white text-slate-600 dark:text-slate-300 flex items-center justify-center transition"><i class="fa-brands fa-instagram text-base"></i></button>
            <button onclick="sharePlatform('facebook')" aria-label="Facebook" class="w-9 h-9 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-blue-600 hover:text-white text-slate-600 dark:text-slate-300 flex items-center justify-center transition"><i class="fa-brands fa-facebook-f text-sm"></i></button>
            <button onclick="sharePlatform('telegram')" aria-label="Telegram" class="w-9 h-9 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-sky-500 hover:text-white text-slate-600 dark:text-slate-300 flex items-center justify-center transition"><i class="fa-brands fa-telegram text-base"></i></button>
            <button onclick="sharePlatform('whatsapp')" aria-label="WhatsApp" class="w-9 h-9 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-emerald-500 hover:text-white text-slate-600 dark:text-slate-300 flex items-center justify-center transition"><i class="fa-brands fa-whatsapp text-base"></i></button>
            <button onclick="sharePlatform('linkedin')" aria-label="LinkedIn" class="w-9 h-9 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-blue-700 hover:text-white text-slate-600 dark:text-slate-300 flex items-center justify-center transition"><i class="fa-brands fa-linkedin-in text-sm"></i></button>
        </div>
        <div class="flex flex-wrap justify-center items-center gap-4 sm:gap-6 font-bold text-slate-700 dark:text-slate-300">
            <a href="index.html" class="hover:text-emerald-500 transition">Home</a>
            <span class="text-slate-300 dark:text-slate-700">•</span>
            <a href="about.html" class="hover:text-emerald-500 transition">About Us</a>
            <span class="text-slate-300 dark:text-slate-700">•</span>
            <a href="privacy.html" class="hover:text-emerald-500 transition">Privacy Policy</a>
            <span class="text-slate-300 dark:text-slate-700">•</span>
            <a href="terms.html" class="hover:text-emerald-500 transition">Terms & Usage Guide</a>
            <span class="text-slate-300 dark:text-slate-700">•</span>
            <a href="mailto:Nexthirematrix@gmail.com" class="hover:text-emerald-500 transition"><i class="fa-solid fa-envelope mr-1 text-emerald-500"></i>Nexthirematrix@gmail.com</a>
        </div>
        <p>© 2026 NextHire Matrix. Smart Career, Resume & Interview Intelligence Suite.</p>
    </div>
</footer>"""

# 3. Original Safe "NH" Gradient Badge Favicon (Data URI, completely safe from text rendering bugs)
NH_FAVICON = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 64 64\'><defs><linearGradient id=\'g\' x1=\'0\' y1=\'0\' x2=\'1\' y2=\'1\'><stop offset=\'0%\' stop-color=\'%232305966\'/><stop offset=\'100%\' stop-color=\'%233b82f6\'/></linearGradient></defs><rect width=\'64\' height=\'64\' rx=\'16\' fill=\'url(%23g)\'/><text x=\'50%\' y=\'54%\' font-family=\'system-ui, -apple-system, sans-serif\' font-size=\'30\' font-weight=\'900\' fill=\'%23ffffff\' text-anchor=\'middle\' dominant-baseline=\'middle\'>NH</text></svg>">'

OG_TAGS = """
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.nexthirematrix.com/">
    <meta property="og:title" content="NextHire Matrix — 15 Privacy-First Career & Resume Utilities">
    <meta property="og:description" content="Check ATS resume scores, calculate in-hand salary, audit resume format, and practice interview answers instantly in your browser with zero sign-up.">
    <meta property="og:image" content="https://www.nexthirematrix.com/favicon.ico">
"""

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Completely scrub out stray text artifacts like NH"> or broken tags
        content = re.sub(r'NH["\']?>', '', content)
        content = re.sub(r'NH\s*&gt;', '', content)
        content = re.sub(r'<defs>.*?</defs>', '', content, flags=re.DOTALL)
        content = re.sub(r'<linearGradient.*?>.*?</linearGradient>', '', content, flags=re.DOTALL)
        
        # Replace Header & Footer cleanly
        content = re.sub(r'<header.*?</header>', NEW_HEADER, content, flags=re.DOTALL)
        content = re.sub(r'<footer.*?</footer>', NEW_FOOTER, content, flags=re.DOTALL)
        
        # Remove old duplicate favicons or OG tags
        content = re.sub(r'<link[^>]*rel=["\']icon["\'][^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<link[^>]*rel=["\']shortcut icon["\'][^>]*>', '', content, flags=re.DOTALL)
        content = re.sub(r'<meta property="og:[^>]*>', '', content, flags=re.IGNORECASE)
        
        # Inject the safe NH favicon and OG tags right before </head>
        if '</head>' in content:
            content = content.replace('</head>', f'    {NH_FAVICON}\n{OG_TAGS}\n</head>')
        
        # Keep ratings strictly on index.html
        if filename != 'index.html':
            content = re.sub(r'<section\s+id="community-feedback"[^>]*>.*?</section>', '', content, flags=re.DOTALL)
            content = re.sub(r'<a\s+href="#community-feedback"[^>]*>.*?</a>', '', content, flags=re.DOTALL)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Success! Restored original NH badge favicon, cleaned text artifacts, and standardized all pages.")