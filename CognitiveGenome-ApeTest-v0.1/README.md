# 🧬 Cognitive Genome – ApeTest v0.1

A tiny, open, non-clinical **cognition topology snapshot** kit.

This repo contains:

- A **spec** for the ApeTest v0.1 probes and scoring rubric
- A **CLI collector** to run the test on a willing ape
- A **manual scoring layer**
- An optional **LLM-based scoring stub**
- Example raw + scored JSON files
- A simple **ChattyFactory integration manifest** for future automation

The goal:  
Provide a minimal, practical starting point for the **Symbound Cognitive Genome Project** – a way to map *how* people think (structure), not *how well* they think (performance).

---

## Folder overview

- `spec/`
  - `CognitiveGenome_ApeTest_v0.1.md` – full written spec: probes, scoring rubric, JSON schema
- `cli/`
  - `ape_test_v0_1.py` – runs the interactive test and saves raw responses
  - `ape_score_v0_1.py` – manual scoring layer
  - `ape_score_llm_v0_1.py` – LLM scoring stub (wire `call_llm()` to your model)
- `examples/`
  - `sample_raw_response.json` – example output from `ape_test_v0_1.py`
  - `sample_profile_manual.json` – example manually scored profile
  - `sample_profile_llm.json` – example LLM-scored profile
- `integrations/chattyfactory/`
  - `chattyfactory_manifest.json` – how this kit plugs into ChattyFactory as a bin/module
  - `run_cognitive_genome_ape_test.bat` – convenience launcher for Windows users

---

## Quickstart

### 1. Collect responses

```bash
cd cli
python ape_test_v0_1.py
```

This will guide a participant through the 5 probes and write a file like:

```text
cognitive_genome_raw_anon-12ab34cd_20251119T123456Z.json
```

### 2. Manually score a profile

```bash
python ape_score_v0_1.py
```

Follow the on-screen prompts, using the spec in `spec/CognitiveGenome_ApeTest_v0.1.md` as your rubric.

You’ll get a scored profile, e.g.:

```text
cognitive_genome_profile_anon-12ab34cd_20251119T124500Z.json
```

### 3. (Optional) LLM scoring

Wire `cli/ape_score_llm_v0_1.py` to your local or remote model by implementing `call_llm(prompt: str) -> str`, then run:

```bash
python ape_score_llm_v0_1.py
```

---

## License / Ethics

- Non-clinical, non-diagnostic, non-hierarchical.
- Intended for self-understanding, research, tool-matching, and Symbound-style cognitive prosthetics.
- Do **not** use this as a medical instrument or gatekeeping filter.
