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
        .attr("id","thesvg")
        .append("svg:g")
        .attr("id","theg")
    .attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

//Change the .json to the correct location for any other project.
d3.json("plumbum/plumbum.json", function(error, root) {
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
      .style("fill-opacity", "10.6")
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
        .style("dy", "0.35em");

  var node = svg.selectAll("circle,text");

  zoomTo([root.x, root.y, root.r * 2 + margin]);

  function zoom(d) {
    var focus0 = focus; focus = d;
      
            // check if there exists a div tag
          divtagchecker(d);
      
        var box = { left: 0, top: 0, wdith: 0, height: 0 };

    if (!d.children){
        console.log(d.json);
        appendScroller(box, d.json, d.name);
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

    // check if current div tag exists.
    function divtagchecker(d){

    var doesthisexist = document.getElementById("newblock");
    //console.log(doesthisexist);
    if (doesthisexist == null){
        return;
    }else {
        console.log("tthe else is running");
        // remove the div tag that currently exists and zoom out
        doesthisexist.parentNode.removeChild(doesthisexist);
        }

    }
    
    function appendScroller(box, path, name){

        // find the path of the json file according to the path
    d3.json(path, function (data) {
            
            // create the div tag where everything sits
        dynamicDiv(box);

        var scrollSVG = d3.select(".newblock").append("svg")
                .attr("class", "scroll-svg")
                .attr("id", "othersvg");

        document.getElementById("othersvg").style.zIndex = "20";
        document.getElementById("othersvg").style.width = 1000 + "px";

        // chartgroup is set to append onto scroll svg and class is set...
        var chartGroup = scrollSVG.append("g")
                .attr("class", "chartGroup")

        // we append a rectangle onto chartgroup...
        chartGroup.append("rect")
                .attr("fill", "#FFFFFF");

        var infoSVG = d3.select(".information").append("svg")
                .attr("class", "info-svg");

        // these are all the squares that are entering the frame...
        var rowEnter = function(rowSelection) {
            rowSelection.append("rect")
                    .attr("rx", 3)
                    .attr("ry", 3)
                    .attr("width", "3000")
                    .attr("height", "24")
                    .attr("fill-opacity", 0.60)
            rowSelection.append("text")
                    .attr("transform", "translate(10,15)");
        };
        // this is what is updating the index...
        var max = maxLength(data);
        var rowUpdate = function(rowSelection) {
            rowSelection.select("rect")
                    .attr("fill", function(d) {
                        // set the color of every rectangle according to json
                        return d.colour == "orange" ? "white": d.colour;
                    });

            rowSelection.select("text")
                    .text(function (d) {
                        // set the text in each line
                        var txt =  line( max ,d.author, d.index, d.code);
                        return txt;
                    });
        };

        var rowExit = function(rowSelection) {
        };

        // finds the number of lines in file
        var Array = [];
        data.lines.forEach(function(currentData, i) {
            Array.push(currentData);
        });
        var lastOne = Array[Array.length - 1];
        var IndexSize = lastOne.index;

            // initliaze the virtual scroller
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

    });
}
    // creates a div tag
    function dynamicDiv(box){
        // the id and the class
        var name = "newblock";

        var iDiv = document.createElement('div');
        iDiv.id = name;
        iDiv.className = name;
        document.getElementsByTagName('body')[0].appendChild(iDiv);

        document.getElementById(name).style.width = 500 + "px"
        document.getElementById(name).style.height = 500 + "px";
        // set attributes of the div tag
        var a = document.getElementById(name);
        a.style.position = "absolute";
        a.style.left =  "225px"; //xcoord;
        a.style.top = "225px"; //ycoord;
        a.style.overflowY = "auto";
        a.style.border = 1 + "px solid #AAAAAA";
        a.style.backgroundColor = "#e8e8e8";
        a.style.overflowX = "auto";
        a.style.zIndex = "20";
}
    
    function line(size, author, index, code){
     var total = author;
        while(total.length <= size)
            total = total +  " ";
        total = total + " : " + index + ": " + code;
    return total;
    }
    
    function maxLength(d){
        var max = 0;
        for(var i = 0; i < d.lines.length ; i++)
            if( max <= d.lines[i].author.length)
                max = d.lines[i].author.length;
        return max;
    }
    
});

d3.select(self.frameElement).style("height", diameter + "px");
