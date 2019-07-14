<?php

// Complete the riddle function below.
function riddle($arr) {
    // complete this function
    $n = count($arr);
    $min_element=$arr[0];
    $diff=$arr[1] - $arr[0];
    for($i=1; $i<$n; $i++)
    {
        if($arr[$i]-$min_element > $diff)
            $diff=$arr[$i] - $min_element;
        if($arr[$i]<$min_element)
            $min_element=$arr[$i];
    }
    return $diff;

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
