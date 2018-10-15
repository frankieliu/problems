var seq = [
  {id: "Library Prep",
   options: [
     "yes",
     "no"]
   }
];

var experimentType = [
  
];  
var model_options = {
  1: [{ text: "Accord", id: 1 }, { text: "Civic", id: 2 }],
  2: [{ text: "Corolla", id: 3 }, { text: "Hi Ace", id: 4 }],
  3: [{ text: "Altima", id: 5 }, { text: "Zuke", id: 6 }],
  4: [{ text: "Alto", id: 7 }, { text: "Swift", id: 8 }]
};

var makes_options = [
  { text: "Honda", id: 1 },
  { text: "Toyota", id: 2 },
  { text: "Nissan", id: 3 },
  { text: "Suzuki", id: 4 }
];

if (0) {
var vm_makes = new Vue({
  el: "#app",
  data: {
    label: ["label 0", "label 1"],
    value0: null,
    value1: null,
    options: [makes_options, model_options],
  },
  watch: {
    value0: function(event) {
      $('#id1').dropdown('clear');
    }
  }
});
};

// Define a simple component
Vue.component(
  'my-dropdown-simple',
  {
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
                    <select class="ui dropdown" v-model="value" :id="id">
                        <option v-for="(option,index) in options" v-bind:value="index">
                            {{ option }}
                        </option>
                    </select>
                </div>`
  });

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

Vue.component(
  'App',
  {
    template:`
<div>
  <my-dropdown-simple 
   v-for="menu in menus"
   :key="menu.label" 
   :label="menu.label"
   :options="menu.options"
   :id="menu.label">
  </my-dropdown-simple>
</div>
`,
    data: function() {
      return {
        menus: [
          {
            label: exp.id,
            options: exp.options
          },
          {
            label: org.id,
            options: org.options
          },
        ]
      };
    }
  });

$('.ui.dropdown').dropdown();

var vm_test = new Vue({
  render: h => h('App')}).$mount("#app1");
