export AOC="~/Python/Advent_of_Code" # remember to change this to whatever your AOC directory is
#export AOC_COOKIE="" # get this from the cookies tab in network tools on the AOC website
alias aos="python3 solution.py < in.txt"
alias aot="python3 solution.py < test.txt"
alias aoc="aot; echo; aos"

 aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > $AOC/$1/Day_$2/in.txt
    else
        curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%-d/input`)" > "$(echo `date +$AOC/%Y/Day_%-d/in.txt`)"
    fi
}
