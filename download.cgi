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

my $Pubmed_JET_file = '<PLACEHOLDER>';
my $Pubmed_JET_size = -1;

my $UMLS_JET_file = '<PLACEHOLDER>';
my $UMLS_JET_size = -1;

my $NLM_WSD_JET_file = '<PLACEHOLDER>';
my $NLM_WSD_JET_size = -1;

my $uname = param('username');
my $passw = param('password');
my $dataset = param('dataset');

$ua = LWP::UserAgent->new;
my $req = POST 'https://uts-ws.nlm.nih.gov/restful/isValidUMLSUser',
[ licenseCode => $UTS_API_license_key, user => param("username"), password => param("password") ];

my $response = $ua->request($req);
my $status = $response -> content;

$status = (split(/\>/, $status))[-1];
$status = (split(/\</, $status))[0];

if ($status eq "true") {
    if ($dataset eq "BMASS") {
        print "Content-type: application/octet-stream\n";
        print "Accept-Ranges: bytes\n";
        print "Content-Length: $BMASS_size\n";
        print "Content-disposition: filename=BMASS.zip\n\n";

        open(FIN, $BMASS_file);
        binmode FIN;
        print <FIN>;
    } elsif ($dataset eq "Pubmed_JET") {
        print "Content-type: application/octet-stream\n";
        print "Accept-Ranges: bytes\n";
        print "Content-Length: $Pubmed_JET_size\n";
        print "Content-disposition: filename=Pubmed_JET.zip\n\n";

        open(FIN, $Pubmed_JET_file);
        binmode FIN;
        print <FIN>;
    } elsif ($dataset eq "UMLS_JET") {
        print "Content-type: application/octet-stream\n";
        print "Accept-Ranges: bytes\n";
        print "Content-Length: $UMLS_JET_size\n";
        print "Content-disposition: filename=JET_strings.zip\n\n";

        open(FIN, $UMLS_JET_file);
        binmode FIN;
        print <FIN>;
    } elsif ($dataset eq "NLM_WSD_JET") {
        print "Content-type: application/octet-stream\n";
        print "Accept-Ranges: bytes\n";
        print "Content-Length: $NLM_WSD_JET_size\n";
        print "Content-disposition: filename=NLM_WSD_JET.zip\n\n";

        open(FIN, $NLM_WSD_JET_file);
        binmode FIN;
        print <FIN>;
    }
} else {
    $q = new CGI;
    print $q->redirect('index.html?status=LoginError&dataset='.$dataset)
}
