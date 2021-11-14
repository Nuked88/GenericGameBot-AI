config_string = '''game_name:  test
path_game: test_path
commands:
  w : 'Nothing'
  a : 'Left'
  s : 'Down'
  d : 'Right'
  ' ' : 'Jump'
'''

with open('config.yaml', 'w') as f:
    f.write(config_string)