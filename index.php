<?php
function sendSMS($txt) {
    // Function to send a message to Apifonica to send to a specified phone.
    // Most of these are option parameters which have been set from an example.
    // Nothing needs to be changed apart from the user and password,
    // from Apifonica if a different account is used, as well as the account
    // in the website link
    $url = "https://api.apifonica.com/v2/accounts/acce76c9324-1b7c-36a5-8e00-ed83be6c2043/messages";
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt ($curl, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt ($curl, CURLOPT_FOLLOWLOCATION, 1);
    // // Set user and password
    curl_setopt ($curl, CURLOPT_USERPWD, "acce76c9324-1b7c-36a5-8e00-ed83be6c2043:aut0eac9ad3-ee88-3f3f-8664-e0bc1dd60cc8");
    // Do not check SSL
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 0);
    // Add header
    curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    // Set POST
    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($txt));

    $result = curl_exec($curl); // executes the sending of the msg to Apifonica

    echo($result); // print out the message sent to DEBUG

    if ($result) {
      $result = json_decode($result, true);
    } else {
      $result = array(
        'error_text' => curl_error($curl),
        'error_code' => curl_errno($curl),
        'status_code' => 600,
      );
  }
}


// Recieve message data from the server input
$var = file_get_contents('php://input');

$data = json_decode($var, true); // decode the data gathered

// there are many parameters which can be taken, such as the numbers by using
// 'from' or 'to', however this was hardcoded, so only the text is needed
$txt = $data['text'];

// check the text against the regex to see if its is in an Australian postcode format
$pattern = '/^[0-9]{3,4}$/';
if(preg_match($pattern, $txt)) {
    // check within the databse containing all Australian postcodes, if it is a valid postcode
    $pdo = new PDO('mysql:host=localhost;port=3306;dbname=region_board_db', 'root', 'secret');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $query = $pdo->prepare("SELECT postcode FROM postcodes_geo"); // select all the postcodes from the database table
    try {
        $query->execute();
    } catch (PDOException $e) {
        echo $e->getMessage();
    }
    $data = $query->fetchAll(PDO::FETCH_ASSOC);

    foreach ($data as $row) { // run through all the postcodes to check if the postcode is valid
        if($txt == $row['postcode']) {
            $txt = array( // send a welcome msg plus the info for that postcode
                "from" => "61476857592",
                "to" => "61487646948",
                "text" => "-Welcome to EventMuster, An event service for rural communities."."\n"."-Events in Roma:"."\n"."#1. Bake off"."\n"."#2. Oracle Chess"."\n"."#3. CWA Monthly"."\n"."-Type 'INFO #'' for more information or 'RSVP #' to r.s.v.p.",
            );
            sendSMS($txt);
        }
    }
} elseif ($txt == 'RSVP 2') { // hardcoded msg for an RSVP with the secodn option (chess club)
  $txt = array(
      "from" => "61476857592",
      "to" => "61487646948",
      "text" => "Thank you for the RSVP to Oracle Chess. We'll keep you updated.",
  );
  sendSMS($txt);

} elseif ($txt == 'Sarah') {
  $txt = array(
      "from" => "61476857592",
      "to" => "61487646948",
      "text" => "Thank you Sarah. We'll keep you updated.",
  );
  sendSMS($txt);

} elseif ($txt == 'INFO 2') {
  $txt = array(
      "from" => "61476857592",
      "to" => "61487646948",
      "text" => "Oracle Chess"."\n"."Host: Joe Blogs"."\n"."When: Sunday 16:00"."\n"."Where: Oracle Brisbane - Roma"."\n"."Info: Come along for our 4th meeting this year"."\n"."-Type your name to RSVP or CANCEL to cancel.",
  );
  sendSMS($txt);

} elseif ($txt == 'CANCEL') {
  $txt = array(
      "from" => "61476857592",
      "to" => "61487646948",
      "text" => "Type a new post code to being event search.",
  );
  sendSMS($txt);

}
?>
