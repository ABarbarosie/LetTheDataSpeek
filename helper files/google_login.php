<?php
//source does not work because we don't have the xhttp class

header('content-type: text/plain');

// Set account login info
$data['post'] = array(
  'accountType' => 'HOSTED_OR_GOOGLE',  // indicates a Google account
  'Email'       => 'letthedataspeak@gmail.com',  // full email address
  'Passwd'      => 'ilovemagic!',
  'service'     => 'trendspro', // Name of the Google service
  'source'      => 'magicSoftwareInc-letTheDataSpeak-0.1' // Application's name, e.g. companyName-applicationName-versionID
);

$response = xhttp::fetch('https://www.google.com/accounts/ClientLogin', $data);

// Test if unsuccessful
if(!$response['successful']) {
    echo 'response: '; print_r($response);
    die();
}

// Extract SID
preg_match('/SID=(.+)/', $response['body'], $matches);
$sid = $matches[1];

// Erase POST variables used on the previous xhttp call
$data = array();

// Set the SID in cookies
$data['cookies'] = array(
    'SID' => $sid
);

$response = xhttp::fetch('http://www.google.com/insights/search/overviewReport?q=lingerie&geo=ID&cmpt=q&content=1&export=1', $data);

// CSV data in the response body
echo $response['body'];

?>