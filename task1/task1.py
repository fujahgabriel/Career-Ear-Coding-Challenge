<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */

$stacknew= array();
$stackold = array();

function enqueue($val){
    global $stacknew;
    array_push($stacknew,$val);
}
function peek(){
    global $stackold;
    sortx();
    return peek($stackold);
}

function dequeue(){
    global $stackold;
    sortx();
    return array_pop($stackold);
}

function sortx(){
   global $stacknew;
   global $stackold;

   if(count($stackold) === 0){
       while(count($stacknew) > 0){
           array_push($stackold, array_pop($stacknew));
       }
   }
}


?>

