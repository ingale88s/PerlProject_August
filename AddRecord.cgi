#!C:/Strawberry/perl/bin/perl.exe
	#Developer: Sandeep Ingale
use strict;
use warnings;

use CGI;
use JSON;
use Template;
use DBI;
use CGI qw(:standard);
use JSON;

my $driver   = "SQLite"; 
my $database = "PerlDB.db";
my $dsn = "dbi:SQLite:dbname=$database";
my $userid = "";
my $password = "";

my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 });

my $sth = $dbh->prepare('
   INSERT INTO appointment (date, time, desc)
   VALUES (?,?,?)
');

my $q = new CGI;
my %data;
my $date = $q->param('date');
my $time = $q->param('time');
my $desc = $q->param('desc');

my $result = $sth->execute($date,$time,$desc);

$sth = $dbh->prepare('
   select * from appointment
');
$result = $sth->execute();

print $q->header('application/json');
my @data_to_json; 
while ( my ($date, $time, $desc ) = $sth->fetchrow_array ) {
    my $data_to_json = {date=>$date,time=>$time,desc=>$desc};
    push @data_to_json, $data_to_json;
}
print to_json(\@data_to_json);
    
$dbh->disconnect;
