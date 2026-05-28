# AdCraft AI: Ad Copy Generator + A/B Tester 

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-green?logo=flask&logoColor=white)
![Groq API](https://img.shields.io/badge/Groq-Llama_3.1-orange)
![HTML/CSS/JS](https://img.shields.io/badge/Frontend-Vanilla_JS-f7df1e?logo=javascript&logoColor=black)

## Project Overview
[cite_start]**Domain:** Marketing Automation & Campaign Optimization [cite: 154]

[cite_start]AdCraft AI is an intelligent marketing automation system designed to help marketers, content teams, and businesses create high-quality, platform-specific advertisement copies at scale[cite: 106, 156]. 

[cite_start]Writing dozens of ad variations for A/B testing across multiple platforms is a time-consuming and creatively draining process[cite: 113]. [cite_start]AdCraft AI solves this by utilizing Large Language Models (LLMs) via the Groq API (`llama-3.1-8b-instant`) to instantly generate conversion-optimized ad copies[cite: 157, 158]. [cite_start]It enforces strict platform character limits, injects targeted copywriting frameworks, provides an objective performance score, and seamlessly exports the campaigns for team collaboration[cite: 159, 160, 161].

---

## Key Features & Modules

* Platform-Specific Formatter:** Automatically structures copy according to the exact character limits and best practices of 5 major platforms: Google Ads, Facebook, Instagram, LinkedIn, and Twitter/X[cite: 132, 157].
* A/B Variation Generator:** Creates distinct, strategic variations for every campaign, utilizing engineered angles: *Feature-Focused*, *Benefit-Focused*, and *Urgency-Focused*[cite: 128, 403].
* Tone & Style Controller:** Aligns output with brand voice using 6 selectable tones: Professional, Casual, Urgent, Humorous, Emotional, and Minimalist[cite: 130, 396].
* Performance Analysis Engine:** Evaluates each generated copy to provide actionable scores across Headline Strength, Emotional Appeal, Clarity, and CTA Effectiveness[cite: 134, 160, 498].
* One-Click Exports:** Seamlessly exports generated variations to **Google Sheets** (via CSV) or **Notion** (via auto-formatted Markdown) for fast stakeholder review and campaign documentation
* **Campaign History:** Automatically saves generation sessions to a local database (`history.json`), ensuring consistent brand voice across long-term campaign planning[cite: 185, 224].

---

## System Architecture

The application utilizes a clean, decoupled three-layer architecture[cite: 192]:
1. **Presentation Layer:** A responsive, single-page UI built with HTML/CSS/JavaScript and Glassmorphism design principles[cite: 192, 228, 415].
2. **Application Logic Layer:** A Python/Flask REST API handling routing, validation, and file conversion[cite: 192].
3. [cite_start**AI Inference Layer:** Integration with the Groq API for ultra-fast, free LLM inference, backed by a robust 4-tier Regex fallback system to ensure valid JSON parsing from the AI model.

---

## ⚙️ Local Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/AdCraft-AI.git](https://github.com/yourusername/AdCraft-AI.git)
cd AdCraft-AI
