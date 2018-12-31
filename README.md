# baseball_bracket
NCAA Division I Baseball Tournament Bracket Modeler
by Carl James

This app web scrapes data from online RPI sites and
processes the data in such a way as to attempt to emulate the
process the NCAA committee goes through to build a field of
64 for the NCAA Division I Baseball Tournament.

The output is a text file with a field of 64.

This takes current data of games played to the date of running the
app. It does not make any predictions about games not yet played.
Essentially this is what the field would look like if the season ended today.

In the off-season the field generated is as if the field was re-established
with the same criteria after the Men's College World Series(CWS). 
For example
even though Oregon State won the 2018 CWS title, this model only places
the Beavers as the national #3 seed - largely because they were
not the Pac-12 champions. The #1 and #2 teams both got a boost due to winning
there respective conference titles even though #2 Stanford didn't even win
their own regional.


Tests are written only for data collection at this point,
but now that I have .json files to work with I plan to add tests for
the rest of the application as well. A concern is while it works well
for the current data, there are edge cases I can envision 
which may cause problems that do not exist in this data set.
