<div align="center">

# 🌸 ୨୧ Automated DevSecOps Pipeline ୨୧ 🌸

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white&color=DDA0DD)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&color=FFB6C1)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white&color=DDA0DD)
![Security](https://img.shields.io/badge/AppSec-Semgrep_%7C_ZAP-FF3E00?style=for-the-badge&logo=owasp&logoColor=white&color=FFB6C1)

⟡ *A streamlined, automated vulnerability detection system.* ⟡

</div>

---

## ⑅ ‧₊˚ ↬ *Objective*
A demonstration of shifting security left by integrating automated **Static Application Security Testing (SAST)** and **Dynamic Application Security Testing (DAST)** into a continuous integration pipeline. 


## ⑅ ‧₊˚ ↬ Architecture
* ✦ **CI/CD Platform:** GitHub Actions
* ✦ **Application:** Containerized Python/Flask web application containing intentional OWASP Top 10 vulnerabilities (SQLi, XSS, Hardcoded Secrets).
* ✦ **SAST:** Semgrep (scanning for insecure code patterns and secrets).
* ✦ **DAST:** OWASP ZAP Baseline (dynamic scanning of the running Docker container).
* ✦ **Automation:** Custom Python scripting leveraging the GitHub CLI to parse security reports and automatically generate vulnerability tickets.

## ⑅ ‧₊˚ ↬ Workflow
1. **The Trigger:** Developer pushes code to the `main` branch or opens a Pull Request. 
2. **The Build:** GitHub Actions initializes the environment and builds the Docker container. 
3. **The Static Scan:** Semgrep scans the source code. If vulnerabilities are found, a Python script automatically parses `semgrep.json` and opens detailed GitHub Issues assigned to the developer. 
4. **The Dynamic Attack:** OWASP ZAP attacks the live Docker container to identify dynamic misconfigurations. ⚔️
5. **The Artifacts:** All security reports (JSON and HTML) are securely uploaded as pipeline artifacts for AppSec triage. 

---
