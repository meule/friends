var d4={

	show : function (cssName) { 
		t=d3.selectAll(cssName); 
		t.attr('display') ? t.attr('display',null) :''
		return t.style('display',null); 
	},

	hide: function (cssName) { 
		return d3.selectAll(cssName).style('display','none'); 
	},

	visible: function(cssName) {
		return ((Math.round((+d3.select(cssName).style('fill-opacity'))*100)!=0)&&(d3.selectAll(cssName).style('display')!='none'))
	},

	showOp: function(cssName,duration) {
		return d3.selectAll(cssName).transition().style("fill-opacity",1).duration(duration ? duration : 800);
	},

	hideOp: function(cssName,duration) {
		return d3.selectAll(cssName).transition().style("fill-opacity",0).duration(duration ? duration : 800);
	},

	rect: function (d3element,x,y,width,height,id,fill,stroke,strokeWidth,nonVisible,cssClass) {
		return d3element.append('rect')
			.attr('x',x)
			.attr('y',y)
			.attr('width',width)
			.attr('height',height)
			.attr('id',id ? id : null)
			.style('fill',fill ? fill : 'none')
			.style('stroke',stroke ? stroke : 'none')
			.style('stroke-width',strokeWidth ? strokeWidth : 0)
			.style('display',nonVisible ? 'none' : null)
			.attr('class',cssClass ? cssClass : null)
	},

	text: function(d3element, text, x, y, cssClass, id, align,anima) {
		textEl=d3element.append('text')
			.attr('id',id)
			.attr('class',cssClass)
	        .style('text-anchor',align ? (align=='right'||'end' ? 'end' : (align=='left' ? 'begin' : 'middle')) : '')
	        .style('text-align',align ? align : 'left')
	        .text(text)
	        .attr('y',y)
	        .attr('x',x);		
	    if (anima) 
	    	textEl.style('opacity',0)
	    		.transition()
	    		.style('opacity',1)
	    		.duration(500);
	    return textEl;
	},
	wWidth: function () {
		var w = window,
		    d = document,
		    e = d.documentElement,
		    g = d.getElementsByTagName('body')[0];
		    return w.innerWidth || e.clientWidth || g.clientWidth
	},

	elWidth: function (element) {
		return parseInt(window.getComputedStyle(element,null).getPropertyValue("width"))
	},
	wHeight: function () {
		var w = window,
		    d = document,
		    e = d.documentElement,
		    g = d.getElementsByTagName('body')[0];
		    return w.innerHeight|| e.clientHeight|| g.clientHeight;
	},
	svg2canvas: function(svgID, canvasID,cwidth,cheight){
    // convert base64 to raw binary data held in a string
    // doesn't handle URLEncoded DataURIs

		canvg(canvasID, $("#"+svgID).html(),{
			'scaleWidth':cwidth,
			'scaleHeight':cheight,
			'useCORS':true,
			'log':true
		});
		// the canvas calls to output a png
		return document.getElementById(canvasID);
	},

	canvas2png: function(canvas){

		dataURI = canvas.toDataURL("image/png");

	    var byteString = atob(dataURI.split(',')[1]);
	    var ab = new ArrayBuffer(byteString.length);
	    var ia = new Uint8Array(ab);
	    for (var i = 0; i < byteString.length; i++) {
	        ia[i] = byteString.charCodeAt(i);
	    }
	    return new Blob([ab], {
	        type: 'image/png'
	    });

	}
}