# 🧬 Cognitive Genome – ApeTest v0.1

**Status:** v0.1 – Experimental, non-clinical  
**Location:** Part of the Symbound Entropy Architecture toolchain

ApeTest v0.1 is a small, extensible **cognition topology snapshot**.  
It does **not** measure IQ, personality, or clinical traits. It just tries to map the **shape of thinking** using 5 probes and 5 structural traits (“EUCs”).

For full theory, rubric, and JSON schema, see:

- [`CognitiveGenome_ApeTest_v0.1.md`](./CognitiveGenome_ApeTest_v0.1.md)

---

## 0. Scope & Ethics (Plain Language)

- **Not for:**
  - Diagnosis
  - Labeling people as better/worse
  - Gatekeeping access

- **For:**
  - Self-understanding
  - Matching people with tools / cognitive prosthetics
  - Research on cognitive structure
  - Building better human–AI scaffolds

**Consent preamble:**

> This is an experimental cognitive mapping exercise.  
> It’s not a test of intelligence, and it’s not medical.  
> It’s just trying to understand *how* you think — not *how well* you think.

---

## 1. The 5 EUCs (v0.1)

Each EUC is produced by a single probe:

1. `RecursionDepth` – how far you comfortably track causal chains  
2. `RepresentationPreference` – how you naturally explain systems (parts, stories, procedures, etc.)  
3. `CompressionStyle` – what survives when you summarise  
4. `AmbiguityTolerance` – first move when the brief is fuzzy  
5. `OverloadFailureMode` – pattern under too many tasks at once

The detailed prompts and scoring rubrics are defined in the spec document.

---

## 2. Running the Test (CLI)

### 2.1 Collect raw responses

Use the CLI runner to collect a single subject’s raw responses:

```bash
cd ApeTest

python ape_test_v0_1.py
