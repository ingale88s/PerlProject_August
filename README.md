# Test_August


To run this project Follow these steps

#!C:/Strawberry/perl/bin/perl.exe
1. Keep PerlDB.db file in your running folder (typically it can be C:\Apache24\cgi-bin)
2. Place GetRecord.cgi and AddRecord.cgi in \Apache24\cgi-bin folder and check perl exe location is correct (#!C:/Strawberry/perl/bin/perl.exe), otherwise change the location.
3. Place Index.html in your html document folder (\Apache24\htdocs)
4. After following above steps run the localhost/index.html
5. Check out screenshots for better understanding

Note: If you get any 'Internal server error', then take a look at ajax url: "/cgi-bin/GetRecord.cgi" and form action="/cgi-bin/AddRecord.cgi" , if you kept files in some other folder then change these paths.
