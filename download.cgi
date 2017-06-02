#!/usr/bin/perl -wT
# example code adapted from
#  https://uts.nlm.nih.gov///help/license/validateumlsuserhelp.html

use CGI qw(:standard);

use HTTP::Request::Common qw(POST);
use LWP::UserAgent; 
use XML::Twig;

my $UTS_API_license_key = '<PLACEHOLDER>';
 
my $BMASS_file = '<PLACEHOLDER>';
my $BMASS_size = -1;

my $uname = param('username');
my $passw = param('password');

$ua = LWP::UserAgent->new;
my $req = POST 'https://uts-ws.nlm.nih.gov/restful/isValidUMLSUser',
[ licenseCode => $UTS_API_license_key, user => param("username"), password => param("password") ];

my $response = $ua->request($req);
my $status = $response -> content;
$status = (split(/\>/, $status))[-1];
$status = (split(/\</, $status))[0];

if ($status eq "true") {
    print "Content-type: application/octet-stream\n";
    print "Accept-Ranges: bytes\n";
    print "Content-Length: $BMASS_size\n";
    print "Content-disposition: filename=BMASS.zip\n\n";

    open(FIN, $BMASS_file);
    binmode FIN;
    print <FIN>;
} else {
    $q = new CGI;
    print $q->redirect('index.html?status=LoginError')
}
