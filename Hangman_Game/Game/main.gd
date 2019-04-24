extends Control


var word = 'CHICKEN'

const BUTTON_SCENE = preload("res://button.tscn")


# Called when the node enters the scene tree for the first time.
func _ready():
	$win_panel.hide()
	var grid = get_node("grid_container")
	for b in range(word.length()):
		var button = BUTTON_SCENE.instance()
		
		button.size_flags_horizontal = 7
		button.size_flags_vertical = 7
		grid.add_child(button)
	grid.columns = 3



func _input(event):
	if event is InputEventKey:
		var letter = (OS.get_scancode_string(event.get_scancode_with_modifiers()))
		if letter in word:
			word = word.replace(letter, '')
			print(word)
		else:
			print('eat shit')
		if word.empty():
			get_tree().paused = true
			$win_panel.show()