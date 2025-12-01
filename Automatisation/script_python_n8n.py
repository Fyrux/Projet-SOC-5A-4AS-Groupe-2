# Mode: Run Once For All Items 
# Language: Python Beta

# Loop over input items and add a new field called 'myNewField' to the JSON of each one
for item in _input.all():
  item.json.body.results_link = item.json.body.results_link.replace("c7e85cf33ced:8000", "172.16.150.36:8000")
return _input.all()
