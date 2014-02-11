var d4={

	show : function (cssName) { 
		t=d3.selectAll(cssName); 
		t.style('display',null); 
		t.attr('display') ? t.attr('display',null) :''; 
	},

	hide: function (t) { 
		d3.selectAll(cssName).style('display','none'); 
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
		return d3element.append('text')
			.attr('id',id)
			.attr('class',cssClass)
	        .style('text-anchor',align ? (align=='right'||'end' ? 'end' : (align=='left' ? 'begin' : 'middle')) : '')
	        .style('text-align',align ? align : 'left')
	        .text(text)
	        .attr('y',y)
	        .attr('x',x);		
	    if (anima) 
	    	d3element
	    		.attr('opacity','0')
	    		.transition()
	    		.attr('opacity','1')
	    		.duration(500)
	    		.attr('opacity',null)
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
	}

}