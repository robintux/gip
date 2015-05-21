<?php
 

/////////////////////////////////////////////////////////////////////////////
/// We have http://www.arachnedesign.net/ to thank for this script
/////////////////////////////////////////////////////////////////////////////
// Set up some basic configuration - set at least the value assigned to
// $email_to to your own email address so that you'll get the submitted
// forms.
/////////////////////////////////////////////////////////////////////////////

///be sure to enter your OWN email below.
$email_to  = 'larisan@post.tau.ac.il';



// take the two slash marks out of the line below if you want to enter a custom from address
//$from      = 'cgi-mailer@perfora.net';
///choose any subject you want
$subject   = 'GIP 2015 - registration';



// the result array will report the outcome of the attempt to email the
// submitted form data back to your Flash movie

$result = array(
	'did_mail_send'  => 'yes',        // we'll assume everything is fine
	'errormessage' => ''
	);


// let's require that 'email' has a value.  we'll be using the empty() function
// to determine this.  You can learn more about empty() here:
// 
//    http://php.net/manual/en/function.empty.php

if ( !empty($_POST['email']) ) {
	
	// build the message body using the form information (note that the whitespace
	// naturally doesn't matter, it's just set up this way for readability)

	$message  = "name:     " . $_POST['username'] . "<br/>\n";

	$message .= "phone:    " . $_POST['phone']  . "<br/>\n";

    $message .= "email:    " . $_POST['email']     . "<br/>\n\n";
	 
	$message .= "programming expirience:  " . $_POST['program']     . "<br/>\n\n";
	
	// set other headers (we only care about 'From' in this example)
	
	

$headers .= "From:\"GIP 2015\" <noreply@post.tau.ac.il>\r\nContent-type: text/html; charset=windows-1255\r\n";
	
	
	// attempt to send the submission via email to the address specified at
	// the top of this file using PHP's mail() function.  You can find out more
	// about mail() here:
	// 
	//    http://php.net/manual/en/function.mail.php

	if ( !mail($email_to, $subject, $message, $headers) ) {
	
		// an error of some sort caused the emailing of the form data to fail
		$result[ 'did_mail_send' ] = 'no';
		$result[ 'errormessage' ]  = 'For some reason mail did not send';
		echo "For some reason mail did not send";
	}
}
else {
	
	// report that sending failed because no email address was supplied in
	// the POST variables from the form.
	
	$result[ 'did_mail_send' ] = 'no';
	$result[ 'errormessage' ]  = 'No email address supplied';
	echo "No email address supplied";

}



// now we're going to return the result information back to the flash movie.
// note we're encoding the values using PHP's urlencode() function.  You can
// read up on urlencode() at:
// 
//     http://php.net/manual/en/function.urlencode.php
if ($result[ 'errormessage' ] == '') {
	echo "Your Details Were Submitted Successfully";
}
?>
