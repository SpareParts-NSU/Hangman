extends Control

var word = 'ADMINISTRATION'

const LETTER_SCENE = preload("res://letter.tscn")

const BUTTON_SCENE = preload("res://button.tscn")
const BUTTON_SCRIPT = preload("res://text_button.gd")

const GET_DATA = preload('res://get_data.tscn')
const PUT_DATA = preload('res://put_data.tscn')

var gameID = null
var game_state = null

var get_data_instance = null


# Called when the node enters the scene tree for the first time.
func _ready():
	
	get_game_ID()
	
	get_word()
	
	var grid = get_node("letter_container")
	grid.columns = word.length()
	create_letter_spaces(grid, word)
	
	
	while(game_state != true):
		get_game_state()
	
	
	grid = get_node("button_container")
	grid.columns = word.length()/2
	create_buttons(grid, word)


func _process(delta):
	if word == '':
		win()
	pass



func check_win():
	return(parse_json(get_data_instance.get_data('/Game/' + gameID + '/'))['Winner'])

func get_game_ID():
	get_data_instance = GET_DATA.instance()
	get_data_instance.http_connect()
	gameID = get_data_instance.get_data('/matchID/')


func get_game_state():
	game_state = parse_json(get_data_instance.get_data('/Game/' + gameID + '/'))['gameStart']
	print(game_state)


func get_word():
	var data = parse_json(get_data_instance.get_data('/Game/' + gameID + "/"))
	print(data)
	word = data['word']
	word = clean_word(word)
	word = word.to_upper()


func clean_word(word):
	word.erase(word.length() - 2, 2)
	word.erase(0,2)
	return word


func create_letter_spaces(grid, word):
	for letter in word:
		var space = LETTER_SCENE.instance()
		space.letter = letter
		space.size_flags_horizontal = 7
		space.size_flags_vertical = 7
		grid.add_child(space)


func create_buttons(grid, word):
	word = remove_duplicate_letters(word)
	var word_array = []
	for letter in word:
		word_array.append(letter)
	
	for i in range (ceil(word_array.size()/2.0)):
		var rand_letter = OS.get_scancode_string(randi() % 26 + 65)
		while rand_letter in word_array:
			rand_letter = OS.get_scancode_string(randi() % 26 + 65)
		word_array.append(rand_letter)
	
	word_array.shuffle()
	
	for letter in word_array:
		var button = BUTTON_SCENE.instance()
		button.size_flags_horizontal = 7
		button.size_flags_vertical = 7
		button.text = letter
		button.set_script(BUTTON_SCRIPT)
		grid.add_child(button)


func remove_duplicate_letters(word):
	var unique = ''
	for letter in word:
		if not letter in unique:
			unique = unique + letter
	return unique


func win():
	
#	var put_data = PUT_DATA.instance()
#	put_data.http_connect()
#	var body = '{"Winner": ' + global.username + '}'
#	put_data.put_data("/Game/" + gameID + '/', body)
	
	yield(get_tree().create_timer(0.3), "timeout")
	var error = get_tree().change_scene('win_panel.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))


func lose():
	yield(get_tree().create_timer(0.3), "timeout")
	var error = get_tree().change_scene('lose_panel.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))
