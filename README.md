## Dscription
Another project about web scraping from Wikipedia. Here is the link: https://en.wikipedia.org/wiki/List_of_ongoing_armed_conflicts

`script.py`: code of scraping data from Wikipedia

`event_sourcing.csv`: expected dataset extracted by script. 

Second time using Beautifulsoup, way more proficient than the first time, which is good news!

## Lessons Learnt
`regex` library: it is a good library to remove content inside of {}, () etc. ex: `re.sub("[\(\[].*?[\)\]]", "",<String>)`
