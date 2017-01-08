
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

        <form action="Books.py">

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
                                                        <li><a href="Home.py">Home</a></li>
							<li><a href="Movies.py">Movies</a></li>                   
							<li><a href="Twitterati.py">Twitterati</a></li>
							<li><a href="television.py">Television Soap Opera</a></li>
							<li><a class="active" href="Books.py">Books</a></li>
							<li><a href="Theatre.py">Theatre</a></li>
							<!--<li style="float:right"><input class="cl" type="submit" value="Log Out" name="bl"></li>-->
						</ul>
                                            </tr>
                                            <tr style="height:50%">

<!--<div style=" box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
<h2 style="color:White; text-align:center;">Calender:</h2>-->


<div class="dropdown">
  <button class="dropbtn"><h2>Calender&nbsp;&#8681;</h2></button>
  <div class="dropdown-content">


<p style="color:White">
From date: <br>
Year:"""



sd=form.getvalue('sd')
if sd:
    fm=form.getvalue('fmonth')
    fy=form.getvalue('fyear')
    fd=form.getvalue('fday')
    tm=form.getvalue('tmonth')
    ty=form.getvalue('tyear')
    td=form.getvalue('tday')
    
print "<select name='fyear'>"


    
for num in range(2000,2017):
    snum=str(num)
    if sd and snum==fy:
        print "<option value="+snum+" selected='selected'>"+snum+"</option>"
    else:
        print "<option value="+snum+">"+snum+"</option>"
    
##print "</select>&nbsp;&nbsp;Month:<select name='fmonth'>"
##print "<option value='1'>January</option><option value='2'>February</option>February<option value='3'>March</option><option value='4'>April</option>"
##print "<option value='5'>May</option><option value='6'>June</option><option value='7'>July</option><option value='8'>August</option>"
##print "<option value='9'>September</option><option value='10'>October</option><option value='11'>November</option><option value='12'>December</option>"
##print "</select>&nbsp;Day:<select name='fday'>"

print "</select>&nbsp;&nbsp;Month:<select name='fmonth'>"
Months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
mi=1
for m in Months:
    smi=str(mi)
    if sd and smi==fm:
        print "<option value='"+smi+"' selected='selected'>"+m+"</option>"
        #print smi
    else:
        print "<option value='"+smi+"'>"+m+"</option>"
    mi=mi+1
print "</select>&nbsp;Day:<select name='fday'>"

for num in range(1,31):
    snum=str(num)
    if sd and snum==fd:
        print "<option value="+snum+" selected='selected'>"+snum+"</option>"
    else:
        print "<option value="+snum+">"+snum+"</option>"
        
print "</select>"

print """<br><br>To date: <br>
Year:
<select name="tyear">"""
for num in range(2000,2017):
    snum=str(num)
    if sd and snum==ty:
        print "<option value="+snum+" selected='selected'>"+snum+"</option>"
    else:
        print "<option value="+snum+">"+snum+"</option>"
    
##print "</select>&nbsp;&nbsp;Month:<select name='tmonth'>"
##print "<option value='1'>January</option><option value='2'>February</option>February<option value='3'>March</option><option value='4'>April</option>"
##print "<option value='5'>May</option><option value='6'>June</option><option value='7'>July</option><option value='8'>August</option>"
##print "<option value='9'>September</option><option value='10'>October</option><option value='11'>November</option><option value='12'>December</option>"
##print "</select>&nbsp;Day:<select name='tday'>"

print "</select>&nbsp;&nbsp;Month:<select name='tmonth'>"
mi=1
for m in Months:
    smi=str(mi)
    if sd and smi==tm:
        print "<option value="+smi+" selected='selected'>"+m+"</option>"
        
    else:
        print "<option value="+smi+">"+m+"</option>"
    mi=mi+1
        
print "</select>&nbsp;Day:<select name='tday'>"
        
for num in range(1,31):
    snum=str(num)
    if sd and snum==td:
        print "<option value="+snum+" selected='selected'>"+snum+"</option>"
    else:
        print "<option value="+snum+">"+snum+"</option>"
        
print "</select><br> <br>"

print "<input type='checkbox' name='sd' value='sd'>Search by date</p>"

print """   </div>
                    </div>
				</tr>
				</table>
					
					</td>
					
					
					<td  style="background-color: #DCDCDC; height:550px; width:65%;">

                                            <table style="width:100%">

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
						<input type="submit" class="button" name="bb" value="Authors" />&nbsp;
						<input type="submit" class="button" name="bb" value="New Releases" />&nbsp;
						<input type="submit" class="button" name="bb" value="Reviews" />&nbsp;
						<input type="submit" class="button" name="bb" value="Awards" />&nbsp;
						

						<br><br>
                                               </div>
						
                                            </td>
                                            </tr>
                                            <tr>
                                            <td style="">
                                                <div style="width:100%; height: 500px; overflow:scroll; ">
						<br><br><br>

                                                
						"""

#<a href="search.py">Search</a>
#if search and t:


if bb:

    fot=form.getvalue('fot')
    if fot=="simple":
        inentities='true'
    else:
        inentities='false'
    
    cnt=form.getvalue('notw')
    #print cnt
    s="book%20"+bb+"%20OR%20books%20author%20"+bb+"-filter:retweets" 
    if sd:
        snc=fy+"-"+fm+"-"+fd
        print " since ", snc
        untl=ty+"-"+tm+"-"+td
        print "  until ", untl
        iterator = twitter.search.tweets(q=s, lang='en', since=snc, until=untl, result_type='mixed', count=cnt, include_entities=inentities)
    else:
        iterator = twitter.search.tweets(q=s, lang='en', result_type='mixed', count=cnt, include_entities=inentities)
    #s="movie%20"+bb+"%20OR%20actor%20"+bb
    
    tweets = iterator["statuses"]
    tweet_count = 100


    if fot=="simple":

        for tweet in tweets:
                                                               
            if 'text' in tweet:
                                                     
                print """<div class="polaroid">"""
                text = tweet['text']
                entities = tweet['entities']
        
                if 'media' in entities:
                    for media_element in entities['media']:
                        if media_element['type'] == 'photo':
                            text = text.replace(media_element['url'], '')
                        #if media_element['type'] == 'video':
                            #text = text.replace(media_element['url'], '')

                if 'urls' in entities:
                    for url_element in entities['urls']:
                        if url_element['url']:
                            us="<a href='"+url_element['url']+"' title='"+url_element['expanded_url']+"'>"+ url_element['display_url']+"</a>"
                            text = text.replace(url_element['url'], us)

                if 'extended_entities' in tweet:
                    ee = tweet['extended_entities']
                    if ee['media']:
                        media=ee['media'][0]
                        #print "EE: type:", media['type']
                        if media['type']=='video':
                            variants=media['video_info']['variants']
                            for variant in variants:
                                if variant['content_type']=='video/mp4':
                                    print "<br><video  style='width:100%;' controls><source src='"+variant['url']+"' type='video/mp4'>Video cannot be played</video>"
                                    break;
                        else:
                            print "<br><img src='", media['media_url_https']
                            print "' alt='Image cannot be displayed.' style='width:100%;'/>"
                    
                print "<div class='container'> "
                print "<img src='"+tweet["user"]["profile_image_url_https"]+"' alt='img' style='vertical-align:middle;'>"
                if tweet['user']['name']:
                    print "<b>&nbsp;&nbsp;"+tweet['user']['name'].encode('utf-8')+"</b>"
                if tweet['user']['screen_name']:
                    print "<font color='gray'>&nbsp;&nbsp;@"+tweet['user']['screen_name'].encode('utf-8')+"</font><br>"

                print "<br>Tweet:    ", text.encode('utf-8')

                print "<br><small><font color='gray'>"

                crt=tweet["created_at"].split();
                crt1=""+crt[1]+" "+crt[2]+" "+crt[5]

                print " <hr> Created at: "+crt[3]+" - "+crt1
                
                if tweet["favorite_count"]:
                    print "  &nbsp;&nbsp;&nbsp;&nbsp;     Likes:", tweet["favorite_count"]
                if tweet["retweet_count"]:
                    print "  &nbsp;&nbsp;&nbsp;&nbsp;     Re-tweets:", tweet["retweet_count"]
                print "</font></small></p> </div></div><br>"



    else:

        for tweet in tweets:
                                                               
            if 'text' in tweet:

                resp = twitter.statuses.oembed(_id=tweet['id_str'])

                print "<div class='polaroid'>"+resp['html'].encode('utf-8')+" </div><br>"
                
                #tweet_count += 1
                #print " TWEET COUNT: ", tweet_count

        


print """
                </td>	</tr> 	</table>		</div>

						<br />
						<br />

					</td>
                                        
					<td style="background-color: black; color:white; text-align:center; vertical-align:top;">
					<table border="2">
                                        <tr>
					<img src="http://plusquotes.com/images/quotes-img/Happy_birthday.jpg" height="150" width="200" alt="Birthdays:">
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

print"""                                </tr>
                                        <tr style="border: 3px solid black;">
                                        <div style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
                                        <hr><h2><br>Format of <br>Tweets:</h2><br> """

fot = form.getvalue('fot')
if fot=="simple":
    print """ <input type="radio" name="fot" value="simple" checked="checked">Simple (Faster) <br>"""
elif fot:
    print """ <input type="radio" name="fot" value="simple" >Simple (Faster) <br>"""
else:
    print """ <input type="radio" name="fot" value="simple" checked="checked" >Simple (Faster) <br>"""

if fot=="embed":
    print """ <input type="radio" name="fot" value="embed" checked="checked">Embedded (Slower) """
else:
    print """ <input type="radio" name="fot" value="embed">Embedded (Slower) """
print """

<br>No. of Tweets:&nbsp;<input type="number" name="notw" min="1" max="100" value="25">
</div></tr></table></td>
				</tr>		
				</div>
				</table>
            </div>

        </form>



    </body>
</html>"""

