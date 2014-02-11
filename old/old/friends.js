var already=false;
var width=1200, height=1200, xMargin=20;
    sSize=20, lSize=50, delta=1, tMargin=5, tHeight=20, tHeightAxis=15;
    pWidth=200, pHeight=50, labelWidth=50; 
var you, friends, me;
var num={}, minAge={}, maxAge={}, maxNum={}, ages=[];
var fr=[], frM=[], frF=[], byAge={}, byAgeM={}, byAgeF={};

var svg=d3.select('#svg').append('svg').attr('width',width+'px').attr('height',height+'px');
svg.append('rect').attr('x',0).attr('y',0).attr('width',width).attr('height',height).attr('fill','none').attr('stroke','none').attr('id','back');

function fbLogin(){
    FB.login(function(response) {
        }, {scope: 'user_about_me,user_birthday,friends_about_me,friends_birthday'});
}

window.fbAsyncInit = function() {
    FB.init({
        appId    : '130978340377178',
        status    : true, // check login status
        cookie    : true, // enable cookies to allow the server to access the session
        xfbml    : true // parse XFBML
    });
    FB.Event.subscribe('auth.authResponseChange', function(response) {
         if (response.status === 'connected') {
            if (!already) testAPI();
            already=true;
         } else if (response.status === 'not_authorized') {
            fbLogin();
         } else {
            fbLogin();
         }
    });

 };

 // Load the SDK asynchronously
(function(d){
     var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement('script'); js.id = id; js.async = true;
     js.src = "//connect.facebook.net/en_US/all.js";
     ref.parentNode.insertBefore(js, ref);
     console.log(js);
 }(document));

function testAPI() {
    console.log('Welcome! Fetching your information.... ');
    FB.api('/me?fields=id,name,birthday,gender', function(response) { you=response; console.log(response); });
    FB.api('/me/friends?fields=id,name,birthday,gender', function(response) { friends=response.data; fshow(); });
}
        
function fshow() {
    console.log(you,friends);
    if (!you.birthday) friends.push(you);
    today=new Date();
    num.all=friends.length;
    num.dates=0;
    num.ages=0;
    num.toomuch=0;
    num.gender=0;
    num.m=0;
    num.f=0;
    friends.forEach(function(d){
            if (d.birthday) {
                num.dates++;
                if (d.date=d3.time.format('%m/%d/%Y').parse(d.birthday)) {
                    num.ages++;
                    if ((age=(today - d.date)/31557600000)<90) {
                        num.toomuch++;
                        d.age=age;
                        d.fAge=Math.floor(d.age);
                        fr.push(d);
                        if (!byAge[Math.round(age)]) byAge[Math.round(age)]=[];
                        byAge[Math.round(age)].push(d);
                        if (d.gender) {
                            num.gender++;
                        }
                    }
                }
            }
        });
    if (!you.birthday) me=fr[0];
    fr.sort(function(a,b){if (b.age) {return a.age-b.age} else return false; });
    minAge.all=fr[0].age;
    minAge.allR=Math.floor(minAge.all);
    maxAge.all=fr[fr.length-1].age;
    maxAge.allR=Math.floor(maxAge.all);
   
    ii=0;
    for (i=minAge.allR;i<(maxAge.allR+1);i++) ages.push({'n':ii++,'text':i});
    
    var curAge=0, curAgeM=0, curAgeF=0;
    maxNum.all=0, maxNum.f=0, maxNum.m=0;
    var ii=0, iiM=0, iiF=0, iM=0, iF=0;
    for (i=0;i<fr.length;i++) { 
            if ((fr[i].age-curAge)>1) { curAge=Math.floor(fr[i].age); ii=0;}
            if ((fr[i].age-curAgeM)>1) { curAgeM=Math.floor(fr[i].age); iiM=0;}
            if ((fr[i].age-curAgeF)>1) { curAgeF=Math.floor(fr[i].age); iiF=0;}
            fr[i].ageNum=ii;
            maxNum.all=Math.max(ii,maxNum.all);
            ii++;
            if (fr[i].gender=='male') {
                fr[i].ageNumM=iiM;
                maxNum.m=Math.max(iiM,maxNum.m);
                iiM++ 
            } else {
                fr[i].ageNumF=iiF;
                maxNum.f=Math.max(iiF,maxNum.f); 
                iiF++;
            }
    }
    
    xMargin=(width-(maxNum.all*(sSize+delta)+labelWidth))/2;

    d3.select('.control').append('span').attr('id','all').text('All together    |');
    d3.select('.control').append('span').attr('id','fm').text('|    By gender    |');
    d3.select('.control').append('span').attr('id','third').text('|    Third option').attr('color','#999 ');


    if (!you.birthday) svg.append('rect').attr('x',0).attr('y',(me.fAge-minAge.allR)*(sSize+delta)-1).attr('width',width).attr('height',sSize+delta+1).attr('fill','#ccc');
    
    svg.selectAll('g').data(ages).enter().append('text').attr('class','axis')
        .style('text-anchor','middle')
        .text(function(d){ return d.text; })//.attr('font-size','12px')
        .transition()
        .attr('y',function(d){ return d.n*(sSize+delta)+tHeightAxis; })
        .attr('x',-labelWidth);
    
    d3.select('#button').style('display','none');
    svg.selectAll('g').data(fr).enter().append('svg:image').attr('id',function(d){return d.id})
        .attr('width',sSize).attr('height',sSize).attr('fill','#777')
        .attr('y',function(d){return (d.fAge-minAge.allR)*(sSize+delta); })
        .attr('xlink:href',function(d){
        return "http://graph.facebook.com/"+d.id+"/picture"})
        .on('mouseover',function(d){popup(d,this)});
    showAll();
} 
 
function popup(d,t){
    d3.select(t).on('mouseout',function(){
        d3.selectAll('.popup').attr('fill-opacity','0%').remove(); });
    d3.select('#back').on('click',function(){
        d3.selectAll('.popup').attr('fill-opacity','0%').remove(); 
        d3.select(this).on('click',null); });
    xx=1*d3.select(t).attr('x'); 
    yy=1*d3.select(t).attr('y');

    svg.append('rect').attr('class','popup').attr('stroke-width',0)
        .attr('y',yy).attr('x',xx+sSize).attr('height',pHeight).attr('width',pWidth)
        .attr('fill','#444').attr('fill-opacity','0%').transition().attr('fill-opacity','90%');
    svg.append('rect').attr('class','popup').attr('stroke-width',0)
        .attr('y',yy+sSize).attr('x',xx).attr('height',pHeight-sSize).attr('width',sSize)
        .attr('fill','#444').attr('fill-opacity','0%').transition().attr('fill-opacity','90%');

     pText=svg.append('text').attr('class','popup')
        .attr('fill-opacity','0%')
        .attr('fill','#fff').transition()
        .attr('fill-opacity','100%');
    d3.select('text.popup').append('tspan').attr('y',tHeight+yy).attr('x',sSize+2*tMargin+xx)
        .text(function(){return d.name}); 
    d3.select('text.popup').append('tspan').attr('y',2*tHeight+yy).attr('x',sSize+2*tMargin+xx)
        .text(function(){return d.fAge+' ('+d.birthday+')'});
}

function showAll(){
    d3.select('#all').style('cursor',null).style('font-weight','bold').on('click',null);
    d3.select('#fm').style('cursor','pointer').style('font-weight','normal').on('click',function(){showFM();});
    svg.selectAll('image')
        .transition()
        .attr('x',function(d){return d.ageNum*(sSize+delta)+labelWidth+xMargin; })
        .duration(800);
    svg.selectAll('.axis').transition().attr('x',(sSize+delta)/2+labelWidth/2+xMargin).duration(800);
}

function showFM(){
    d3.select('#fm').style('cursor',null).style('font-weight','bold').on('click',null);
    d3.select('#all').style('cursor','pointer').style('font-weight','normal').on('click',function(){showAll();});
    svg.selectAll('image')
        .transition()
        .attr('x',function(d){
            if (d.gender)
                if (d.gender=='female') return xMargin+(maxNum.f-d.ageNumF)*(sSize+delta)
                else return (maxNum.f+d.ageNumM)*(sSize+delta)+labelWidth+xMargin
            else return -sSize;
        })
        .duration(800);
    svg.selectAll('.axis').transition().attr('x',xMargin+(0.5+maxNum.f)*(sSize+delta)+labelWidth/2).duration(800);
}