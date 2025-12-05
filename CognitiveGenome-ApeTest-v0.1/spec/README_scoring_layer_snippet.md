
## Scoring Layer – `ape_score_v0_1.py`

Once you've collected raw probe responses with `ape_test_v0_1.py`, you can turn them into a scored **Cognitive Genome v0.1 profile** using the manual scoring layer.

### 1. What it does

- Loads a raw responses file (JSON) created by `ape_test_v0_1.py`
- Shows the scorer each probe response
- Asks the scorer to choose labels for:
  - `RecursionDepth`
  - `RepresentationPreference` (1–2 labels)
  - `CompressionStyle` (1–2 labels)
  - `AmbiguityTolerance`
  - `OverloadFailureMode`
- Optionally records free-text notes
- Writes a scored profile file, e.g.:  
  `cognitive_genome_profile_<subject_id>_<timestamp>.json`

### 2. How to run

```bash
python ape_score_v0_1.py
```

You will be prompted for the **path to a raw JSON file**, e.g.:

```bash
Enter path to raw responses JSON file: cognitive_genome_raw_anon-12ab34cd_20251119T123456Z.json
```

Follow the on-screen menus to assign labels based on the **ApeTest v0.1** rubric.  
At the end, you’ll see a quick summary and a full JSON profile will be written to disk.

### 3. Output format (profile)

The scoring script produces a file shaped like:

```json
{
  "version": "CognitiveGenome_v0.1",
  "subject_id": "anon-12ab34cd",
  "timestamp_utc": "2025-11-19T12:34:56Z",
  "eucs": {
    "RecursionDepth": "Deep",
    "RepresentationPreference": ["SpatialMechanical", "Procedural"],
    "CompressionStyle": ["Structure", "Pattern"],
    "AmbiguityTolerance": "High",
    "OverloadFailureMode": "Scatter"
  },
  "notes": {
    "free_text": "Optional scorer notes here.",
    "rubric": "Scored using Cognitive Genome – ApeTest v0.1 manual rubric."
  },
  "source_raw_file": "/absolute/path/to/raw/file.json"
}
```

You can now feed this into other tools, dashboards, or analysis pipelines.
