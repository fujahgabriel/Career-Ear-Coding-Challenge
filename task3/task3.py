<?php

// Complete the minimumBribes function below.
function minimumBribes($q) {

    $swaps = 0;
    $min = count($q);
    for ($i = $min - 1; $i >= 0; i--){
        if ($q[$i] - $i > 3){
            return 'Too chaotic';
        }
        if ($q[$i] > $i+1){
            $swaps += ($q[$i]-($i+1));
        } else {
            if ($min > $q[$i]){
                $min = $q[$i];
            } else if ($q[$i] != $min){
                $swaps++;
            }
        }
    }
    
    return $swaps;

}

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $t);

for ($t_itr = 0; $t_itr < $t; $t_itr++) {
    fscanf($stdin, "%d\n", $n);

    fscanf($stdin, "%[^\n]", $q_temp);

    $q = array_map('intval', preg_split('/ /', $q_temp, -1, PREG_SPLIT_NO_EMPTY));

    minimumBribes($q);
}

fclose($stdin);
