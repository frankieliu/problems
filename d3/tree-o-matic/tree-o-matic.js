// URL: https://beta.observablehq.com/@frankieliu/tree-o-matic
// Title: Tree-o-Matic
// Author: frankieliu (@frankieliu)
// Version: 313
// Runtime version: 1

const m0 = {
  id: "13a3ca21047d402e@313",
  variables: [
    {
      inputs: ["md"],
      value: (function(md){return(
md`# Tree-o-Matic

Edit the textarea below to update the chart!`
)})
    },
    {
      name: "chart",
      inputs: ["tree","data","d3","DOM"],
      value: (function(tree,data,d3,DOM)
{
  const root = tree(data);

  const svg = d3.select(DOM.svg(500, 500))
      .style("background", "white")
      .style("font", "10px sans-serif");

  const g = svg.append("g");

  const link = g.append("g")
    .attr("fill", "none")
    .attr("stroke", "#555")
    .attr("stroke-opacity", 0.4)
    .attr("stroke-width", 1.5)
  .selectAll("path")
    .data(root.links())
    .enter().append("path")
      .attr("d", d => `
        M${d.target.y},${d.target.x}
        C${d.source.y + root.dy / 2},${d.target.x}
         ${d.source.y + root.dy / 2},${d.source.x}
         ${d.source.y},${d.source.x}
      `);

  const node = g.append("g")
      .attr("stroke-linejoin", "round")
      .attr("stroke-width", 3)
    .selectAll("g")
    .data(root.descendants().reverse())
    .enter().append("g")
      .attr("transform", d => `translate(${d.y},${d.x})`);

  node.append("circle")
      .attr("fill", d => d.children ? "#555" : "#999")
      .attr("r", 2.5);

  node.append("text")
      .attr("dy", "0.31em")
      .attr("x", d => d.children ? -6 : 6)
      .text(d => d.data.name)
    .filter(d => d.children)
      .attr("text-anchor", "end")
    .clone(true).lower()
      .attr("stroke", "white");

  document.body.appendChild(svg.node());

  const {x, y, width, height} = g.node().getBBox();

  svg.remove()
      .style("max-width", "100%")
      .style("height", "auto")
      .attr("width", width + 10)
      .attr("height", height + 10)
      .attr("viewBox", `${x - 5} ${y - 5} ${width + 10} ${height + 10}`);

  return svg.node();
}
)
    },
    {
      inputs: ["html","DOM","rasterize","chart","serialize"],
      value: (async function(html,DOM,rasterize,chart,serialize){return(
html`
${DOM.download(await rasterize(chart), null, "Download as PNG")}
${DOM.download(await serialize(chart), null, "Download as SVG")}
`
)})
    },
    {
      name: "viewof algorithm",
      inputs: ["html"],
      value: (function(html){return(
html`<select>
  <option selected value="cluster">Cluster
  <option value="cluster-no-separation">Cluster (no separation)
  <option value="tree">Tree
</select>`
)})
    },
    {
      name: "algorithm",
      inputs: ["Generators","viewof algorithm"],
      value: (G, _) => G.input(_)
    },
    {
      name: "viewof source",
      inputs: ["html"],
      value: (function*(html)
{
  const textarea = html`<textarea>Coffee
 Tastes
  Sour
   Soury
   Winey
    Tart
    Tangy
  Sweet
  Salt
  Bitter
 Aromas
  Enzymatic
   Fruity
    Citrus
    Berry-like
  Sugar browning
   Nutty
   Carmelly
  Dry distillation`;
  textarea.style.display = "block";
  textarea.style.boxSizing = "border-box";
  textarea.style.width = "calc(100% + 28px)";
  textarea.style.font = "var(--mono_fonts)";
  textarea.style.minHeight = "60px";
  textarea.style.border = "none";
  textarea.style.padding = "4px 10px";
  textarea.style.margin = "0 -14px";
  textarea.style.background = "rgb(247,247,249)";
  textarea.style.tabSize = 2;
  textarea.onkeypress = event => {
    if (event.key !== "Enter" || event.shiftKey || event.altKey || event.metaKey || event.ctrlKey) return;
    let i = textarea.selectionStart;
    let j = textarea.selectionEnd;
    let v = textarea.value;
    if (i === j) {
      let k = 0;
      while (i > 0 && v[--i - 1] !== "\n");
      while (i < j && v[i] === " ") ++i, ++k;
      textarea.value = v.substring(0, j) + "\n" + new Array(k + 1).join(" ") + v.substring(j);
      textarea.selectionStart = textarea.selectionEnd = j + k + 1;
      textarea.dispatchEvent(new CustomEvent("input"));
      event.preventDefault();
    }
  };
  textarea.oninput = () => {
    textarea.style.height = "auto";
    textarea.style.height = `${textarea.scrollHeight}px`;
  };
  yield textarea;
  textarea.oninput();
  yield textarea;
}
)
    },
    {
      name: "source",
      inputs: ["Generators","viewof source"],
      value: (G, _) => G.input(_)
    },
    {
      inputs: ["md"],
      value: (function(md){return(
md`Each line in the textarea above represents a node in the tree. The depth of the node is determined by the number of leading spaces (the indentation): the root node has depth zero; its direct children have depth one; their children have depth two, and so on. The parent of each node is the closest preceding node with lesser depth.`
)})
    },
    {
      inputs: ["md"],
      value: (function(md){return(
md`---

## Appendix`
)})
    },
    {
      name: "data",
      inputs: ["source"],
      value: (function(source)
{
  const parents = [];
  const nodes = source.trim().split(/\n/g);
  parents.push({children: []});
  for (let i = 0, n = nodes.length; i < n; ++i) {
    let parent, depth = nodes[i].match(/^\s*/)[0].length;
    while (!(parent = parents[depth])) --depth;
    if (!parent.children) parent.children = [];
    parent.children.push(parents[depth + 1] = {name: nodes[i].slice(depth)});
  }
  return parents[0].children.length === 1 ? parents[0].children[0] : parents[0];
}
)
    },
    {
      name: "tree",
      inputs: ["d3","width","algorithm"],
      value: (function(d3,width,algorithm){return(
data => {
  const root = d3.hierarchy(data);
  root.dx = 10;
  root.dy = width / (root.height + 1);
  let layout;
  switch (algorithm) {
    case "cluster": layout = d3.cluster(); break;
    case "cluster-no-separation": layout = d3.cluster().separation(() => 1); break;
    case "tree": layout = d3.tree(); break;
  }
  return layout.nodeSize([root.dx, root.dy])(root);
}
)})
    },
    {
      name: "width",
      value: (function(){return(
932
)})
    },
    {
      from: "@mbostock/saving-svg",
      name: "rasterize",
      remote: "rasterize"
    },
    {
      from: "@mbostock/saving-svg",
      name: "serialize",
      remote: "serialize"
    },
    {
      name: "d3",
      inputs: ["require"],
      value: (function(require){return(
require("d3@5")
)})
    }
  ]
};

const m1 = {
  id: "@mbostock/saving-svg",
  variables: [
    {
      name: "rasterize",
      inputs: ["DOM","serialize"],
      value: (function(DOM,serialize){return(
function rasterize(svg) {
  let resolve, reject;
  const promise = new Promise((y, n) => (resolve = y, reject = n));
  const image = new Image;
  image.onerror = reject;
  image.onload = () => {
    const rect = svg.getBoundingClientRect();
    const context = DOM.context2d(rect.width, rect.height);
    context.drawImage(image, 0, 0, rect.width, rect.height);
    context.canvas.toBlob(resolve);
  };
  image.src = URL.createObjectURL(serialize(svg));
  return promise;
}
)})
    },
    {
      name: "serialize",
      value: (function()
{
  const xmlns = "http://www.w3.org/2000/xmlns/";
  const xlinkns = "http://www.w3.org/1999/xlink";
  const svgns = "http://www.w3.org/2000/svg";
  return function serialize(svg) {
    svg = svg.cloneNode(true);
    svg.setAttributeNS(xmlns, "xmlns", svgns);
    svg.setAttributeNS(xmlns, "xmlns:xlink", xlinkns);
    const serializer = new window.XMLSerializer;
    const string = serializer.serializeToString(svg);
    return new Blob([string], {type: "image/svg+xml"});
  };
}
)
    }
  ]
};

const notebook = {
  id: "13a3ca21047d402e@313",
  modules: [m0,m1]
};

export default notebook;
