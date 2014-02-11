<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Python Simple HTTP Server for testing POST and forms submission</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" type="text/css" href="/static/css/raw.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/themes.css" />
    </head>
    <body>
        <div class="autumn">
            <table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#L-1"> 1</a>
<a href="#L-2"> 2</a>
<a href="#L-3"> 3</a>
<a href="#L-4"> 4</a>
<a href="#L-5"> 5</a>
<a href="#L-6"> 6</a>
<a href="#L-7"> 7</a>
<a href="#L-8"> 8</a>
<a href="#L-9"> 9</a>
<a href="#L-10">10</a>
<a href="#L-11">11</a>
<a href="#L-12">12</a>
<a href="#L-13">13</a>
<a href="#L-14">14</a>
<a href="#L-15">15</a>
<a href="#L-16">16</a>
<a href="#L-17">17</a>
<a href="#L-18">18</a>
<a href="#L-19">19</a>
<a href="#L-20">20</a>
<a href="#L-21">21</a>
<a href="#L-22">22</a>
<a href="#L-23">23</a>
<a href="#L-24">24</a>
<a href="#L-25">25</a>
<a href="#L-26">26</a>
<a href="#L-27">27</a>
<a href="#L-28">28</a>
<a href="#L-29">29</a>
<a href="#L-30">30</a>
<a href="#L-31">31</a>
<a href="#L-32">32</a>
<a href="#L-33">33</a>
<a href="#L-34">34</a>
<a href="#L-35">35</a>
<a href="#L-36">36</a>
<a href="#L-37">37</a>
<a href="#L-38">38</a>
<a href="#L-39">39</a>
<a href="#L-40">40</a>
<a href="#L-41">41</a>
<a href="#L-42">42</a>
<a href="#L-43">43</a>
<a href="#L-44">44</a>
<a href="#L-45">45</a>
<a href="#L-46">46</a>
<a href="#L-47">47</a>
<a href="#L-48">48</a>
<a href="#L-49">49</a>
<a href="#L-50">50</a>
<a href="#L-51">51</a>
<a href="#L-52">52</a>
<a href="#L-53">53</a>
<a href="#L-54">54</a>
<a href="#L-55">55</a>
<a href="#L-56">56</a>
<a href="#L-57">57</a>
<a href="#L-58">58</a>
<a href="#L-59">59</a>
<a href="#L-60">60</a>
<a href="#L-61">61</a>
<a href="#L-62">62</a>
<a href="#L-63">63</a>
<a href="#L-64">64</a></pre></div></td><td class="code"><div class="highlight"><pre><span id="L-1"><a name="L-1"></a><span class="c">#!/usr/bin/python</span>
</span><span id="L-2"><a name="L-2"></a>
</span><span id="L-3"><a name="L-3"></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-4"><a name="L-4"></a><span class="sd">Save this file as server.py</span>
</span><span id="L-5"><a name="L-5"></a><span class="sd">&gt;&gt;&gt; python server.py 0.0.0.0 8001</span>
</span><span id="L-6"><a name="L-6"></a><span class="sd">serving on 0.0.0.0:8001</span>
</span><span id="L-7"><a name="L-7"></a>
</span><span id="L-8"><a name="L-8"></a><span class="sd">or simply</span>
</span><span id="L-9"><a name="L-9"></a>
</span><span id="L-10"><a name="L-10"></a><span class="sd">&gt;&gt;&gt; python server.py</span>
</span><span id="L-11"><a name="L-11"></a><span class="sd">Serving on localhost:8000</span>
</span><span id="L-12"><a name="L-12"></a>
</span><span id="L-13"><a name="L-13"></a><span class="sd">You can use this to test GET and POST methods.</span>
</span><span id="L-14"><a name="L-14"></a>
</span><span id="L-15"><a name="L-15"></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-16"><a name="L-16"></a>
</span><span id="L-17"><a name="L-17"></a><span class="kn">import</span> <span class="nn">SimpleHTTPServer</span>
</span><span id="L-18"><a name="L-18"></a><span class="kn">import</span> <span class="nn">SocketServer</span>
</span><span id="L-19"><a name="L-19"></a><span class="kn">import</span> <span class="nn">logging</span>
</span><span id="L-20"><a name="L-20"></a><span class="kn">import</span> <span class="nn">cgi</span>
</span><span id="L-21"><a name="L-21"></a>
</span><span id="L-22"><a name="L-22"></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-23"><a name="L-23"></a>
</span><span id="L-24"><a name="L-24"></a>
</span><span id="L-25"><a name="L-25"></a><span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">2</span><span class="p">:</span>
</span><span id="L-26"><a name="L-26"></a>    <span class="n">PORT</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
</span><span id="L-27"><a name="L-27"></a>    <span class="n">I</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-28"><a name="L-28"></a><span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-29"><a name="L-29"></a>    <span class="n">PORT</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-30"><a name="L-30"></a>    <span class="n">I</span> <span class="o">=</span> <span class="s">&quot;&quot;</span>
</span><span id="L-31"><a name="L-31"></a><span class="k">else</span><span class="p">:</span>
</span><span id="L-32"><a name="L-32"></a>    <span class="n">PORT</span> <span class="o">=</span> <span class="mi">8000</span>
</span><span id="L-33"><a name="L-33"></a>    <span class="n">I</span> <span class="o">=</span> <span class="s">&quot;&quot;</span>
</span><span id="L-34"><a name="L-34"></a>
</span><span id="L-35"><a name="L-35"></a>
</span><span id="L-36"><a name="L-36"></a><span class="k">class</span> <span class="nc">ServerHandler</span><span class="p">(</span><span class="n">SimpleHTTPServer</span><span class="o">.</span><span class="n">SimpleHTTPRequestHandler</span><span class="p">):</span>
</span><span id="L-37"><a name="L-37"></a>
</span><span id="L-38"><a name="L-38"></a>    <span class="k">def</span> <span class="nf">do_GET</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-39"><a name="L-39"></a>        <span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s">&quot;======= GET STARTED =======&quot;</span><span class="p">)</span>
</span><span id="L-40"><a name="L-40"></a>        <span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">)</span>
</span><span id="L-41"><a name="L-41"></a>        <span class="n">SimpleHTTPServer</span><span class="o">.</span><span class="n">SimpleHTTPRequestHandler</span><span class="o">.</span><span class="n">do_GET</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-42"><a name="L-42"></a>
</span><span id="L-43"><a name="L-43"></a>    <span class="k">def</span> <span class="nf">do_POST</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-44"><a name="L-44"></a>        <span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s">&quot;======= POST STARTED =======&quot;</span><span class="p">)</span>
</span><span id="L-45"><a name="L-45"></a>        <span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">)</span>
</span><span id="L-46"><a name="L-46"></a>        <span class="n">form</span> <span class="o">=</span> <span class="n">cgi</span><span class="o">.</span><span class="n">FieldStorage</span><span class="p">(</span>
</span><span id="L-47"><a name="L-47"></a>            <span class="n">fp</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">rfile</span><span class="p">,</span>
</span><span id="L-48"><a name="L-48"></a>            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
</span><span id="L-49"><a name="L-49"></a>            <span class="n">environ</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;REQUEST_METHOD&#39;</span><span class="p">:</span><span class="s">&#39;POST&#39;</span><span class="p">,</span>
</span><span id="L-50"><a name="L-50"></a>                     <span class="s">&#39;CONTENT_TYPE&#39;</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">[</span><span class="s">&#39;Content-Type&#39;</span><span class="p">],</span>
</span><span id="L-51"><a name="L-51"></a>                     <span class="p">})</span>
</span><span id="L-52"><a name="L-52"></a>        <span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s">&quot;======= POST VALUES =======&quot;</span><span class="p">)</span>
</span><span id="L-53"><a name="L-53"></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">form</span><span class="o">.</span><span class="n">list</span><span class="p">:</span>
</span><span id="L-54"><a name="L-54"></a>            <span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
</span><span id="L-55"><a name="L-55"></a>        <span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span>
</span><span id="L-56"><a name="L-56"></a>        <span class="n">SimpleHTTPServer</span><span class="o">.</span><span class="n">SimpleHTTPRequestHandler</span><span class="o">.</span><span class="n">do_GET</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-57"><a name="L-57"></a>
</span><span id="L-58"><a name="L-58"></a><span class="n">Handler</span> <span class="o">=</span> <span class="n">ServerHandler</span>
</span><span id="L-59"><a name="L-59"></a>
</span><span id="L-60"><a name="L-60"></a><span class="n">httpd</span> <span class="o">=</span> <span class="n">SocketServer</span><span class="o">.</span><span class="n">TCPServer</span><span class="p">((</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">PORT</span><span class="p">),</span> <span class="n">Handler</span><span class="p">)</span>
</span><span id="L-61"><a name="L-61"></a>
</span><span id="L-62"><a name="L-62"></a><span class="k">print</span> <span class="s">&quot;@rochacbruno Python http server version 0.1 (for testing purposes only)&quot;</span>
</span><span id="L-63"><a name="L-63"></a><span class="k">print</span> <span class="s">&quot;Serving at: http://</span><span class="si">%(interface)s</span><span class="s">:</span><span class="si">%(port)s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">dict</span><span class="p">(</span><span class="n">interface</span><span class="o">=</span><span class="n">I</span> <span class="ow">or</span> <span class="s">&quot;localhost&quot;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="n">PORT</span><span class="p">)</span>
</span><span id="L-64"><a name="L-64"></a><span class="n">httpd</span><span class="o">.</span><span class="n">serve_forever</span><span class="p">()</span>
</span></pre></div>
</td></tr></table>
        </div>
    </body>
</html>
