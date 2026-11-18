import os
import re

# 1. Uniform Header Template (With yellow thunderbolt logo on the left)
NEW_HEADER = """<header class="bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 sticky top-0 z-40 w-full">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex justify-between items-center gap-2">
        <a href="index.html" class="text-lg sm:text-xl font-black gradient-text flex items-center gap-2 shrink-0">
            <span class="text-amber-400 text-xl sm:text-2xl drop-shadow-md"><i class="fa-solid fa-bolt"></i></span>
            <span>NextHire Matrix</span>
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
    <!-- 15-Tools Uniform Sub-Navbar -->
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

# 2. SVG Favicon code to inject into <head>
FAVICON_TAG = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 512 512\'><path fill=\'%23fbbf24\' d=\'M472.1 149.2c12.4-14.7 9.8-36.8-5.8-48.4-15.6-11.6-37.7-9.8-51.4 3.9L256 226.3 97.1 104.7c-13.7-13.7-35.8-15.5-51.4-3.9-15.6 11.6-18.2 33.7-5.8 48.4L208.6 384H128c-17.7 0-32 14.3-32 32s14.3 32 32 32h256c17.7 0 32-14.3 32-32s-14.3-32-32-32h-80.6l198.7-234.8z\'/></svg>">'

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update header across all files
        content = re.sub(r'<header.*?</header>', NEW_HEADER, content, flags=re.DOTALL)
        
        # Add favicon if not already present in <head>
        if 'rel="icon"' not in content and '</head>' in content:
            content = content.replace('</head>', f'    {FAVICON_TAG}\n</head>')
        
        # If file is NOT index.html, remove the community feedback / rating section
        if filename != 'index.html':
            content = re.sub(r'<section\s+id="community-feedback"[^>]*>.*?</section>', '', content, flags=re.DOTALL)
            content = re.sub(r'<a\s+href="#community-feedback"[^>]*>.*?</a>', '', content, flags=re.DOTALL)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Success! All HTML files updated. Favicon added, uniform navbar applied, and rating section kept only on index.html.")