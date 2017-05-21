echo
echo 'Solving test0 problems with naive 0'
echo
./test0.sh naive 0 > results/results0naive.txt

echo
echo 'Solving test1 problems with naive 0'
echo
./test1.sh naive 0 > results/results1naive.txt

echo
echo 'Solving test1 problems with add 3'
echo
./test1.sh add 3 > results/results1add3.txt

echo
echo 'Solving test2 problems with add 3'
echo
./test2.sh add 3 > results/results2add3.txt

echo
echo 'Solving test3 problems with add 3'
echo
./test3.sh add 3 > results/results3add3.txt
