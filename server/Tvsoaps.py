
# to run type in browser: http://localhost:8000/Movies.py


# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
bb = form.getvalue('bb')

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

            li:last-child {
                border-right: none;
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
                
        </style>

    </head>
    <body style="background-image: url('bg_vertical.jpg');">

        <h1>Welcome!</h1>

        <form action="Tvsoaps.py">

            <div class="class1" align="center">

                <div class="class2" align="left" >
                    <table >
                        <tr>
                            <td>
                                <img class="imgclass" src="bg_vertical.jpg" alt="Photo: <%=un%>"/>
                            </td>
                            <td colspan="4">
                                <p class="unclass">Entertainment</p>
                            </td>
                            <td style="align:left; float:left">
                            <p class="unclass">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search:&nbsp;&nbsp;<input type="text" name="t" value="search" style="color:grey;font-family:Lucida Bright; font-size:15px; height:30px; margin-left: 0px; box-shadow: 3px 3px;
                                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);"></p>
                            </td>
                        </tr>
                    </table>
                     
                </div>
				
					
				
				<br />
				<br />

				<div>
				
				<table class="table1">
				
				<tr>
				
					<td style="background-color:black; align:left; width:20%; height:100%">
					
						<ul style="font-size:x-large;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
                                                        <li><a href="Home.py">Home</a></li>
							<li><a href="Movies.py">Movies</a></li>                   
							<li><a href="Twitterati.py">Twitterati</a></li>
							<li><a class="active" href="Tvsoaps.py">Television Soap Opera</a></li>
							<li><a href="Books.py">Books</a></li>
							<li><a href="Theatre.py">Theatre</a></li>
							<!--<li style="float:right"><input class="cl" type="submit" value="Log Out" name="bl"></li>-->
						</ul>
					
					</td>
					
					
					<td  style="background-color: #DCDCDC; height:550px;">

                                            <table>

                                            <tr> <td>
                            
                                                <div style="width:100%; font-size:smaller; height:100%">
						<!--<ul style="font-size:x-large;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
							<li><a class="active" href="Home.jsp">Home</a></li>                   
							<li><a href="Profile.jsp">Profile</a></li>
							<li><a href="SendReq.jsp">Friend requests</a></li>
							<li><a href="Friends.jsp">Friends</a></li>
							<li><a href="FriendProfile.jsp">View Users</a></li>
							<!--<li style="float:right"><input class="cl" type="submit" value="Log Out" name="bl"></li>
						</ul>
						-->
						<input type="submit" class="button" name="bb" value="Fan Theory" />&nbsp;
						<input type="submit" class="button" name="bb" value="Characterization" />&nbsp;
						<input type="submit" class="button" name="bb" value="Facts" />&nbsp;
						<input type="submit" class="button" name="bb" value="Plot" />&nbsp;
						<input type="submit" class="button" name="bb" value="Actors" />&nbsp;
						<input type="submit" class="button" name="bb" value="Awards" />&nbsp;
						<input type="submit" class="button" name="bb" value="Reviews" />
						
                                                </div>
						
                                            </td>
                                            </tr>
                                            <tr>
                                            <td>
						<div style="width:100%; height: 500px; overflow: scroll;">
						<br><br><br>"""


if bb:
    #movie%20trailers%20OR%20actors%20trailors
    #s="movie "+bb+" OR actors "+bb
    #s="movie%20trailer%20OR%20actor%20trailer"
    s="tv%20"+bb+"%20OR%20soaps%20"+bb+"%20OR%20series%20"+bb
    iterator = twitter.search.tweets(q=s, lang='en')
    tweets = iterator["statuses"]
    tweet_count = 10000

    for tweet in tweets:
                                                               
        if 'text' in tweet:
                                                 
            print """<div style='border-radius: 10px; border: 2px solid #191970;
            padding: 3px; background-color: white; position:relative; left:10%;
            width:80%; '><p> """
                                                
            tweet_count -= 1
            if tweet['user']['name']:
                print "User: ",tweet['user']['name'].encode('utf-8')
            if tweet['user']['screen_name']:
                print " &nbsp;&nbsp;&nbsp;  Screen name:  ",tweet['user']['screen_name'].encode('utf-8')
            print "<hr> Tweet:    ", tweet["text"].encode('utf-8')
            print "<br><small>"
            print " <hr> Created at:", tweet["created_at"].encode('utf-8')
            if tweet["favorite_count"]:
                print "  &nbsp;&nbsp;&nbsp;&nbsp;     Likes:", tweet["favorite_count"]
            if tweet["retweet_count"]:
                print "  &nbsp;&nbsp;&nbsp;&nbsp;     Re-tweets:", tweet["retweet_count"]
            print "</small></p></div><br>"
            if tweet_count <= 0:
                print "<br><br><br>", tweet_count
                break


print """		</td>	</tr> 	</table>		</div>

						<br />
						<br />

					</td>
				</tr>		
				</div>
				</table>
            </div>

        </form>



    </body>
</html>"""

