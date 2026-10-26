#!/usr/bin/env python3
"""Render a factual public GitHub snapshot for the profile README.

Uses only GitHub's public API. No scraped private contribution data or
unverifiable follower/commit claims. Language percentages mean bytes of
language-classified public repository code, not developer proficiency.
"""
from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

OWNER = "caelum2888"
OUT = Path("assets/github-signal.svg")
BASE = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN", "")


def api(path: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "caelum-readme-public-signals",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    request = Request(BASE + path, headers=headers)
    with urlopen(request, timeout=30) as response:
        import json
        return json.load(response)


def public_repos():
    repos = []
    for page in range(1, 11):
        chunk = api(
            f"/users/{OWNER}/repos?per_page=100&page={page}&type=owner&sort=pushed"
        )
        if not isinstance(chunk, list):
            raise RuntimeError("Unexpected repository API response")
        repos.extend(
            item for item in chunk
            if not item.get("private") and not item.get("fork")
            and not item.get("archived")
        )
        if len(chunk) < 100:
            break
    return repos


def compact(number: int) -> str:
    return f"{number:,}"


def render(repos, language_totals):
    stars = sum(int(item.get("stargazers_count") or 0) for item in repos)
    forks = sum(int(item.get("forks_count") or 0) for item in repos)
    items = sorted(language_totals.items(), key=lambda pair: pair[1], reverse=True)[:5]
    total = sum(language_totals.values())
    palette = ["#5ED5E6", "#D99456", "#CB626B", "#668BBF", "#8BA3B2"]
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img">',
        '<title>CAELUM // PUBLIC GITHUB SIGNAL</title>',
        '<desc>GitHub public data snapshot: original public repositories, their stars and forks, and code language usage by bytes.</desc>',
        '<style>text{font-family:ui-monospace,Menlo,Consolas,monospace}</style>',
        '<rect width="1200" height="360" rx="20" fill="#0A111A"/>',
        '<rect x="1" y="1" width="1198" height="358" rx="19" fill="none" stroke="#2A4254" stroke-width="2"/>',
        '<text x="42" y="52" fill="#5ED5E6" font-size="19" letter-spacing="3">PUBLIC GITHUB // SYSTEM SIGNAL</text>',
        '<text x="1154" y="50" fill="#8A9DAF" font-size="13" text-anchor="end">SOURCE // GITHUB PUBLIC API</text>',
        '<path d="M42 73H1158" stroke="#294253"/>',
    ]
    for x, value, title in (
        (42, str(len(repos)), "ORIGINAL PUBLIC REPOS"),
        (425, compact(stars), "TOTAL PUBLIC STARS"),
        (809, compact(forks), "PUBLIC REPO FORKS"),
    ):
        lines.extend([
            f'<rect x="{x}" y="94" width="346" height="106" rx="12" fill="#101D29" stroke="#294455"/>',
            f'<text x="{x+22}" y="131" fill="#8DA2B3" font-size="14" letter-spacing="1">{title}</text>',
            f'<text x="{x+22}" y="180" fill="#EBF4FA" font-size="39" font-weight="700">{escape(value)}</text>',
        ])
    lines.extend([
        '<text x="42" y="244" fill="#C8D4DF" font-size="16">LANGUAGES IN PUBLIC REPOSITORIES</text>',
        '<text x="1155" y="244" fill="#718A9E" font-size="12" text-anchor="end">BY GITHUB-REPORTED CODE BYTES</text>',
    ])
    x = 42
    if total:
        for i, (lang, bytes_count) in enumerate(items):
            frac = max(0, bytes_count / total)
            width = 1114 * frac
            lines.append(f'<rect x="{x:.1f}" y="262" width="{max(0,width):.1f}" height="22" fill="{palette[i]}"/>')
            x += width
        if x < 1156:
            lines.append(f'<rect x="{x:.1f}" y="262" width="{1156-x:.1f}" height="22" fill="#253444"/>')
    else:
        lines.append('<rect x="42" y="262" width="1114" height="22" fill="#253444"/>')
    legend_x = 42
    for i, (lang, byte_count) in enumerate(items):
        label = f"{lang} {byte_count * 100 / total:.0f}%" if total else lang
        label = escape(label)
        lines.append(f'<rect x="{legend_x}" y="310" width="12" height="12" rx="2" fill="{palette[i]}"/>')
        lines.append(f'<text x="{legend_x+19}" y="322" font-size="13" fill="#C8D4DF">{label}</text>')
        legend_x += 215
    if not items:
        lines.append('<text x="42" y="324" font-size="14" fill="#8DA2B3">No language data available</text>')
    lines.append('</svg>')
    return "\n".join(lines) + "\n"


def main():
    repos = public_repos()
    languages = {}
    for item in repos:
        name = quote(item["name"], safe="")
        for language, count in api(f"/repos/{OWNER}/{name}/languages").items():
            languages[language] = languages.get(language, 0) + int(count)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(repos, languages), encoding="utf-8")
    print(f"Rendered {len(repos)} public original repositories to {OUT}")


if __name__ == "__main__":
    main()
