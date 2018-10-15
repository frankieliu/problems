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
    "No", "Yes"
  ]
};

const libType = {
  id: 'Library Type',
  options: [
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

const loN = {
  id: 'Low Nucleotide Diversity or Significant Imbalance',
  options: [
    "No", "Yes"
  ]
};

const spike = {
  id: 'Percent Spike in PhiX',
  options: [
    "5% Spike-in PhiX- sligntly unbalance",
    "10% Spike-in PhiX- more than sligntly unbalance",
    "15% Spike-in PhiX-10X, Single Cell, Methyl Seq ",
    "20% Spike-in PhiX-PCR ",
    "25% Spike-in PhiX-iRepertoire",
    "30% Spike-in PhiX-PCR single region amplification",
    "40% Spike-in PhiX-extremetly unbalance "
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
    "Illumina",
    "PacBio",
    "Oxford Nanopore"
  ]
};

// Define a simple component
Vue.component(
  'my-dropdown-simple',
  {
    model: {
      event: 'change',
      prop: 'value'
    },
    props: {
      label: String,
      id: String,
      options: Array,
    },
    data: function() {
      return { value: null };
    },
    template: `
<div class="ui label"> {{ label }}
  <select class="ui dropdown" v-model="value" :id="id"
   v-on:change="$emit('change', $event.target.value)">
    <option v-for="(option,index) in options" v-bind:value="index">
      {{ option }}
     </option>
  </select>
</div>`
  });

Vue.component(
  'my-number-input',
  {
  }
);

Vue.component(
  'my-dropdown-y-n-dependent',
  {
    template:`
<div>
  <my-dropdown-simple 
   :label="label"
   :options="options"
   :id="label"
   v-model="value"
   v-on:change="$emit('change', $event.target.out)">
  </my-dropdown-simple>
  <my-dropdown-simple
   v-if="value == 1"
   :label="deplabel"
   :options="depoptions"
   :id="deplabel"
   v-model="depvalue"
   v-on:change="$emit('change', $event.target.out)">>
  </my-dropdown-simple>
</div>
    `,
    props: {
      label: String,
      options: Array,
      deplabel: String,
      depoptions: Array
    },
    data: function() {
      return {
        value: null,
        depvalue: null,
      };
    },
    computed: {
      out: function() {
        return {
          value: this.value,
          depvalue: (this.value == 0 ? null : this.depvalue)
        };
      }
    },
    model: {
      prop: 'out',
      event: 'change'
    }
  });

Vue.component(
  'App',
  {
    template:`
<div>
<div v-for="(menu,index) in menus" :key="menu.label">

  <my-dropdown-simple 
   :label="menu.label"
   :options="menu.options"
   :id="menu.label"
   v-model="values[index]">
  </my-dropdown-simple>

  <my-dropdown-simple
   v-if="menu.dep && (menu.yn ? values[index] == 1 : values[index])"
   :label="menu.dep[values[index]|0].label"
   :options="menu.dep[values[index]|0].options"
   :id="menu.dep[values[index]|0].label"
   v-model="depvalues[index]">
  </my-dropdown-simple>
</div>

<div class="ui label"> Average Library Size in bp
  <input class="ui input" v-model.number="libSizeBp" placeholder="(bp)">
</div>
<div class="ui label"> Sample Volume (nl)
  <input class="ui input" v-model.number="sampleVolNl" placeholder="(>= 10 (ul))">
  <span class="ui error" v-if="(sampleVolNl_comp != sampleVolNl) && (sampleVolNl != null)">Error</span>
</div>
<div class="ui label"> Sample Concentration (ng/ul)
  <input class="ui input" v-model.number="sampleConcNgUl" placeholder="(>= 5 (ng/ul))">
  <span class="ui error" v-if="(sampleConcNgUl_comp != sampleConcNgUl) && (sampleConcNgUl != null)">Error</span>
</div>

</div>
`,
    computed: 
      {
        sampleVolNl_comp : function() {
          return (this.sampleVolNl >= 10 ? this.sampleVolNl : 10);
        },
        sampleConcNgUl_comp : function() {
          return (this.sampleConcNgUl >= 5 ? this.sampleConcNgUl : 5);
        }
      },
    data: function() {
      return {
        libSizeBp: null,
        sampleVolNl: null,
        sampleConcNgUl: null,
        menus: [
          {
            label: exp.id,
            options: exp.options
          },
          {
            label: org.id,
            options: org.options
          },
          {
            label: libPrep.id,
            options: libPrep.options,
            yn: true,
            dep: [
              {
                label:"NA",
                options: ["None"]
              },
              {
                label: libType.id,
                options: libType.options
              }]
          },
          {
            label: loN.id,
            options: loN.options,
            yn: true,
            dep: [
              {
                label:"NA",
                options: ["None"]
              },
              {
                label: spike.id,
                options: spike.options
              }]
          },
          {
            label: conc.id,
            options: conc.options
          }
        ],
        values: [],
        depvalues: [],
      };
    }
  });

$('.ui.dropdown').dropdown();

var vm_test = new Vue({
  render: h => h('App')}).$mount("#app1");

// vm_test.$children[0].$children[0].$data.value
// vm_test.$children[0].$data.values
