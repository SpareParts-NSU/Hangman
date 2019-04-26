extends Control

var word = 'ALIEN'

const LETTER_SCENE = preload("res://letter.tscn")

const BUTTON_SCENE = preload("res://button.tscn")
const BUTTON_SCRIPT = preload("res://text_button.gd")


# Called when the node enters the scene tree for the first time.
func _ready():
	var grid = get_node("button_container")
	grid.columns = 3
	create_buttons(grid,word)
	grid = get_node("letter_container")
	grid.columns = word.length()
	create_letter_spaces(grid, word)
	

func create_letter_spaces(grid, word):
	for letter in word:
		var space = LETTER_SCENE.instance()
		space.name = letter
		space.size_flags_horizontal = 7
		space.size_flags_vertical = 7
		grid.add_child(space)


func create_buttons(grid, word):
	var word_array = []
	for letter in word:
		word_array.append(letter)
	word_array.shuffle()
	
	for letter in word_array:
		var button = BUTTON_SCENE.instance()
		button.name = letter
		button.size_flags_horizontal = 7
		button.size_flags_vertical = 7
		button.text = letter
		button.set_script(BUTTON_SCRIPT)
		grid.add_child(button)


func _process(delta):
	if word == '':
		yield(get_tree().create_timer(0.3), "timeout")
		var error = get_tree().change_scene('win_panel.tscn')
		if error != OK:
			print('Error code: {error_code}'.format({'error_code':error}))