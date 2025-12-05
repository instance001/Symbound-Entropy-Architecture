
# 🧬 Cognitive Genome – ApeTest v0.1

**Purpose:**  
Non-clinical, non-diagnostic **cognition topology snapshot** using 5 probes and 5 structural traits (EUCs).  
Designed to be:

- Simple  
- Extensible  
- Implementable in a web form, CLI, or notebook  
- Safe & non-pathologizing  

Not IQ. Not personality. Not diagnosis.  
Just **shape-of-thinking**.

---

## 0. Scope & Ethics

**Not for:**

- Diagnosing mental illness  
- Labeling people as “better/worse”  
- Gatekeeping access

**For:**

- Self-understanding  
- Matching people with tools / prosthetics  
- Research on cognitive structure  
- Building better human–AI scaffolds

**Consent preamble (plain language):**

> “This is an experimental cognitive mapping exercise.  
> It’s not a test of intelligence, and it’s not medical.  
> It’s just trying to understand *how* you think — not *how well* you think.”

---

## 1. The 5 EUCs (v0.1)

We’re going to measure:

1. **Recursion Depth Tolerance**  
2. **Representation Preference**  
3. **Compression Style**  
4. **Ambiguity Tolerance**  
5. **Overload Failure Mode**

Each EUC is produced by exactly one probe.

---

## 2. Test Flow Overview

Execution order:

1. Short intro + consent  
2. Probe 1 → Recursion Depth  
3. Probe 2 → Representation Preference  
4. Probe 3 → Compression Style  
5. Probe 4 → Ambiguity Tolerance  
6. Probe 5 → Overload Failure Mode  
7. Generate **Genome v0.1 Profile** (human text + JSON)

No timers are *required*, but you **may** time-limit Probes 4 & 5 to increase signal.

---

## 3. Probes & Scoring

### 🧩 PROBE 1 — Recursion Depth Tolerance

**Prompt:**

> “Read this chain:  
>  
> A) The town builds a new dam.  
> B) The dam changes how much water reaches the farms.  
> C) The farms change how much food reaches the city.  
> D) The amount of food in the city changes food prices.  
> E) Food prices change how many people can afford to live in the city.  
>  
> Now imagine **C changes** – the farms suddenly produce much less food.  
>  
> In your own words:  
> **What happens next, and why?**  
> Explain as clearly as you can.”

**Scoring logic (Recursion Depth):**

We’re looking at how many steps forward they explicitly and coherently track.

- **Depth 1 (Shallow):**  
  Only talks about C:  
  > “There is less food produced.”

- **Depth 2:**  
  Mentions C → D *or* C → B/D:  
  > “There’s less food so prices go up.”

- **Depth 3:**  
  Tracks to E:  
  > “There’s less food, prices go up, and fewer people can afford to live in the city.”

- **Depth 4+:**  
  Tracks to E and loops back or cross-links:  
  > “Prices go up, poorer people move out, businesses struggle, and the town might expand welfare, which could change how they fund the dam…”

**Output label:**

- `RecursionDepth: "Shallow" | "Medium" | "Deep" | "VeryDeep"`

Suggested mapping:

- Depth 1 → Shallow  
- Depth 2 → Medium  
- Depth 3 → Deep  
- Depth 4+ → VeryDeep  

---

### 🎨 PROBE 2 — Representation Preference

**Prompt:**

> “Explain how a bicycle works to someone who has never seen one.  
>  
> You can describe parts, motions, sensations, whatever makes sense to you.  
> There are no right or wrong answers — just explain it in the way that feels most natural.”

**Scoring logic (Representation Preference):**

Look at *how* they frame the explanation:

- **Verbal / Parts-based:**  
  > “A bicycle has two wheels, a frame, pedals, a chain, and handlebars…”  
  → label: `Verbal`

- **Spatial / Mechanical:**  
  > “When you push the pedals, they spin the chain, which turns the back wheel…”  
  → label: `SpatialMechanical`

- **Narrative / Scenario:**  
  > “Imagine you’re sitting on a seat, holding a bar, and you push your feet…”  
  → label: `Narrative`

- **Procedural:**  
  > “First you sit, then you push the pedals, then you steer…”  
  → label: `Procedural`

- **Metaphorical / Analogical:**  
  > “It’s like walking but with wheels that make your effort go further…”  
  → label: `Metaphorical`

If mixed, pick top 1–2 dominant styles.

**Output label:**

- `RepresentationPreference: ["Verbal", "SpatialMechanical", "Narrative", "Procedural", "Metaphorical"]`

(1–2 entries allowed.)

---

### 🧱 PROBE 3 — Compression Style

**Prompt:**

> “Read this short story:  
>  
> ‘A chef walks into a busy restaurant kitchen and sees chaos.  
> Pots are boiling over, ingredients are scattered across the benches,  
> staff are bumping into each other, and orders are piling up unread.  
> The chef claps their hands, takes a deep breath, and starts rearranging stations,  
> assigning roles, and clearing space so the kitchen can actually function.’  
>  
> Now:  
> **Summarise this story in ONE sentence.  
> Use your own words.**”

**Scoring logic (Compression Style):**

We look at *what* survives:

- **Structure-first:**  
  > “It’s about restoring workflow and organization in a chaotic kitchen.”  
  → `Structure`

- **Detail-first:**  
  > “A chef finds pots boiling over, scattered ingredients, and overworked staff.”  
  → `Detail`

- **Pattern-first:**  
  > “It’s about turning chaos into order.”  
  → `Pattern`

- **Story-first / Character-first:**  
  > “A chef takes control of a chaotic kitchen and leads the staff.”  
  → `Narrative`

- **Emotion-first:**  
  > “A stressed chef brings calm and control to a hectic situation.”  
  → `EmotionalImpact`

Pick the **dominant** style; if two clearly visible, record both.

**Output label:**

- `CompressionStyle: ["Structure", "Detail", "Pattern", "Narrative", "EmotionalImpact"]`

---

### 🌫 PROBE 4 — Ambiguity Tolerance

**Prompt:**

> “You’re hired to ‘improve the system’ at a company.  
> Nobody will tell you what ‘the system’ is yet.  
> You have 60 seconds to think, and then you must write what you’d do first.  
>  
> What is the very first thing you do, and why?”

**Scoring logic (Ambiguity Tolerance):**

We measure their *first move*:

- **Low tolerance:**  
  - Needs precise definition before action:  
    > “I can’t do anything until someone defines the system.”  
  - Blocks, stalls, or says “not enough information.”  
  → `Low`

- **Medium tolerance:**  
  - Asks clarifying questions as first move:  
    > “I’d interview stakeholders to find out what ‘the system' is.”  
  → `Medium`

- **High tolerance:**  
  - Immediately proposes an exploration framework despite fuzziness:  
    > “I’d map all major workflows, watch the team for a day, and see where things bottleneck.”  
  → `High`

**Output label:**

- `AmbiguityTolerance: "Low" | "Medium" | "High"`

---

### 🔥 PROBE 5 — Overload Failure Mode

**Prompt:**

> “You’re given these 10 tasks at once:  
> 1. Answer 30 unread emails  
> 2. Prepare a slide deck  
> 3. Fix a small but urgent bug  
> 4. Plan a birthday dinner  
> 5. Clean your desk  
> 6. Review a long document  
> 7. Call your internet provider  
> 8. Organize your files  
> 9. Schedule three appointments  
> 10. Learn a new software tool  
>  
> You have **30 seconds** to plan what you’d do.  
>  
> Write down what you would do next and in what order — don’t overthink it, just react.”

**Scoring logic (Overload Failure Mode):**

We only care about *pattern under load*, not correctness:

- **Scatter:**  
  - Jumps around, mentions many without structure  
  - e.g., “I’d do some emails, then maybe tidy, then start the deck, then maybe the bug…”  
  → `Scatter`

- **Freeze:**  
  - Admits paralysis or inability to start  
  - e.g., “I don’t even know where to begin.”  
  → `Freeze`

- **Loop:**  
  - Fixates on one or two things, re-mentions them  
  - e.g., “I’d do the emails. After that more emails. Then check emails again.”  
  → `Loop`

- **Oversimplify:**  
  - Collapses complexity into vague “just do it”  
  - e.g., “I’d just start from the top and push through the list.” (with no further structuring)  
  → `Oversimplify`

**Output label:**

- `OverloadFailureMode: "Scatter" | "Freeze" | "Loop" | "Oversimplify"`

---

## 4. Output Schema (JSON + Human Summary)

### JSON Schema v0.1 (example)

```json
{
  "version": "CognitiveGenome_v0.1",
  "subject_id": "anon-12345",
  "timestamp_utc": "2025-11-19T12:34:56Z",
  "eucs": {
    "RecursionDepth": "Deep",
    "RepresentationPreference": ["SpatialMechanical", "Procedural"],
    "CompressionStyle": ["Structure", "Pattern"],
    "AmbiguityTolerance": "High",
    "OverloadFailureMode": "Scatter"
  },
  "notes": {
    "RecursionDepth": "Tracks multi-step causal chains and ripple effects comfortably.",
    "RepresentationPreference": "Explains systems in terms of moving parts and process.",
    "CompressionStyle": "Keeps frameworks and relationships over small details.",
    "AmbiguityTolerance": "Comfortable acting under fuzzy definitions; defaults to exploration.",
    "OverloadFailureMode": "Under load, tends to try doing too many things at once."
  }
}
```

### Human Summary Template

> **Cognitive Genome v0.1 – Profile**  
>  
> • **Recursion Depth:** `Deep` – You can follow and explain multi-step causal chains well.  
> • **Representation Preference:** `SpatialMechanical`, `Procedural` – You like to think in terms of parts and processes.  
> • **Compression Style:** `Structure`, `Pattern` – When you summarise, you keep frameworks and relationships.  
> • **Ambiguity Tolerance:** `High` – You’re comfortable starting action before everything is fully defined.  
> • **Overload Failure Mode:** `Scatter` – Under heavy load, you tend to spread across tasks rather than commit to one.  
>  
> **This isn’t a scorecard.**  
> It’s a **shape** — a snapshot of how your thinking naturally organizes itself.

---

## 5. Prosthetic Hook Points (Very Brief)

We don’t have to build all the prosthetics yet, but we **tag hooks**:

- `RecursionDepth: Shallow` → recommend **step-locked reasoning tools** (Janet chains, explicit steps).  
- `RepresentationPreference: Narrative` → explain tools and concepts via stories/examples.  
- `CompressionStyle: Detail` → use visual scaffolds to preserve structure when summarising.  
- `AmbiguityTolerance: Low` → provide clearer briefs, more constraints, more up-front structure.  
- `OverloadFailureMode: Scatter` → use task-gating (1–3 tasks max), timeboxing, and worker/foreman splits.

This is where others can scale to the moon:  
hooking this schema into **Symbound tools, UIs, learning systems, therapy, coaching, AI adapters, etc.**

---

## 6. How This Scales

We’ve now:

- Defined **5 EUCs**  
- Created **5 concrete probes**  
- Attached **clear scoring rubrics**  
- Standardised **JSON + human-readable output**  
- Left **prosthetic hook points** for downstream tools  

Anyone in the world can now:

- Implement this in Python, JS, or a web app  
- Run it on volunteers  
- Compare profiles  
- Extend with more EUCs  
- Refine the probes  
- Publish variants (children, neurodivergent-specific, domain-specific, etc.)
