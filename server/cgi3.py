# Import modules for CGI handling 
import cgi, cgitb

print """ <html>
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
                float: left;
                border-right:1px solid #bbb;
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
                //height:100vh; 
                width:80%; 
                position:relative; 
                left:10%; 
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
                font-family:Comic Sans MS; 
                font-size:large;
                       /* position:relative; top:-307px; left: 238px; */
                
            }
            
            .cl {
                background-color: black;
                font-size:50px;
                height:50px;
                color: white;
                //font-family: serif;
                }
                
        </style>

    </head>
    <body style="background-image: url('bg_vertical.jpg');">

        <h1>Welcome!</h1>
        
                
        
        <form action="Home.jsp">

            <div class="class1" align="center">

                <div class="class2" align="left" >
                    <table >
                        <tr>
                            <td>
                                <img class="imgclass" src="bg_vertical.jpg" alt="Photo: <%=un%>"/>
                            </td>
                            <td colspan="4">
                                <p class="unclass">ash</p>
                            </td>
                        </tr>
                    </table>
                </div>

                <br />
                <br />


                <ul style="font-size:x-large;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
                    <li><a class="active" href="Home.jsp">Home</a></li>                   
                    <li><a href="Profile.jsp">Profile</a></li>
                    <li><a href="SendReq.jsp">Friend requests</a></li>
                    <li><a href="Friends.jsp">Friends</a></li>
                    <li><a href="FriendProfile.jsp">View Users</a></li>
                    <li style="float:right"><input class="cl" type="submit" value="Log Out" name="bl"></li>
                </ul>

                                    <br>
                    <br>
            </div>

        </form>

                    <br>
                    <br>

    </body>
</html>
 """
