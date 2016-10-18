
# to run type in browser: http://localhost:8000/Movies1.py


# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError

# Import modules for CGI handling 
import cgi, cgitb
import urllib2

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
                
        </style>

    </head>
    <body style="background-image: url('bg_vertical.jpg');">

        <h1>Welcome!</h1>

        <form action="Movies1.py">

            <div class="class1" align="center">

                <div class="class2" align="left" >
                    <table >
                        <tr>
                            <td>
                                <img class="imgclass" src="http://r.ddmcdn.com/s_f/o_1/cx_633/cy_0/cw_1725/ch_1725/w_720/APL/uploads/2014/11/too-cute-doggone-it-video-playlist.jpg" alt="Photo: <%=un%>"/>
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
							<li><a class="active" href="Movies.py">Movies</a></li>                   
							<li><a href="Twitterati.py">Twitterati</a></li>
							<li><a href="Tvsoaps.py">Television Soap Opera</a></li>
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
						<input type="submit" class="button" name="bb" value="Trailers" />&nbsp;
						<input type="submit" class="button" name="bb" value="Controversies" />&nbsp;
						<input type="submit" class="button" name="bb" value="Birthdays" />&nbsp;
						<input type="submit" class="button" name="bb" value="Facts" />&nbsp;
						<input type="submit" class="button" name="bb" value="Famous Dialogues" />&nbsp;
						<input type="submit" class="button" name="bb" value="Time-lapse" />&nbsp;
						<input type="submit" class="button" name="bb" value="Place of shoot" />&nbsp;
						<input type="submit" class="button" name="bb" value="Actors" />&nbsp;
						<input type="submit" class="button" name="bb" value="Reviews" />
						
                                                </div>
						
                                            </td>
                                            </tr>
                                            <tr>
                                            <td>
						<div style="width:100%; height: 500px; overflow: scroll;">
						<br><br><br>"""

print "<img src='https://giphy.com/gifs/baby-asian-uB6QWX8osFdo4'>"
print """<iframe src="//giphy.com/embed/uB6QWX8osFdo4" width="480" height="218" frameBorder="0" class="giphy-embed"
allowFullScreen></iframe><p><a href="https://giphy.com/gifs/baby-asian-uB6QWX8osFdo4">via GIPHY</a></p>"""

##print """<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Nakshatram Movie First Ten Looks Countdown Promo
##| 1 Days To Go | Latest Trailers 2016: <a href="https://t.co/7oKXMJVqap">https://t.co/7oKXMJVqap</a> via <a href="https://twitter.com/YouTube">@YouTube</a>
##</p>&mdash; Tollywood Filmnagar (@tfnagar) <a href="https://twitter.com/tfnagar/status/784411052591026176">October 7, 2016</a></blockquote>
##<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>""" 

if bb:
    #movie%20trailers%20OR%20actors%20trailors
    #s="movie "+bb+" OR actors "+bb
    #s="movie%20trailer%20OR%20actor%20trailer"
    #s="movie%20"+bb+"%20OR%20actor%20"+bb
    #s="video -include:retweets"
    s="movies"
    iterator = twitter.search.tweets(q=s, lang='en', result_type='mixed', count=100, include_entities='false')
    tweets = iterator["statuses"]
    tweet_count = 100

    for tweet in tweets:
                                                               
        if 'text' in tweet:

            
            #resp = urllib2.urlopen("https://api.twitter.com/1.1/statuses/oembed.json?id="+tweet['id_str']).read()
            #resp = url.get("https://api.twitter.com/1.1/statuses/oembed.json?id="+tweet['id_str'])
            #print resp["html"]
            #print resp[2]
            #print resp
            
            #oem = NewFromJsonDict(resp)
            #print oem.GetHTML(resp)

            
            #twitter.statuses.oembed(_id=tweet['id_str'])
            resp = twitter.statuses.oembed(_id=tweet['id_str'])
            #print resp
            #print "\n\ntttttttttt"
            print resp['html'].encode('utf-8')
                                                 
##            print """<div style='border-radius: 10px; border: 2px solid #191970;
##            padding: 3px; background-color: white; position:relative; left:10%;
##            width:80%; '><p> """
##                                                
##            tweet_count -= 1
##            if tweet['user']['name']:
##                print "User: ",tweet['user']['name'].encode('utf-8')
##            if tweet['user']['screen_name']:
##                print " &nbsp;&nbsp;&nbsp;  Screen name:  ",tweet['user']['screen_name'].encode('utf-8')
##
##            text = tweet['text']
##            entities = tweet['entities']
##            
##            #text=tweet["text"]
##            #entities = tweet["entities"]
##            if 'media' in entities:
##                for media_element in entities['media']:
##                    if media_element['type'] == 'photo':
##                        text = text.replace(media_element['url'], '')
##                    #if media_element['type'] == 'video':
##                        #text = text.replace(media_element['url'], '')
##
##            if 'urls' in entities:
##                for url_element in entities['urls']:
##                    if url_element['url']:
##                        us="<a href='"+url_element['url']+"' title='"+url_element['expanded_url']+"'>"+ url_element['display_url']+"</a>"
##                        text = text.replace(url_element['url'], us)
##
##                
##            print "<hr> Tweet:    ", text.encode('utf-8')
##            
##
####            if 'media' in entities:
####                for media_element in entities['media']:
####                    if media_element['type'] == 'photo':
####                        #text = text.replace(media_element['url'], '')
####                        #print "<iframe src='", media_element['media_url_https']
####                        #print "'></iframe>"
####                        print "<img src='", media_element['media_url_https']
####                        print "' />"
##
##
####            if 'extended_entities' in tweet:
####                ee = tweet['extended_entities']
####                #if ee['type'] == 'video':
####                        #text = text.replace(media_element['url'], '')
####                print "EE: type:", ee['type']
####                print "<iframe src='", ee['media_url_https']
####                print "'></iframe>"
##
##            if 'extended_entities' in tweet:
##                ee = tweet['extended_entities']
##                
##                if ee['media']:
##                    media=ee['media'][0]
##                    #print "EE: type:", media['type']
##                    if media['type']=='video':
##                        variants=media['video_info']['variants']
##                        for variant in variants:
##                            if variant['content_type']=='video/mp4':
##                                print "<br><video controls><source src='"+variant['url']+"' type='video/mp4'>Video cannot be played</video>"
##                                break;
##
##                    else:
##                        print "<br><img src='", media['media_url_https']
##                        print "' alt='Image cannot be displayed.' />"
##                        
####                        print "<iframe src='", media['media_url_https']
####                        print "'></iframe>"
####                    else:
####                        print "<img src='", media['media_url_https']
####                        print "' />"
##
##                        
##
##            #if 'urls' in entities:
##            #    for url_element in entities['urls']:
##            #        if url_element['url']:
##            #            #text = text.replace(url_element['url'], 'gggggg')
##            #            print "URL: <iframe src='", url_element['url']
##            #            print "'></iframe>"
##                        
##            
##            #if entities['media']['media_url_https']:
##            #    print "<iframe src='", entities["media"]["media_url_https"]
##            #    print "'></iframe>"
##
##            print "<br><small>"
##            print " <hr> Created at:", tweet["created_at"].encode('utf-8')
##            
##            if tweet["favorite_count"]:
##                print "  &nbsp;&nbsp;&nbsp;&nbsp;     Likes:", tweet["favorite_count"]
##            if tweet["retweet_count"]:
##                print "  &nbsp;&nbsp;&nbsp;&nbsp;     Re-tweets:", tweet["retweet_count"]
##            print "</small></p></div><br>"
##            #print "<br><br><br>", tweet_count
            if tweet_count <= 0:
                print "<br><br><br>", tweet_count
                break



print """		</td>	</tr> 	</table>		</div>

						<br />
						<br />

					</td>
				</tr>		
				</div>"""
print "<br><br><br>", tweet_count
print """

				
				</table>
            </div>

        </form>



    </body>
</html>"""

