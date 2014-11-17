var margin = 20,
    diameter = 960;

var color = d3.scale.linear()
    .domain([-1, 5])
    .range(["hsl(152,80%,80%)", "hsl(228,30%,40%)"])
    .interpolate(d3.interpolateHcl);

var pack = d3.layout.pack()
    .padding(2)
    .size([diameter - margin, diameter - margin])
    .value(function(d) { return d.size; })

var svg = d3.select("body").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
  .append("g")
    .attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

d3.json("plumbum.json", function(error, root) {
  if (error) return console.error(error);

  var focus = root,
      nodes = pack.nodes(root),
      view;

  var circle = svg.selectAll("circle")
      .data(nodes)
    .enter().append("circle")
      .attr("class", function(d) { return d.parent ? d.children ? "node" : "node" : "node node--root"; })
    //Chnage colors here ? ? ? ?     ??? ? ?? ? ?? ? ? ? ? ?
      .style("fill", function(d) { return //colorize(d);
       d.children ? color(d.depth) : null; 
                                 })
      .style("fill-opacity", "1")
      .style("visibility", function (d)
               { if(d===root) return "visible";
                else return d.parent === root ? "visible": "hidden";})
      .on("click", function(d) { if (focus !== d) zoom(d), d3.event.stopPropagation(); })
        
    //Ateempt scollder
 // var scr = circle//.append("info-svg")
   //     .append("text")
     //   .text("ASAHAHHS\n\n\n\\n\n\n\\n\nn\n\n\\n\n\n\\n");
  //.style("display", function(d) { return d.parent === root ? null : "none"; });
    
    
    /* gARBAGE */
    /************/
            
    
  var text = svg.selectAll("text")
      .data(nodes)
    .enter().append("text")           
      .attr("class", "label")
      .style("fill-opacity", function(d) { return d.parent === root ? 1 :0; })
      .style("display", function(d) { return d.parent === root ? null : "none"; })
      .text(function(d) { return d.name; })
    //Size of text need to resize wont ?
        .style("font-size", "2.5vmin");

  var node = svg.selectAll("circle,text");

  d3.select("body")
      .style("background", color(-1))
      .on("click", function() //TODO: change here for scroll thing
          { zoom( focus.parent ? focus.parent : root); });

  zoomTo([root.x, root.y, root.r * 2 + margin]);

  function zoom(d) {
    var focus0 = focus; focus = d;

    var transition = d3.transition()
        .duration(d3.event.altKey ? 7500 : 750)
        .tween("zoom", function(d) {
          var i = d3.interpolateZoom(view, [focus.x, focus.y, focus.r * 2 + margin]);
          return function(t) { zoomTo(i(t)); };
        });

      //TODO: Maybe show neighbouring children
      //Zooming in and out of a circle.
      transition.selectAll("circle")
        .filter(function(d) {return d.parent === focus 
                    || this.style.visibility === "visible" 
                    || d === focus; })
        .each("start", function(d) { if (d.parent === focus || d === focus ) 
                    this.style.visibility = "visible";})
        .each("end", function(d) { 
            if (d.parent !== focus && d !== focus) 
                    this.style.visibility = "hidden";});
      
      
    transition.selectAll("text")
      .filter(function(d) { return d === focus || d.parent === focus || this.style.display === "inline"; })
        .style("fill-opacity", function(d) { return d.parent === focus ? 1 : 0; })
        .each("start", function(d) { if (d.parent === focus) this.style.display = "inline"; })
        .each("end", function(d) { if (d.parent !== focus) this.style.display = "none"; });
  }

  function zoomTo(v) {
    var k = diameter / v[2]; view = v;
    node.attr("transform", function(d) { return "translate(" + (d.x - v[0]) * k + "," + (d.y - v[1]) * k + ")"; });
    circle.attr("r", function(d) { return d.r * k; });
  }
    
    /*
    function colorize (d){
        var green = 0;
        var red = 0;
        var blue = 0;
            for( var a in d.children){
                console.log(a.colour);
                if(a.chilren){
                green += countg(a);
                red += countr(a);
                blue += countb(a);
                }
            }
        var total = (green + blue + red);
       var redPercentage = red/total;
       var greenPercentage = green/ total;
       var bluePercentage = blue/total;
       var redAmount = 255 * redPercentage;
       var greenAmount = 255 * greenPercentage;
       var blueAmount = 255 * bluePercentage;
       var tColor = new RGBColour(redAmount, greenAmount, blueAmount);
       var newColor = tColor.getCSSHexadecimalRGB();
       return newColor;
    }
    
    function countg(d){
        var a = 0;
        for (var b in d.children){
            if(b.children)
                a += countg(b);
            else{ if(b.colour == "green")
                return a++;}
            return a;
        }
    }
    function countb(d){
        var a = 0;
        for (var b in d.children){
            if(b.children)
                a += countg(b);
            if(b.colour == "blue")
                return a++;
            return a;
        }
    }
    function countr(d){
        var a = 0;
        for (var b in d.children){
            if(b.children)
                a += countg(b);
            if(b.colour == "red")
                return a++;
            return a;
        }
    }
   // */
    
});

d3.select(self.frameElement).style("height", diameter + "px");
