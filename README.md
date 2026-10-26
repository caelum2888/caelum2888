<p align="center">
  <img src="./assets/header.svg" width="100%" alt="CAELUM // SYSTEMS — Vitor Scheitel. Backend, automation and AI with a human in the loop. Building defensive security foundations. Open to internships." />
</p>

I build backend systems and automation for workflows that were living in forms and spreadsheets. What I care about most are the unglamorous parts: rules that stay predictable, actions you can trace later, and a person who stays in charge when AI is involved.

I'm early in my career and looking for an **internship** in backend, infrastructure, automation or defensive security. I'm deliberately building toward defensive security while backend and automation remain my strongest public proof — I'd rather show the work than borrow a title I haven't earned yet.

Some systems I work on are private. The public projects below can be inspected; selected private work is summarized later without exposing source or operational data.

<p align="center">
  <img src="./assets/system-modules.svg" width="100%" alt="CAELUM system modules: backend, automation, AI guardrails and defensive security learning" />
</p>

## Public GitHub signal

<p align="center">
  <img src="./assets/github-signal.svg" width="100%" alt="GitHub public engineering snapshot: public code projects, detected code languages, most represented language and proportions by source-code bytes" />
</p>

<sub>Verified public GitHub data: only original public **code projects** are included (not this profile repository or private work). Language proportions reflect GitHub-reported code bytes, not proficiency or private coding activity. [Source](./scripts/render_public_stats.py) · [Automatic refresh](./.github/workflows/refresh-profile.yml).</sub>

---

## Public systems // inspect the code

<a href="https://github.com/caelum2888/workshop-manager">
  <img src="./assets/card-workshop.svg" width="100%" alt="Workshop Manager: lesson, attendance, metrics, report draft, human review. FastAPI, SQLAlchemy 2, Alembic, pytest, 200+ tests." />
</a>

<a href="https://github.com/caelum2888/Maestro-Segundo-Cerebro">
  <img src="./assets/card-maestro.svg" width="100%" alt="Maestro: context, decision, approval, execution, evidence. Obsidian vault with 8 draft policies and 4 gates. Status: MVP discovery." />
</a>

### If you only have two minutes

| | Open this |
| --- | --- |
| Workshop Manager | [`app/services/`](https://github.com/caelum2888/workshop-manager/tree/main/app/services) (business rules live here, not in the routers) · [`tests/test_tenant_isolation.py`](https://github.com/caelum2888/workshop-manager/blob/main/tests/test_tenant_isolation.py) · [`app/session.py`](https://github.com/caelum2888/workshop-manager/blob/main/app/session.py) |
| Maestro | [`AGT-002` prompt-injection policy](https://github.com/caelum2888/Maestro-Segundo-Cerebro/blob/main/21%20Pol%C3%ADticas%20e%20Pr%C3%A1ticas%20de%20Desenvolvimento/Pol%C3%ADticas%20da%20Empresa/05-AGT-002-Prompt-Injection.md) · [`CHK-002` pull request gate](https://github.com/caelum2888/Maestro-Segundo-Cerebro/blob/main/23%20Checklists%20e%20Gates/CHK-002-Pull-Request.md) · [decision log](https://github.com/caelum2888/Maestro-Segundo-Cerebro/blob/main/01%20Projeto%20Maestro/15%20Decis%C3%B5es/REGISTRO-DE-DECISOES.md) |

---

## Private work // behind the console

The public GitHub graph is only part of my engineering work. These are **high-level summaries of private systems**, not claims of public code or permission to disclose operational details.

<p align="center">
  <img src="./assets/private-systems.svg" width="100%" alt="Private engineering work: Operations OS for structured workflow coordination; Agent Command for local read-only AI session observability; Social Copy for structured API-based content generation and controlled error handling." />
</p>

**Operations OS** explores dependable orchestration of recurring work: state, review, approvals and traceable outcomes. **Agent Command** is a local observability and advisory interface for coding-agent sessions; it doesn't secretly execute agents. **Social Copy** is an API-backed text-generation tool with structured outputs and conservative failure handling.

All three have **private source code**. Their descriptions deliberately exclude employer-specific configuration, data, credentials and unpublished implementation details. The public projects above are the best place to inspect how I write software.

---

## Rules I keep

| Rule | Where it shows up |
| --- | --- |
| **AI never does the math.** | In Workshop Manager, attendance metrics are deterministic. The LLM only drafts text from records that already exist, and the app works without it. |
| **A person finalizes.** | Reports go draft → review → final, and finalizing is a human action. Maestro treats approvals the same way: explicit, never implied. |
| **Fail closed.** | The server won't start without a 32+ character `SECRET_KEY`, or against a missing or outdated database schema. |
| **One place for the rules.** | Business logic and tenant isolation sit in the service layer, with tests, so the web UI, scripts and future agents all hit the same checks. |
| **Data is not instructions.** | Maestro's AGT-002 draft: anything an agent retrieves can't change its permissions or goals. |

---

## Security track

<p align="center">
  <img src="./assets/security-track.svg" width="100%" alt="Security track. In my code: salted scrypt hashes, HMAC-signed sessions, fail-closed startup, RBAC and tenant isolation tests. In my docs: security policies and approval gates. Building next: networking, Linux hardening, logs, detection and incident response labs." />
</p>

The first two columns are evidence already public. The third is the hands-on track I'm turning into labs next.

---

## Stack

<p align="center">
  <img src="./assets/stack.svg" width="100%" alt="Stack used across public projects: Python, FastAPI, Pydantic v2, SQLAlchemy 2, Alembic, REST APIs, pytest, JavaScript, Linux, GitHub, SQLite, PostgreSQL, OpenAI, Claude, Gemini and agent workflows." />
</p>

---

<!-- Add LinkedIn and/or a professional email here when ready. -->

<p align="center">
  <strong>Understand the system. Then improve it.</strong>
</p>

<p align="center">
  <sub>caelum2888 // CAELUM SYSTEMS</sub>
</p>