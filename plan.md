# Model to predict the NCAA Tournament Bracket

## Database design

### Tables

Teams
- primary_key
- alt_names (relation one to many)
- address
- city
- state
- zip
- conference (relation many to one)

Conferences
- primary_key
- team (relation one to many)

AlternateNames
- primary_key
- team (relation many to one)
- alternate_name

2019Performance
- primary_key
- team (relation)
- wins
- losses
- ties
- conf_wins
- conf_losses
- conf_ties
- rpi_value
- sos_rank
- non_con_sos_rank
- isr_rank

2018Regionals
- primary_key
- team (relation)
- host 
