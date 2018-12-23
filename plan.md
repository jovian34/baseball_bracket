# Model to predict the NCAA Tournament Bracket

## Database design

### Tables

Teams
- Alternate_names (one to many)
- Address
- Conference (one to one)

Conferences
- Teams (many to one)

Alternate-Names
-alternate names (many to one - teams)

2019_Performance
- Team (one to one)
- Wins
- Losses
- Ties
- conf_wins
- conf_losses
- conf_ties
- RPI
- SOS
- Non-con SOS
- ISR

2018_Regionals
- team
- host 
