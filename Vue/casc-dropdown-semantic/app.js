// Define a simple component
// const data = require('./data.js');

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
  'my-dropdown-categories',
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
    <option v-for="(option,index) in options" v-bind:value="index" v-bind:disabled="option.disabled">
      {{ option.text }}
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

<my-dropdown-categories
 :label="seqmenu.id"
 :options="seqmenu.options"
 :id="seqmenu.label"
 v-model="seqvalues">
</my-dropdown-categories>

<h2>Analysis Information</h2>

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
        seqmenu: seq,
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
            options: libPrep.options
            /*
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
            */
          },
          /*
          {
            label: loN.id,
            options: loN.options
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
          */
          {
            label: spike.id,
            options: spike.options
          },
          {
            label: conc.id,
            options: conc.options
          }
        ],
        values: [],
        depvalues: [],
        seqvalues: null
      };
    }
  });

$('.ui.dropdown').dropdown();

var vm_test = new Vue({
  render: h => h('App')}).$mount("#app1");

// vm_test.$children[0].$children[0].$data.value
// vm_test.$children[0].$data.values
