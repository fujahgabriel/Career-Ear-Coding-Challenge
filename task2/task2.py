<?php

// Complete the riddle function below.
function riddle($arr) {
    // complete this function

}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $n);

fscanf($stdin, "%[^\n]", $arr_temp);

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

$res = riddle($arr);

fwrite($fptr, implode(" ", $res) . "\n");

fclose($stdin);
fclose($fptr);
