extends Control

var word = 'ALIEN'

const BUTTON_SCENE = preload("res://button.tscn")
const BUTTON_SCRIPT = preload("res://text_button.gd")


# Called when the node enters the scene tree for the first time.
func _ready():
	var grid = get_node("grid_container")
	create_buttons(grid,word)
	grid.columns = 3


func create_buttons(grid, word):
	var word_array = []
	for letter in word:
		word_array.append(letter)
	word_array.shuffle()
	
	for letter in word_array:
		var button = BUTTON_SCENE.instance()
		
		button.size_flags_horizontal = 7
		button.size_flags_vertical = 7
		button.text = letter
		button.set_script(BUTTON_SCRIPT)
		grid.add_child(button)


func _process(delta):
	if word == '':
		var error = get_tree().change_scene('win_panel.tscn')
		if error != OK:
			print('Error code: {error_code}'.format({'error_code':error}))