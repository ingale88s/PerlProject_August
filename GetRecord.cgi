#!C:/Strawberry/perl/bin/perl.exe
use strict;
use warnings;

use CGI;
use JSON;
use Template;
use DBI;
use CGI qw(:standard);
use JSON;

my $q = new CGI;

my $driver   = "SQLite"; 
my $database = "PerlDB.db";
my $dsn = "dbi:SQLite:dbname=$database";
my $userid = "";
my $password = "";

my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 });

    my $sth = $dbh->prepare('select * from appointment');
    my $result = $sth->execute();

    my $desc_filter = $q->param('desc');
    if( defined $desc_filter){
            $sth = $dbh->prepare('select * from appointment where desc like ?');
            $result = $sth->execute($desc_filter);
    }
print $q->header('application/json');
my @data_to_json; 
while ( my ($date, $time, $desc ) = $sth->fetchrow_array ) {
    my $data_to_json = {date=>$date,time=>$time,desc=>$desc};
    push @data_to_json, $data_to_json;
}
print to_json(\@data_to_json);
    
$dbh->disconnect;
