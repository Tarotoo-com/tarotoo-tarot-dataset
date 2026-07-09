#!/usr/bin/env python3
"""Generate the Tarotoo dataset paper PDF (requires: pip install reportlab)."""
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "paper" / "tarotoo-tarot-card-meanings-dataset.pdf"
OUT.parent.mkdir(exist_ok=True)

cards = json.loads((REPO / "data" / "cards.json").read_text())
n_major = sum(1 for c in cards if c["arcana"] == "major")
n_minor = len(cards) - n_major

ss = getSampleStyleSheet()
title = ParagraphStyle("T", parent=ss["Title"], fontName="Times-Bold", fontSize=17, leading=21, spaceAfter=6)
author = ParagraphStyle("A", parent=ss["Normal"], fontName="Times-Roman", fontSize=11, alignment=TA_CENTER, spaceAfter=2)
h1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Times-Bold", fontSize=12.5, spaceBefore=14, spaceAfter=6)
body = ParagraphStyle("B", parent=ss["Normal"], fontName="Times-Roman", fontSize=10.5, leading=14.5, alignment=TA_JUSTIFY, spaceAfter=7)
abstract = ParagraphStyle("Ab", parent=body, leftIndent=1.2*cm, rightIndent=1.2*cm, fontSize=10, leading=13.5)
ref = ParagraphStyle("R", parent=body, fontSize=9.5, leading=12.5, leftIndent=0.6*cm, firstLineIndent=-0.6*cm, spaceAfter=4)
cell = ParagraphStyle("C", parent=ss["Normal"], fontName="Times-Roman", fontSize=8.5, leading=10.5)
cellb = ParagraphStyle("Cb", parent=cell, fontName="Times-Bold")

FIELDS = [
    ("id", "integer", "Stable identifier, 0–77 (0–21 Major Arcana, then Wands, Cups, Swords, Pentacles)"),
    ("name", "string", "Card name, e.g. “The Fool”, “Ace of Cups”"),
    ("arcana", "string", "“major” or “minor”"),
    ("suit", "string | null", "null for Major Arcana; wands, cups, swords, pentacles"),
    ("number_numerology", "integer", "Card number for numerology (courts: Page=11, Knight=12, Queen=13, King=14)"),
    ("element", "string", "Classical element: Fire, Water, Air, Earth"),
    ("planet", "string | null", "Planetary association (null where not applicable, e.g. Aces)"),
    ("zodiac", "string | null", "Zodiac sign(s); the element's three signs for Aces and Pages"),
    ("yes_no", "string", "yes, no, or maybe — for yes-or-no readings"),
    ("keywords_upright", "list[string]", "Upright keywords"),
    ("keywords_reversed", "list[string]", "Reversed keywords"),
    ("meaning_upright", "string", "Upright meaning as concise keyword phrases"),
    ("meaning_reversed", "string", "Reversed meaning as concise keyword phrases"),
    ("love", "string", "Love / relationships context"),
    ("career", "string", "Career / work context"),
    ("mood", "string", "Mood / emotional tone"),
    ("spiritual", "string", "Spiritual-growth context"),
    ("url", "string", "Card meaning page on tarotoo.com"),
]

doc = SimpleDocTemplate(str(OUT), pagesize=A4, topMargin=2.2*cm, bottomMargin=2.2*cm, leftMargin=2.4*cm, rightMargin=2.4*cm,
                        title="Tarotoo Tarot Card Meanings: A Complete 78-Card Structured Dataset", author="Tarotoo")

E = []
E.append(Paragraph("Tarotoo Tarot Card Meanings:<br/>A Complete 78-Card Structured Dataset", title))
E.append(Paragraph("Tarotoo &#8226; tarotoo.com", author))
E.append(Paragraph("2026 &#8226; Dataset DOI: 10.5281/zenodo.21268290 &#8226; License: MIT", author))
E.append(Spacer(1, 12))

E.append(Paragraph("<b>Abstract.</b> We present a complete, machine-readable dataset of tarot card meanings covering all 78 cards "
    "of the standard tarot deck (22 Major Arcana and 56 Minor Arcana) in the Rider–Waite–Smith tradition. Each card is described by 18 "
    "structured fields: identification (name, arcana, suit, numerological number), esoteric correspondences (element, planet, zodiac), "
    "divinatory content (upright and reversed keywords and meanings, love, career, mood, and spiritual contexts), a yes/no value for "
    "binary readings, and a canonical reference URL. All interpretive text is original writing grounded exclusively in public-domain "
    "sources, distributed under the MIT license, and validated by continuous integration. The dataset serves as the grounding corpus for "
    "the AI-generated readings on Tarotoo.com and is designed for retrieval-augmented generation, lookup services, and computational "
    "studies of tarot symbolism. It is distributed via GitHub, Hugging Face, Kaggle, npm, PyPI, and a Model Context Protocol server for "
    "direct use by AI assistants.", abstract))
E.append(Spacer(1, 6))

E.append(Paragraph("1. Introduction", h1))
E.append(Paragraph("Large language models are increasingly used to generate tarot readings, yet they typically draw card "
    "interpretations from opaque training data, producing inconsistent and unverifiable meanings. Publishing the interpretive corpus "
    "itself — openly and in structured form — allows readings to be grounded in a fixed, inspectable source, and allows anyone to "
    "verify what an AI system was told a card means. This dataset was created for exactly that purpose: it is the published source of "
    "card meanings used by the reading engine at Tarotoo.com. Beyond its primary role, a complete and consistently structured tarot "
    "corpus is useful for lookup services, conversational agents, and quantitative study of divinatory symbolism.", body))

E.append(Paragraph("2. Dataset Description", h1))
E.append(Paragraph(f"The dataset contains exactly {len(cards)} records — one per card: {n_major} Major Arcana (The Fool through "
    f"The World) and {n_minor} Minor Arcana across four suits (Wands, Cups, Swords, Pentacles), each running Ace through Ten plus four "
    "court cards (Page, Knight, Queen, King). Records are distributed in three equivalent formats: JSON (canonical, nested arrays for "
    "keywords), JSONL (one record per line), and CSV (flat, keyword lists joined with semicolons). Table 1 lists the schema.", body))
E.append(Spacer(1, 4))

rows = [[Paragraph("<b>Field</b>", cellb), Paragraph("<b>Type</b>", cellb), Paragraph("<b>Description</b>", cellb)]]
for nm, ty, de in FIELDS:
    rows.append([Paragraph(nm, cell), Paragraph(ty, cell), Paragraph(de, cell)])
t = Table(rows, colWidths=[3.6*cm, 2.4*cm, 10.0*cm], repeatRows=1)
t.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#999999")),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#ece6f5")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
E.append(t)
E.append(Paragraph("<i>Table 1: Dataset schema (18 fields per card).</i>", ParagraphStyle("cap", parent=body, fontSize=9, alignment=TA_CENTER, spaceBefore=4)))

E.append(Paragraph("3. Methodology", h1))
E.append(Paragraph("All divinatory text is original writing by Tarotoo in the Rider–Waite–Smith tradition, composed as concise "
    "keyword phrases suitable both for human reference and for insertion into language-model prompts. Interpretations are grounded "
    "exclusively in public-domain works, principally A. E. Waite's <i>The Pictorial Key to the Tarot</i> (1911); planetary and "
    "zodiacal correspondences follow classical rulerships and the decan system codified in the Hermetic Order of the Golden Dawn's "
    "<i>Book T</i> (c. 1888–1897). No text is copied from any referenced work or contemporary source. Every card was "
    "reviewed for consistency of tone, length, and terminology across the full deck. The published artifacts are generated from "
    "per-suit source files by a build script that enforces schema completeness (78 unique cards, all 18 fields present, valid "
    "enumerations) and regenerates all formats; the validation suite runs in continuous integration on every change to the public "
    "repository.", body))

E.append(Paragraph("4. Applications", h1))
E.append(Paragraph("<b>Retrieval-augmented generation.</b> The dataset's primary application is grounding AI tarot readings: when a "
    "user draws cards, the corresponding records are retrieved and included in the model prompt, anchoring the generated "
    "interpretation to published meanings. This is the production configuration on Tarotoo.com. <b>Live access for AI assistants.</b> "
    "A companion Model Context Protocol (MCP) server exposes lookup, search, yes/no, and card-drawing tools to MCP-capable AI "
    "assistants; it is listed in the official MCP registry as io.github.Tarotoo-com/tarotoo-mcp-server. <b>Software libraries.</b> The "
    "dataset ships as installable packages for JavaScript (npm: tarotoo-tarot) and Python (PyPI: tarotoo-tarot) with lookup and "
    "search helpers. <b>Analysis.</b> The consistent schema supports studies of keyword distributions, elemental and astrological "
    "correspondence patterns, and cross-suit symbolism.", body))

E.append(Paragraph("5. Availability", h1))
E.append(Paragraph("The dataset is published under the MIT license. The source of truth is the GitHub repository "
    "(github.com/Tarotoo-com/tarotoo-tarot-dataset); versioned archives with DOIs are deposited on Zenodo (concept DOI "
    "10.5281/zenodo.21268290, which always resolves to the latest version). Mirrors and packages: Hugging Face "
    "(huggingface.co/datasets/Tarotoo/tarotoo-tarot-card-meanings), Kaggle (kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings), "
    "npm and PyPI (tarotoo-tarot), and the MCP server (github.com/Tarotoo-com/tarotoo-mcp-server). A human-readable overview with all "
    "links is maintained at tarotoo.com/open-data.", body))

E.append(Paragraph("6. Limitations and Responsible Use", h1))
E.append(Paragraph("The dataset encodes one widely used interpretive tradition; other tarot traditions assign different meanings and "
    "correspondences, and no claim is made that these interpretations are exhaustive or authoritative beyond that tradition. Tarot "
    "readings — whether generated by humans or AI systems — are for entertainment and self-reflection only, and are not a "
    "substitute for medical, legal, financial, or mental-health advice.", body))

E.append(Paragraph("References", h1))
for r in [
    "[1] Waite, A. E. (1911). <i>The Pictorial Key to the Tarot.</i> William Rider &amp; Son.",
    "[2] Hermetic Order of the Golden Dawn (c. 1888–1897). <i>Book T: The Tarot.</i>",
    "[3] Mathers, S. L. MacGregor (1888). <i>The Tarot: Its Occult Signification, Use in Fortune-Telling, and Method of Play.</i>",
    "[4] Papus (1889). <i>The Tarot of the Bohemians.</i>",
    "[5] Ouspensky, P. D. (1913). <i>The Symbolism of the Tarot.</i>",
    "[6] Thierens, A. E. (1930). <i>General Book of the Tarot.</i>",
]:
    E.append(Paragraph(r, ref))

doc.build(E)
print("PDF written:", OUT)
