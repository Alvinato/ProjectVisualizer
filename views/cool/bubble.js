var margin = 20,
    diameter = 960;
//ALVIN CODE
var firstLayerText = [];
var jsonobjectstosend = {};
var Json = new Object;

var idList = [];
var idList2 = []
//ALVIN CODE


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
    //ALVIN CODE
        .attr("id","thesvg")
        .append("svg:g")
        .attr("id","theg")
    //ALVIN CODE
    //.append("g")
    .attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

//ALVIN CODE
document.getElementById("thesvg").style.zIndex ="1";
document.getElementById("theg").style.zIndex ="1";
//ALVIn  CODe

d3.json("plumbum.json", function(error, root) {
  if (error) return console.error(error);

  var focus = root,
      nodes = pack.nodes(root),
      view;

  var circle = svg.selectAll("circle")
      .data(nodes)
    .enter().append("circle")
      .attr("class", function(d) // "node"
            { return d.parent ? d.children ? "node" : "node" : "node"; })
      .style("fill", function(d) { return colorize(d); })
      .style("fill-opacity", "1")
      .style("visibility", function (d)
               { if(d===root) return "visible";
                else return d.parent === root ? "visible": "hidden";})
      .on("click", function(d) 
          { if (focus !== d) zoom(d)
            else zoom(d.parent ? d.parent : root)  
          , d3.event.stopPropagation(); })
        
  var text = svg.selectAll("text")
      .data(nodes)
    .enter().append("text")           
      .attr("class", "label")
      .style("fill-opacity", function(d) { return d.parent === root ? 1 :0; })
      .style("display", function(d) { return d.parent === root ? null : "none"; })
      .text(function(d) { return d.name; })
    //Size of text need to resize wont ?
        .style("dy", "0.35em");
    
    //ALVIN CODE -----------------------------
     for (var k = 0; k < idList.length; k++){
        // lets select every single one
        //console.log("this is the idlist" + idList[k]);
        var selection = document.getElementById(idList[k]);
        var selection2 = document.getElementById(idList2[k]);

        // for every selection give it a low z
        selection.style.zIndex = "1";
        selection2.style.zIndex = "1";
    }
    
    
    //ALVIN CODE -------------------

  var node = svg.selectAll("circle,text");

  zoomTo([root.x, root.y, root.r * 2 + margin]);

  function zoom(d) {
    var focus0 = focus; focus = d;
      
      //ALvni
          divtagchecker(d);
      
        var box = { left: 0, top: 0, wdith: 0, height: 0 };
      console.log(d.name);
   // box = document.getElementById(d.name).getBoundingClientRect();

    var xcoord =  box.left;
    var ycoord = box.top;
    var width = box.width;
    var height = box.height;

    if (d.name.substring(d.name.length-3, d.name.length) == ".py"){
        appendScroller(box, d.path, d.name);
    }

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
                    || d === focus
                    || d === root; })
        .each("start", function(d) { if (d.parent === focus || d === focus ) 
                    this.style.visibility = "visible";})
        .each("end", function(d) { 
            if (d.parent !== focus && d !== focus && d !== focus.parent && d!== root) 
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
      
    function colorize (d){
        if(!d.children)
            return d.colour;
        
        var g = d.children;
        
        var green = 0;
        var red = 0;
        var blue = 0;

        for(i = 0; i < g.length; i++){
            green += count(g[i], "green");             
            red += count(g[i], "red");
            blue += count(g[i], "blue");
        }

       var total = (green + blue + red);
       var redPercentage = red/total;
       var greenPercentage = green/ total;
       var bluePercentage = blue/total;
       var redAmount = (255 * redPercentage);
       var greenAmount = (255 * greenPercentage);
       var blueAmount = (255 * bluePercentage);
       var tColor = d3.rgb(redAmount, greenAmount, blueAmount);
       return tColor;
    }
    
    function count(d, c){
        var a = 0;
        if(d.children){
            for(var i = 0, len = d.children.length; i < len; i ++){
                a += count(d.children[i], c);
            }
        }
        else{
            if(d.colour == c)
                a = 1;
            else
                a = 0;     
        }
        return a;
    }
    
    
    function jsonnamegetter(path) {
        console.log(path);
        var allStrings = path.split("/");
        for (var m = 0; m < allStrings.length; m++)
            console.log(allStrings[m]);

        var directory = allStrings[allStrings.length - 2];
        var pythonfile = allStrings[allStrings.length-1];
        pythonfile = pythonfile.substring(0, pythonfile.length-3);

        console.log("the directory: " + directory + "the pythonfile" + pythonfile);

        var intermediate = (directory.concat("-")).concat(pythonfile);
        var finalFilename = intermediate.concat(".json");

        //console.log("this should be the file name"  +finalFilename ); // this yields directory        - pythonfile.py

    return finalFilename;
}
    function divtagchecker(d){

    var doesthisexist = document.getElementById("newblock");
    //console.log(doesthisexist);
    if (doesthisexist == null){
      //  console.log("this should be running");
        return;
    }else {
        console.log("tthe else is running");
        // else... delete the div tag
        // grab the parent node then remove the children form the parent node
        doesthisexist.parentNode.removeChild(doesthisexist);
    }

}
    function appendScroller(box, path, name){

    var filename = jsonnamegetter(path);
        console.log(filename);

    d3.json(filename, function (data) {

        dynamicDiv(box);

        var scrollSVG = d3.select(".newblock").append("svg")
                .attr("class", "scroll-svg")
                .attr("id", "othersvg");

        document.getElementById("othersvg").style.zIndex = "20";
        document.getElementById("othersvg").style.width = 1000 + "px";

        // putting defs together so they can be filtered properly...
        var defs = scrollSVG.insert("defs", ":first-child");
        createFilters(defs);

        // chartgroup is set to append onto scroll svg and class is set...
        var chartGroup = scrollSVG.append("g")
                .attr("class", "chartGroup")

        // we append a rectangle onto chartgroup...
        chartGroup.append("rect")
                .attr("fill", "#FFFFFF");

        var infoSVG = d3.select(".information").append("svg")
                .attr("class", "info-svg");

        var braceGroup = infoSVG.append("g")
                .attr("transform", "translate(0,0)");

        braceGroup.append("path")
                .attr("class", "brace")
                .attr("d", makeCurlyBrace(10, 380, 10, 20, 30, 0.55));

        var braceLabelGroup = braceGroup.append("g")
                .attr("transform", "translate(45, 176)");

        braceLabelGroup.append("text")
                .attr("class", "infotext")
                .attr("transform", "translate(0, 0)")
                .text("50 data items but only ");

        braceLabelGroup.append("text")
                .attr("class", "infotext")
                .attr("transform", "translate(-1, 30)")
                .text("15 dom nodes rendered");

        braceLabelGroup.append("text")
                .attr("class", "infotext")
                .attr("transform", "translate(0, 60)")
                .text("at any given time!");


        // these are all the squares that are entering the frame...
        var rowEnter = function(rowSelection) {
            rowSelection.append("rect")
                    .attr("rx", 3)
                    .attr("ry", 3)
                    .attr("width", "3000")
                    .attr("height", "24")
                    .attr("fill-opacity", 0.25)
                    .attr("stroke", "#999999")
                    .attr("stroke-width", "2px");
            rowSelection.append("text")
                    .attr("transform", "translate(10,15)");
        };
        // this is what is updating the index...
        var rowUpdate = function(rowSelection) {
            rowSelection.select("rect")
                    .attr("fill", function(d) {
                        return d.colour;
                    });

            rowSelection.select("text")
                    .text(function (d) {
                        return (d.author) +":  " + (d.index) + ". " + d.code;
                    });
        };

        var rowExit = function(rowSelection) {
        };

        //----> this finds the row numbers...
        var Array = [];
        data.lines.forEach(function(currentData, i) {
            Array.push(currentData);
        });
        var lastOne = Array[Array.length - 1];  // it is correct...
        var IndexSize = lastOne.index;

        // have to place a div tag inside every single bubble...
        var virtualScroller = d3.VirtualScroller()
                .rowHeight(30)
                .enter(rowEnter)
                .update(rowUpdate)
                .exit(rowExit)
                .svg(scrollSVG)
                .totalRows(IndexSize)
                .viewport(d3.select(".newblock"));


        virtualScroller.data(data.lines, function(d) { return d.index; });

        chartGroup.call(virtualScroller);

        function createFilters(svgDefs) {
            var filter = svgDefs.append("svg:filter")
                    .attr("id", "dropShadow1")
                    .attr("x", "0")
                    .attr("y", "0")
                    .attr("width", "200%")
                    .attr("height", "200%");

            filter.append("svg:feOffset")
                    .attr("result", "offOut")
                    .attr("in", "SourceAlpha")
                    .attr("dx", "1")
                    .attr("dy", "1");

            filter.append("svg:feColorMatrix")
                    .attr("result", "matrixOut")
                    .attr("in", "offOut")
                    .attr("type", "matrix")
                    .attr("values", "0.1 0 0 0 0 0 0.1 0 0 0 0 0 0.1 0 0 0 0 0 0.2 0");

            filter.append("svg:feGaussianBlur")
                    .attr("result", "blurOut")
                    .attr("in", "matrixOut")
                    .attr("stdDeviation", "1");

            filter.append("svg:feBlend")
                    .attr("in", "SourceGraphic")
                    .attr("in2", "blurOut")
                    .attr("mode", "normal");
        }

        function makeCurlyBrace(x1,y1,x2,y2,w,q)
        {
            //Calculate unit vector
            var dx = x1-x2;
            var dy = y1-y2;
            var len = Math.sqrt(dx*dx + dy*dy);
            dx = dx / len;
            dy = dy / len;

            //Calculate Control Points of path,
            var qx1 = x1 + q*w*dy;
            var qy1 = y1 - q*w*dx;
            var qx2 = (x1 - .25*len*dx) + (1-q)*w*dy;
            var qy2 = (y1 - .25*len*dy) - (1-q)*w*dx;
            var tx1 = (x1 -  .5*len*dx) + w*dy;
            var ty1 = (y1 -  .5*len*dy) - w*dx;
            var qx3 = x2 + q*w*dy;
            var qy3 = y2 - q*w*dx;
            var qx4 = (x1 - .75*len*dx) + (1-q)*w*dy;
            var qy4 = (y1 - .75*len*dy) - (1-q)*w*dx;

            return ( "M " +  x1 + " " +  y1 +
                    " Q " + qx1 + " " + qy1 + " " + qx2 + " " + qy2 +
                    " T " + tx1 + " " + ty1 +
                    " M " +  x2 + " " +  y2 +
                    " Q " + qx3 + " " + qy3 + " " + qx4 + " " + qy4 +
                    " T " + tx1 + " " + ty1 );
        }
    });
}
    function dynamicDiv(box){
   var xcoord =  box.left;
   var ycoord = box.top;
    var width = box.width;
    var height = box.height;

    var name = "newblock";

        // ---> inside here create more div tags...
        var iDiv = document.createElement('div');
        iDiv.id = name;
        iDiv.className = name;
        document.getElementsByTagName('body')[0].appendChild(iDiv);

        document.getElementById(name).style.width = 550 + "px"
        document.getElementById(name).style.height = 550 + "px";
            // we just have to position this better...
        var a = document.getElementById(name);
        a.style.position = "absolute";
        a.style.left =  "203px" //xcoord;
        a.style.top = "203px" //ycoord;
        a.style.overflowY = "auto";
        a.style.border = 1 + "px solid #AAAAAA";
        a.style.backgroundColor = "#e8e8e8";
        a.style.overflowX = "auto";
        a.style.zIndex = "20";
}

    
});

d3.select(self.frameElement).style("height", diameter + "px");
