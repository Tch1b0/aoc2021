# Day 8
### [Task](https://adventofcode.com/2021/day/8)
## Code
```py
def part1(segments: list[list[str]]) -> int:
    p = 0
    for segment in segments:
        for s in segment[1]:
            if len(s) in [2, 3, 4, 7]:
                p += 1

    return p

def part2(segments) -> str:
    for segment in segments:
        decrypt_segment(segment)

```
## Input
```
gbcead cfgaeb beadf adb egafd fbeac dbfegca fdaceb dbfc bd | dfcb gedaf dcfb bcfdea
dgfcb gcdeafb eg egb fcdebg cegf becad dfbcag fbgdea gecdb | dbfcge dacbe bge fgdbca
bgdacf ga egab bfeacdg bfaec agc efbcda agfec cfedg abfceg | bega cga febac aebg
cbgfad ed ecdgfb dge deabg fgdab geacb gabfced dfae dbgfea | afed dfea de eabgc
fdaegb fae acedgfb dgbae fedcb daefb gebadc af bcfgae gafd | egadb afdbe eaf af
cfg cegbdf fecgb fg cdageb fbgcad egfd gdcbe eafcb abdgcfe | gdbace fbgce gecfb bdfcge
bgcfed aebgdcf gcbd edbcf ecdfag ebc efcdg bc befacg daefb | dfabe edbfc cdebf gbcfea
dbfge cfebd dega facbge adbgcfe bfage fgdeba gfdbac gd dgb | bgd eabcfg bcdfega egafdcb
...
```
## Output
```
Part 1:
344
=========
Part 2:
None
```