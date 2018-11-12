
const exp = {
  id:'Experiment Type',
  options: [
    "Whole-Genome DNA Fragments",
    "Whole-Genome DNA Mate Pairs",
    "Targeted Genomic DNA",
    "ChIP Seq Experiment",
    "ChIA-PET",
    "ChIP Control",
    "Methyl Seq",
    "Whole-Transcript mRNA, Non-Directional",
    "Whole-Transcript mRNA, Strand-Specific",
    "3'-End-Biased mRNA",
    "5'-End-Biased mRNA",
    "Small RNA",
    "Micro RNA",
    "Total RNA",
    "ATAC-Seq",
    "Single-Cell",
    "10X Genomics",
    "CRISPR library",
    "Custom Design"]};

const org = {
  id: 'Organism',
  options: [
    "H. sapiens (Human)",
    "P. troglodytes (Chimp)",
    "M. mulatta (Rhesus)",
    "M. musculus (Mouse)",
    "C. lupus (Dog)",
    "M. eugenii (Wallaby)",
    "G. gallus (Chicken)",
    "X. tropicalis (Frog)",
    "D. melanogaster (Fly)",
    "C. elegans (Worm)",
    "A. thaliana (Wall Cress)",
    "Z. mays B73 (Maize)",
    "S. cerevisiae (Yeast)",
    "S. bayanus (Yeast)",
    "S. paradoxus (Yeast)",
    "S. mikatae (Yeast)",
    "C. albicans (Yeast)",
    "E. coli",
    "Pseudomonas aeruginosa",
    "Streptomyces coelicolor",
    "Phi X 174",
    "Other",
    "None"]};

const libPrep = {
  id: 'Library Prep',
  options: [
    "No prep",
    "Single End- only available as FC (8 lanes)",
    "Single End with Index- only available as FC (8 lanes)",
    "Single End with Dual Index- only available as FC (8 lanes)",
    "Paired End",
    "Paired End with Index",
    "Paired End with Dual Index",
    "Mate Pairs",
    "Mate Pairs with Index",
    "Mate Pairs with Dual Index"]
};

const spike = {
  id: 'Percent Spike in PhiX',
  options: [
    "No low nucleotide diversity or significant imbalance",
    "05% Spike-in PhiX- sligntly unbalanced",
    "10% Spike-in PhiX- more than sligntly unbalanced",
    "15% Spike-in PhiX-10X, Single Cell, Methyl Seq ",
    "20% Spike-in PhiX-PCR ",
    "25% Spike-in PhiX-iRepertoire",
    "30% Spike-in PhiX-PCR single region amplification",
    "40% Spike-in PhiX-extremetly unbalanced"
  ]
};    

const conc = {
  id: 'Concentration Methods',
  options: [
    "NanoDrop",
    "Qubit",
    "Bioanalyzer",
    "qPCR",
    "Digital PCR",
    "Tapestation",
    "Fragment Analyzer",
    "SYBR Gold",
    "SYBR Green",
    "Other "
    ]
};

const seq = {
  id: "Sequencing Platform",
  options: [
    {
      text: "Illumina", disabled: true
    },
    {
      text: "Miseq-onelane", disabled: true
    },
    {
      text: "1x51 MiSeq with Index", disabled: null
    },
    {
      text: "1x101 MiSeq with Index", disabled: null
    },
    {
      text: "1x151 MiSeq with Index", disabled: null
    },
    {
      text: "2x76 MiSeq with Index", disabled: null
    },
    {
      text: "2x101 MiSeq with Index", disabled: null
    },
    {
      text: "2x151 MiSeq with Index", disabled: null
    },
    {
      text: "2x251 MiSeq with Index", disabled: null
    },
    {
      text: "2x301 MiSeq with Index", disabled: null
    },
    {
      text: "Hiseq4000-8 lanes", disabled: true
    },
    {
      text: "1x51 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "1x101 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "1x151 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "2x51 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "2x101 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "2x151 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "NovaSeq 6000 Standard Mode", disabled: true
    },
    {
      text: "1x51 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "1x101 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "1x151 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "2x51 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "2x101 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "2x151 HiSeq 4000 with Index", disabled: null
    },
    {
      text: "NovaSeq 6000 XP Mode", disabled: true
    },
    {
      text: "XP-2 S1 1x101 NovaSeq with Index", disabled: null
    },
    {
      text: "XP-2 S2 1x101 NovaSeq with Index", disabled: null
    },
    {
      text: "XP-2 S1 2x101 NovaSeq with Index", disabled: null
    },
    {
      text: "XP-2 S2 2x101 NovaSeq with Index", disabled: null
    },
    {
      text: "XP-2 S1 2x151 NovaSeq with Index", disabled: null
    },
    {
      text: "XP-2 S2 2x151 NovaSeq with Index", disabled: null
    },
    {
      text: "XP-4 S4 2x151 NovaSeq with Index", disabled: null
    },
    {
      text: "PacBio Magbead Loading - 10 hr movie", disabled: true
    },
    {
      text: "Magbead Loading - 1 Smart cell", disabled: null
    },
    {
      text: "Magbead Loading - 4 Smart cell", disabled: null
    },
    {
      text: "Magbead Loading - 8 Smart cell", disabled: null
    },
    {
      text: "Magbead Diffusion < 2kb size - 10 hr movie", disabled: true
    },
    {
      text: "Magbead Loading - 1 Smart cell", disabled: null
    },
    {
      text: "Magbead Loading - 4 Smart cell", disabled: null
    },
    {
      text: "Magbead Loading - 8 Smart cell", disabled: null
    },
    {
      text: "Magbead Diffusion > 2kb size - 10 hr movie", disabled: true
    },
    {
      text: "Magbead Loading - 1 Smart cell", disabled: null
    },
    {
      text: "Magbead Loading - 4 Smart cell", disabled: null
    },
    {
      text: "Magbead Loading - 8 Smart cell", disabled: null
    },
    {
      text: "Oxford Nanopore", disabled: true
    },
    {
      text: "IonTorrent", disabled: null
    }
  ]
};

const mp = {
  id: "Mapping Reference Sequence",
  options: [
    "No reference",
    "Human Male (hg19)",
    "Human Female (hg19)",
    "Human (hg18)",
    "Chimp (CGSC 2.1)",
    "Rhesus (rheMac2)",
    "Mouse Male (mm9)",
    "Mouse Female (mm9)",
    "Dog (canFam2)",
    "Wallaby (1.0)",
    "Chicken (galGal3)",
    "Frog (xenTro2)",
    "Fly (dm3)",
    "Worm (ce6)",
    "Worm (WS182)",
    "A. thaliana (TAIR9)",
    "Maize (ZmB73_AGPv1)",
    "Maize (ZmB73_AGPv2)",
    "Yeast (SGD 4/11)",
    "Yeast (SGD 6/08/sacCer2)",
    "Yeast (SGD 5/08)",
    "Yeast ORFs (SGD 5/08)",
    "Yeast, C. albicans (Ca21)",
    "Yeast, C. albicans (WO1)",
    "E. coli K-12 MG1655",
    "Pseudomonas aeruginosa UCBPP-PA14",
    "S. coelicolor (Sco)",
    "PhiX"
  ]
};

const indexSelection = {
  id: "Index Selection:",
  table: {
    col:
    [
      "Index",
      "Sequence"
    ]
  }
};


const mm = {
  id: "Mapping Method",
  options: [
    "BWA (DNA-Seq)",
    "STAR (RNA-Seq)",
    "CellRanger (10X Single Cell)"
  ]
};

const submit = {
  id: "Submit",
  options: [
    "Finished",
    "Submit Another Lane"
  ]
};
