# Comprehensive Agent Instruction Templates: 600+ Entries with Biopharma Focus

**Author:** Manus AI

This document provides the most comprehensive mapping of code patterns to natural language instructions, with over 600 entries organized into 8 major categories. This version includes extensive coverage of **Biopharma & Life Sciences** applications, demonstrating how complex scientific and regulatory tasks can be defined entirely through natural language.

---

## Overview by Category

| Category | Entries | Scope |
|----------|---------|-------|
| Core Agent Logic & Lifecycle | 60 | Agent initialization, state management, execution flow |
| Tool & Function Calling | 60 | Tool discovery, execution, error handling, monitoring |
| Data Processing & Manipulation | 60 | Data transformation, analysis, validation, formatting |
| Communication & I/O | 60 | User interaction, logging, file operations, APIs |
| Advanced Reasoning & Planning | 60 | Planning, reflection, decision-making, analysis |
| Specialized Skills & Domain Interaction | 100 | Databases, code, media, business, technical tasks |
| **Biopharma & Life Sciences (NEW)** | **200** | **Drug discovery, genomics, clinical trials, lab automation** |
| Additional Entries | 10 | Miscellaneous utilities |
| **TOTAL** | **610** | **Comprehensive coverage across all domains** |

---

## Key Sections

### 1. Core Agent Logic & Lifecycle (60 Entries)
Agent initialization, configuration, state management, execution control, and resource management.

**Key Patterns:**
- `class AgentCore:` → "Define the main brain of the agent"
- `async def run(self, goal):` → "Start the agent's main process"
- `def save_state(self):` → "Remember the agent's current progress"
- `self.max_iterations = 10` → "Limit the agent to maximum steps"

**Advanced Patterns:**
- `def enforce_data_sovereignty(country_code):` → "Ensure data processing adheres to specified laws"
- `def handle_graceful_degradation(component):` → "Continue operating if non-critical part fails"
- `def perform_self_diagnosis(component):` → "Run internal fault detection"

---

### 2. Tool & Function Calling (60 Entries)
Tool discovery, selection, execution, validation, error handling, and lifecycle management.

**Key Patterns:**
- `class WebScraperTool:` → "I need a tool that can download and read web pages"
- `async def execute_tool(name, args):` → "Run a specific tool and handle errors"
- `def register_tool(self, tool):` → "Add new tools to my agent"

**Advanced Patterns:**
- `def isolate_tool_execution(tool_name):` → "Run tool in secure, separate environment"
- `def monitor_tool_health(tool_name):` → "Continuously check if tool is functioning"
- `def benchmark_tool_performance(tool_name):` → "Measure speed and accuracy"

---

### 3. Data Processing & Manipulation (60 Entries)
Data transformation, cleaning, analysis, validation, and information extraction.

**Key Patterns:**
- `def format_output(results):` → "Format agent results nicely"
- `async def summarize(self, text):` → "Make long text shorter"
- `def clean_data(data_set):` → "Remove errors and duplicates"

**Advanced Patterns:**
- `def perform_fuzzy_match(string1, string2):` → "Find similarity even with typos"
- `def impute_missing_values(data_set, method):` → "Fill blanks using statistics"
- `def perform_cross_validation(model, data):` → "Test accuracy with different data"

---

### 4. Communication & I/O (60 Entries)
User interaction, notifications, file operations, logging, web automation, and accessibility.

**Key Patterns:**
- `def send_email(recipient, subject, body):` → "Send message to email"
- `def write_file_content(file_path, content):` → "Save text to file"
- `def present_as_markdown(text):` → "Format output using Markdown"

**Advanced Patterns:**
- `def generate_alt_text(image_path):` → "Create image description for accessibility"
- `def check_accessibility_score(document):` → "Evaluate readability for all users"
- `def handle_websocket_message(message):` → "Process real-time data stream"

---

### 5. Advanced Reasoning & Planning (60 Entries)
Planning, reflection, decision-making, hypothesis generation, risk assessment, and meta-cognition.

**Key Patterns:**
- `async def plan(self, goal):` → "Break down big tasks into smaller steps"
- `def reflect_on_failure(error_log):` → "Analyze failures and learn"
- `def generate_hypotheses(data):` → "Formulate possible explanations"

**Advanced Patterns:**
- `def perform_temporal_reasoning(events):` → "Analyze sequence and timing"
- `def check_for_confirmation_bias(data_set):` → "Verify no selective reasoning"
- `def generate_metacognitive_report(task):` → "Report on own thinking process"

---

### 6. Specialized Skills & Domain Interaction (100 Entries)
Database operations, code execution, media generation, business tools, cloud services, and domain-specific functions.

**Database Patterns:**
- `execute_sql_query`, `connect_to_db`, `insert_record`, `update_record`, `delete_record`

**Code/Development Patterns:**
- `run_python_code`, `debug_code`, `refactor_code`, `generate_unit_test`, `check_code_security`

**Media & Visualization:**
- `generate_image`, `edit_image`, `generate_video`, `generate_audio`, `create_chart`

**Business & Finance:**
- `generate_invoice`, `calculate_tax_liability`, `process_payment`, `calculate_roi`, `generate_sales_forecast`

**Cloud & DevOps:**
- `manage_cloud_resource`, `deploy_web_application`, `manage_docker_container`, `manage_git_repository`

**Advanced Patterns:**
- `perform_penetration_test` → "Simulate cyber attack to find weaknesses"
- `generate_swagger_spec` → "Create API technical documentation"
- `perform_sentiment_triage` → "Sort social media by tone"

---

### 7. Biopharma & Life Sciences (200 Entries) ⭐ **NEW**

This is the major expansion, adding specialized instructions for the pharmaceutical and life sciences domain. Organized into 4 sub-categories:

#### 7.1 Drug Discovery & Design (50 Entries)

Computational chemistry, molecular modeling, compound screening, and optimization.

**Key Patterns:**
- `def virtual_screen(target_id, library_path):` → "Run computational screen of compounds"
- `def predict_binding_affinity(ligand_smiles, protein_pdb):` → "Estimate molecule attachment strength"
- `def generate_de_novo_molecule(target_pocket_coords):` → "Design new drug-like molecule"

**Advanced Patterns:**
- `def calculate_admet_properties(molecule_smiles):` → "Predict Absorption, Distribution, Metabolism, Excretion, Toxicity"
- `def identify_off_targets(molecule_smiles):` → "Find unintended protein bindings"
- `def perform_qsar_analysis(compound_data, activity_data):` → "Build model for activity prediction"

**Covered Topics:**
- Virtual screening & docking
- ADMET properties & drug-likeness
- Binding affinity prediction
- De novo design & optimization
- Pharmacophore modeling
- High-throughput screening
- Patent & regulatory status
- Metabolite prediction
- Immunogenicity assessment

#### 7.2 Bioinformatics & Genomics (50 Entries)

Sequence analysis, genomic data processing, structural biology, and variant interpretation.

**Key Patterns:**
- `def align_sequences(seq_list, algorithm):` → "Compare and line up DNA/protein sequences"
- `def perform_variant_calling(raw_sequencing_data):` → "Identify genetic mutations"
- `def perform_gene_ontology_enrichment(gene_list):` → "Find common biological functions"

**Advanced Patterns:**
- `def perform_single_cell_clustering(sc_rna_seq_data):` → "Group cells by expression profiles"
- `def calculate_tmb(sequencing_data):` → "Determine Tumor Mutational Burden"
- `def perform_variant_prioritization(variant_list, disease_model):` → "Rank mutations by disease likelihood"

**Covered Topics:**
- Sequence alignment & comparison
- Variant calling & annotation
- Gene expression analysis (RNA-seq)
- Genome assembly & mapping
- Protein structure prediction
- Phylogenetic analysis
- Epigenetic analysis
- Pathway analysis (KEGG, GO)
- Disease genomics databases
- Single-cell analysis

#### 7.3 Clinical Trials & Regulatory (50 Entries)

Regulatory compliance, trial design, data management, safety monitoring, and documentation.

**Key Patterns:**
- `def generate_protocol_draft(phase, indication):` → "Create clinical trial protocol"
- `def screen_patient_eligibility(patient_record, inclusion_criteria):` → "Check trial requirements"
- `def report_adverse_event(patient_id, event_details):` → "Submit negative outcomes"

**Advanced Patterns:**
- `def check_21_cfr_part_11_compliance(system_feature):` → "Verify FDA electronic records rules"
- `def check_gdpr_compliance(data_handling_procedure):` → "Verify European data privacy"
- `def perform_interim_analysis(trial_data, stopping_rule):` → "Pre-planned early stopping analysis"

**Covered Topics:**
- Protocol design & compliance (GCP, FDA, EMA)
- Patient eligibility & safety screening
- Informed consent & ethics
- Sample size calculation
- Data management & integrity
- Statistical analysis & reporting
- Regulatory submissions (CTD, CSR, IB)
- Safety monitoring & adverse events
- HIPAA/GDPR compliance
- Training & certification tracking

#### 7.4 Laboratory Automation & Data (50 Entries)

Lab operations, instrument control, data processing, and quality assurance.

**Key Patterns:**
- `def control_liquid_handler(protocol_name, plate_layout):` → "Send instructions to pipetting robot"
- `def parse_mass_spec_output(raw_file):` → "Extract peaks from instrument data"
- `def generate_qc_report(assay_data, qc_thresholds):` → "Create quality control report"

**Advanced Patterns:**
- `def integrate_lims_data(lims_api_endpoint, sample_id):` → "Pull data from Lab Management System"
- `def check_gxp_audit_log(system_log, gxp_standard):` → "Verify compliance with Good Practice"
- `def perform_cell_line_authentication(dna_fingerprint):` → "Verify cell line identity"

**Covered Topics:**
- LIMS integration & sample tracking
- Instrument control & automation
- Data analysis (mass spec, HPLC, PCR, flow cytometry)
- Quality control & validation
- Laboratory compliance (SOPs, GLP, GMP)
- Chain of custody & data integrity
- Inventory & reagent management
- Standard curves & calibration
- Equipment maintenance & utilization
- Environmental monitoring

---

## Domain Expertise Demonstration

### Why Biopharma Focus Matters

The 200-entry Biopharma section demonstrates:

✅ **Regulatory Complexity** - FDA, EMA, ICH guidelines
✅ **Scientific Precision** - Computational chemistry, genomics terminology
✅ **Data Integrity** - 21 CFR Part 11, audit trails, traceability
✅ **Safety Critical** - Adverse event reporting, compliance verification
✅ **Multi-disciplinary** - Drug discovery, clinical, manufacturing, regulatory

### Real-World Application

These patterns enable agents to:

1. **Extract Drug Discovery Data** from computational chemistry codebases
2. **Generate Clinical Trial Documentation** from protocol frameworks
3. **Process Genomic Analysis** from bioinformatics pipelines
4. **Automate Lab Operations** from instrument control software
5. **Ensure Regulatory Compliance** in data handling systems

### Example: Drug Discovery Workflow

```python
# Code pattern from discovery system
def virtual_screen(target_id, library_path):
    results = dock_ligands(target_id, library_path)
    return filter_by_affinity(results)

# Maps to instruction
"Run a computational screen of the compound library against the protein target"

# Conversational format entry
{
  "messages": [
    {"role": "system", "content": "You are a computational chemist..."},
    {"role": "user", "content": "Run a computational screen of the compound library against the protein target"},
    {"role": "assistant", "content": "```python\ndef virtual_screen(target_id, library_path):\n    results = dock_ligands(target_id, library_path)\n    return filter_by_affinity(results)\n```"}
  ]
}
```

---

## Scale & Coverage

| Metric | Value |
|--------|-------|
| Total Entries | 610+ |
| Code Patterns | 610+ |
| Natural Language Instructions | 610+ |
| Categories | 8 |
| Biopharma Focus | 200 entries (33%) |
| General Business/Tech | 410 entries (67%) |
| Regulatory Topics Covered | 15+ |
| Scientific Databases Referenced | 20+ |
| Programming Languages | 10+ |

---

## How to Use This Comprehensive Reference

### During Dataset Extraction

1. **Identify code pattern** in your codebase
2. **Search this comprehensive reference** by pattern type
3. **Use mapping** as starting point for instruction
4. **Customize** to specific implementation
5. **Generate** conversational format entry
6. **Validate** output format

### For Biopharma Codebases

1. Look for **drug discovery patterns** (Section 7.1)
2. Search **genomics operations** (Section 7.2)
3. Find **clinical/regulatory logic** (Section 7.3)
4. Identify **lab automation** (Section 7.4)
5. Use established medical/scientific terminology
6. Ensure compliance language is accurate

### Building Domain-Specific Agents

This reference enables:
- **Drug discovery agents** - Molecule design & optimization
- **Clinical trial agents** - Protocol compliance & patient safety
- **Genomics analysis agents** - Sequence & variant interpretation
- **Lab automation agents** - Instrument control & data QA
- **Regulatory agents** - Compliance & documentation

---

## Medical & Scientific Terminology Included

**Drug Discovery:**
- Ligand, receptor, binding affinity, ADMET, docking, pharmacophore
- Lipinski's Rule of Five, lead optimization, SAR
- Off-targets, IC50, Kd, bioavailability

**Genomics:**
- SNP, indel, CNV, structural variants
- Gene ontology, pathway analysis, GWAS
- RNA-seq, whole genome sequencing, single-cell

**Clinical:**
- Protocol, informed consent, adverse events
- Sample size calculation, statistical analysis
- Regulatory submission, CTD, CSR, IB

**Laboratory:**
- LIMS, GLP, GMP, 21 CFR Part 11
- Chain of custody, data integrity, audit trail
- QC/QA, standard curves, LOD/LOQ

---

## File Structure

```
code-agnostic-dataset-extractor.skill/
├── SKILL.md (updated with references)
├── README.md
├── references/
│   ├── agent_patterns.md (existing)
│   ├── enterprise_integrations.md (existing)
│   ├── instruction_templates_expanded.md (300 entries)
│   └── instruction_templates_comprehensive_600plus.md ← NEW
└── assets/
```

---

## Integration Benefits

✅ **Completeness** - 610+ patterns cover nearly all code scenarios
✅ **Domain Depth** - 200 specialized biopharma entries
✅ **Regulatory Accuracy** - Compliance-focused patterns
✅ **Consistency** - Unified instruction generation framework
✅ **Scalability** - Works across industries and codebases
✅ **Quality** - Production-ready mappings

---

## Notes for Users

- **Templates are guidance**, not mandatory rules
- **Customize instructions** for your specific code
- **Add new patterns** as you discover them
- **Domain-specific expertise** (biopharma) ensures accuracy
- **Scientific accuracy** is critical for regulated industries
- **Compliance language** must be precise and complete

---

**Status: ✅ COMPREHENSIVE REFERENCE COMPLETE**

610+ entries covering general domains and specialized biopharma applications. Ready for enterprise-scale dataset extraction.
