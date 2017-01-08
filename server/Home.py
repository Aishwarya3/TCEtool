
# to run type in browser: http://localhost:8000/Home.py


# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError

# Import modules for CGI handling 
import cgi, cgitb 
import time
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
bb = form.getvalue('bb')
t = form.getvalue('t')
search = form.getvalue('search')

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '778543465860915200-2e6vYoCTyhmqQdBcRV5r1LQvK8SLpez'
ACCESS_SECRET = 'RB5lFlpwWRo4Ieu3eVNEUYzrG7Wr3T2yOvTYDgcUQQump'
CONSUMER_KEY = 'Wq5WnCX5fiNyuPPmgEXHPj9G4'
CONSUMER_SECRET = 'YQhF1tAVH5Jn5AlaiE7NprgoLXJdMET0nlfrlEdplAJoY1bxsA'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)



print """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Home</title>

        <style type="text/css">
            .style3
            {
                width: 231px;
            }
            .style4
            {
                height: 28px;
            }
            .style5
            {
                height: 28px;
                width: 231px;
            }
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            li {
                float: top;
                border-bottom:1px solid #bbb;
                
            }

            li:first-child {
                //border-right: none;
                border-top:1px solid #bbb;
            }

            li a {
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            li a:hover:not(.active) {
                background-color: #111;
            }

            .active {
                background-color: #4CAF50;
            }

            .class1 {
                background-color:White; 
                height:100vh; 
                width:96%; 
                position:relative; 
                left:2%; 
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
            }
            
            .class2 {
                background-color:#000033; 
                height: 89px; 
                width: 100%; 
                color: White;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
                     /* position:relative; top:-307px; left: 238px; */ 
            }
            
            .imgclass {
                margin-top:0px; 
                border-radius:25%; 
                width:106px; 
                height:86px
            }
            
            .unclass {
                font-family:'Lucida Handwriting'; 
                font-size:X-Large; 
                color:White;
            }
            
            .ulclass {
                font-size:x-large;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
            }
            
            input[type = "submit"] {
                font-family:Lucida Bright; 
                font-size:15px; 
                height:40px; 
                margin-left: 0px; 
                box-shadow: 3px 3px;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); 
            }

            .table1 {
                color:Black; 
                background-color:White; 
                font-family:'Times new roman'; 
                font-size:large;
				font-weight:bold;
				width:100%;
				vertical-align:top;
                       /* position:relative; top:-307px; left: 238px; */
                
            }
            
            .cl {
                background-color: black;
                font-size:50px;
                height:50px;
                color: white;
                //font-family: serif;
                }
				
            .button {
                    background-color: #4CAF50; /* Green */
                    border: 1px solid green;
                    color: white;
                    padding: 5px 14px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    cursor: pointer;
                    float: left;
            }

            .button:hover {
                    background-color: #3e8e41;
            }

            div.polaroid {
              //width: 250px;
              box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
              //text-align: center;
              //border: 2px solid #191970;
              background-color: white;
              position:relative; left:23%;
              font-family:Arial;
              width:54%; 
            }

            div.container {
              padding: 10px;
            }

            .dropbtn {
                background-color: black;
                color: white;
                //padding: 16px;
                //padding: 50px 50px 50px 50px;
                padding-left: 80px;
                padding-right:80px;
                
                font-size: 16px;
                border: none;
                cursor: pointer;
                width:100%
            }

            .dropdown {
                position: relative;
                display: inline-block;
            }

            .dropdown-content {
                display: none;
                position: absolute;
                background-color: black;
                overflow:auto;
                width:100%;
                //min-width: 160px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            }

            /*.dropdown-content a {
                color: black;
                padding: 12px 16px;
                text-decoration: none;
                display: block;
            }

            .dropdown-content a:hover {background-color: #f1f1f1}
            */


            .dropdown:hover .dropdown-content {
                display: block;
            }

            .dropdown:hover .dropbtn {
                background-color: #3e8e41;
            }
                
        </style>

    </head>
    <body style="background-image: url('http://www.pixelstalk.net/wp-content/uploads/2016/06/Light-Blue-Backgrounds-Free-Downlaod.jpg');">

        <br><br>

        <form action="Home.py">

            <div class="class1" align="center">

                <div class="class2" align="left" >

                     <table >
                        <tr>
                            <td colspan="4" style="padding-left:20px;">
                                <p class="unclass">Entertainment</p>
                            </td>
                            <td style="align:left; float:left">
                            <p class="unclass">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <!--<input type="text" name="t" value="search" style="color:grey;font-family:Lucida Bright; font-size:15px; height:30px; margin-left:0px;
                            box-shadow: 3px 3px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">&nbsp;
                            <input type="submit" name="search" value="Search">-->
                            <a href="Search1.py" style="color:white">Search</a>
                            
                            </p>
                            </td>
                        </tr>
                    </table>
                </div>
				
					
				
				<br />
				<br />

				<div>
				
				<table class="table1">
				
				<tr>
				
					<td style="background-color:black; align:left; width:20%; height:100%; vertical-align:top;">

                                            <table>
                                            <tr>
						<ul style="font-size:x-large;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
						        <li><a class="active" href="Home.py">Home</a></li>
							<li><a href="Movies.py">Movies</a></li>                  
							<li><a href="Twitterati.py">Twitterati</a></li>
							<li><a href="television.py">Television Soap Opera</a></li>
							<li><a href="Books.py">Books</a></li>
							<li><a href="Theatre.py">Theatre</a></li>
							<!--<li style="float:right"><input class="cl" type="submit" value="Log Out" name="bl"></li>-->
						</ul>
                                            </tr>
                                            <tr style="height:50%">

<!--<div style=" box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
<h2 style="color:White; text-align:center;">Calender:</h2>


<div class="dropdown">
  <button class="dropbtn"><h2>Calender&nbsp;&#8681;</h2></button>
  <div class="dropdown-content">


<p style="color:White">
From date: <br>
Year: -->"""




print """   </div>
                    </div>
				</tr>
				</table>
					
					</td>
					
					
					<td  style="background-color: #DCDCDC; height:550px; width:65%;">
                                           <img src="http://www.sethlevine.com/wp-content/uploads/welcome.jpg" width="99%" height="140%" border="5"  alt="Photo: <%=un%>"/>
                                           <!-- <table>

                                            <tr>
                                            <td style="">
                                                <div style="width:100%; height: 500px; overflow:scroll; ">
						<br><br><br> -->

                                                
						"""


print """
              <!--  </td>	</tr> 	</table> -->		</div>

						<br />
						<br />

					</td>
                                        
					<td style="background-color: black; color:white; text-align:center; vertical-align:top;">
					<table border="2">
                                        <tr>
					<img src="http://plusquotes.com/images/quotes-img/Happy_birthday.jpg" height="150" width="225" alt="Birthdays:">
                                        </img>
                                        </tr>
                                        <tr>
                                        

"""
print "<h3>Date: "+(time.strftime("%d/%m"))+"</h3>"

fo = open("Birthdaysorted.txt", "r")
list = fo.read()
newlist = list.split("\n")
fo.close()

date=time.strftime("%d")
month=time.strftime("%m")
ndate=int(date)
nmonth=int(month)

for l in newlist:
    #print l
    bd = l.split()
    #print bd
    lmonth = int(bd[4])
    ldate = int(bd[3])
    if nmonth < lmonth:
        break
    if nmonth==lmonth:
        if ndate==ldate:
            print "<h3>"+bd[0] + " " + bd[1]+"</h3>"

print """</div></tr></table></td>
				</tr>		
				</div>
				</table>
            </div>

        </form>



    </body>
</html>"""

