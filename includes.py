#!/usr/local/bin/python

from random import choice


quotes = ["'Love hides in molecular structures.' Jim Morrison",\
 "'The more that you read, the more things that you'll know. The more that you learn, the more places you'll go.' Dr. Suess",\
"'When you get blue, and you've lost all your dreams, there's nothing like a camp fire and a can of beans.' Tom Waits",\
#"'I urge you to please notice when you are happy, and exclaim or murmur or think at some point, \"If this isn\'t nice, I don't know what is.\"' Kurt Vonnegut Jr. (attributed to his uncle, Alex)",\
"'I really wonder what gives us the right to wreck this poor planet of ours.' Kurt Vonnegut Jr.",\
#"'If people think nature is their friend, then they sure don't need an enemy.' Kurt Vonnegut Jr.",\
#"'The sun's not yellow, it's chicken.' Bob Dylan",\
"'The well-meaning contention that all ideas have equal merit seems to me little different from the disastrous contention that no ideas have any merit.' Carl Sagan",\
"'I suppose that apples might start to rise tomorrow but the possibility does not merit equal time in physics classrooms.' Stephen Jay Gould"]

#colors = ["#230000","#000023","#000013"]
colors = ["#000013"]
def get_header():
    
    color = choice(colors)
    return """<html>
<head>
<STYLE TYPE="text/css">
    BODY
        {
        color:#666666;
        font-family:verdana, ariel;
        line-height:1.7em;
		margin: 0;
		padding: 0;
        }
    H2
        {
        color:469103;
        font-size:3.18em;
        font-family:monospace
        }
    H3
        {
        color:469103;
        font-size:2.45em;
        font-family:monospace
        }
    H4
        {
        color:""" + color + """;
        font-size:1.8em;
        font-family:monospace
		}
    a:link {
			text-decoration: none;
            color:""" + color + """;
    }

    a:visited {
			text-decoration: none;
            color:""" + color + """;
    }

    a:hover {
			text-decoration: none;
            color:#FFFFFF;
            background-color:""" + color + """;
    }

	p, li {
		margin:0px 30px 10px 30px;
		font-size:0.75em;
		}


table.header {
	border-width: 0px 0px 0px 0px;
	border-spacing: 0px;
	border-style: none none none none;
	border-color: white white white white;
	border-collapse: separate;
	background-color: white;
}
table.header th {
	border-width: 0px 0px 0px 0px;
	padding: 0px 0px 0px 0px;
	border-style: none none none none;
	border-color: white white white white;
	background-color: white;
	-moz-border-radius: 0px 0px 0px 0px;
}
table.header td {
	border-width: 0px 0px 0px 0px;
	padding: 0px 0px 0px 0px;
	border-style: none none none none;
	border-color: white white white white;
	background-color: """ + color + """;
	-moz-border-radius: 0px 0px 0px 0px;
}


table.footer {
	border-width: 0px 0px 0px 0px;
	border-spacing: 0px;
	border-style: none none none none;
	border-color: white white white white;
	border-collapse: separate;
	background-color: white;
}
table.footer th {
	border-width: 0px 0px 0px 0px;
	padding: 0px 0px 0px 0px;
	border-style: none none none none;
	border-color: white white white white;
	background-color: white;
	-moz-border-radius: 0px 0px 0px 0px;
}
table.footer td {
	border-width: 0px 0px 0px 0px;
	padding: 0px 0px 0px 0px;
	border-style: none none none none;
	border-color: white white white white;
	background-color: """ + color + """;
	-moz-border-radius: 0px 0px 0px 0px;
}

</STYLE>

<title>JG Caporaso</title></head>

<body>
<center>
	<table class=header width=100%>
		<tr>
			<td width=100% height=20px align=right valign=middle>
				<font color=white size=+3>&nbsp;&nbsp;&nbsp;&nbsp;</font>
			</td>
		</tr>
	</table>"""

	
def get_footer():
    quote = choice(quotes)
    return """<table width=100%>
		<tr>
			<td width=100% height=30px align=right valign=middle>
			<a rel="license" href="http://creativecommons.org/licenses/by/3.0/us/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/us/88x31.png" /></a><br><font size=-2>This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/us/">Creative Commons Attribution 3.0 United States License</a></font>.
            </td>
		</tr>
	<table class=footer width=100%>
		<tr>
			<td width=85% height=30px align=left valign=middle>
				<font color=white size=-2><i>&nbsp;&nbsp;""" + quote + """</i></font>
			</td>
			<td width=5%>&nbsp;</td>
			<td width=10% height=30px align=right valign=middle>
				<font color=white size=-2>
				J. Gregory Caporaso&nbsp;&nbsp;&nbsp;<br>gregcaporaso@gmail.com&nbsp;&nbsp;&nbsp;</font>
			</td>
		</tr>
	</table>
</center>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-6636235-1");
pageTracker._trackPageview();
} catch(err) {}</script>
</body>
</html>

<!-- Page by Greg Caporaso gregcaporaso@gmail.com -->

"""



def get_filler_space(num_lines=10):
    return '\n'.join(["<p>&nbsp;</p>"] * num_lines)